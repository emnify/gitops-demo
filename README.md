# Overview

This repo aims to present gitops principles by showing the automatic reconciliation steps with ArgoCD.
It uses minikube as a replacement for a real k8s cluster.

# Prerequisites
- Docker v26.1.3 or higher
- Minikube v1.33.1 or higher
- kubectl v1.22.10 or higher
- argocd CLI v2.11.3 or higher

### How to install argocd CLI

Steps taken from: https://argo-cd.readthedocs.io/en/stable/cli_installation/

1. curl -sSL -o argocd https://github.com/argoproj/argo-cd/releases/latest/download/argocd-linux-amd64
2. chmod +x argocd
3. sudo mv argocd /usr/local/bin/

# How to demo

## Start minikube and install argocd

Steps taken from argocd docs: https://argo-cd.readthedocs.io/en/stable/getting_started/#1-install-argo-cd

1. minikube start
2. kubectl create namespace argocd
3. kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
3. kubectl get pods -n argocd
4. argocd login --core

If these steps have been followed once, steps 2-4 can be skipped.

## Build Docker image and push to minikube

#### Build the image
2. docker build -t shrimp:latest .
#### Check image is present
2. docker images | grep shrimp 
#### Verify image runs as intended and returns a message every second
3. docker run --name shrimp -e MESSAGE="test" shrimp:latest
4. docker logs -f shrimp
#### Stop the container
5. docker stop shrimp
#### Make minikube use docker-env
6. eval $(minikube docker-env)
#### Load docker image via minikube
7. minikube image load shrimp

## Create the application in argocd

