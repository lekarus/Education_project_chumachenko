#!/bin/bash

flask db migrate;
flask db upgrade;
python fill_db.py fill_db;
gunicorn -b 0.0.0.0:8000 -w 4 app:app;
