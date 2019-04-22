https://fxdata.cloud/tutorials/serve-django-applications-with-apache-and-mod_wsgi-on-centos-7

user and group permissions:
httpd.conf - apache / apache
djangouser - djangouser / users
supervisord celery.ini - djangouser
----------------------------------------------------------------------------------------------------------------------
run with python2 and django1.11

autostart vm
change user and root passwords.
update yum.conf
disable ipv6
vi /etc/sysctl.conf
net.ipv6.conf.all.disable_ipv6 = 1
net.ipv6.conf.eno16777736.disable_ipv6 = 1


wooey notes:


sudo yum -y install gcc libffi-devel python-devel openssl-devel python-crypto htop nmap python-pip python-setuptools vim-enhanced iftop ifconfig bind-utils moreutils net-tools glances git wget sshpass python36 python-virtualenv python36-pip.noarch ntfs-3g.x86_64 python-pip httpd mod_wsgi supervisor

reboot
-------------------------------
sudo firewall-cmd --permanent --add-port=80/tcp
sudo firewall-cmd --reload
sudo systemctl enable httpd.service
sudo systemctl start httpd.service
sudo systemctl status httpd.service

set_proxy
mkdir wooey
cd wooey
virtualenv venv
source venv/bin/activate
pip install pip setuptools --upgrade

pip install wooey
wooify -p automation
cd automation
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000

wget http://localhost:8000/admin


cd /home/djangouser/wooey/automation/automation/settings
vim django_settings.py
ALLOWED_HOSTS = ['*']
TIME_ZONE = 'America/New_York'


---------------------------------------------
https://fxdata.cloud/tutorials/serve-django-applications-with-apache-and-mod_wsgi-on-centos-7
vim /etc/httpd/conf.d/django.conf


Alias /static /home/djangouser/wooey/automation/automation/static
<Directory /home/djangouser/wooey/automation/automation/static>
    Require all granted
</Directory>

<Directory /home/djangouser/wooey/automation/automation>
    <Files wsgi.py>
        Require all granted
    </Files>
</Directory>

WSGIDaemonProcess automation python-path=/home/djangouser/wooey/automation:/home/djangouser/wooey/venv/lib/python2.7/site-packages
WSGIProcessGroup automation
WSGIScriptAlias / /home/djangouser/wooey/automation/automation/wsgi.py

sudo systemctl restart httpd.service
sudo systemctl enable httpd.service

------------------------------

Supervisord Notes:
sudo systemctl start supervisord.service
sudo systemctl enable supervisord.service
sudo systemctl restart supervisord.service
sudo vim /etc/supervisord.d/celery.ini

sudo systemctl restart supervisord.service
sudo systemctl status supervisord.service -l


[program:automation]
command=/home/djangouser/wooey/venv/bin/celery -A automation worker -c 1 -E --beat -l info
directory=/home/djangouser/wooey/automation
environment=HOME="/tmp"
user=djangouser
numprocs=1
stdout_logfile=/var/log/celery/mail_beat.log
stderr_logfile=/var/log/celery/mail_beat.log
autostart=true
autorestart=true
priority=999
redirect_stderr=true

mkdir /var/log/celery
touch /var/log/celery/mail_beat.log

--------------------------------------------------------------------
Webui mods:

/home/djangouser/wooey/automation/automation/static/wooey/css
.wooey {
    font-family: 'Palatino Linotype',cursive;
    color: #fff !important;


./venv/lib/python3.6/site-packages/wooey/settings.py
/home/djangouser/wooey/venv/lib/python3.6/site-packages/wooey
# User interface settings
WOOEY_SHOW_LOCKED_SCRIPTS = get('WOOEY_SHOW_LOCKED_SCRIPTS', True)
WOOEY_SITE_NAME = get('WOOEY_SITE_NAME', _('ITIA'))
WOOEY_SITE_TAG = get('WOOEY_SITE_TAG', _('A web UI for Python scripts'))


---------------------------
ISSUES:
---------------
Fix write permissions to /tmp
/usr/lib/tmpfiles.d/tmp.conf


[Thu Apr 18 13:56:41.557745 2019] [core:error] [pid 3940] (13)Permission denied: [client 165.115.44.107:62474] AH00035: access to / denied (filesystem path '/home/djangouser/wooey') because search permissions are missing on a component of the path
sudo chown -R djangouser:apache wooey/
 sudo chmod 755 /home/djangouser -----------> resolved

OperationalError at /admin/login/
attempt to write a readonly database
chmod 777 db.sqlite3 ----> resolved.

vim /usr/lib/tmpfiles.d/tmp.conf
comments out everything

Permission denied: '/home/djangouser/wooey/automation/automation/user_uploads/wooey_files'
chmod 777 ./user_uploads/ ----> resolved issue.


---------------------------------- --> resolved

celery -A automation worker -c 1
nohup celery -A automation worker -c 1 –beat -l info &
chmod 777 /tmp



sudo usermod -a -G users apache
sudo usermod -a -G users djangouser
sudo chown -R :users wooey/
sudo chmod 755 /home/djangouser/
sudo chmod 777 db.sqlite3
[root@ittellab-lxvm05 ~]# chmod -R 777 /tmp
[root@ittellab-lxvm05 ~]# chown -R :users /tmp

-------------------------------------------------------
POST INSTALL:
------------------------
pip install netaddr requests netmiko enum34 utils



