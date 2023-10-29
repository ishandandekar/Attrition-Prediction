# Attrition Prediction End-to-End Project

### Instructions for inference:

- Clone the repo
  ```bash
  git clone https://github.com/AarnoStormborn/Attrition-Prediction.git
  ```
- Build and run Docker image
  ```bash
  docker build -t attripred . && \
  docker run --rm -p 8000:8000 attripred
  ```
- And you're good to go! You can now leverage the API to get predictions by hitting the **`infer/`** endpoint of the URL.
