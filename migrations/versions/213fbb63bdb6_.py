"""empty message

Revision ID: 213fbb63bdb6
Revises: 723d35e3a80a
Create Date: 2021-07-26 22:29:33.892069

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '213fbb63bdb6'
down_revision = '723d35e3a80a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('anomaly_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('kpi_id', sa.Integer(), nullable=False),
    sa.Column('anomaly_type', sa.String(length=80), nullable=False),
    sa.Column('base_anomaly_id', sa.Integer(), nullable=True),
    sa.Column('drilldown_dimensions', sa.JSON(), nullable=True),
    sa.Column('chart_data', sa.JSON(), nullable=True),
    sa.Column('severity_score', sa.Integer(), nullable=True),
    sa.Column('anomaly_timestamp', sa.BigInteger(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('anomaly_data')
    # ### end Alembic commands ###