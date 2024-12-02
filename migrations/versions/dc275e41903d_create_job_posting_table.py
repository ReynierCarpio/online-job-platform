"""empty message

Revision ID: dc275e41903d
Revises: dc275e41903c
Create Date: 2024-12-02 16:40:00.041665
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'dc275e41903d'
down_revision = 'dc275e41903c'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table('job_posting',
    sa.Column('job_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('employer_id', sa.Integer(), nullable=False),
    sa.Column('job_title', sa.String(length=255), nullable=False),
    sa.Column('job_description', sa.Text(), nullable=False),
    sa.Column('location', sa.String(length=255), nullable=True),
    sa.Column('category', sa.String(length=255), nullable=False),
    sa.Column('industry', sa.String(length=255), nullable=False),
    sa.Column('min_salary', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('max_salary', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('job_id')
    )

def downgrade():
    op.drop_table('job_posting')
