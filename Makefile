build:
	docker build . --tag flask-api

shell:
	docker run -it flask-api sh

serve:
	docker run -p 5000:5000 flask-api
