import os 
from flask import Flask

app = Flask(__name__)

@app.route('/shop')
def service():
    return "Service name: shop"

@app.route('/cart')
def service():
    return "Service name: cart"

@app.route('/payment')
def service():
    return "Service name: payment"

@app.route('/checkout')
def service():
    return "Service name: checkout"
