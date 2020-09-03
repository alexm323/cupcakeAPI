from app import app
from models import db, Cupcake


db.drop_all()
db.create_all()

c1 = Cupcake(
    flavor="cherry",
    size="large",
    rating=5,
    image='https://thriftyjinxy.com/wp-content/uploads/2017/01/Maraschino-Cherry-Cupcakes-480x480.jpg'
)

c2 = Cupcake(
    flavor="chocolate",
    size="small",
    rating=9,
    image="https://www.bakedbyrachel.com/wp-content/uploads/2018/01/chocolatecupcakesccfrosting1_bakedbyrachel.jpg"
)

c3 = Cupcake(
    flavor='vanilla',
    size='medium',
    rating=8,
    image='https://natashaskitchen.com/wp-content/uploads/2020/05/Vanilla-Cupcakes-3.jpg'

)
c4 = Cupcake(
    flavor='red velvet',
    size='large',
    rating=10,
    image='https://toughcupcakes.files.wordpress.com/2013/08/img_05631.jpg?w=487'

)

db.session.add_all([c1, c2, c3, c4])
db.session.commit()
