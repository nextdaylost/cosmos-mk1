"""Query resources."""


from typing import Annotated

from fastapi import Depends
from pydantic import NonNegativeInt


def pagination_parameters(limit: NonNegativeInt = 100, offset: NonNegativeInt = 0):
    """Query parameters used by pagination operations."""
    return {"limit": limit, "offset": offset}


PaginationParams = Annotated[dict, Depends(pagination_parameters)]
