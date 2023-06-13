from flask import Flask, render_template, request, redirect
from flask import Blueprint 
from models.product import Product
from models.manufacturer import Manufacturer
import repositories.product_repository as product_repository
import repositories.manufacturer_repository as manufacturer_repository

products_blueprint = Blueprint("products", __name__)

@products_blueprint.route("/products")
def products():
    print("triggered")
    products = product_repository.select_all()
    return render_template("products/index.html", all_products = products)

#NEW
@products_blueprint.route("/products/new", methods=['GET'])
def new_product():
    manufacturers = manufacturer_repository.select_all()
    return render_template("/products/new.html", all_manufacturers = manufacturers)

#CREATE
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


#EDIT
@products_blueprint.route("/products/<id>/edit", methods=['GET'])
def edit_product(id):
    product = product_repository.select(id)
    manufacturers = manufacturer_repository.select_all()
    return render_template('products/edit.html', product = product, all_manufacturers = manufacturers)

#UPDATE
@products_blueprint.route("/products/<id>", methods=['POST'])
def update_product(id):
    name = request.form['name']
    description = request.form['description']
    manufacturer_id = request.form['manufacturer_id']
    stock_quantity = request.form['stock_quantity']
    buying_cost = request.form['buying_cost']
    selling_price = request.form['selling_price']
    category = request.form['category']
    manufacturer = manufacturer_repository.select(manufacturer_id)
    product = Product(name, description, stock_quantity, buying_cost, selling_price, category, manufacturer, id)
    product_repository.update(product)
    return redirect('/products')


@products_blueprint.route("/manufacturers")
def manufacturers():
    manufacturers = manufacturer_repository.select_all()
    return render_template("/manufacturers/index.html", all_manufacturers = manufacturers)


#MANUFACTURER NEW
@products_blueprint.route("/manufacturers/new", methods=['GET'])
def new_manufacturer():
    return render_template("/manufacturers/new.html")


#MANUFACTURER CREATE
@products_blueprint.route("/manufacturers", methods=['POST'])
def create_manufacturer():
    name = request.form['name']
    location = request.form['location']
    contact = request.form['contact']
    manufacturer = Manufacturer(name, location, contact, id)
    manufacturer_repository.save(manufacturer)
    return redirect('/manufacturers')

#Manufacturer SHOW - WORKS
@products_blueprint.route("/manufacturers/<id>", methods=['GET'])
def show_manufacturer(id):
    manufacturer = manufacturer_repository.select(id)
    return render_template('/manufacturers/manufacturer.html', manufacturer = manufacturer)

#Product SHOW - WORKS
@products_blueprint.route("/products/<id>", methods=['GET'])
def show_product(id):
    product = product_repository.select(id)
    return render_template('/products/product.html', product = product)

#DELETE PRODUCT
@products_blueprint.route("/products/<id>/delete", methods=['POST'])
def delete_product(id):
    product_repository.delete(id)
    return redirect("/products")


#DELETE MANUFACTURER
@products_blueprint.route("/manufacturers/<id>/delete", methods=['POST'])
def delete_manufacturer(id):
    manufacturer_repository.delete(id)
    return redirect("/manufacturers")

#EDIT
@products_blueprint.route("/manufacturers/<id>/edit", methods=['GET'])
def edit_manufacturer(id):
    manufacturer = manufacturer_repository.select(id)
    return render_template('/manufacturers/edit.html', manufacturer = manufacturer)

#UPDATE MANUFACTURER
@products_blueprint.route("/manufacturers/<id>", methods=['POST'])
def update_manufacturer(id):
    name = request.form['name']
    location = request.form['location']
    contact = request.form['contact']
    manufacturer = Manufacturer(name, location, contact, id)
    manufacturer_repository.update(manufacturer)
    return redirect('/manufacturers')

