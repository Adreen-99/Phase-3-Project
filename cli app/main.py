import click

from CRUD import *

while True:
    click.secho("Welcome to the Order Management App ===", fg='green', bold=True)
    click.secho("Select Option to Proceed", fg='blue')
    click.secho("1 Customers", fg='yellow')
    click.secho("2 Products", fg='yellow')
    click.secho("3 Order", fg='yellow')
    click.secho("4 Exit", fg='red')

    user_input = click.prompt("Select Option", type=int)

#-----------------------------------Customers--------------------------------------- 
    if user_input == 1:
        click.secho("=== Customer Management ===", fg='blue', bold=True)
        click.secho("1. Add New Customer", fg='yellow')
        click.secho("2. List All Customers", fg='yellow')
        click.secho("3. Back to Main Menu", fg='green')
        
        customer_option = click.prompt("Select Customer Option", type=int)

        if customer_option == 1:
            click.secho("Adding New Customer...", fg='yellow')
            name = click.prompt("Enter Customer Name")
            email = click.prompt("Enter Email")
            phone = click.prompt("Enter Phone Number", default="")
            address = click.prompt("Enter Address", default="")
            try:
                msg = add_customer(name, email, phone, address)
                click.secho(msg, fg="green")
            except Exception as e:
                click.secho(f"Error Adding Customer: {e}", fg="red")
            click.prompt("Press Enter to continue...")

        elif customer_option == 2:
            click.secho("Listing All Customers...", fg='blue')
            try:
                customers = list_customers()
                if customers:
                    click.secho("\n=== CUSTOMERS LIST ===", fg='green', bold=True)
                    for customer in customers:
                        click.echo(f"ID: {customer.id} | Name: {customer.name} | Email: {customer.email} | Phone: {customer.phone}")
                else:
                    click.secho("No customers found!", fg='yellow')
            except Exception as e:
                click.secho(f"Error retrieving customers: {e}", fg="red")
            click.prompt("Press Enter to continue...")

        elif customer_option == 3:
            continue


#--------------------------------Products-----------------------------------------
    if user_input == 2:
        click.secho("Products Management ===",fg='blue')
        click.secho("1. Add New Product",fg='green')
        click.secho("2. List PProducts", fg='green')
        click.secho("3. Back to Main Menu", fg='yellow')
        
        product_option = click.prompt("Select Product Option", type=int)

        if product_option == 1:
            click.secho("Adding New Product....", fg="yellow")
            name = click.prompt("Enter Product Name")
            description = click.prompt("Enter Description")
            price = click.prompt("Enter Price", type=float)
            stock = click.prompt("Enter Stock", type=int)
            category = click.prompt("Enter Category")
            try:
                msg = add_product(name, description, price, stock, category)
                click.secho(msg, fg="green")
            except Exception as e:
                click.secho(f"Error Adding Product: {e}", fg="red")

        elif product_option == 2:
            click.secho("Listing All Products .....", fg='blue')  
            try:
                products = list_products()
                if products:
                    click.secho("\n=== PRODUCTS LIST ===", fg='green', bold=True)
                    for product in products:
                        click.echo(f"ID: {product.id} | Name: {product.name} | Price: ${product.price} | Stock: {product.stock} | Category: {product.category}")
                else:
                    click.secho("No products found!", fg='yellow')
            except Exception as e:
                click.secho(f"Error retrieving products: {e}", fg="red")
            click.prompt("Press Enter to continue...")

        elif product_option == 3:
            continue

#----------------------------------Order------------------------------------------------------------------------
    if user_input == 3:
            while True:
                click.secho("\n=== Order Management ===", fg='blue', bold=True)
                click.secho("1. Add New Order", fg='yellow')
                click.secho("2. List All Orders", fg='yellow')
                click.secho("3. Back to Main Menu", fg='green')

                order_option = click.prompt("Select Order Option", type=int)

                if order_option == 1:
                    click.secho("Adding New Order...", fg='yellow')
                    customer_id = click.prompt("Enter Customer ID", type=int)
                    product_id = click.prompt("Enter Product ID", type=int)
                    quantity = click.prompt("Enter Quantity", type=int)
                    try:
                        msg = add_order(customer_id, product_id, quantity)
                        click.secho(msg, fg="green")
                    except Exception as e:
                        click.secho(f"Error creating order: {e}", fg="red")
                    click.prompt("Press Enter to continue...")

                elif order_option == 2:
                    click.secho("Listing All Orders...", fg='blue')
                    try:
                        orders = list_orders()
                        if orders:
                            click.secho("\n=== ORDERS LIST ===", fg='green', bold=True)
                            for order in orders:
                                click.echo(
                                    f"Order ID: {order.id} | Customer: {order.customer.name} | "
                                    f"Product: {order.product.name} | Quantity: {order.quantity}"
                                )
                        else:
                            click.secho("No orders found!", fg='yellow')
                    except Exception as e:
                        click.secho(f"Error retrieving orders: {e}", fg="red")
                    click.prompt("Press Enter to continue...")

                elif order_option == 3:
                    break

        # ----------------------------------------- Exit ----------------------------------------------------------
    elif user_input == 4:
            click.secho("Exiting Order Management App... Goodbye!", fg='red', bold=True)
            break

    