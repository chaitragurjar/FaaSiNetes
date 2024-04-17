#!/bin/bash
# trigger has happened
echo "Trigger has happened"

# create deployment from image
kubectl create deployment master --image=$0
kubectl expose deployment master --port=8080 --type=NodePort
kubectl port-forward service/master 7865:8080
echo "Service created for listening to trigger at localhost:7865" 
