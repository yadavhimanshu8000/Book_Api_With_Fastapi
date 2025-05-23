from models import Book
from sqlalchemy.orm import Session
from schemas import BookCreate

def Create_book(db: Session, data: BookCreate):
    book_instance = Book(**data.model_dump())  
    db.add(book_instance)
    db.commit()
    db.refresh(book_instance)
    return book_instance


def get_book(db: Session):
    return db.query(Book).all()

def get_book_id(book_id: int, db: Session):
    return db.query(Book).filter(Book.id == book_id).first()

def update_book(db: Session, data: BookCreate, book_id: int):
    book_query = db.query(Book).filter(Book.id == book_id).first()
    if book_query:
        for key,value in data.model_dump().items():
            setattr(book_query,key,value)
        db.commit()
        db.refresh(book_query)
    return book_query


def delete_book(db:Session, book_id: int):
    book_query = db.query(Book).filter(Book.id == book_id).first()
    if book_query:
        db.delete(book_query)
        db.commit()
    return book_query
            


