#!/bin/bash
# 1 func name 2 image name 3 port 4 cooldown
# trigger has happened
echo "Trigger has happened"

# create deployment from image
containerport=5000
kubectl create deployment $1 --image=$2
kubectl expose deployment $1 --port=$containerport --type=NodePort
kubectl wait --for=condition=Available deployment/$1 --timeout=-60s
kubectl port-forward service/$1 $3:$containerport &
echo "Service created for listening to trigger at localhost:$3" 

echo "Sleeping for $4 seconds"
sleep $4
echo "Deleting $1"s
kubectl delete deployment $1
kubectl delete service $1




