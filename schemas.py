from pydantic import BaseModel
from models import *

class BookBase(BaseModel):
    Book_title : str
    description : str
    author : str
    year : str
    
    
class BookCreate(BookBase):
    pass

class Book(BookBase):
    id : int
    
    class config:
        from_attribute = True
        
        
        

    
    