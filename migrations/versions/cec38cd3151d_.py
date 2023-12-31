"""empty message

Revision ID: cec38cd3151d
Revises: 
Create Date: 2023-07-30 10:06:05.577380

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cec38cd3151d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('patrol_student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('day', sa.Integer(), nullable=False),
    sa.Column('type', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('studentTest')
    with op.batch_alter_table('student', schema=None) as batch_op:
        batch_op.drop_index('ix_student_index')

    op.drop_table('student')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('student',
    sa.Column('index', sa.TEXT(), nullable=True),
    sa.Column('월요일', sa.TEXT(), nullable=True),
    sa.Column('화요일', sa.TEXT(), nullable=True),
    sa.Column('수요일', sa.TEXT(), nullable=True),
    sa.Column('목요일', sa.TEXT(), nullable=True),
    sa.Column('금요일', sa.TEXT(), nullable=True)
    )
    with op.batch_alter_table('student', schema=None) as batch_op:
        batch_op.create_index('ix_student_index', ['index'], unique=False)

    op.create_table('studentTest',
    sa.Column('id', sa.INTEGER(), nullable=True),
    sa.Column('name', sa.TEXT(), nullable=True),
    sa.Column('day', sa.INTEGER(), nullable=True),
    sa.Column('type', sa.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('patrol_student')
    # ### end Alembic commands ###
