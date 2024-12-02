"""empty message

Revision ID: dc275e41903g
Revises: dc275e41903f
Create Date: 2024-12-02 17:10:00.041665
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'dc275e41903g'
down_revision = 'dc275e41903f'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table('application',
    sa.Column('application_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('job_seeker_id', sa.Integer(), nullable=False),
    sa.Column('job_id', sa.Integer(), nullable=False),
    sa.Column('resume', sa.LargeBinary(), nullable=True),
    sa.Column('status', sa.Enum('pending', 'interview', 'rejected', 'accepted'), nullable=False),
    sa.Column('skills', sa.Text(), nullable=True),
    sa.Column('work_experience', sa.Text(), nullable=True),
    sa.Column('applied_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['job_id'], ['job_posting.job_id'], ),
    sa.ForeignKeyConstraint(['job_seeker_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('application_id')
    )

def downgrade():
    op.drop_table('application')
