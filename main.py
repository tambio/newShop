# app.py
from flask import Flask, render_template
import psycopg2
from config import db_name, user, password, host

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def fetch_data(query):
    with psycopg2.connect(database=db_name, user=user, host=host, password=password) as conn:
        with conn.cursor() as curs:
            curs.execute(query)
            result = curs.fetchall()
            column_names = [desc[0] for desc in curs.description]
            return render_template('show_data.html', column_names=column_names, data=result)

@app.route('/brands')
def show_brand():
    return fetch_data("SELECT * FROM brands")

@app.route('/categories')
def show_categories():
    return fetch_data("SELECT * FROM categories")

@app.route('/products')
def show_products():
    return fetch_data("SELECT * FROM products")

@app.route('/warehouses')
def show_warehouses():
    return fetch_data("SELECT * FROM warehouse")

@app.route('/orders')
def show_orders():
    return fetch_data("SELECT * FROM orders")

@app.route('/ordered_products')
def show_ordered_products():
    return fetch_data("SELECT * FROM ordered_products")

@app.route('/customers')
def show_customers():
    return fetch_data("SELECT * FROM customers")

@app.route('/product_availability')
def show_inventory():
    return fetch_data("SELECT * FROM product_availability")

@app.route('/shopping_cart')
def show_cart_products():
    return fetch_data("SELECT * FROM shopping_cart")

@app.route('/reviews')
def show_feedbacks():
    return fetch_data("SELECT * FROM reviews")

@app.route('/information')
def show_info():
    return fetch_data("""
        SELECT o.order_id, o.order_date, c.customer_name, d.delivery_date, d.delivery_address
        FROM orders o
        JOIN customers c ON o.customer_id = c.customer_id
        LEFT JOIN delivery d ON o.order_id = d.order_id;
    """)

@app.route('/deliveries')
def show_deliveries():
    return fetch_data("SELECT * FROM delivery")

if __name__ == '__main__':
    app.run(debug=True)
