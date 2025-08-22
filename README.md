# ml-kubernetes-app






### 1. Build the inference server image

### 2. Create a Deployment

```bash
kubectl apply -f deployment.yaml
```

### 3. Create a Service to expose the Deployment

```bash
kubectl apply -f service.yaml

# check
kubectl get svc
```

### 4. Test access the Service

Get the URL:

```bash
minikube service inference-service --url
```

Test request:

```bash
curl -X POST <URL>/predict \
    -H "Content-Type: application/json" \
    -d '{"prediction_request":"hi"}'
```