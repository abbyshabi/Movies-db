"""fourth  Migration

Revision ID: 56c141a4666f
Revises: f6d776e3bbe4
Create Date: 2019-02-07 15:30:39.671263

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56c141a4666f'
down_revision = 'f6d776e3bbe4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.String(length=255), nullable=True))
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=False)
    op.drop_column('users', 'password_secure')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_secure', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_column('users', 'password_hash')
    # ### end Alembic commands ###
