sleep $1
echo "Deleting " > $(pwd)/out$2.log
bash delete_function.sh $2
crontab -l | grep -v out$2.log  | crontab -