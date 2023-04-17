"""empty message

Revision ID: ea3c57af3c16
Revises: 1734bb83acfc
Create Date: 2023-04-17 13:02:36.275163

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea3c57af3c16'
down_revision = '1734bb83acfc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favorite_character',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('character_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['character_id'], ['character.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('favorite__character')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favorite__character',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('character_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['character_id'], ['character.id'], name='favorite__character_character_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='favorite__character_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='favorite__character_pkey')
    )
    op.drop_table('favorite_character')
    # ### end Alembic commands ###
