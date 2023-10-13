# To get running:
`cd` into `backend` and :
```bash
poetry install
```

Then `poetry shell` to activate the virtual env.

Then :
```bash
poetry run pre-commit install
```
to install the pre-commit hooks.

# Pushing into Google Artifact Registry
1. `cd` into location of `Dockerfile`.
2. Build and tag the docker image:
    ```bash
    docker buildx build --platform linux/amd64 -t us-central1-docker.pkg.dev/merantix-genai23ber-9525/alfred-cr/alfred-backend  .
    ```
    This makes sure the docker image is built for the amd64 architecture such that it runs on Google Platform, which might be different than the local machine's architecture.

3. Push the Docker image to Google Artifact Registry:
    ```bash
    docker push us-central1-docker.pkg.dev/merantix-genai23ber-9525/alfred-cr/alfred-backend
    ```

4. Deploy the container to Cloud Run:
    ```bash
    gcloud run deploy alfred-backend-service --image us-central1-docker.pkg.dev/merantix-genai23ber-9525/alfred-cr/alfred-backend
    ```
# Testing Docker Image locally
After building the docker image from step 2. in the above, run:
```bash
PORT=8080 && docker run -p 9090:${PORT} -e PORT=${PORT} us-central1-docker.pkg.dev/merantix-genai23ber-9525/alfred-cr/alfred-backend
```
Then navigate to `http://127.0.0.1:9090/`.
