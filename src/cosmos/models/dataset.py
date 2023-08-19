"""Dataset models.

Representation of datasets as informational objects.
"""


from typing import Optional

from pydantic import BaseModel
from sqlalchemy import Column, Text

from cosmos.db.base import Base as BaseOrm
from cosmos.models.base import Base as BaseInMemory


class Dataset(BaseInMemory):
    """Dataset information and metadata container class."""

    name: str


class DatasetCreateDto(BaseModel):
    """Dataset representation as transferred from the client prior to creation."""

    name: str


class DatasetUpdateDto(BaseModel):
    """Dataset representation as transferred from the client prior to update."""

    name: Optional[str]


class DatasetOrm(BaseOrm):
    """Dataset object-relational mapping."""

    __tablename__ = "dataset"

    name = Column(Text, nullable=False)
