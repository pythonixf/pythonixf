"""empty message

Revision ID: 2a0571896eee
Revises: 
Create Date: 2018-10-12 21:11:55.012276

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2a0571896eee'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cat',
    sa.Column('c_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('c_name', sa.String(length=32), nullable=True),
    sa.Column('c_age', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('c_id'),
    sa.UniqueConstraint('c_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cat')
    # ### end Alembic commands ###
