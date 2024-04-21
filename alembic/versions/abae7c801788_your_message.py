"""your message

Revision ID: abae7c801788
Revises: 0bac0f8979f6
Create Date: 2024-04-21 16:35:35.543027

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'abae7c801788'
down_revision: Union[str, None] = '0bac0f8979f6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
