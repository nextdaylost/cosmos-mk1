"""Dataset endpoint resources."""


from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status

from cosmos.db.exceptions import NotFoundException
from cosmos.models.dataset import DatasetCreateDto, DatasetUpdateDto
from cosmos.models.query import PaginationParams
from cosmos.repositories.dataset import DatasetRepository


router = APIRouter(prefix="/datasets")


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_dataset(
    dataset_dto: DatasetCreateDto,
    repository: DatasetRepository = Depends(DatasetRepository),
):
    """Creates a dataset."""
    return repository.create(dataset_dto)


@router.delete("/{dataset_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_dataset(
    dataset_id: UUID,
    repository: DatasetRepository = Depends(DatasetRepository),
):
    """Deletes a dataset."""
    repository.delete_by_id(dataset_id)


@router.get("/{dataset_id}", status_code=status.HTTP_200_OK)
def read_dataset(
    dataset_id: UUID,
    repository: DatasetRepository = Depends(DatasetRepository),
):
    """Retrieves a dataset."""
    try:
        return repository.get_by_id(dataset_id)
    except NotFoundException:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@router.get("/", status_code=status.HTTP_200_OK)
def read_datasets(
    pagination: PaginationParams,
    repository: DatasetRepository = Depends(DatasetRepository),
):
    """Retrieves a list of all datasets."""
    return repository.get_multiple(**pagination)


@router.patch("/{dataset_id}", status_code=status.HTTP_200_OK)
def update_dataset(
    dataset_id: UUID,
    dataset_dto: DatasetUpdateDto,
    repository: DatasetRepository = Depends(DatasetRepository),
):
    """Updates a dataset."""
    try:
        return repository.update_by_id(dataset_id, dataset_dto)
    except NotFoundException:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
