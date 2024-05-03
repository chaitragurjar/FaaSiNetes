## Installations

We require minikube and kubectl tools.
```
$ curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
$ sudo install minikube-linux-amd64 /usr/local/bin/minikube && rm minikube-linux-amd64
$ sudo apt-get install -y kubectl
```

## Getting Started

Start the local K8 cluster.
```
$ minikube start
$ minikube dashboard
```

## Start the FaaS Wrapper
The FaaS wrapper is inside the scripts folder.
```
$ cd scripts
$ python3 faas_wrapper.py
```
