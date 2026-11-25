from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional

class RegisterRequest(BaseModel):
    full_name: str
    email: str
    password: str
    phone_number: str

class RegisterResponse(BaseModel):
    id: int
    full_name: str
    email: str
    password: str
    phone_number: str
    token: str

class LoginRequest(BaseModel):
    email: str
    password: str

class LoginResponse(BaseModel):
    id: int
    email: str
    full_name: str
    phone_number: str
    token: str

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

class STKPushRequest(BaseModel):
    sale_id : int
    amount : float
    phone_number : str    