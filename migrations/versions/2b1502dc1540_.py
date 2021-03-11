"""empty message

Revision ID: 2b1502dc1540
Revises: 
Create Date: 2021-03-11 08:21:50.053837

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '2b1502dc1540'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    op.drop_table('user')
    op.add_column('comments', sa.Column('comment', sa.String(), nullable=True))
    op.add_column('comments', sa.Column('comment_at', sa.DateTime(), nullable=True))
    op.add_column('comments', sa.Column('comment_by', sa.String(), nullable=True))
    op.add_column('comments', sa.Column('like_count', sa.Integer(), nullable=True))
    op.add_column('comments', sa.Column('post_id', sa.Integer(), nullable=True))
    op.add_column('comments', sa.Column('user_id', sa.Integer(), nullable=True))
    op.drop_index('ix_comments_text', table_name='comments')
    op.drop_index('ix_comments_timestamp', table_name='comments')
    op.drop_constraint('comments_post_fkey', 'comments', type_='foreignkey')
    op.create_foreign_key(None, 'comments', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'comments', 'posts', ['post_id'], ['id'])
    op.drop_column('comments', 'timestamp')
    op.drop_column('comments', 'post')
    op.drop_column('comments', 'text')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('text', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column('comments', sa.Column('post', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('comments', sa.Column('timestamp', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.create_foreign_key('comments_post_fkey', 'comments', 'post', ['post'], ['id'])
    op.create_index('ix_comments_timestamp', 'comments', ['timestamp'], unique=False)
    op.create_index('ix_comments_text', 'comments', ['text'], unique=False)
    op.drop_column('comments', 'user_id')
    op.drop_column('comments', 'post_id')
    op.drop_column('comments', 'like_count')
    op.drop_column('comments', 'comment_by')
    op.drop_column('comments', 'comment_at')
    op.drop_column('comments', 'comment')
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('user_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('image_file', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('password', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='user_pkey'),
    sa.UniqueConstraint('email', name='user_email_key'),
    sa.UniqueConstraint('username', name='user_username_key'),
    postgresql_ignore_search_path=False
    )
    op.create_table('post',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.Column('date_posted', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('content', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='post_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='post_pkey')
    )
    # ### end Alembic commands ###