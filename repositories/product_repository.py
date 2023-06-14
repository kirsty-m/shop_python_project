from db.run_sql import run_sql
from models.product import Product
from models.manufacturer import Manufacturer
import repositories.manufacturer_repository as manufacturer_repository

def save(product):
    sql = "INSERT INTO products (name, description, stock_quantity, buying_cost, selling_price, category, manufacturer_id) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [product.name, product.description, product.stock_quantity, product.buying_cost, product.selling_price, product.category, product.manufacturer.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    product.id = id
    return product

def select_all():
    products = []
    sql = "SELECT * FROM products"
    results = run_sql(sql)

    for row in results:
        manufacturer = manufacturer_repository.select(row['manufacturer_id'])
        product = Product(row['name'], row['description'], row['stock_quantity'], row['buying_cost'], row['selling_price'], row['category'], manufacturer, row['id'])
        products.append(product)
    return products

def select(id):
    product = None
    sql = "SELECT * FROM products WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        manufacturer = manufacturer_repository.select(result['manufacturer_id'])
        product = Product(result['name'], result['description'], result['stock_quantity'], result['buying_cost'], result['selling_price'], result['category'], manufacturer, result['id'])
    return product

def delete_all():
    sql = "DELETE FROM products"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM products WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(product):
    sql = "UPDATE products SET (name, description, stock_quantity, buying_cost, selling_price, category, manufacturer_id) = (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [product.name, product.description, product.stock_quantity, product.buying_cost, product.selling_price, product.category, product.manufacturer.id, product.id]
    run_sql(sql, values)


#FILTER PRODUCTS BY CATEGORY
def select_by_category(category):
    products = []
    sql = "SELECT * FROM products WHERE category = %s"
    values = [category]
    results = run_sql(sql, values)


#FILTER PRODUCTS BY MANUFACTURER
def select_by_manufacturer(manufacturer):
    products = []
    sql = "SELECT * FROM products WHERE manufacturer_id = %s"
    values = [manufacturer_id]
    results = run_sql(sql, values)