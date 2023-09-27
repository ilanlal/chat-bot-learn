# 
Run `gcloude builds submit --tag gcr.io/ez-mailboxes-investigation-dev/learning-chatbot` # Build and push image to Google Container Registry
Run `gcloud run deploy --image gcr.io/ez-mailboxes-investigation-dev/learning-chatbot --platform managed` # Deploy image to Cloud Run

## How to create a brand python project




## How to start a new project

### Local
Run `python3 -m venv env` # Create virtual environment
Run `source env/bin/activate` # Activate virtual environment
Run `pip3 install -r requirements.txt` # Install dependencies
Run `python3 app.py` # Run locally


### Cloud Run
Run `gcloud run services list` # List all services
Run `gcloud run services delete learning-chatbot` # Delete service

