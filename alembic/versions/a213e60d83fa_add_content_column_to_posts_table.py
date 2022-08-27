"""add content column to posts table

Revision ID: a213e60d83fa
Revises: cdcc0f93bd1a
Create Date: 2022-08-27 14:56:16.836958

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a213e60d83fa'
down_revision = 'cdcc0f93bd1a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable = False))
    pass


def downgrade() -> None:
    # table want, field you want
    op.drop_column('posts','content')
    pass
