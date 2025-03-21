from flask import Flask, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)

# Configure SQLite database
app.config["MONGO_URI"] = "mongodb://atlas-sql-67dc87ea8fffd152f43953a3-9hxok.a.query.mongodb.net/sample_mflix?ssl=true&authSource=admin"
mongo = PyMongo(app)


@app.route('/')
def index():
    # Example of querying the database
    users = mongo.db.users.find()
    return str(users)

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/test')
def test():
    return render_template('test.html')

if __name__ == "__main__":
    app.run(debug=True)