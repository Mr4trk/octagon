from app.db.db import Base, SessionLocal, engine
from app.db.crud import create_book, create_category

Base.metadata.create_all(bind=engine)

db = SessionLocal()

cat1 = create_category(db, title="Программирование")
cat2 = create_category(db, title="Фантастика")

create_book(
    db,
    title="Изучаем Python",
    description="Полное руководство",
    price=1200.0,
    category_id=cat1.id,
)
create_book(
    db, title="Грокаем алгоритмы", description="Иллюстрированное пособие", price=850.0, category_id=cat1.id
)
create_book(
    db, title="Дюна", description="Научная фантастика Фрэнка Герберта", price=950.0, category_id=cat2.id
)

db.close()
print("База данных успешно инициализирована и заполнена тестовыми данными!")