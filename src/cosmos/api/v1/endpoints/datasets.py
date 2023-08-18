"""Dataset endpoint resources."""


from uuid import UUID

from fastapi import APIRouter, Response, status


router = APIRouter(prefix="/datasets")


@router.post("/")
def create_dataset():
    """Creates a dataset."""
    return Response(status_code=status.HTTP_201_CREATED)


@router.delete("/{dataset_id}")
def delete_dataset(dataset_id: UUID):
    """Deletes a dataset."""
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get("/{dataset_id}")
def read_dataset(dataset_id: UUID):
    """Retrieves a dataset."""
    return Response(status_code=status.HTTP_200_OK)


@router.get("/")
def read_datasets():
    """Retrieves a list of all datasets."""
    return Response(status_code=status.HTTP_200_OK)


@router.patch("/{dataset_id}")
def update_dataset(dataset_id: UUID):
    """Updates a dataset."""
    return Response(status_code=status.HTTP_200_OK)
