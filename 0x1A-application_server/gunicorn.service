[Unit]
Description = HBNB
After = network.target

[Service]
PermissionsStartOnly = true
PIDFile = /run/hbnb/hbnb.pid
User = ubuntu
Group = ubuntu
WorkingDirectory = /home/ubuntu/AirBnB_clone_v4
ExecStartPre = /bin/mkdir /run/hbnb
ExecStartPre = /bin/chown -R ubuntu:ubuntu /run/hbnb
ExecStart = /usr/bin/env HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db gunicorn -w 3 --access-logfile /tmp/airbnb-access.log --error-logfile /tmp/airbnb-error.log --bind 0.0.0.0:5003 web_dynamic.2-hbnb:app --pid /run/hbnb/hbnb.pid
ExecReload = /bin/kill -s HUP $MAINPID
ExecStop = /bin/kill -s TERM $MAINPID
ExecStopPost = /bin/rm -rf /run/hbnb
PrivateTmp = false 

[Install]
WantedBy = multi-user.target
