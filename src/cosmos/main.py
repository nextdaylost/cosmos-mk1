"""Application entrypoint."""


from fastapi import APIRouter, FastAPI
from starlette.middleware.cors import CORSMiddleware

from cosmos.api.v1 import api
from cosmos.core.config import settings
from cosmos.utils.endpoints import ping


def main() -> FastAPI:
    """Application factory function.

    Returns an initialized instance of the application.
    """
    app = FastAPI()

    if settings.cors_origins:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=[str(origin) for origin in settings.cors_origins],
            allow_credentials=True,
            allow_headers=["*"],
            allow_methods=["*"],
        )

    api_router = APIRouter(prefix=settings.api_prefix)

    api_router.include_router(api.router)
    api_router.include_router(ping.router)

    app.include_router(api_router)

    return app
