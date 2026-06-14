from flask import Flask, render_template
import json

app = Flask(__name__)

with open("products.json") as f:
    products = json.load(f)
@app.route("/")
def home():
    return """
    <h1>QR Product System</h1>
    <a href="/product/P0001">View Product</a>
    """

@app.route('/product/<product_id>')
def product(product_id):
    product = products.get(product_id)

    if product:
        return render_template("product.html", product=product)
    else:
        return "Product not found"

if __name__ == '__main__':
    app.run(debug=True)

from flask import request, redirect

@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        new_id = request.form["id"]
        name = request.form["name"]
        frp = request.form["frp"]
        rubber = request.form["rubber"]
        mp = request.form["mp"]
        wo = request.form["wo"]

        with open("products.json") as f:
            products = json.load(f)

        products[new_id] = {
            "name": name,
            "FRP": frp,
            "Rubber": rubber,
            "MP": mp,
            "WO": wo,
            "image": "product1.jpg"
        }

        with open("products.json", "w") as f:
            json.dump(products, f, indent=4)

        return redirect("/admin")

    return """
    <h2>Add Product</h2>
    <form method="post">
        ID: <input name="id"><br>
        Name: <input name="name"><br>
        FRP: <input name="frp"><br>
        Rubber: <input name="rubber"><br>
        MP: <input name="mp"><br>
        WO: <input name="wo"><br>
        <button type="submit">Add</button>
    </form>
import os

if __name__ == "__main__":
    port =
int( os. environ. get( "PORT" , 10000))
    app.run(host="0.0.0.0", port=port)