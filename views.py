from flask import render_template, request, redirect, flash, url_for
from models import Category, Product, db
from SalesApp import app




@app.route('/')
def welcome():
    return render_template(
        'welcome.html'
    )


@app.route('/list_products')
def list_all():
    return render_template(
        'list_products.html',
        categories=Category.query.all(),
        products=Product.query.all(),

    )


@app.route('/list_products/<name>')
def list_products():
    category=Category.query.filter_by(name=name).first()
    return render_template(
        'list_products.html',
        products=Product.query.filter_by(category=category).all(),
        categories=Category.query.all(),

    )



@app.route('/<int:product_id>', methods=['GET', 'POST'])
def update_product(product_id):
    product = Product.query.get(product_id)
    if request.method == 'GET':
        return render_template(
            'new-product.html',
            product=product,
            categories=Category.query.all(),
        )
    else:
        category = Category.query.filter_by(id=request.form['category']).first()
        specificmodel = request.form['specificmodel']
        product.category = category
        product.specificmodel = specificmodel
        db.session.commit()
        return redirect('/list_products')



@app.route('/edit_category/<int:category_id>', methods=['GET', 'POST'])
def edit_category(category_id):
    category = Category.query.get(category_id)
    if request.method == 'GET':
        return render_template(
            'new-category.html',
            category=category
        )
    else:
        category_name = request.form['category']
        category.name = category_name
        db.session.commit()
        return redirect('/list_products')


@app.route('/delete-category/<int:category_id>', methods=['POST'])
def delete_category(category_id):
    if request.method == 'POST':
        category = Category.query.get(category_id)
        if not category.products:
            db.session.delete(category)
            db.session.commit()
        else:
            flash('You have Products in that category. Remove them first.')
        return redirect('/list_products')


@app.route('/delete-product/<int:product_id>', methods=['POST'])
def delete_product(product_id):
    if request.method == 'POST':
        product = Product.query.get(product_id)
        db.session.delete(product)
        db.session.commit()
        return redirect('/list_products')



@app.route('/new-category', methods=['GET', 'POST'])
def new_category():
    if request.method == 'POST':
        category = Category(name=request.form['category'])
        db.session.add(category)
        db.session.commit()
        return redirect('/list_products')
    else:
        return render_template(
            'new-category.html',
            page='new-category.html')



@app.route('/new-product', methods=['GET', 'POST'])
def new_product():
    if request.method == 'POST':
        category = Category.query.filter_by(id=request.form['category']).first()
        product = Product(category=category, sku = request.form['sku'], invcode = request.form['invcode'], specificmodel = request.form['specificmodel'])
        db.session.add(product)
        db.session.commit()
        return redirect('/list_products')
    else:
        return render_template('new-product.html',
            categories=Category.query.all(),
            page='new-product.html'
            
            )
