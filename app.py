"""Flask app for Cupcakes"""
from flask import Flask, request, render_template,  redirect, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db,  connect_db, Cupcake
# from forms import Sample_Form

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "ILessThan3You"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)


@app.route('/')
def home_page():
    cupcakes = Cupcake.query.all()
    return render_template('index.html', cupcakes=cupcakes)


@app.route('/api/cupcakes', methods=['GET'])
def list_cupcakes():
    cupcakes = [cupcake.serialize()
                for cupcake in Cupcake.query.all()]
    # Note that i dont understand exactly what is happening when I pass in cupcake to be equal to cupcake
    return jsonify(cupcakes=cupcakes)


@app.route('/api/cupcakes/<int:id>')
def cupcake_details(id):
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake=cupcake.serialize())


@app.route('/api/cupcakes', methods=['POST'])
def create_cupcake():
    flavor = request.json['flavor']
    size = request.json['size']
    image = request.json['image']
    rating = request.json['rating']
    cupcake = Cupcake(flavor=flavor, size=size, image=image, rating=rating)

    db.session.add(cupcake)
    db.session.commit()
    print(cupcake)
    res_json = jsonify(cupcake=cupcake.serialize())
    return (res_json, 201)


@app.route('/api/cupcakes/<int:id>', methods=['PATCH'])
def update_cupcake(id):
    data = request.json
    cupcake = Cupcake.query.get_or_404(id)
    cupcake.flavor = data.get('flavor', cupcake.flavor)
    cupcake.size = data.get('size', cupcake.size)
    cupcake.image = data.get('image', cupcake.image)
    cupcake.rating = data.get('rating', cupcake.rating)
    db.session.commit()
    return jsonify(cupcake=cupcake.serialize())


@app.route('/api/cupcakes/<int:id>', methods=['DELETE'])
def eat_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message='You ate this cupcake!')
