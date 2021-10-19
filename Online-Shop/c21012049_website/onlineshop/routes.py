from flask import render_template, url_for, request, redirect, flash
from onlineshop import app, db
from onlineshop.models import User, Product, Reviews, Baskets, Wishlist
from onlineshop.forms import RegistrationForm, CheckoutForm, LoginForm, ReviewForm
from flask_login import login_user, logout_user, login_required, current_user
import time

@app.route("/")
@app.route("/home")
def home():
  products=Product.query.all()
  return render_template('home.html', products=products)


@app.route("/home/sortName")
def sortName():
    products=Product.query.order_by(Product.name).all()
    return render_template('home.html', products=products)

@app.route("/home/highToLow")
def sortHigh():
    products=Product.query.order_by(Product.price.desc()).all()
    return render_template('home.html', products=products)

@app.route("/home/lowToHigh")
def sortLow():
    products=Product.query.order_by(Product.price).all()
    return render_template('home.html', products=products)




@app.route("/product/<int:product_id>")
def product(product_id):
    product = Product.query.get_or_404(product_id)
    users=User.query.all()
    reviews=Reviews.query.filter_by(product_id=product_id).all()
    return render_template('product.html', product=product, users = users, reviews=reviews)

@app.route("/updatebasket/<int:user_id>/<int:product_id>")
def updatebasket(user_id, product_id):
    basket = Baskets(user_id=user_id, product_id=product_id)
    current_item = Baskets.query.filter_by(user_id=user_id, product_id=product_id).first()
    if current_item is None:
        db.session.add(basket)
        db.session.commit()
        flash('Added to basket!')
    return redirect(url_for('home'))

@app.route("/wishlist/<int:user_id>")
def wishlist(user_id):
    current_wishlist = Wishlist.query.filter_by(user_id=user_id).all()
    products=Product.query.all()
    return render_template('wishlist.html', products=products, wishlist=current_wishlist)


@app.route("/updatewishlist/<int:user_id>/<int:product_id>")
def updatewishlist(user_id, product_id):
    wishlist = Wishlist(user_id=user_id, product_id=product_id)
    current_item = Wishlist.query.filter_by(user_id=user_id, product_id=product_id).first()
    if current_item is None:
        db.session.add(wishlist)
        db.session.commit()
        flash('Added to wishlist!')
    return redirect(url_for('home'))

@app.route("/removefrombasket/<int:user_id>/<int:product_id>")
def removefrombasket(user_id, product_id):
    Baskets.query.filter_by(user_id=user_id, product_id=product_id).delete()
    db.session.commit()
    return redirect(url_for('basket', user_id=user_id))

@app.route("/removefromwishlist/<int:user_id>/<int:product_id>")
def removefromwishlist(user_id, product_id):
    Wishlist.query.filter_by(user_id=user_id, product_id=product_id).delete()
    db.session.commit()
    return redirect(url_for('wishlist', user_id=user_id))


@app.route("/shoppingbasket/<int:user_id>")
@login_required
def basket(user_id):
    current_basket = Baskets.query.filter_by(user_id=user_id).all()
    products=Product.query.all()
    sum=0
    for item in current_basket:
        sum += products[item.product_id-1].price
    return render_template('basket.html', products=products, basket=current_basket, total="{:.2f}".format(sum))

@app.route("/checkout/<int:user_id>")
@login_required
def checkout(user_id):
    form = CheckoutForm()
    current_basket = Baskets.query.filter_by(user_id=user_id).all()
    products=Product.query.all()
    sum=0
    for item in current_basket:
        sum += products[item.product_id-1].price
    if form.validate_on_submit():
        return redirect(url_for('home'))
    else:
        flash('Incorrect payment details')
    return render_template('checkout.html', form=form, products = products, basket=current_basket, total="{:.2f}".format(sum))

@app.route("/register",methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,email=form.email.data,password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('register.html',title='Register',form=form)

@app.route("/login",methods=['GET','POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user is not None and user.verify_password(form.password.data):
      login_user(user)
      return redirect(url_for('home'))
  flash('Invalid email address or password.')
  return render_template('login.html',title='Login',form=form)

@app.route("/writeReview/<int:user_id>/<int:product_id>", methods=['GET','POST'])
@login_required
def leaveAReview(user_id, product_id):
    form = ReviewForm()
    if form.validate_on_submit():
        review = Reviews(user_id=user_id, product_id=product_id, comment=form.Comment.data)
        db.session.add(review)
        db.session.commit()
    return render_template('comment.html', form=form)



@app.route("/logout")
def logout():
  logout_user()
  flash('Logout (probably?) successful!')
  return redirect(url_for('home'))
