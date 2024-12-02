"""empty message

Revision ID: dc275e41903e
Revises: dc275e41903d
Create Date: 2024-12-02 16:50:00.041665
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'dc275e41903e'
down_revision = 'dc275e41903d'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table('job_performance',
    sa.Column('performance_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('job_id', sa.Integer(), nullable=False),
    sa.Column('applicants_count', sa.Integer(), nullable=True),
    sa.Column('views_count', sa.Integer(), nullable=True),
    sa.Column('open_date', sa.DateTime(), nullable=False),
    sa.Column('close_date', sa.DateTime(), nullable=True),
    sa.Column('time_to_fill', sa.Integer(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['job_id'], ['job_posting.job_id'], ),
    sa.PrimaryKeyConstraint('performance_id')
    )

def downgrade():
    op.drop_table('job_performance')
