from flask import Flask, render_template
import requests
import csv
import sqlite3
import pandas as pd



# Database creation

conn = sqlite3.connect('messier.db')
c = conn.cursor()

# Get Data from API

app = Flask(__name__)


CSV_URL = 'https://www.datastro.eu/explore/dataset/catalogue-de-messier/download/?format=csv&timezone=Europe/Berlin&use_labels_for_header=true&csv_separator=%3B'


@app.route('/Messier')

def messier():

    df = pd.read_csv(CSV_URL, sep=';') 

    df.to_html('messier_csv.html') 
    html_table = df.to_html()


    return html_table


    if response.status_code != 200:
        return "Status Error"

       
            
if __name__ == "__main__":
    app.run(debug=True)
