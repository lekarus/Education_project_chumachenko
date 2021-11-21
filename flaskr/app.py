import flask_login
from flask import jsonify, request
from flask_login import login_user, login_required, current_user, logout_user
from flask_migrate import Migrate
from flask_restx import Api, Resource

from database import *
from database.Directors import Directors, directors_schema
from database.Films import Films, films_schema
from database.Films_Directors import FilmsDirectors, films_directors_schema
from database.Films_Genres import FilmsGenres, films_genres_schema
from database.Genres import Genres, genres_schema
from database.Users import Users, users_schema

api = Api(app)
migrate = Migrate(app, db)


@api.route('/user/<id>')
@api.route('/users')
class UsersAPI(Resource):
    @staticmethod
    @login_required
    def get(id='all'):
        if not current_user.isAdmin:
            return jsonify({'message': 'you don\'t have access'})
        if id == 'all':
            all_users = Users.query.all()
            result = users_schema.dump(all_users)
            return jsonify(result)
        user = Users.query.filter_by(user_id=id)
        result = users_schema.dump(user)
        return jsonify(result)

    @staticmethod
    @login_required
    def post():
        if not current_user.isAdmin:
            return jsonify({'message': 'you don\'t have access'})
        user = Users.query.filter_by(username=request.args.get('username'))
        if users_schema.dump(user):
            return jsonify({'message': 'duplicate username'})
        new_user = Users(request.args.get('username'), request.args.get('password'),
                         bool(int(request.args.get('isAdmin'))))
        db.session.add(new_user)
        db.session.commit()
        return 200

    @staticmethod
    @login_required
    def put():
        if not current_user.isAdmin:
            return jsonify({'message': 'you don\'t have access'})
        user = Users.query.\
            where(Users.user_id != request.args.get('user_id')).\
            where(Users.username == request.args.get('username'))
        if users_schema.dump(user):
            return jsonify({'message': 'duplicate username'})
        user = Users.query.where(Users.user_id == request.args.get('user_id'))
        if not users_schema.dump(user):
            return jsonify({'message': 'user not found'})
        user.update({'username': request.args.get('username'),
                     'password': request.args.get('password'),
                     'isAdmin': bool(int(request.args.get('isAdmin')))
                     })
        db.session.commit()
        return 200

    @staticmethod
    @login_required
    def delete():
        if not current_user.isAdmin:
            return jsonify({'message': 'you don\'t have access'})
        if int(request.args.get('user_id')) == 2:
            return jsonify({'message': 'you cant remove admin'})
        user = Users.query.where(Users.user_id == request.args.get('user_id'))
        if not users_schema.dump(user):
            return jsonify({'message': 'user not found'})
        if Films.query.filter_by(user_id=int(request.args.get('user_id'))):
            return jsonify({'message': 'this user has movies, please delete them first'})
        user.delete()
        db.session.commit()
        return 200


@api.route('/genre/<id>')
@api.route('/genres')
class GenreAPI(Resource):
    @staticmethod
    def get(id='all'):
        if id == 'all':
            all_genres = Genres.query.all()
            result = genres_schema.dump(all_genres)
            return jsonify(result)
        genre = Genres.query.filter_by(genre_id=id)
        result = genres_schema.dump(genre)
        return jsonify(result)

    @staticmethod
    @login_required
    def post():
        if not current_user.isAdmin:
            return jsonify({'message': 'you don\'t have access'})
        if genres_schema.dump(Genres.query.filter_by(genre=request.args.get('genre'))):
            return jsonify({'message': 'genre already exists'})
        new_genre = Genres(genre=request.args.get('genre'))
        db.session.add(new_genre)
        db.session.commit()
        return 200

    @staticmethod
    @login_required
    def put():
        if not current_user.isAdmin:
            return jsonify({'message': 'you don\'t have access'})
        if genres_schema.dump(Genres.query.filter_by(genre=request.args.get('genre'))):
            return jsonify({'message': 'genre already exists'})
        genre = Genres.query.filter_by(genre_id=request.args.get('genre_id'))
        genre.update({'genre': request.args.get('genre')})
        db.session.commit()
        return 200

    @staticmethod
    @login_required
    def delete():
        if not current_user.isAdmin:
            return jsonify({'message': 'you don\'t have access'})
        genre = Genres.query.where(Genres.genre_id == request.args.get('genre_id'))
        if not genres_schema.dump(genre):
            return jsonify({'message': 'genre not found'})
        fg = FilmsGenres.query.filter_by(genre_id=request.args.get('genre_id'))
        if films_genres_schema.dump(fg):
            fg.delete()
        genre.delete()
        db.session.commit()
        return 200


@api.route('/director/<id>')
@api.route('/directors')
class DirectorsAPI(Resource):
    @staticmethod
    def get(id='all'):
        if id == 'all':
            all_directors = Directors.query.all()
            result = directors_schema.dump(all_directors)
            return jsonify(result)
        director = Directors.query.filter_by(director_id=id)
        result = directors_schema.dump(director)
        return jsonify(result)

    @staticmethod
    @login_required
    def post():
        if not current_user.isAdmin:
            return jsonify({'message': 'you don\'t have access'})
        director = Directors.query.filter_by(first_name=request.args.get('first_name'),
                                             last_name=request.args.get('last_name'))
        if directors_schema.dump(director):
            return jsonify({'message': 'director already exists'})
        new_director = Directors(first_name=request.args.get('first_name'),
                                 last_name=request.args.get('last_name'))
        db.session.add(new_director)
        db.session.commit()
        return 200

    @staticmethod
    @login_required
    def put():
        if not current_user.isAdmin:
            return jsonify({'message': 'you don\'t have access'})
        director = Directors.query.filter_by(first_name=request.args.get('first_name'),
                                             last_name=request.args.get('last_name'))
        if genres_schema.dump(director):
            return jsonify({'message': 'director already exists'})
        director = Directors.query.filter_by(director_id=request.args.get('director_id'))
        if not directors_schema.dump(director):
            return jsonify({'message': 'director not found'})
        director.update({'first_name': request.args.get('first_name'),
                         'last_name': request.args.get('last_name')})
        db.session.commit()
        return 200

    @staticmethod
    @login_required
    def delete():
        if not current_user.isAdmin:
            return jsonify({'message': 'you don\'t have access'})
        director = Directors.query.where(Directors.director_id == request.args.get('director_id'))
        if not directors_schema.dump(director):
            return jsonify({'message': 'director not found'})
        fd = FilmsDirectors.query.filter_by(director_id=request.args.get('director_id'))
        if films_genres_schema.dump(fd):
            fd.delete()
        director.delete()
        db.session.commit()
        return 200


@api.route('/film/<id>')
@api.route('/films')
class FilmsAPI(Resource):
    @staticmethod
    def get(id='all'):
        if id == 'all':
            all_films = Films.query.all()
            result = films_schema.dump(all_films)
            return jsonify(result)
        film = Films.query.filter_by(film_id=id)
        result = films_schema.dump(film)
        return jsonify(result)

    @staticmethod
    @login_required
    def post():
        film = Films.query.filter_by(film_title=request.args.get('film_title'),
                                     release_date=request.args.get('release_date'))
        if films_schema.dump(film):
            return jsonify({'message': 'film already exists'})
        new_film = Films(film_title=request.args.get('film_title'),
                         release_date=request.args.get('release_date'),
                         film_desc=request.args.get('film_desc'),
                         rating=float(request.args.get('rating')),
                         poster=request.args.get('poster'),
                         user_id=current_user.user_id)
        db.session.add(new_film)
        db.session.commit()
        return 200

    @staticmethod
    @login_required
    def put():
        film = Films.query.filter_by(film_id=int(request.args.get('film_id'))).first()
        if not film:
            return jsonify({'message': 'film not found'})
        if not current_user.isAdmin and \
                current_user.user_id != int(film.user_id):
            return jsonify({'message': 'you don\'t have access'})
        check_existing = Films.query.filter_by(film_title=request.args.get('film_title')).first()
        if check_existing:
            return jsonify({'message': 'film already exists'})
        film.film_title = request.args.get('film_title')
        film.film_desc = request.args.get('film_desc')
        film.release_date = request.args.get('release_date')
        film.rating = float(request.args.get('rating'))
        film.poster = request.args.get('poster')
        db.session.commit()
        return 200

    @staticmethod
    @login_required
    def delete():
        film = Films.query.filter_by(film_id=request.args.get('film_id')).first()
        if not film:
            return jsonify({'message': 'film not found'})
        if not current_user.isAdmin and \
                current_user.user_id != int(film.user_id):
            return jsonify({'message': 'you don\'t have access'})
        fg = FilmsGenres.query.filter_by(film_id=request.args.get('film_id'))
        fd = FilmsDirectors.query.filter_by(film_id=request.args.get('film_id'))
        if films_genres_schema.dump(fg):
            fg.delete()
        if films_directors_schema.dump(fd):
            fd.delete()
        db.session.delete(film)
        db.session.commit()
        return 200


@api.route('/films_directors')
class FilmsDirectorsAPI(Resource):
    @staticmethod
    @login_required
    def get():
        all_fd = FilmsDirectors.query.join(Directors,
                                           Directors.director_id == FilmsDirectors.director_id) \
            .join(Films, Films.film_id == FilmsDirectors.film_id) \
            .add_columns(Films.film_title, Directors.director_id, Directors.first_name, Directors.last_name)
        result = films_directors_schema.dump(all_fd)
        return jsonify(result)

    @staticmethod
    @login_required
    def post():
        film = Films.query.filter_by(film_id=request.args.get('film_id')).first()
        if not current_user.isAdmin and \
                current_user.user_id != int(film.user_id):
            return jsonify({'message': 'you don\'t have access'})
        new_fd = FilmsDirectors(film_id=request.args.get('film_id'),
                                director_id=request.args.get('director_id'))
        db.session.add(new_fd)
        db.session.commit()
        return 200

    @staticmethod
    @login_required
    def put():
        film = Films.query.filter_by(film_id=request.args.get('film_id')).first()
        if not current_user.isAdmin and \
                current_user.user_id != int(film.user_id):
            return jsonify({'message': 'you don\'t have access'})
        fd = FilmsDirectors.query.filter_by(film_id=request.args.get('film_id'))
        if not films_directors_schema.dump(fd):
            return jsonify({'message': 'film not found'})
        fd.update({
            'film_id': request.args.get('film_id'),
            'director_id': request.args.get('director_id')
        })
        db.session.commit()
        return 200

    @staticmethod
    @login_required
    def delete():
        film = Films.query.filter_by(film_id=request.args.get('film_id')).first()
        if not current_user.isAdmin and \
                current_user.user_id != int(film.user_id):
            return jsonify({'message': 'you don\'t have access'})
        fd = FilmsDirectors.query.filter_by(film_id=request.args.get('film_id'),
                                            director_id=request.args.get('director_id'))
        if not films_directors_schema.dump(fd):
            return jsonify({'message': 'row not found'})
        fd.delete()
        db.session.commit()
        return 200


@api.route('/films_genres')
class FilmsGenresAPI(Resource):
    @staticmethod
    @login_required
    def get():
        all_fg = FilmsGenres.query.join(Genres, Genres.genre_id == FilmsGenres.genre_id) \
            .join(Films, Films.film_id == FilmsGenres.film_id) \
            .add_columns(Films.film_title, Genres.genre)
        result = films_genres_schema.dump(all_fg)
        return jsonify(result)

    @staticmethod
    @login_required
    def post():
        film = Films.query.filter_by(film_id=request.args.get('film_id')).first()
        if not current_user.isAdmin and \
                current_user.user_id != int(film.user_id):
            return jsonify({'message': 'you don\'t have access'})
        new_fg = FilmsGenres(film_id=request.args.get('film_id'),
                             gerne_id=request.args.get('genre_id'))
        db.session.add(new_fg)
        db.session.commit()
        return 200

    @staticmethod
    @login_required
    def put():
        film = Films.query.filter_by(film_id=request.args.get('film_id')).first()
        if not current_user.isAdmin and \
                current_user.user_id != int(film.user_id):
            return jsonify({'message': 'you don\'t have access'})
        fg = FilmsGenres.query.filter_by(film_id=request.args.get('film_id'))
        if not films_genres_schema.dump(fg):
            return jsonify({'message': 'film not found'})
        fg.update({
            'film_id': request.args.get('film_id'),
            'genre_id': request.args.get('genre_id')
        })
        db.session.commit()
        return 200

    @staticmethod
    @login_required
    def delete():
        film = Films.query.filter_by(film_id=request.args.get('film_id')).first()
        if not current_user.isAdmin and \
                current_user.user_id != int(film.user_id):
            return jsonify({'message': 'you don\'t have access'})
        fg = FilmsGenres.query.filter_by(film_id=request.args.get('film_id'),
                                         genre_id=request.args.get('genre_id'))
        if not films_genres_schema.dump(fg):
            return jsonify({'message': 'row not found'})
        fg.delete()
        db.session.commit()
        return 200


@api.route('/login')
class Login(Resource):
    @staticmethod
    def post():
        user = Users.query.filter_by(username=request.args.get('username'),
                                     password=request.args.get('password')).first()
        if user:
            login_user(user)
            return 200
        return jsonify({'message': 'incorrect username or password'})


@api.route('/register')
class Register(Resource):
    @staticmethod
    def post():
        new_user = Users(request.args.get('username'),
                         request.args.get('password'), False)
        db.session.add(new_user)
        db.session.commit()
        return 200


@api.route('/register')
class Logout(Resource):
    @staticmethod
    @login_required
    def get():
        logout_user()
        return 200


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
