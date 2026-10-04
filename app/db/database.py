from app.core.config import Config

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.dialects.postgresql import JSONB


# echo=True будет выводить в консоль все SQL-запросы, которые генерирует SQLAlchemy
engine = create_engine(Config.DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Ваша модель из предыдущих шагов
class FormTemplate(Base):
    __tablename__ = "form_templates"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    fields_schema = Column(JSONB, nullable=False)

def run_test():
    print("--- 1. СОЗДАНИЕ ТАБЛИЦ ---")
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    try:
        print("\n--- 2. ЗАПИСЬ ДАННЫХ В БД ---")
        test_form = FormTemplate(
            title="Тестовая анкета для проверки",
            fields_schema=[{"name": "test_field", "type": "text", "label": "Test"}]
        )
        db.add(test_form)
        db.commit()
        db.refresh(test_form)
        print(f"УСПЕХ! Форма сохранена под ID: {test_form.id}")

        print("\n--- 3. ЧТЕНИЕ ДАННЫХ ИЗ БД ---")
        fetched_form = db.query(FormTemplate).filter(FormTemplate.id == test_form.id).first()
        if fetched_form:
            print(f"НАЙДЕНО В БД: Название = '{fetched_form.title}'")
            print(f"СОДЕРЖИМОЕ JSONB = {fetched_form.fields_schema}")
        else:
            print("Ошибка: Запись не найдена.")

    except Exception as e:
        print(f"\nОШИБКА ПОДКЛЮЧЕНИЯ ИЛИ ЗАПИСИ: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    run_test()