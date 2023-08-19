"""Value transformer utility functions."""


def to_camel(s: str) -> str:
    """Converts snake case strings to camel case strings."""
    s = s.lstrip("_").split("_")
    return "".join([s[0], *[p.capitalize() for p in s[1:]]])
