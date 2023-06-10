from db.run_sql import run_sql
from models.manufacturer import Manufacturer
from models.product import Product

def save(manufacturer):
    sql = "INSERT INTO manufacturers (name, location) VALUES (%s, %s) RETURNING *"
    values = [manufacturer.name, manufacturer.location]
    results = run_sql(sql, values)
    id = results[0]['id']
    manufacturer.id = id
    return manufacturer

