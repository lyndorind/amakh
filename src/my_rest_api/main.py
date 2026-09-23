from fastapi import FastAPI

app = FastAPI()

# API Routes


@app.get("/")
def read_root():
    return {"message": "Welcome to the REST API"}


@app.get("/items")
def get_items():
    return [{"item_id": 1, "name": "Apple"}, {"item_id": 2, "name": "Banana"}]
