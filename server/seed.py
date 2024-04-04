from app import db
from models import Farmer, Farm, Product

# Create some farmers
farmer1 = Farmer(username='farmer1', password='password1', bio='Lorem ipsum...')
farmer2 = Farmer(username='farmer2', password='password2', bio='Lorem ipsum...')

# Create some farms
farm1 = Farm(name='Farm 1', location='Location 1', size=100, farmer=farmer1)
farm2 = Farm(name='Farm 2', location='Location 2', size=200, farmer=farmer2)

# Create some products
product1 = Product(name='Product 1', description='Description 1', price=10.0, quantity_available=50, farm=farm1)
product2 = Product(name='Product 2', description='Description 2', price=20.0, quantity_available=100, farm=farm2)

# Add the objects to the session
db.session.add_all([farmer1, farmer2, farm1, farm2, product1, product2])

# Commit the session to the database
db.session.commit()
