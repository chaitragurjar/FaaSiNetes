
(crontab -l ; echo $0 /bin/bash /scripts/trigger_dispatch.sh $1 > /tmp/cronjob ) | crontab -