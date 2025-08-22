## Build the image and run container locally

```bash
# Build the Docker image
docker build -t inference-server .

# Run a container
docker run -p 8000:8000 inference-server
```

While running, do `docker ps` to see the running container.

## Test request

```bash
curl -X POST http://localhost:8000/predict \
    -H "Content-Type: application/json" \
    -d '{"prediction_request": "hello there!"}'
```


# To use in minikube

Minikube has its own Docker daemon, so we need to switch to this and build the container there.

```bash
eval $(minikube -p minikube docker-env)
```