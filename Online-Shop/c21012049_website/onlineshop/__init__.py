from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '03f00a4c3c310dcf92917f2e3d40fb91d7f8ddc7fb99df45'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://c21012049:NNMXxa8JSWa34iq@csmysql.cs.cf.ac.uk:3306/c21012049_shopbase'

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

"""
from onlineshop.models import Product
db.session.add(Product(name="Rare 5* Venti keyring",image_file="Venti.png", description="Exclusive limited time Venti keyring from Ballad in Goblets. Gain the vision of anemo with this new and exclusive keyring, made by mihoyo themself! Material: Thick Acrylic (3mm Thick) Size: 62mm X 63 mm, Ke Qing, Hu Tao and Xiao expected to be shipped out in Early May. Place your order now to secure your favorite Genshin Impact merchandise!", price="12.49"))

db.session.add(Product(name="Rare 5* Childe Keyring", image_file="Childe.png", description="Exclusive limited time Childe keyring from farewell of Snezhnaya. Feel the power of a fatui harbinger as you own this new vision like keyring. Exclusive keyring made by Mihoyo. Material: Thick Acrylic (3mm Thick) Size: 62mm X 63 mm Ke Qing, Hu Tao and Xiao expected to be shipped out in Early May. Place your order now to secure your favorite Genshin Impact merchandise!", price="7.49"))

db.session.add(Product(name="Rare 5* Hu tao keyring", image_file="Hutao.png", description="Feel at rest with this new exclusive and limited time Moment of Bloom: Hy Tao keyring. Make sure you never wear this around QiQi! Material: Thick Acrylic (3mm Thick) Size: 62mm X 63 mm Ke Qing, Hu Tao and Xiao expected to be shipped out in Early May. Place your order now to secure your favorite Genshin Impact merchandise!", price="10.99"))

db.session.add(Product(name="Diona keyring", image_file="Diona.png", description="Join Diona in the crashing of the wine industry with this new cute and limited edition key ring made by Mihoyo directly! Material: Thick Acrylic (3mm Thick) Size: 62mm X 63 mm Ke Qing, Hu Tao and Xiao expected to be shipped out in Early May. Place your order now to secure your favorite Genshin Impact merchandise!", price="5.49"))

db.session.add(Product(name="Xinyan Keyring", image_file="Xinyan.png", description="Feel the flames of passion with this new Xinyan Keyring. The power of rock flows through you! Limited edition keyring from Mihoyo. Material: Thick Acrylic (3mm Thick) Size: 62mm X 63 mm Ke Qing, Hu Tao and Xiao expected to be shipped out in Early May. Place your order now to secure your favorite Genshin Impact merchandise!", price="5.49"))

db.session.add(Product(name="Rare 5* LIMITED Zhongli Keyring", image_file="Zhongli.png", description="Will you have order!?! You will with this new keyring of the Geo god Zhongli from the Gentry of Hermitage banner. Feel closer to Liyue with this brand new highly exclusive Keyring. KEYRING LIMITED FOR NEXT 48HRS; NO MORE WILL BE IN PRODUCTION AFTER THIS DATE. **LIMITED EDITION**. Material: Thick Acrylic (3mm Thick) Size: 62mm X 63 mm Ke Qing, Hu Tao and Xiao expected to be shipped out in Early May. Place your order now to secure your favorite Genshin Impact merchandise!", price="29.99"))
db.session.commit()
"""

from onlineshop import routes
