"""empty message

Revision ID: 4fffd108a516
Revises: 
Create Date: 2020-03-26 19:27:32.528779

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4fffd108a516'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('admin', sa.BOOLEAN(), nullable=True),
    sa.Column('first_name', sa.String(length=255), nullable=True),
    sa.Column('last_name', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('passwordHash', sa.String(length=255), nullable=True),
    sa.Column('creator_name', sa.String(length=255), nullable=True),
    sa.Column('earnings_tips', sa.Float(), nullable=True),
    sa.Column('earnings_donations', sa.Float(), nullable=True),
    sa.Column('earnings_watcher_seconds', sa.Float(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('user_image', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('FBUsers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('oauth_user_id', sa.Integer(), nullable=True),
    sa.Column('first_name', sa.String(length=255), nullable=True),
    sa.Column('last_name', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['Users.id'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Streams',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('stream_link', sa.String(length=255), nullable=True),
    sa.Column('num_current_watchers', sa.Integer(), nullable=True),
    sa.Column('num_total_watchers', sa.Integer(), nullable=True),
    sa.Column('earnings_tips', sa.Float(), nullable=True),
    sa.Column('earnings_donations', sa.Float(), nullable=True),
    sa.Column('earnings_watcher_seconds', sa.Float(), nullable=True),
    sa.Column('amount_watcher_seconds', sa.Time(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('time_running', sa.Time(), nullable=True),
    sa.Column('stream_author_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['stream_author_id'], ['Users.id'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Videos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('video_link', sa.String(length=255), nullable=True),
    sa.Column('num_times_watched', sa.Integer(), nullable=True),
    sa.Column('earnings_tips', sa.Float(), nullable=True),
    sa.Column('earnings_donations', sa.Float(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('video_author_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['video_author_id'], ['Users.id'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Videos')
    op.drop_table('Streams')
    op.drop_table('FBUsers')
    op.drop_table('Users')
    # ### end Alembic commands ###
