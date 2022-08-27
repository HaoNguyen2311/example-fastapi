"""add last few columns to posts table

Revision ID: ea62d13233e5
Revises: 162fd1342d5f
Create Date: 2022-08-27 19:32:34.935561

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea62d13233e5'
down_revision = '162fd1342d5f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean(),
                  nullable=False, server_default='TRUE'))
    op.add_column('posts',  sa.Column('create_at', sa.TIMESTAMP(timezone=False),
                                      server_default=sa.text('now()'), nullable=False))
    pass


def downgrade() -> None:
    # table , field
    op.drop_column('posts','published')
    op.drop_column('posts','create_at')
    pass
