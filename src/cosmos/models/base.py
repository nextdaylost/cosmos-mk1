"""Base in-memory data object resources."""


from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict

from cosmos.utils.transformers import to_camel


class Base(BaseModel):
    """Global base class for in-memory data objects."""

    model_config = ConfigDict(
        alias_generator=to_camel,
        from_attributes=True,
        populate_by_name=True,
    )

    id: UUID
    created_at: datetime
    updated_at: datetime
