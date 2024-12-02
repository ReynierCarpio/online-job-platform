"""empty message

Revision ID: dc275e41903f
Revises: dc275e41903e
Create Date: 2024-12-02 17:00:00.041665
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'dc275e41903f'
down_revision = 'dc275e41903e'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table('user',
    sa.Column('user_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('authentication_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('birth_date', sa.Date(), nullable=False),
    sa.Column('skills', sa.Text(), nullable=True),
    sa.Column('work_experience', sa.Text(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['authentication_id'], ['authentication.authentication_id'], ),
    sa.PrimaryKeyConstraint('user_id')
    )

def downgrade():
    op.drop_table('user')
