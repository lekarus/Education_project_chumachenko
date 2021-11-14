from database import *
from flask_migrate import Migrate
from database.Directors import Directors
from database.Films import Films
from database.Users import Users
from database.Genres import Genres
from database.Films_Directors import Films_Directors
from database.Films_Genres import Films_Genres


migrate = Migrate(app, db)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/<path:name>")
def hello(name):
    return f"Hello, {name}!"


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
