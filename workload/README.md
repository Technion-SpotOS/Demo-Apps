# GOLEM Workload App

A simple workload that POSTs to a deployed [rest-logger](../rest-logger) upon initialization and death.


### Environment Variables

Set the following env vars before deploying:

1. REST server URL (keep unset if deploying [rest-logger](../rest-logger), which is defaulted to through cluster local service):
```
    export REST_SERVER=... 
```

2. App name - application name sent in posts
```
    export APP_NAME='golem-workload'
```

### Deploying
```
    envsubst < k8s/deployment.yaml | kubectl apply -f -
```