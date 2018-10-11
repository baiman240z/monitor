# -*- coding: utf-8 -*-
from core.config import Config
import subprocess
import re
import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate
from jinja2 import Environment, FileSystemLoader

threshold = Config.get('disk-threshold')

args = ['df', '-h']
result = subprocess.check_output(args)
lines = result.decode('utf-8').split("\n")

warnings = []
for line in lines:
    line = line.strip()

    if len(line) == 0:
        continue

    columns = re.split('\s+', line)
    try:
        per = int(columns[4][:-1])
        if per >= threshold:
            warnings.append({
                'per': per,
                'size': columns[1],
                'used': columns[2],
                'avail': columns[3],
                'path': columns[5],
            })
    except ValueError as e:
        continue

if len(warnings) > 0:
    env = Environment(loader=FileSystemLoader(Config.view_dir() + '/email', encoding='utf8'))
    template = env.get_template('disk.txt')
    body = template.render({'warnings': warnings})

    message = MIMEText(body)
    message['Subject'] = '[monitor:' + Config.get('target') + ']disk space'
    message['From'] = Config.get('from')
    message['To'] = Config.get('to')
    message['Date'] = formatdate()

    sender = smtplib.SMTP('localhost', 25)
    sender.sendmail(
        Config.get('from'),
        Config.get('to'),
        message.as_string()
    )
    sender.close()
