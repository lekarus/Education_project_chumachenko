"""initial migration

Revision ID: 78ba727ae3cc
Revises: 
Create Date: 2021-11-14 01:24:22.615317

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '78ba727ae3cc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('directors',
    sa.Column('director_id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=255), nullable=False),
    sa.Column('last_name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('director_id')
    )
    op.create_table('genres',
    sa.Column('genre_id', sa.Integer(), nullable=False),
    sa.Column('genre', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('genre_id')
    )
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=32), nullable=False),
    sa.Column('password', sa.String(length=32), nullable=False),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('films',
    sa.Column('film_id', sa.Integer(), nullable=False),
    sa.Column('film_title', sa.String(length=255), nullable=False),
    sa.Column('release_date', sa.Date(), nullable=False),
    sa.Column('film_desc', sa.String(length=255), nullable=True),
    sa.Column('poster', sa.String(length=255), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('film_id')
    )
    op.create_table('films_directors',
    sa.Column('film_id', sa.Integer(), nullable=False),
    sa.Column('director_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['director_id'], ['directors.director_id'], ),
    sa.ForeignKeyConstraint(['film_id'], ['films.film_id'], ),
    sa.PrimaryKeyConstraint('film_id', 'director_id')
    )
    op.create_table('films_genres',
    sa.Column('film_id', sa.Integer(), nullable=False),
    sa.Column('genre_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['film_id'], ['films.film_id'], ),
    sa.ForeignKeyConstraint(['genre_id'], ['genres.genre_id'], ),
    sa.PrimaryKeyConstraint('film_id', 'genre_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('films_genres')
    op.drop_table('films_directors')
    op.drop_table('films')
    op.drop_table('users')
    op.drop_table('genres')
    op.drop_table('directors')
    # ### end Alembic commands ###
