from flask import Flask
app=Flask(__name__)
from protect.views.login import log
app.register_blueprint(log)


