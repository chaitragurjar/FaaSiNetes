# 1 cron 2 func name , 3 image 4 port 5 cooldown
echo "Triggering " > $(pwd)/out$2.log
/bin/bash $(pwd)/trigger_dispatch.sh $2 $3 $4 $5 >> $(pwd)/out$2.log 2>&1 &
echo "Creating cronjob for $1"
(crontab -l ; echo "$1 /bin/bash $(pwd)/trigger_dispatch.sh $2 $3 $4 $5>> $(pwd)/out$2.log 2>&1" ) | crontab -
