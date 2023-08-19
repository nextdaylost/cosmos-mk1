"""Ping endpoint resources."""


from fastapi import APIRouter, Response, status


router = APIRouter(prefix="/ping")


@router.get("/", include_in_schema=False)
def ping():
    """Ping path operation.

    Helps confirm the application is reachable and debug networking issues.
    """
    return Response(status_code=status.HTTP_200_OK)
