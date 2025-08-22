* `storage.yaml` creates storage objects.
    - `PersistentVolume` (PV) is an abstraction of disk space on minikube node, backed by a `hostPath`.
    - `PersistentVolumeClaim` (PVC) is the Pod's request for storage.
* `postgres.yaml` creates a Deployment (Pod) running the `postgres:14` container. 
* `postgres-service.yaml` creates a Service (stable network entrypoint).


Apply all of these and then check `kubectl get pods`, `kubectl get svc`.