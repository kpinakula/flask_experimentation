build:
	docker build . --tag flask-api

shell:
	docker run -it flask-api sh

serve:
	docker run flask-api