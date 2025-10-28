"""Shortlinks schemas for Pydantic models."""

from typing import Optional

from pydantic import BaseModel


class Shortlink(BaseModel):
    """Shortlink model."""

    _id: Optional[str] = None
    url_id: Optional[str] = None
    account_uid: Optional[str] = None
    name: Optional[str] = None
    status: Optional[str] = None
    base_url: Optional[str] = None
    short_url: Optional[str] = None
    long_url: Optional[str] = None
    visits: Optional[int] = 0
    unique_visits: Optional[int] = 0
    preview_visits: Optional[int] = 0
    created_by: Optional[str] = None
    created_on: Optional[int] = None
    reference_type: Optional[str] = None
    expiration: Optional[bool] = False
    expiration_date: Optional[int] = None
    study_uid: Optional[str] = None
    reference_uid: Optional[str] = None


class CreateShortlinkData(BaseModel):
    """Data for creating a shortlink."""

    long_url: str
    name: Optional[str] = None
    status: Optional[str] = "ACTIVE"


class UpdateShortlinkStatusData(BaseModel):
    """Data for updating shortlink status."""

    status: str


class ListShortlinksParams(BaseModel):
    """Parameters for listing shortlinks."""

    id: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    limit: Optional[int] = None
    offset: Optional[int] = None

