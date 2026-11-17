from fastapi import FastAPI, HTTPException
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
        user_id=1, 
        product_name=prod.product_name,
        buying_price=prod.buying_price,
        selling_price=prod.selling_price,
        stock_quantity=prod.stock_quantity,
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

@app.put("/products/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, prod: ProductRequest):
    dbprod = session.get(Product, product_id)
    if dbprod is None:
        raise HTTPException(status_code=404, detail="Product not found")

    dbprod.product_name = prod.product_name
    dbprod.buying_price = prod.buying_price
    dbprod.selling_price = prod.selling_price
    dbprod.stock_quantity = prod.stock_quantity

    session.commit()
    return dbprod


@app.put("/purchases/{purchase_id}", response_model=PurchaseResponse)
def update_purchase(purchase_id: int, purchase: PurchaseRequest):
    dbpurchase = session.get(Purchase, purchase_id)
    if dbpurchase is None:
        raise HTTPException(status_code=404, detail="Purchase not found")

    dbpurchase.product_id = purchase.product_id
    dbpurchase.purchase_date = purchase.purchase_date
    dbpurchase.total_amount = purchase.total_amount

    session.commit()
    return dbpurchase


@app.put("/sales/{sale_id}", response_model=SaleResponse)
def update_sale(sale_id: int, sale: SaleRequest):
    dbsale = session.get(Sale, sale_id)
    if dbsale is None:
        raise HTTPException(status_code=404, detail="Sale not found")

    dbsale.user_id = sale.user_id
    dbsale.total_amount = sale.total_amount

    session.commit()
    return dbsale


@app.put("/sale_details/{detail_id}", response_model=SaleDetailResponse)
def update_sale_detail(detail_id: int, detail: SaleDetailRequest):
    dbdetail = session.get(Sale_detail, detail_id)
    if dbdetail is None:
        raise HTTPException(status_code=404, detail="Sale detail not found")

    dbdetail.sale_id = detail.sale_id
    dbdetail.product_id = detail.product_id
    dbdetail.quantity = detail.quantity

    session.commit()
    return dbdetail


@app.put("/payments/{payment_id}", response_model=PaymentResponse)
def update_payment(payment_id: int, payment: PaymentRequest):
    dbpayment = session.get(Payment, payment_id)
    if dbpayment is None:
        raise HTTPException(status_code=404, detail="Payment not found")

    dbpayment.sale_id = payment.sale_id
    dbpayment.amount = payment.amount
    dbpayment.mrid = payment.mrid
    dbpayment.crid = payment.crid
    dbpayment.phone_number = payment.phone_number

    session.commit()
    return dbpayment