"""Custom database exceptions."""


from typing import Generic, TypeVar
from uuid import UUID


ModelType = TypeVar("ModelType")


class NotFoundException(Exception, Generic[ModelType]):
    """Raised when a resource does not exist or otherwise cannot be located."""

    entity_type: str = ModelType.__name__

    def __init__(self, entity_id: UUID) -> None:
        """Exception constructor."""
        super().__init__(f"{self.entity_type} '{entity_id}' not found.")
