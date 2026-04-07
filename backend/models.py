from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Customer(Base):
    __tablename__ = "customers"
    
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    paypal_order_id = Column(String, index=True)
    created_at = Column(DateTime, default=func.now())
    total_spent = Column(Float, default=0.0)
    minutes_credits = Column(Integer, default=0)
    last_active = Column(DateTime, default=func.now())

class Transaction(Base):
    __tablename__ = "transactions"
    
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer)
    paypal_order_id = Column(String, unique=True)
    amount = Column(Float)
    minutes_purchased = Column(Integer)
    status = Column(String, default="pending")
    created_at = Column(DateTime, default=func.now())
    completed_at = Column(DateTime, nullable=True)

