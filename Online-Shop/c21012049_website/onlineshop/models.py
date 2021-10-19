from datetime import datetime
from onlineshop import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin,db.Model):
  id=db.Column(db.Integer,primary_key=True)
  username=db.Column(db.String(15),unique=True,nullable=False)
  email=db.Column(db.String(120),unique=True,nullable=False)
  password_hash=db.Column(db.String(128))
  password=db.Column(db.String(60),nullable=False)
  basket = db.relationship('Baskets', backref='user', lazy=True)
  wishlist = db.relationship('Wishlist', backref='user', lazy=True)
  #post=db.relationship('Post',backref='user',lazy=True)
  #comment=db.relationship('Comment',backref='user',lazy=True)

  def __repr__(self):
    return f"User('{self.username}','{self.email}')"

  @property
  def password(self):
    raise AttributeError('password is not a readable attribute')

  @password.setter
  def password(self,password):
    self.password_hash=generate_password_hash(password)

  def verify_password(self,password):
    return check_password_hash(self.password_hash,password)

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))


class Product(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    price = db.Column(db.Float(), nullable=False)
    image_file = db.Column(db.String(40))
    description = db.Column(db.String(1024))
    basket = db.relationship('Baskets', backref='product', lazy=True)
    wishlist = db.relationship('Wishlist', backref='product', lazy=True)
    reviews= db.relationship('Reviews', backref='product', lazy=True)

    def __repr__(self):
        return f"Product('{self.name}', '{self.description}', '{self.image_file}', '{self.price}')"

class Reviews(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    comment = db.Column(db.String(150), nullable=False)

class Baskets(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)

    def __repr__(self):
        return f"Baskets('{self.user_id}', '{self.product_id}')"

class Wishlist(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)

    def __repr__(self):
        return f"Wishlist('{self.user_id}', '{self.product_id}')"
