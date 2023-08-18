"""API v1 module.

Aggregates path operations for API version 1.
"""


from fastapi import APIRouter

from cosmos.api.v1.endpoints import datasets


router = APIRouter(prefix="/v1")

router.include_router(datasets.router)
