"""Dataset repository resources."""


from contextlib import AbstractContextManager
from typing import Callable

from fastapi import Depends
from sqlalchemy.orm import Session

from cosmos.db.session import session_factory
from cosmos.models.dataset import (
    Dataset,
    DatasetCreateDto,
    DatasetOrm,
    DatasetUpdateDto,
)
from cosmos.repositories.base import CrudBase


class DatasetRepository(
    CrudBase[Dataset, DatasetOrm, DatasetCreateDto, DatasetUpdateDto]
):
    """Handles persistence operations for Dataset objects."""

    def __init__(
        self,
        _session_factory: Callable[..., AbstractContextManager[Session]] = Depends(
            session_factory
        ),
    ):
        """Repository constructor."""
        super().__init__(
            model=Dataset,
            model_orm=DatasetOrm,
            session_factory_func=session_factory,
        )
