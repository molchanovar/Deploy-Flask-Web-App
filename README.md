# Deploy-Flask-Web-App
AutoDeploy Flask Web Application on Apache | Vagrant + Ansible

1. [Flask](https://github.com/pallets/flask)
2. [YouTube_Deploy](https://www.youtube.com/watch?v=2Pcy44-wtio)
3. [StartAnsibleLocally](https://gist.github.com/alces/caa3e7e5f46f9595f715f0f55eef65c1)
4. [Ansible_CentOS8_Install](https://linuxhint.com/install_ansible_centos8/)
5. [Flask_CentOS8_Install](https://www.itmanagement101.co.uk/how-to-install-python-wsgi-flask-apache-on-centos-8-and-get-your-first-python-web-app-up-and-running/)

### Настройка Apache под cgi-scripts и Flask: 
```
<IfModule alias_module>
      ScriptAlias /cgi-bin/ "/var/www/cgi-bin/"
      WSGIScriptAlias / /var/www/myflask/app.wsgi
</IfModule>

<Directory "/var/www/myflask">
    Order allow,deny
    Allow from all
</Directory>

<Directory "/var/www/cgi-bin">
    AllowOverride None
    Options None
    Require all granted
</Directory>
```

/var/www/cgi-bin/shell.sh
```
#!/bin/bash
echo Content-type: text/plain
echo ""
echo "Hello from Shell"
```

/var/www/myflask/app.wsgi
```
import sys
sys.path.insert(0, "/var/www/myflask")
from init import app as application
```

#### Python env
```
python -m venv env
source env/bin/activate
pip install flask uwsgi
```
