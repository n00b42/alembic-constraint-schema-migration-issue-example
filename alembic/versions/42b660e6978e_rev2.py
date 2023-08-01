"""REV2

Revision ID: 42b660e6978e
Revises: f1267aee652f
Create Date: 2023-08-01 19:38:57.553744

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42b660e6978e'
down_revision = 'f1267aee652f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('test_user_id_fkey', 'test', type_='foreignkey')
    op.create_foreign_key(None, 'test', 'users', ['user_id'], ['id'], source_schema='myschema', referent_schema='public', ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'test', schema='myschema', type_='foreignkey')
    op.create_foreign_key('test_user_id_fkey', 'test', 'users', ['user_id'], ['id'], referent_schema='public', ondelete='CASCADE')
    # ### end Alembic commands ###
