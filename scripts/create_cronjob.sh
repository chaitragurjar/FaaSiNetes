echo "Creating cronjob for $1"
(crontab -l ; echo "$1 /bin/bash $(pwd)/trigger_dispatch.sh $2 $3 > $(pwd)/out.log 2>&1" ) | crontab -