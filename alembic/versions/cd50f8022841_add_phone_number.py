"""add phone number

Revision ID: cd50f8022841
Revises: ee3f9e7096fe
Create Date: 2022-08-27 21:01:09.103643

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd50f8022841'
down_revision = 'ee3f9e7096fe'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('phone_number', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'phone_number')
    # ### end Alembic commands ###
