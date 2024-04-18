"""your message1

Revision ID: 0bac0f8979f6
Revises: befbf8cb7001
Create Date: 2024-04-16 17:25:53.248259

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0bac0f8979f6'
down_revision: Union[str, None] = 'befbf8cb7001'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
