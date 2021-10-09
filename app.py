import os 
from flask import Flask

app = Flask(__name__)

@app.route('/shop')
def service_shop():
    return "Service name: shop"

@app.route('/cart')
def service_cart():
    return "Service name: cart"

@app.route('/payment')
def service_payment():
    return "Service name: payment"

@app.route('/checkout')
def service_checkout():
    return "Service name: checkout"

if __name__ == '__main__':
    app.run(port=8080, debug=True)
