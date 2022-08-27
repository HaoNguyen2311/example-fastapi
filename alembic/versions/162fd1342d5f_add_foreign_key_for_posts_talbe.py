"""add foreign key for posts talbe

Revision ID: 162fd1342d5f
Revises: 958a0007ced3
Create Date: 2022-08-27 19:13:30.547311

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '162fd1342d5f'
down_revision = '958a0007ced3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    # name foreign key
    op.create_foreign_key('post_user_fk', source_table='posts', referent_table='user', local_cols=[
                          'owner_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade() -> None:
    op.drop_constraint('post_user_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
