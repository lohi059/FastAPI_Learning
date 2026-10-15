from typing import annotated

from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str
    email: str
    password: str

class Product(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    description: str
    price: float
    inventory_count: int

class Supplier(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    contact_email: str
    phone_number: str

class Location(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    address: str
    city: str
    state: str
    zip_code: str

class Transaction(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    product_id: int | None = Field(default=None, foreign_key="product.id")
    quantity: int
    total_price: float
    transaction_date: str
    transaction_type: str
    supplier_id: int | None = Field(default=None, foreign_key="supplier.id") 
    