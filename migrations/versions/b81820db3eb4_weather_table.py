"""Weather table

Revision ID: b81820db3eb4
Revises: 
Create Date: 2018-11-20 19:57:03.842353

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b81820db3eb4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('weathers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('today', sa.DateTime(), nullable=False),
    sa.Column('temperature', sa.Float(), nullable=True),
    sa.Column('weather_type', sa.String(length=128), nullable=True),
    sa.Column('rainfall_probability', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id', 'today')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('weathers')
    # ### end Alembic commands ###