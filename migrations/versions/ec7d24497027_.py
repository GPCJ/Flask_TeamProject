"""empty message

Revision ID: ec7d24497027
Revises: d120dd3eb9a5
Create Date: 2022-12-02 15:53:54.373820

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec7d24497027'
down_revision = 'd120dd3eb9a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.drop_constraint('uq_question_subject', type_='unique')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.create_unique_constraint('uq_question_subject', ['subject'])

    # ### end Alembic commands ###