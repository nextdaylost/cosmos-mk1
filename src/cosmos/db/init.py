"""Local development database initialize resources."""


from cosmos.db.session import _engine
from cosmos.db.base import Base


def initialize_db() -> None:
    """Creates database resources attached to the global ORM base class.

    Intended for use in local development only. Alembic should be used in publicly
    accessible deployments.
    """
    Base.metadata.create_all(_engine)
