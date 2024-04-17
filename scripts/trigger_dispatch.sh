#!/bin/bash
# trigger has happened
echo "Trigger has happened"

# create deployment from image
kubectl create deployment $1 --image=$2
kubectl expose deployment $1 --port=8000 --type=NodePort
kubectl port-forward service/$1 $3:8000
echo "Service created for listening to trigger at localhost:$3" 


