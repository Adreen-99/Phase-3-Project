from models import Customer, Product, Order, OrderItem, session

#Adding Customer
def add_customer(name, email, phone=None, address=None):
    new_cutomer = Customer(name= name, email= email, phone= phone , address= address)
    session.add(new_cutomer)
    session.commit()
    session.close()
    return f"Customer {name} added."

#Adding Product
def add_product(name, description, price, stock, category, created_at):
    new_product = Product(name=name, description=description, price=price, stock=stock, category=category, created_at=created_at)
    session.add(new_product)
    session.commit()
    session.close()
    return f"Product {name} added."

#Adding Order
def add_order(customer_id, order_date, status, total):
    new_order = Order(customer_id=customer_id, order_date=order_date, status=status, total=total)
    session.add(new_order)
    session.commit()
    session.close()
    return f"Order for Customer {customer_id} created."

#Adding Order Item
def add_order_item(order_id, product_id, quantity, price, subtotal):
    subtotal = quantity * price
    item = OrderItem(order_id=order_id, product_id=product_id, quantity=quantity, price=price, subtotal=subtotal)
    session.add(item)
    
    order = session.query(Order).get(order_id)
    if order:
        order.total += subtotal

    session.commit()
    session.close()
    return f"Item {product_id} added to Order {order_id}."
