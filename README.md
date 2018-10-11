# Server resources monitor with Python3

![A screenshot of your package](https://f.cloud.github.com/assets/69169/2290250/c35d867a-a017-11e3-86be-cd7c5bf3ff9b.gif)

## setup

1. Python
    ```
    yum install python3x python3x-devel
    ```
1. virtualenv
    ```
    python3 -m venv venv
    . venv/bin/activate
    ```
1. install packages
    ```
    pip install mysqlclient
    pip install jinja2
    ```
1. include path
    ```
    echo '/{install dir}/app/packages' > /{install dir}/venv/lib/python3.x/site-packages/my.pth
    ```
1. cron example
    ```
    * * * * * . /www/monitor/venv/bin/activate; python /www/monitor/app/bin/disk.py
    ```