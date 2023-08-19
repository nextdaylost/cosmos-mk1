"""Repository pattern generic."""


from typing import Generic, List, Optional, Type, TypeVar
from uuid import UUID

from fastapi import Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from cosmos.db.base import Base as BaseOrm
from cosmos.db.session import session_factory
from cosmos.db.exceptions import NotFoundException
from cosmos.models.base import Base as BaseInMemory


ModelType = TypeVar("ModelType", bound=BaseInMemory)
ModelOrmType = TypeVar("ModelOrmType", bound=BaseOrm)
CreateDtoType = TypeVar("CreateDtoType", bound=BaseModel)
UpdateDtoType = TypeVar("UpdateDtoType", bound=BaseModel)


class CrudBase(Generic[ModelType, ModelOrmType, CreateDtoType, UpdateDtoType]):
    """Base class for repositories registering CRUD operations."""

    def __init__(
        self,
        model: Type[ModelType],
        model_orm: Type[ModelOrmType],
        session_factory_func=Depends(session_factory),
    ) -> None:
        """Repository constructor."""
        self._model = model
        self._model_orm = model_orm
        self._session_factory = session_factory_func

    def _create(self, session: Session, dto: CreateDtoType) -> ModelOrmType:
        """Creates a new persistent data object and returns its ORM.

        Used for intra-repository actions.
        """
        obj_orm = self._model_orm(**dto.model_dump())
        session.add(obj_orm)
        return obj_orm

    def _delete_by_id(self, session: Session, resource_id: UUID) -> None:
        """Deletes a persistent data object.

        Used for intra-repository actions.
        """
        obj_orm = self._get_by_id(session, resource_id)
        session.delete(obj_orm)

    def _get_by_id(self, session: Session, resource_id: UUID) -> ModelOrmType:
        """Retrieves persistent data object as an ORM.

        Used for intra-repository actions.
        """
        obj_orm = session.query(self._model_orm).get(resource_id)
        if not obj_orm:
            raise NotFoundException[self._model](resource_id)
        return obj_orm

    def create(self, dto: CreateDtoType) -> Optional[ModelType]:
        """Creates a new persistent data object and returns an in-memory model."""
        with self._session_factory() as session:
            obj_orm = self._create(session, dto)
            session.commit()
            session.refresh(obj_orm)
            return self._model.model_validate(obj_orm)

    def delete_by_id(self, resource_id: UUID) -> None:
        """Deletes a persistent data object."""
        with self._session_factory() as session:
            self._delete_by_id(session, resource_id)
            session.commit()

    def get_by_id(self, resource_id: UUID) -> ModelType:
        """Retrieves a persistent data object as an in-memory model."""
        with self._session_factory() as session:
            obj_orm = self._get_by_id(session, resource_id)
            return self._model.model_validate(obj_orm)

    def get_multiple(self, *, limit: int = 100, offset: int = 0) -> List[ModelType]:
        """Retrieves a list of persistent data objects as in-memory models."""
        with self._session_factory() as session:
            obj_orm_list = (
                session.query(self._model_orm).offset(offset).limit(limit).all()
            )
            return [self._model.model_validate(obj_orm) for obj_orm in obj_orm_list]

    def update_by_id(self, resource_id: UUID, dto: UpdateDtoType) -> ModelType:
        """Updates a persistent data object and returns an in-memory model."""
        with self._session_factory() as session:
            obj_orm = self._get_by_id(session, resource_id)
            for k, v in dto.model_dump().items():
                setattr(obj_orm, k, v)
            session.commit()
            session.refresh(obj_orm)
            return self._model.model_validate(obj_orm)
