from fastapi import FastAPI
from data_schemas import ProductRequest, ProductResponse
from models import Product, SessionLocal

app = FastAPI()


@app.get("/")
def home():
    return {"Duka FastAPI Version": "1.0"}


@app.post("/products", response_model=ProductResponse)
def create_product(prod: ProductRequest):
    db = SessionLocal()
    try:
        dbprod = Product(
            user_id=1, 
            product_name=prod.name,
            buying_price=prod.buying_price,
            selling_price=prod.selling_price,
            stock_quantity=prod.stock_quantity,
        )
        db.add(dbprod)
        db.commit()
        db.refresh(dbprod)
        return ProductResponse(
            id=dbprod.id,
            name=dbprod.product_name,
            buying_price=dbprod.buying_price,
            selling_price=dbprod.selling_price,
            stock_quantity=dbprod.stock_quantity,
        )
    finally:
        db.close()