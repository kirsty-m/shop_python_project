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

def select_all():
    manufacturers = {}
    sql = "SELECT * FROM manufacturers"
    results = run_sql(sql)

    for row in results:
        manufacturer = Manufacturer(row['name'], row['location'], row['id'])
        manufacturers.append(manufacturer)
    return manufacturers