"""auto vote

Revision ID: ee3f9e7096fe
Revises: ea62d13233e5
Create Date: 2022-08-27 20:52:52.222189

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ee3f9e7096fe'
down_revision = 'ea62d13233e5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('votes',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_id', 'post_id')
    )
    op.add_column('posts', sa.Column('user_id', sa.Integer(), nullable=False))
    op.alter_column('posts', 'title',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.drop_constraint('post_user_fk', 'posts', type_='foreignkey')
    op.create_foreign_key(None, 'posts', 'user', ['user_id'], ['id'], ondelete='CASCADE')
    op.drop_column('posts', 'owner_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('owner_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'posts', type_='foreignkey')
    op.create_foreign_key('post_user_fk', 'posts', 'user', ['owner_id'], ['id'], ondelete='CASCADE')
    op.alter_column('posts', 'title',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_column('posts', 'user_id')
    op.drop_table('votes')
    # ### end Alembic commands ###