"""added email to users

Revision ID: 6740a7155425
Revises: 770bb177a4b1
Create Date: 2016-07-07 12:37:12.836241

"""

# revision identifiers, used by Alembic.
revision = '6740a7155425'
down_revision = '770bb177a4b1'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.Text(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'email')
    ### end Alembic commands ###