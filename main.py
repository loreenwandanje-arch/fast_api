from fastapi import FastAPI
from data_schemas import ProductRequest,ProductResponse
from models import Base,Product,User
from sqlalchemy import create_engine,select
from sqlalchemy.orm import Session

app = FastAPI()

engine = create_engine("sqlite:///./fastduka_api.db", echo=True)

Base.metadata.create_all(engine)

session = Session(engine)

# def add_user():
#     user = User(
#         full_name = "loreen ruth",
#         email = "loreen@gmail.com",
#         password = "1234",
#         phone_number = "0734678865"
#         )
    
#     session.add(user)
#     session.commit()

# add_user()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/products", response_model=ProductResponse)
def create_product(prod: ProductRequest):
    # store in the database
    dbprod = Product(
        user_id=prod.user_id,  
        product_name=prod.product_name,
        buying_price=prod.buying_price,
        selling_price=prod.selling_price,
    )

    session.add(dbprod)
    session.commit()
    return dbprod

@app.get("/products", response_model=list[ProductResponse])
def get_products():
    query = select(Product)
    products = session.scalars(query)

    return products