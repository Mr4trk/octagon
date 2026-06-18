from app.db.db import SessionLocal
from app.db.crud import get_books, get_categories

db = SessionLocal()

print("--- КАТЕГОРИИ ТОВАРОВ ---")
categories = get_categories(db)
for cat in categories:
    print(f"ID: {cat.id} | Категория: {cat.title}")

print("\n--- СПИСОК КНИГ ИЗ БАЗЫ ДАННЫХ ---")
books = get_books(db)
for book in books:
    print(
        f"Книга: '{book.title}' | Цена: {book.price} руб. | Категория ID: {book.category_id}"
    )

db.close()