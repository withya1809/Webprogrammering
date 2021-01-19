"""
Assignment #8: Webshop
"""

from flask import Flask, request, g, render_template, redirect, url_for, session
import mysql.connector

app = Flask(__name__)

# Application config
app.config["DATABASE_USER"] = "root"
app.config["DATABASE_PASSWORD"] = "aKLM25ee"
app.config["DATABASE_DB"] = "dat310"
app.config["DATABASE_HOST"] = "localhost"
app.debug = True  # only for development!
app.secret_key = 'some_secret'  # needed for seshion

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
    products = getProducts()
    # TODO: retrieve products from database

    # get cart items from session
    cart = session.get("cart", {})
    return render_template("index.html", products = products, cart=cart)


@app.route("/product/<int:pid>")
def product(pid):
    products = getProducts()
    # TODO: retrieve products from database


    # get cart items from session
    cart = session.get("cart", {})
    if pid in products.keys():
        product = products[pid]
        product["pid"] = pid

        # compute and format total price
        mytotal = (product["price"] * (100 - product["discount"])/100.0)
        product["total"] = "{:.2f}".format(mytotal)
        return render_template("product.html", product=product, cart=cart)
    return redirect(url_for('index'))

@app.route("/add", methods = ["POST"])
def addToCart():
   
 # get pid, size and count from request
    pid = request.form.get('pid')
    count = int(request.form.get('count'))
    size = request.form.get('size')

    # get cart items from session
    cart = session.get("cart", {})


    # TODO: add item to cart (ckeck for duplicates)
    products = getProducts()

    total = ( products[int(pid)].get("price") * (100 - products[int(pid)].get("discount")) / 100.0 ) * count


    if pid in cart:
        if cart[pid].get("size") == size:
            cart[pid]["count"] += count
            cart[pid]["total"] += ( products[int(pid)].get("price") * (100 - products[int(pid)].get("discount")) / 100.0 ) * count
           

    else:
        cart[pid] = {
            'title' : products[int(pid)].get("title"),
            'count' : count,
            'size' : size,
            'price' : int(products[int(pid)].get("price")),
            'discount' : int(products[int(pid)].get("discount")),
            'total' : total
        }

    
       

    # save in session
    session["cart"] = cart
    return redirect(url_for('product', pid= pid))
    




@app.route("/cart",  methods=["GET", "POST"])
def cart():
    # get cart items from session
    cart = session.get("cart", {})

    # TOTAL PRICE    
    grand_total = 0
    for i in cart.values():
        pris = i["total"]
        grand_total += pris
    
    return render_template("cart.html", cart=cart, grand_total = grand_total)
    
   # return redirect(url_for('chekout'))



@app.route("/remove")
def remove():
    # TODO: get key from request and remove from cart in session
    return redirect(url_for("cart"))

@app.route("/checkout", methods=["POST"])
def checkout():
    
    cart = session.get("cart", {})
    
    firstname = request.form.get('first_name')
    lastname = request.form.get('last_name')
    email = request.form.get('email')
    street = request.form.get('street')
    city = request.form.get('city')
    postal = request.form.get('postal')

    
    grand_total = 0
    for i in cart.values():
        pris = i["total"]
        grand_total += pris
   # print(grand_total)
    # TODO: get address from request
    #   check that fields are not empty
    #   validate that AGB was checked
    #   retrieve cart from session and display checkout



    return render_template("checkout.html", cart=cart, grand_total = grand_total, 
    firstname = firstname, lastname = lastname, email = email, street = street, city = city, postal = postal)


@app.route("/checkout2", methods=["POST"])
def checkout2():
    
    cart = session.get("cart", {})

    firstname = request.form.get('first_name')
    lastname = request.form.get('last_name')
    email = request.form.get('email')
    street = request.form.get('street')
    city = request.form.get('city')
    postal = request.form.get('postal')

    address = { 
        'firstname' : firstname,
        'lastname' : lastname,
        'email' : email,
        'street' : street,
        'city' : city,
        'postal' : postal
    }

    ## ADD TO DATABASE ##
    
    # TODO: get address from request
    #   check that fields are not empty
    #   validate that AGB was checked
    #   retrieve cart from session
    #   save address to database (orders)
    #   save cart items to database (order_rows)

    # commit updates to orders and order_rows
    db = get_db()
    cur = db.cursor()
    cur.execute("INSERT INTO orders (first_name, last_name, email, street, city, postcode) VALUES (%s,%s,%s,%s,%s,%s)", 
    (firstname, lastname, email, street, city, postal ))
    #cur.execute ("INSERT INTO order_rows (product_id, count, size) VALUES (%s,%s,%s)", 
    #())
    db.commit()

    # TODO empty cart items from session

    # TODO: render template, including success or error message
    return render_template("checkout2.html")

def getProducts():
    # TODO: should retrieve products from database instead of hardcoded
    products = {}
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM products")
    prod = cur.fetchall()

    for (product_id,title,price,discount,img,description,details) in prod:
        products[product_id] = {
            'title' : title,
            'price' : price,
            'discount' : discount,
            'img' : img,
            'description' : description,
            'details' : details
        }
    #print(products[1].get("price"))    

    return products


if __name__ == "__main__":
    app.run()
