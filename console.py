import pdb
from models.product import Product
from models.manufacturer import Manufacturer

import repositories.product_repository as product_repository
import repositories.manufacturer_repository as manufacturer_repository

product_repository.delete_all()
manufacturer_repository.delete_all()

manufacturer_1 = Manufacturer("Spirit Publishing Ltd", "UK")
manufacturer_repository.save(manufacturer_1)

manufacturer_2 = Manufacturer("Crystals-R-Us", "UK")
manufacturer_repository.save(manufacturer_2)

manufacturer_3 = Manufacturer("Ghostly Electronics", "USA")
manufacturer_repository.save(manufacturer_3)

manufacturer_repository.select_all()

product_1 = Product("Haunted Houses of UK and Ireland", "Guidebook", 10, 6, 10, "Ghosts", manufacturer_1)
product_repository.save(product_1)

product_2 = Product("Crystal Ball", "120mm", 5, 30, 75, "Calrevoyancy", manufacturer_2)
product_repository.save(product_2)

product_3 = Product("Motion Detector", "Spiritual movement dectector", 8, 25, 50, "Ghosts", manufacturer_3)
product_repository.save(product_3)

products = [product_1, product_2, product_3]

print(products[1].manufacturer.name)




pdb.set_trace()