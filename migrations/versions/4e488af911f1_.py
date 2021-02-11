"""empty message

Revision ID: 4e488af911f1
Revises: 696d51e5611f
Create Date: 2021-02-10 15:32:12.623343

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e488af911f1'
down_revision = '696d51e5611f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('plan',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('sesh_id', sa.Integer(), nullable=True),
    sa.Column('ant_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['ant_id'], ['antagonist.id'], ),
    sa.ForeignKeyConstraint(['sesh_id'], ['sesh.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('user', sa.Column('member_since', sa.String(length=10), nullable=True))
    op.add_column('user', sa.Column('picture', sa.String(length=120), nullable=True))
    op.drop_index('ix_user_registered_at', table_name='user')
    op.create_index(op.f('ix_user_member_since'), 'user', ['member_since'], unique=False)
    op.create_index(op.f('ix_user_picture'), 'user', ['picture'], unique=False)
    op.drop_column('user', 'registered_at')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('registered_at', sa.VARCHAR(length=10), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_user_picture'), table_name='user')
    op.drop_index(op.f('ix_user_member_since'), table_name='user')
    op.create_index('ix_user_registered_at', 'user', ['registered_at'], unique=False)
    op.drop_column('user', 'picture')
    op.drop_column('user', 'member_since')
    op.drop_table('plan')
    # ### end Alembic commands ###
