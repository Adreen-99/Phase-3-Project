from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from datetime import datetime

Base = declarative_base()
engine = create_engine('sqlite:///orders.db')
Session = sessionmaker(bind=engine)
session = Session()

class Customer(Base):
    __tablename__ = 'customers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    phone = Column(String)
    address = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    
    # Relationships
    orders = relationship("Order", back_populates="customer", cascade="all, delete-orphan")

class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    stock = Column(Integer)
    category = Column(String)
    created_at = Column(DateTime, default=datetime.now)
    
    # Relationships
    order_items = relationship("OrderItem", back_populates="product", cascade="all, delete-orphan")

class Order(Base):
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    order_date = Column(DateTime, default=datetime.now)
    status = Column(String, default='pending')  # pending, completed, cancelled
    total = Column(Float, default=0.0)
    
     # Relationships
    customer = relationship("Customer", back_populates="orders")
    items = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")

class OrderItem(Base):
    __tablename__ = 'order_items'
    
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)
    price = Column(Float)
    subtotal = Column(Float)

    # Relationships
    order = relationship("Order", back_populates="items")
    product = relationship("Product", back_populates="order_items")


# Create all tables
Base.metadata.create_all(engine)

print("Database setup complete!")