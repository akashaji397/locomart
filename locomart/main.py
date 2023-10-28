from flask import Flask
from admin import admin
from shop import shop
from public import public
from database import *


app=Flask(__name__)
app. secret_key="abc"

app.register_blueprint(admin)
app.register_blueprint(shop)
app.register_blueprint(public)

app.run(debug=True,port='5055')

