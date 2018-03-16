"""empty message

Revision ID: 13678ad872bd
Revises: 
Create Date: 2018-03-16 02:55:06.698339

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '13678ad872bd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ISBN', sa.String(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('added_by', sa.String(), nullable=False),
    sa.Column('added_date', sa.DateTime(), nullable=False),
    sa.Column('result_all', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('ISBN')
    )
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ISBN', sa.String(), nullable=False),
    sa.Column('star', sa.String(), nullable=False),
    sa.Column('comment', sa.String(), nullable=True),
    sa.Column('added_by', sa.String(), nullable=False),
    sa.Column('added_date', sa.DateTime(), nullable=False),
    sa.Column('result_all', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('reviews')
    op.drop_table('books')
    # ### end Alembic commands ###
