.PHONY: run

run:
	@streamlit run app.py --server.port=8080

run-container:
	@docker build . -t $APP_NAME
	@docker run -p 8080:8080 $APP_NAME

gcloud-deploy:
	@gcloud builds submit --tag gcr.io/$(PROJECT_ID)/$(APP_NAME)
	@gcloud run deploy --image gcr.io/$(PROJECT_ID)/$(APP_NAME) --platform managed
