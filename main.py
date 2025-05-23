from fastapi import FastAPI, Depends

from sqlalchemy.orm import Session
from db import SessionLocal, engine    
from fastapi import FastAPI, Depends,HTTPException
import models,schemas,controller
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        


@app.get('/book/',response_model=list[schemas.Book])
def get_all_book(db: Session= Depends(get_db)):
    return controller.get_book(db)

@app.get('/book/{id}',response_model=schemas.Book)
def get_book_by_id(id: int, db: Session= Depends(get_db)):
    book_query = controller.get_book_id(id,db)
    if book_query:
        return book_query
    raise HTTPException(status_code=404, detail='invalid id ')

@app.post('/createbook/',response_model=schemas.Book)
def create_new_book(book: schemas.BookCreate, db:Session= Depends(get_db)):
    return controller.Create_book(db,book)


@app.put('/updatequery/{id}',response_model=schemas.Book)
def update_book_by_id( book: schemas.BookCreate, id: int, db: Session= Depends(get_db)):
    db_update = controller.update_book(db,book,id)
    if not db_update:
        raise HTTPException(status_code=404,detail= 'Book Not Found')
    return db_update


@app.delete('/delete/{id}',response_model=schemas.Book)
def delete_book(id: int, db: Session= Depends(get_db)):
    db_delete = controller.delete_book(db,id)
    if db_delete:
        return db_delete
    raise HTTPException(status_code=404,detail='Book Not Found')
    


    


