"""empty message

Revision ID: dc275e41903i
Revises: dc275e41903h
Create Date: 2024-12-02 17:30:00.041665
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'dc275e41903i'
down_revision = 'dc275e41903h'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table('message',
    sa.Column('message_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('sender_id', sa.Integer(), nullable=False),
    sa.Column('recipient_id', sa.Integer(), nullable=False),
    sa.Column('application_id', sa.Integer(), nullable=True),
    sa.Column('message_text', sa.Text(), nullable=False),
    sa.Column('is_read', sa.Boolean(), nullable=True),
    sa.Column('message_type', sa.Enum('text', 'image', 'file'), nullable=False),
    sa.Column('sent_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['application_id'], ['application.application_id'], ),
    sa.ForeignKeyConstraint(['recipient_id'], ['user.user_id'], ),
    sa.ForeignKeyConstraint(['sender_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('message_id')
    )

def downgrade():
    op.drop_table('message')
