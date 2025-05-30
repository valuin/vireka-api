dev: 
	uvicorn src.api:app --reload

db-start:
	docker compose up -d

db-stop:
	docker compose down

db-reset:
	docker compose down && docker compose up -d
