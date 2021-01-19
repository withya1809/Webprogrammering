"""
Assignment #8: Webshop
"""

from flask import Flask, request, g, abort
import mysql.connector
import json

app = Flask(__name__)

# Application config
app.config["DATABASE_USER"] = "root"
app.config["DATABASE_PASSWORD"] = "foobarfoo"
app.config["DATABASE_DB"] = "dat310"
app.config["DATABASE_HOST"] = "localhost"
app.debug = True  # only for development!

def get_db():
    if not hasattr(g, "_database"):
        print("create connection")
        g._database = mysql.connector.connect(host=app.config["DATABASE_HOST"], user=app.config["DATABASE_USER"],
                                       password=app.config["DATABASE_PASSWORD"], database=app.config["DATABASE_DB"])
    return g._database


@app.teardown_appcontext
def teardown_db(error):
    """Closes the database at the end of the request."""
    db = getattr(g, '_database', None)
    if db is not None:
        print("close connection")
        db.close()

@app.route("/")
def index():
    return app.send_static_file("index.html")
    
@app.route("/products")
def products():
    # retrieve products from database and return a JSON
    return json.dumps(getProducts())


@app.route("/order", methods=["POST"])
def order():
    data = request.get_json()
    
    # save address into orders table
    # if cur = db.cursor()
    # use cur = cur.lastrowid to get the new order_id

    # save shoppingcart items as multiple rows into order_row
    
    # commit saving order and cart
    db = get_db()
    db.commit()
    return ""

def getProducts():
    # TODO: should retrieve products from database instead of hardcoded
    products = {}
    products[1]= {
        "title": 'Special socks',
        "price": 170,
        "discount": 18,
        "img": "tsock.jpg",
        "description": "Perfectly good socks!",
        "details": ('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sodales neque quis nisi facilisis lobortis. Nam'
                'efficitur eget nisi sit amet bibendum. Vestibulum elementum faucibus quam ut posuere. Vivamus pellentesque'
                'luctus nunc at bibendum. Mauris viverra ultrices nisi, sit amet imperdiet lectus accumsan eu. Morbi ornare diam'
                'nulla, nec aliquet nisl accumsan dictum. Mauris sit amet tellus in ipsum commodo hendrerit. Nunc at mollis'
                'magna. Proin felis nibh, venenatis non lobortis quis, ullamcorper nec dolor. Vivamus tempus volutpat fringilla.'
                'Praesent volutpat sit amet massa nec ultricies. Curabitur sollicitudin pharetra tortor in dictum. In mattis orci'
                'vel augue vehicula rutrum. Nullam vitae sollicitudin orci.')
    }
    products[2]= {
        "title": 'Good socks',
        "price": 170,
        "discount": 0,
        "img": "tsock.jpg",
        "description": "Keep you warm.",
        "details": ('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sodales neque quis nisi facilisis lobortis. Nam'
                'efficitur eget nisi sit amet bibendum. Vestibulum elementum faucibus quam ut posuere. Vivamus pellentesque'
                'luctus nunc at bibendum. Mauris viverra ultrices nisi, sit amet imperdiet lectus accumsan eu. Morbi ornare diam'
                'nulla, nec aliquet nisl accumsan dictum. Mauris sit amet tellus in ipsum commodo hendrerit. Nunc at mollis'
                'magna. Proin felis nibh, venenatis non lobortis quis, ullamcorper nec dolor. Vivamus tempus volutpat fringilla.'
                'Praesent volutpat sit amet massa nec ultricies. Curabitur sollicitudin pharetra tortor in dictum. In mattis orci'
                'vel augue vehicula rutrum. Nullam vitae sollicitudin orci.')
    }
    return products


if __name__ == "__main__":
    app.run()
