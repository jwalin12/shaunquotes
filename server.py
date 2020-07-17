from flask import Flask, request
from flask_restful import Resource, Api
import pandas as pd
import numpy as np

app = Flask(__name__)
api = Api(app)

quotes = pd.read.csv("/Users/jwalinjoshi/PycharmProjects/shaunquotes/scrape/spid-bestoflifemag.com.csv")


class getQuote(Resource):

    def __init__(self):
        pass

    def get(self):
        idx = np.random.randint(0, len(quotes))
        return quotes[idx]


api.add(getQuote, '/')
if __name__ == "__main__":
    app.run(debug=True)
