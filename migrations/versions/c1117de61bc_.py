"""empty message

Revision ID: c1117de61bc
Revises: None
Create Date: 2014-02-12 08:59:33.736832

"""

# revision identifiers, used by Alembic.
revision = 'c1117de61bc'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('venue', sa.Column('type', sa.String(length=64), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('venue', 'type')
    ### end Alembic commands ###
