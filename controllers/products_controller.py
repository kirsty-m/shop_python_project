from flask import Flask, render_template, request, redirect
from flask import Blueprint 
from models.product import Product
import repositories.product_repository as product_repository
import repositories.manufacturer_repository as manufacturer_repository

products_blueprint = Blueprint("products", __name__)

@products_blueprint.route("/products")
def products():
    products = product_repository.select_all()
    return render_template("products/index.html", all_products = products)

@products_blueprint.route("/products/new", methods=['GET'])
def new_product():
    manufacturers = manufacturer_repository.select_all()
    return render_template("/products/new.html", all_manufacturers = manufacturers)

@products_blueprint.route("/products", methods=['POST'])
def create_product():
    name = request.form['name']
    description = request.form['description']
    manufacturer_id = request.form['manufacturer_id']
    stock_quantity = request.form['stock_quantity']
    buying_cost = request.form['buying_cost']
    selling_price = request.form['selling_price']
    category = request.form['category']
    manufacturer = manufacturer_repository.select(manufacturer_id)
    product = Product(name, description, stock_quantity, buying_cost, selling_price, category, manufacturer)
    product_repository.save(product)
    return redirect('/products')

@products_blueprint.route("/products/<id>", methods=['GET'])
def show_product(id):
    product = product_repository.select(id)
    return render_template('/products/product.html', product = product)