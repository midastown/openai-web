from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template
import sqlite3
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.route('/')
def home():
    models = AiModels.query.all()
    return render_template('index.html', models=models)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    requests = db.relationship("ModelRequest", backref='user')

    def __repr__(self):
        return f'<User: {self.username}>'

    def set_password(self, value):
        """Store the password as a hash for security."""
        self.password_hash = generate_password_hash(value)

    # allow password = "..." to set a password
    password = property(fset=set_password)

    def check_password(self, value):
        return check_password_hash(self.password_hash, value)


class AiModels(db.Model):
    __tablename__ = 'ai_models'
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String, unique=True, nullable=False)
    requestsPM = db.Column(db.Integer, nullable=False)
    tokenPM = db.Column(db.Integer, nullable=False)
    pricePerThousandToken = db.Column(db.Integer, nullable=False)
    models = db.relationship('ModelRequest', backref='ai_models', uselist=False)

    def __repr__(self):
        return f'<Model: {self.model}>, <RequestsPerMin: {self.requestsPM}>, <TokenPM: {self.tokenPM}>, <Price: {self.pricePerThousandToken}>'


class ModelRequest(db.Model):
    __tablename__ = 'model_request'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String)
    answer = db.Column(db.String)
    cost = db.Column(db.Integer) # Integer (in cents) since sqlite doesn't like decimals
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    model_id = db.Column(db.Integer, db.ForeignKey('ai_models.id'))


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

