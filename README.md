# Overview

This repo aims to present gitops principles by showing the automatic reconciliation steps with ArgoCD.
It uses minikube as a replacement for a real k8s cluster.

# How to demo

## Install argocd CLI

1. curl -sSL -o argocd https://github.com/argoproj/argo-cd/releases/latest/download/argocd-linux-amd64
2. chmod +x argocd
3. sudo mv argocd /usr/local/bin/

## Start minikube and install argocd
1. minikube start, continue step 7 if done this once.
2. kubectl create namespace argocd
3. kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
3. kubectl get pods -n argocd
4. argocd login --core
5. continue step 6 form here: https://argo-cd.readthedocs.io/en/stable/getting_started/#1-install-argo-cd
6. 