# Phase-3-Project


# Order Management System

A command-line interface (CLI) application for managing customers, products, and orders, built with Python and SQLAlchemy.

##  Features

- **Customer Management**: Add and view customers
- **Product Management**: Add and view
- **Order Management**: Create orders, add products and calculate totals
- **Data Persistence**: SQLite database to store all information

## Technologies Used

- **Python 3.9+**
- **SQLAlchemy** (ORM for database management)
- **Click** (for building the CLI interface)
- **SQLite** (database)

##  Installation

### Prerequisites
- Python 3.9 or higher
- Pipenv (recommended) or pip

### Steps

1. **Clone or download the project files**
   
         git clone --  https://github.com/Adreen-99/Phase-3-Project
   
         cd order-management-system

2. **Create Virtual Environment** 

         pipenv install

         pipenv shell

3. **Install Dependencies**

         pip install / pyenv install

         pipenv shell / pip shell


4. **Run Database Migrations**

         python cli app/models.py

5. **Start the Application**

         python main.py

## Database Migrations
This project uses Alembic for database migrations.

1. To create a new migration after modifying models:

            alembic revision --autogenerate -m "Your migration message"

2. To apply migrations:

            alembic upgrade head


## Usage

Once the program runs, you’ll see a menu-driven CLI with options like:

1. Add a Customer
2. View Customers
3. Add a Product
4. View Products
5. Create an Order
6. View Orders
7. Update Stock
8. Exit


## Contributing

Fork the repository

Create a new feature branch:

      git checkout -b feature-new-function


Commit changes:

      git commit -m "Added new feature"


Push branch:

      git push origin feature-new-function


Open a Pull Request


## License

MIT License

Copyright (c) 2025 Adreen Nyawira G.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Author

Email:   githinjiadreen@gmail.com

GitHub:  https://github.com/Adreen-99