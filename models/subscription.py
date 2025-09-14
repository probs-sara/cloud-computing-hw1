from __future__ import annotations

from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime
from pydantic import BaseModel, Field


class SubscriptionBase(BaseModel):
    subscription_id: str = Field(
        ...,
        description="Subscription ID.",
        json_schema_extra={"example": "55e-Hulu-Allison-Cam"},
    )
    service: str = Field(
        ...,
        description="Name of the service providing subscription.",
        json_schema_extra={"example": "Hulu"},
    )
    member_name: str = Field(
        ...,
        description="Name of the member paying for subscription.",
        json_schema_extra={"example": "Allison Cameron"},
    )
    username: str = Field(
        ...,
        description="Member username.",
        json_schema_extra={"example": "allisonxcameron"},
    )
    password: str = Field(
        ...,
        description="Member password.",
        json_schema_extra={"example": "thisisap4ssw0rd!"},
    )
    gender: Optional[str] = Field(
        None,
        description="Member gender.",
        json_schema_extra={"example": "F"},
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "subscription_id": "55e-Hulu-Allison-Cameron",
                    "service": "Hulu",
                    "member_name": "Allison Cameron",
                    "username": "allisonxcameron",
                    "password": "thisisap4ssw0rd!",
                    "gender": "F",
                }
            ]
        }
    }


class SubscriptionCreate(SubscriptionBase):
    """Create a subscription relation."""
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "subscription_id": "32k-Spotify-Robert-Chase",
                    "service": "Spotify",
                    "member_name": "Robert Chase",
                    "username": "robertxchase",
                    "password": "thisisap4ssw0rd!!",
                    "gender": "M",
                }
            ]
        }
    }


class SubscriptionUpdate(BaseModel):
    """To update a subscription that already exists."""
    service: Optional[str] = Field(
        None, description="Name of the service providing the subscription.", json_schema_extra={"example": "Spotify"}
    )
    member_name: Optional[str] = Field(
        None, description="Name of the person paying for the subscription.", json_schema_extra={"example": "Robert Chase"}
    )
    username: Optional[str] = Field(
        None, description="Member username.", json_schema_extra={"example": "robertxchase"}
    )
    password: Optional[str] = Field(
        None, description="Member password.", json_schema_extra={"example": "thisisap4ssw0rd!!"}
    )
    gender: Optional[str] = Field(
        None, description="Member gender.", json_schema_extra={"example": "M"}
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "subscription_id": "32k-Spotify-Robert-Chase",
                    "service": "Spotify",
                    "member_name": "Robert Chase",
                    "username": "robertxchase",
                    "password": "thisisap4ssw0rd!!",
                    "gender": "M",
                },
                {"password": "Brooklyn!199"},
            ]
        }
    }
