from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Farmer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    bio = db.Column(db.Text)
    profile_picture = db.Column(db.String(100))

    farms = db.relationship('Farm', backref='farmer', lazy=True)

class Farm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    size = db.Column(db.Float, nullable=False)
    farmer_id = db.Column(db.Integer, db.ForeignKey('farmer.id'), nullable=False)

    products = db.relationship('Product', backref='farm', lazy=True)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    quantity_available = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(100))

    farm_id = db.Column(db.Integer, db.ForeignKey('farm.id'), nullable=False)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    ordered_at = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), nullable=False)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text)
