from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import csv, sqlite3
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/collective.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)




#   @app.route('/')
#   def home(): 
#       return render_template('index.html')

#   def retrieve_models():
#       conn = sqlite3.connect("data/collective.db")
#       cursor = conn.cursor()
#       cursor.execute("Select * from aiModels")
#       rows = cursor.fetchall()
#       return rows

#   if __name__ == "__main__":
#       port = int(os.environ.get('PORT', 5000))
#       app.run(debug=True, host='0.0.0.0', port=port)

