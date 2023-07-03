"""empty message

Revision ID: 9e8608e27fa8
Revises: a52d41703066
Create Date: 2023-07-03 12:14:44.463149

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9e8608e27fa8'
down_revision = 'a52d41703066'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('student', schema=None) as batch_op:
        batch_op.add_column(sa.Column('course_name', sa.String(length=100), nullable=True))
        batch_op.drop_column('class_')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('student', schema=None) as batch_op:
        batch_op.add_column(sa.Column('class_', sa.VARCHAR(length=100), nullable=True))
        batch_op.drop_column('course_name')

    # ### end Alembic commands ###
