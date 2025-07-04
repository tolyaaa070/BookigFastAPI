"""empty message

Revision ID: a6fd8394f028
Revises: 82b249b45bd5
Create Date: 2025-06-14 22:32:57.025658

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a6fd8394f028'
down_revision: Union[str, None] = '82b249b45bd5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('userprofile', sa.Column('email', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('userprofile', 'email')
    # ### end Alembic commands ###
