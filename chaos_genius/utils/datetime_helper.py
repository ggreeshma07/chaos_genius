"""Provides helper functions related to datetime operations."""

from datetime import datetime, timezone

from chaos_genius.core.utils.constants import SUPPORTED_TIMEZONES
from chaos_genius.settings import TIMEZONE


def get_server_timezone():
    """Get server timezone."""
    return datetime.now(timezone.utc).astimezone().tzname()


def get_rca_date_from_string(date_value):
    """Get RCA date from string."""
    return datetime.strptime(date_value, "%Y/%m/%d %H:%M:%S").date()


def get_date_string_with_tz(date_value) -> str:
    """Get date string with timezone."""
    return (
        date_value.strftime("%d %b %Y")
        + f" {TIMEZONE} ({SUPPORTED_TIMEZONES[TIMEZONE]})"
    )
