"""Database Session resources."""


from contextlib import contextmanager, AbstractContextManager
from typing import Callable

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, Session, sessionmaker

from cosmos.core.config import settings


_engine = create_engine(settings.sqlalchemy_uri)
_session_factory = scoped_session(sessionmaker(autoflush=False, bind=_engine))


@contextmanager
def session_factory() -> Callable[..., AbstractContextManager[Session]]:
    """Returns a database session."""
    session = _session_factory()
    try:
        yield session
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
