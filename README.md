# My REST API

A simple REST service created for a university laboratory project.

## Technologies

* Python 3.14+
* FastAPI
* Uvicorn
* uv (Package and environment manager)

## Setup
Synchronize the project dependencies:
```bash
uv sync
```
Run the service with Uvicorn:
```bash
uv run uvicorn src.my_rest_api.main:app --reload
```
The service is available at http://localhost:8000.
Interactive Swagger documentation is available at http://localhost:8000/docs.

## Endpoints
* GET / — returns a message confirming that the service is running.
* GET /items — returns a list of items or specific item data.

## Usage
1. Install project dependencies.
2. Run the application: `uvicorn src.my_rest_api:main --reload`
3. Open `http://127.0.0.1:8000` in your browser.
