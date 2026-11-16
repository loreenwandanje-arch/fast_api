from fastapi import FastAPI
from data_schemas import (
    ProductRequest, ProductResponse,
    PurchaseRequest, PurchaseResponse,
    SaleRequest, SaleResponse,
    SaleDetailRequest, SaleDetailResponse,
    PaymentRequest, PaymentResponse,
)
from models import Base, Product, Purchase, Sale, Sale_detail, Payment, User
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

@app.post("/purchases", response_model=PurchaseResponse)
def create_purchase(purchase: PurchaseRequest):
    dbpurchase = Purchase(
        product_id=purchase.product_id,
        purchase_date=purchase.purchase_date,
        total_amount=purchase.total_amount,
    )
    session.add(dbpurchase)
    session.commit()
    return dbpurchase

@app.get("/purchases", response_model=list[PurchaseResponse])
def get_purchases():
    query = select(Purchase)
    purchases = session.scalars(query)
    return purchases


@app.post("/sales", response_model=SaleResponse)
def create_sale(sale: SaleRequest):
    dbsale = Sale(
        user_id=sale.user_id,
        total_amount=sale.total_amount,
    )
    session.add(dbsale)
    session.commit()
    return dbsale

@app.get("/sales", response_model=list[SaleResponse])
def get_sales():
    query = select(Sale)
    sales = session.scalars(query)
    return sales


@app.post("/sale_details", response_model=SaleDetailResponse)
def create_sale_detail(detail: SaleDetailRequest):
    dbdetail = Sale_detail(
        sale_id=detail.sale_id,
        product_id=detail.product_id,
        quantity=detail.quantity,
    )
    session.add(dbdetail)
    session.commit()
    return dbdetail

@app.get("/sale_details", response_model=list[SaleDetailResponse])
def get_sale_details():
    query = select(Sale_detail)
    details = session.scalars(query)
    return details


@app.post("/payments", response_model=PaymentResponse)
def create_payment(payment: PaymentRequest):
    dbpayment = Payment(
        sale_id=payment.sale_id,
        amount=payment.amount,
        mrid=payment.mrid,
        crid=payment.crid,
        phone_number=payment.phone_number,
    )
    session.add(dbpayment)
    session.commit()
    return dbpayment

@app.get("/payments", response_model=list[PaymentResponse])
def get_payments():
    query = select(Payment)
    payments = session.scalars(query)
    return payments