"""
Module for testing app.py
"""
import sys
import random

import pytest
from flask_login import current_user

sys.path.append('/home/lekarus/Education_project_chumachenko/flaskr')

import app


@pytest.fixture
def get_application():
    application = app.app
    application.config['TESTING'] = True
    application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@0.0.0.0:49153/postgres'

    return application


@pytest.fixture
def client(get_application):
    return get_application.test_client()


# @pytest.mark.parametrize("username, password", [('new_user', 'pass'), ('new_user2', 'pass'),
#                                                 ('new_user3', 'pass'), ('new_user4', 'pass')])
# def test_register(client, username, password):
#     """
#         Method for testing register api
#
#         Ags:
#             client: instance of app
#             username: username
#             password: user password
#     """
#     with client:
#         client.post('/register', query_string={'username': username, 'password': password})
#         assert current_user.username == username


@pytest.mark.parametrize("username, password", [('new_user', 'pass'), ('new_user2', 'pass'),
                                                ('new_user3', 'pass'), ('new_user4', 'pass')])
def test_login(client, username, password):
    """
        Method for testing login

        Ags:
            client: instance of app
            username: username
            password: user password
    """
    with client:
        client.post('/login', query_string={'username': username, 'password': password})
        assert current_user.username == username


@pytest.mark.parametrize("url, response_not_logged, response_logged, response_admin_logged",
                         [('/films', '200', '200', '200'), ('/film/10', '200', '200', '200'),
                          ('/genres', '200', '200', '200'), ('/genre/10', '200', '200', '200'),
                          ('/directors', '200', '200', '200'), ('/director/10', '200', '200', '200'),
                          ('/films_directors', 'server could not verify', '200', '200'),
                          ('/films_genres', 'server could not verify', '200', '200'),
                          ('/users', 'server could not verify', 'server could not verify', '200'),
                          ('/user/1', 'server could not verify', 'server could not verify', '200')])
def test_get(client, url, response_not_logged, response_logged, response_admin_logged):
    """
        Method for testing get requests

        Ags:
            client: instance of app
            url: testing url
            response_not_logged: test response for guest
            response_logged: test response for user
            response_admin_logged: test response for admin
    """
    response = client.get(url)
    assert response_not_logged in str(response.data if response_not_logged != '200' else response.status_code)
    client.post('/users?username=user&password=pass')
    response = client.get(url)
    assert response_not_logged in str(response.data if response_not_logged != '200' else response.status_code)
    client.post('/users?username=admin&password=admin')
    response = client.get(url)
    assert response_not_logged in str(response.data if response_not_logged != '200' else response.status_code)


@pytest.mark.parametrize("url, response_not_logged, response_logged, response_admin_logged, params",
                         [('/films', 'server could not verify', '200', '200',
                           {'film_title': 'test_title', 'film_desc': 'test_desc', 'release_date': '12/12/2012',
                            'rating': random.randint(0, 10), 'poster': 'test_poster'
                            }),
                          ('/genres', 'server could not verify', '200', '200',
                           {'genre': 'test_genre'}),
                          ('/directors', 'server could not verify', '200', '200',
                           {'first_name': 'test_first', 'last_name': 'test_last'}),
                          ('/films_directors', 'server could not verify', '200', '200',
                           {'film_id': 2, 'director_id': 1}),
                          ('/films_genres', 'server could not verify', '200', '200',
                           {'film_id': 2, 'genre_id': 1}),
                          ('/users', 'server could not verify', 'have access', '200',
                           {'username': 'test_name', 'last_name': 'test_last'})])
def test_post(client, url, params, response_not_logged, response_logged, response_admin_logged):
    """
        Method for testing post requests

        Ags:
            client: instance of app
            url: testing url
            response_not_logged: test response for guest
            response_logged: test response for user
            response_admin_logged: test response for admin
    """
    with client:
        response = client.post(url, query_string=params)
        assert response_not_logged in str(response.data)
        client.post('/login?username=user&password=pass')
        response = client.post(url, query_string=params)
        assert response_logged in str(response.data if response_logged != '200' else response.status_code)
        client.post('/login?username=admin&password=admin')
        response = client.post(url, query_string=params)
        assert response_admin_logged in str(response.data if response_admin_logged != '200' else response.status_code)


@pytest.mark.parametrize("url, response_not_logged, response_logged, response_admin_logged, params",
                         [('/films', 'server could not verify', '200', '200',
                           {'film_title': 'upd_title', 'film_desc': 'test_desc', 'release_date': '12/12/2012',
                            'rating': random.randint(0, 10), 'poster': 'test_poster', 'film_id': 101
                            }),
                          ('/films', 'server could not verify', 'have access', '200',
                           {'film_title': 'upd_title', 'film_desc': 'test_desc', 'release_date': '12/12/2012',
                            'rating': random.randint(0, 10), 'poster': 'test_poster', 'film_id': 2
                            }),
                          ('/genres', 'server could not verify', 'have access', '200',
                           {'genre': 'test_genre', 'genre_id': 1}),
                          ('/directors', 'server could not verify', 'have access', '200',
                           {'first_name': 'test_first', 'last_name': 'test_last', 'director_id': 1}),
                          ('/films_directors', 'server could not verify', 'have access', '200',
                           {'film_id': 2, 'director_id': 1}),
                          ('/films_directors', 'server could not verify', '200', '200',
                           {'film_id': 104, 'director_id': 1}),
                          ('/films_genres', 'server could not verify', 'have access', '200',
                           {'film_id': 2, 'genre_id': 1}),
                          ('/films_genres', 'server could not verify', '200', '200',
                           {'film_id': 104, 'genre_id': 1}),
                          ('/users', 'server could not verify', 'have access', '200',
                           {'username': 'test_name', 'last_name': 'test_last'})])
def test_put(client, url, params, response_not_logged, response_logged, response_admin_logged):
    """
        Method for testing put requests

        Ags:
            client: instance of app
            url: testing url
            response_not_logged: test response for guest
            response_logged: test response for user
            response_admin_logged: test response for admin
    """
    with client:
        response = client.put(url, query_string=params)
        assert response_not_logged in str(response.data if response_not_logged != '200' else response.status_code)
        client.post('/login?username=user&password=pass')
        response = client.put(url, query_string=params)
        assert response_logged in str(response.data if response_logged != '200' else response.status_code)
        client.post('/login?username=admin&password=admin')
        response = client.put(url, query_string=params)
        assert response_admin_logged in str(response.data if response_admin_logged != '200' else response.status_code)


@pytest.mark.parametrize("url, response_not_logged, response_logged, response_admin_logged, params",
                         [('/films', 'server could not verify', '200', '200',
                           {'film_id': 104}),
                          ('/films', 'server could not verify', 'have access', '200',
                           {'film_id': 2}),
                          ('/genres', 'server could not verify', 'have access', '200',
                           {'genre_id': 1}),
                          ('/directors', 'server could not verify', 'have access', '200',
                           {'director_id': 1}),
                          ('/films_directors', 'server could not verify', 'have access', '200',
                           {'film_id': 2, 'director_id': 1}),
                          ('/films_directors', 'server could not verify', '200', '200',
                           {'film_id': 104, 'director_id': 1}),
                          ('/films_genres', 'server could not verify', 'have access', '200',
                           {'film_id': 2, 'genre_id': 1}),
                          ('/films_genres', 'server could not verify', '200', '200',
                           {'film_id': 104, 'genre_id': 1}),
                          ('/users', 'server could not verify', 'have access', '200',
                           {'username': 'test_name', 'last_name': 'test_last'})])
def test_delete(client, url, params, response_not_logged, response_logged, response_admin_logged):
    """
        Method for testing delete requests

        Ags:
            client: instance of app
            url: testing url
            response_not_logged: test response for guest
            response_logged: test response for user
            response_admin_logged: test response for admin
    """
    with client:
        response = client.delete(url, query_string=params)
        assert response_not_logged in str(response.data if response_not_logged != '200' else response.status_code)
        client.post('/login?username=user&password=pass')
        response = client.delete(url, query_string=params)
        assert response_logged in str(response.data if response_logged != '200' else response.status_code)
        client.post('/login?username=admin&password=admin')
        response = client.delete(url, query_string=params)
        assert response_admin_logged in str(response.data if response_admin_logged != '200' else response.status_code)
