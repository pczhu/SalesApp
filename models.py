from datetime import datetime
from flask.ext.sqlalchemy import SQLAlchemy
from SalesApp import app

db = SQLAlchemy(app)


class Category(db.Model):
    __tablename__ = "Category"
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.VARCHAR)
    
class Product(db.Model):
    __tablename__ = "Product"
    id = db.Column('id', db.Integer, primary_key=True)
    sku = db.Column('sku', db.VARCHAR)
    category_id = db.Column('category_id', db.Integer, db.ForeignKey('Category.id'))
    invcode = db.Column('invcode', db.VARCHAR)
    specificmodel = db.Column('specificmodel', db.VARCHAR)

    category = db.relationship('Category', foreign_keys=category_id, backref="products")
    
    


