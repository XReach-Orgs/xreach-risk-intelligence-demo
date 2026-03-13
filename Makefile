.PHONY: backend-install backend-run backend-test train-model frontend-install frontend-run

backend-install:
	cd backend && python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt -r requirements-dev.txt

backend-run:
	cd backend && . .venv/bin/activate && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

backend-test:
	cd backend && . .venv/bin/activate && pytest -q

train-model:
	cd backend && . .venv/bin/activate && python -m app.ml.training.train

frontend-install:
	cd frontend && npm install

frontend-run:
	cd frontend && npm run dev