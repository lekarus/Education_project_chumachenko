from database import *
from flask_migrate import Migrate
from flask_restx import Api, Resource
from database.Directors import Directors, directors_schema
from database.Films import Films, films_schema
from database.Users import Users, users_schema
from database.Genres import Genres, genres_schema
from database.Films_Directors import FilmsDirectors, films_directors_schema
from database.Films_Genres import FilmsGenres, films_genres_schema

api = Api(app)
migrate = Migrate(app, db)


@api.route('/users')
class UsersAPI(Resource):
    def get(self):
        all_users = Users.query.all()
        result = users_schema.dump(all_users)
        return jsonify(result)


@api.route('/genres')
class GenreAPI(Resource):
    def get(self):
        all_genres = Genres.query.all()
        result = genres_schema.dump(all_genres)
        return jsonify(result)


@api.route('/directors')
class DirectorsAPI(Resource):
    def get(self):
        all_directors = Directors.query.all()
        result = directors_schema.dump(all_directors)
        return jsonify(result)


@api.route('/films')
class FilmsAPI(Resource):
    def get(self):
        all_films = Films.query.all()
        result = films_schema.dump(all_films)
        return jsonify(result)


@api.route('/films_directors')
class FilmsDirectorsAPI(Resource):
    def get(self):
        all_fd = FilmsDirectors.query.join(Directors,
                                           Directors.director_id == FilmsDirectors.director_id) \
            .join(Films, Films.film_id == FilmsDirectors.film_id) \
            .add_columns(Films.film_title, Directors.director_id, Directors.first_name, Directors.last_name)
        result = films_directors_schema.dump(all_fd)
        return jsonify(result)


@api.route('/films_genres')
class FilmsGenresAPI(Resource):
    def get(self):
        all_fg = FilmsGenres.query.join(Genres, Genres.genre_id == FilmsGenres.genre_id) \
            .join(Films, Films.film_id == FilmsGenres.film_id) \
            .add_columns(Films.film_title, Genres.genre)
        result = films_genres_schema.dump(all_fg)
        return jsonify(result)


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
