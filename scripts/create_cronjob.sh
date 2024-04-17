echo "Creating cronjob for $1"
echo "Triggering " > $(pwd)/out.log
(crontab -l ; echo "$1 /bin/bash $(pwd)/trigger_dispatch.sh $2 $3 $4 >> $(pwd)/out.log 2>&1" ) | crontab -