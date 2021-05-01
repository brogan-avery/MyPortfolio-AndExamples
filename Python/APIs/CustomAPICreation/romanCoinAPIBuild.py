"""
***************************************************
Title: Roman Coin API Creation
Author: Brogan Avery
Created: 2020-10-23
Description : Builds a custom API for Roman Coin data using flask framework
OS: macOS Catalina
Copyright : This is my own original work based on specifications issued by the course instructor
***************************************************
"""

import csv
import flask
from flask import request, jsonify
import sqlite3
from sqlite3 import Error

# function that returns dictionaries
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

#————————————————————————————————————————————————————————————————————————————————————
if __name__ == '__main__':
# for using an API with connection to a csv file rather than a database
    # # read csv file into list of dictionaries
    #     with open('RomanCoins.csv') as file:
    #         coins = [{k: v for k, v in row.items()}
    #                       for row in csv.DictReader(file, delimiter=",")]
    # print(coins)

    app = flask.Flask(__name__) # creates flask object
    app.config["DEBUG"] = True

# index page
    @app.route('/', methods=['GET']) # route to url
    def home():
        return '''<h1>Roman Coins</h1>'''

# json output
    @app.route('/api/v1/resources/coins/all', methods=['GET']) #route to url
    def api_all(): # returns all the coin info
        conn = sqlite3.connect('romanCoin.db')
        conn.row_factory = dict_factory  # function that returns dictionaries instead of lists to better output json
        cur = conn.cursor()
        allCoinRows = cur.execute('SELECT * FROM Coins;').fetchall()
        return jsonify(allCoinRows)

# custom error page
    @app.errorhandler(404)
    def page_not_found(e):
        return "<h1>404</h1><p>The resource could not be found.</p>", 404

    # @app.route('/api/v1/resources/coins', methods=['GET'])
    # def api_denomination():
    #     # Check if an author was provided as part of the URL.
    #     # If author is provided, assign it to a variable.
    #     # If no author is provided, display an error in the browser.
    #     if 'denomination' in request.args:
    #         denomination = request.args['denomination']
    #     else:
    #         return "Error: No denomination field provided. Please specify a denomination."
    #
    #     # Create an empty list for our results
    #     results = []
    #
    #     # Loop through the data and match results that fit the requested denomination.
    #     for coin in coins:
    #         if coin['Denomination'] == denomination:
    #             results.append(coin)
    #
    #     # Use the jsonify function from Flask to convert our list of
    #     # Python dictionaries to the JSON format.
    #     return jsonify(results)

    @app.route('/api/v1/resources/coins', methods=['GET'])
    def api_filter():
        query_parameters = request.args

        CoinId = query_parameters.get('CoinId')
        Deity = query_parameters.get('Deity')
        Denomination = query_parameters.get('Denomination')
        Material = query_parameters.get('Material')
        Mint = query_parameters.get('Mint')
        FrontDescription = query_parameters.get('FrontDescription')
        Portrait = query_parameters.get('Portrait')
        Region = query_parameters.get('Region')
        BackDescription = query_parameters.get('BackDescription')
        Year = query_parameters.get('Year')

        query = "SELECT * FROM Coins WHERE" # uses the HTTP URL params to query the database
        to_filter = []

        if CoinId:
            query += ' CoinId=? AND'
            to_filter.append(CoinId)
        if Deity:
            query += ' Deity=? AND'
            to_filter.append(Deity)
        if Denomination:
            query += ' Denomination=? AND'
            to_filter.append(Denomination)
        if Material:
            query += ' Material=? AND'
            to_filter.append(Material)
        if Mint:
            query += ' Mint=? AND'
            to_filter.append(Mint)
        if FrontDescription:
            query += ' FrontDescription=? AND'
            to_filter.append(FrontDescription)
        if Portrait:
            query += ' Portrait=? AND'
            to_filter.append(Portrait)
        if Region:
            query += ' Region=? AND'
            to_filter.append(Region)
        if BackDescription:
            query += ' BackDescription=? AND'
            to_filter.append(BackDescription)
        if Year:
            query += ' Year=? AND'
            to_filter.append(Year)

        query = query[:-4] + ';'  # Removes the last 4 characters from the query -> " AND"

        conn = sqlite3.connect('romanCoin.db')
        conn.row_factory = dict_factory
        cur = conn.cursor()

        results = cur.execute(query, to_filter).fetchall()

        return jsonify(results)

    app.run(debug=True, use_reloader=False)
