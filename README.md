# fin-lab

Лабораторна робота: CI/CD + GitOps на AWS EKS

## Що реалізовано

- Python-додаток (повертає hostname і Pod IP)
- Dockerfile
- GitHub Actions: автоматична збірка і пуш образу в Docker Hub
- Terraform: створення EKS кластера, Nginx Ingress Controller і ArgoCD
- Kubernetes маніфести + ArgoCD Application
- Додаток доступний за адресою: http://app.student1.devops12.test-danit.com
- ArgoCD доступний за адресою: http://argocd.student1.devops12.test-danit.com

## Структура репозиторію
├── app/
│   └── app.py
├── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── ingress.yaml
│   └── argocd-app.yaml
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   ├── nginx-ingress.tf
│   ├── argocd.tf
│   └── outputs.tf
├── .github/workflows/docker-build.yml
└── Dockerfile


## Технології

- AWS EKS
- Terraform
- Helm
- ArgoCD
- Nginx Ingress
- GitHub Actions
- Docker Hub