"""empty message

Revision ID: dc275e41903c
Revises:
Create Date: 2024-12-02 16:29:51.041665
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'dc275e41903c'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table('authentication',
    sa.Column('authentication_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('password_hash', sa.String(length=255), nullable=False),
    sa.Column('role', sa.Enum('user', 'admin'), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('authentication_id'),
    sa.UniqueConstraint('email')
    )

def downgrade():
    op.drop_table('authentication')
