"""add user table

Revision ID: 958a0007ced3
Revises: a213e60d83fa
Create Date: 2022-08-27 15:10:36.096118

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '958a0007ced3'
down_revision = 'a213e60d83fa'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('user',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('create_at', sa.TIMESTAMP(timezone=False),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade() -> None:
    op.drop_table('user')
    pass
