from flask import Flask,render_template,redirect,request

app = Flask(__name__)

productsVar = []


@app.route("/")
def index():
    return render_template("record.html")


@app.route("/registrar", methods=["POST"])
def createProduct():
    productName = request.form["productName"]
    price = request.form["price"]
    category = request.form["category"]

    print(f"""
    =========================
    Nombre   : {productName}
    Precio   : {price}
    Categoria: {category}
    =========================""")

    productsVar.append({
        "name":productName,
        "price":price,
        "category":category
    })

    return redirect("/res")


@app.route("/res")
def products():
    return render_template("res.html",products=productsVar)

@app.route("/ayuda")
def help():
    return render_template("ayuda.html")

if __name__ == "__main__":
    app.run(debug=True)