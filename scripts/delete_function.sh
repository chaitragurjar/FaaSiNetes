sleep $1
echo "Deleting " > $(pwd)/out$2.log
kubectl delete deployment $2
kubectl delete service $2
crontab -l | grep -v out$2.log  | crontab -