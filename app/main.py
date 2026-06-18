from fastapi import FastAPI
from app.api import books, categories
from app.db.db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Octagon Backend API",
    description="API для работы с Книгами и Категориями",
    version="1.0.0"
)

app.include_router(categories.router)
app.include_router(books.router)

@app.get("/health", tags=["System"])
def health_check():
    return {"status": "alive"}