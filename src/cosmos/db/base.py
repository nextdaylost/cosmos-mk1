"""Base data persistence object resources."""


from uuid import uuid4

from sqlalchemy import Column, DateTime, Uuid
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.sql.functions import func


@as_declarative()
class Base:
    """Global base class for data persistence objects."""

    __abstract__ = True

    id = Column(Uuid, primary_key=True, nullable=False, default=uuid4)
    created_at = Column(DateTime, nullable=False, default=func.current_timestamp())
    updated_at = Column(
        DateTime,
        nullable=False,
        default=func.current_timestamp(),
        onupdate=func.current_timestamp(),
    )
