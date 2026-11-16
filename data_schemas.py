from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional

class ProductRequest(BaseModel) :
    product_name : str
    buying_price : float
    selling_price : float
    stock_quantity : int

class ProductResponse(BaseModel):
    id : int
    product_name : str
    buying_price : float
    selling_price : float
    stock_quantity : int

class PurchaseRequest(BaseModel):
    product_id : int
    purchase_date : date
    total_amount : float

class PurchaseResponse(BaseModel):
    id : int
    product_id : int
    purchase_date : date
    total_amount : float


class SaleRequest(BaseModel):
    user_id : int
    total_amount : float

class SaleResponse(BaseModel):
    id : int
    user_id : int
    total_amount : float


class SaleDetailRequest(BaseModel):
    sale_id : int
    product_id : int
    quantity : int

class SaleDetailResponse(BaseModel):
    id : int
    sale_id : int
    product_id : int
    quantity : int


class PaymentRequest(BaseModel):
    sale_id : int
    amount : float
    mrid : str
    crid : str
    phone_number : str

class PaymentResponse(BaseModel):
    id : int
    sale_id : int
    amount : float
    mrid : str
    crid : str
    phone_number : str
    transaction_code : Optional[str] = None
    status : str
    created_at : datetime
    updated_at : datetime