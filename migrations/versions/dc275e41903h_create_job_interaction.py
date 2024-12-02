"""empty message

Revision ID: dc275e41903h
Revises: dc275e41903g
Create Date: 2024-12-02 17:20:00.041665
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'dc275e41903h'
down_revision = 'dc275e41903g'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table('job_interaction',
    sa.Column('interaction_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('job_id', sa.Integer(), nullable=False),
    sa.Column('interaction_type', sa.Enum('view', 'apply', 'save'), nullable=False),
    sa.Column('interaction_date', sa.DateTime(), nullable=True),
    sa.Column('is_applied', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['job_id'], ['job_posting.job_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('interaction_id')
    )

def downgrade():
    op.drop_table('job_interaction')
