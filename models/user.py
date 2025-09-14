from __future__ import annotations

from typing import Optional, List, Annotated
from uuid import UUID, uuid4
from datetime import date, datetime
from pydantic import BaseModel, Field, EmailStr, StringConstraints

from .address import AddressBase

# Columbia UNI: 2–3 lowercase letters + 1–4 digits (e.g., abc1234)
UNIType = Annotated[str, StringConstraints(pattern=r"^[a-z]{2,3}\d{1,4}$")]


class PersonBase(BaseModel):
    first_name: str = Field(
        ...,
        description="Given name.",
        json_schema_extra={"example": "Allison"},
    )
    last_name: str = Field(
        ...,
        description="Family name.",
        json_schema_extra={"example": "Cameron"},
    )
    email: EmailStr = Field(
        ...,
        description="Primary email address.",
        json_schema_extra={"example": "acameron@example.com"},
    )
    username: str = Field(
        ...,
        description="Username for this person.",
        json_schema_extra={"example": "allisonxcameron"},
    )
    password: str = Field(
        ...,
        description="User's password.",
        json_schema_extra={"example": "password9"},
    )
    birth_date: Optional[date] = Field(
        None,
        description="Date of birth (YYYY-MM-DD).",
        json_schema_extra={"example": "1815-12-10"},
    )
    gender: Optional[str] = Field(
        None,
        description="User's gender.",
        json_schema_extra={"example": "F"}
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "first_name": "Allison",
                    "last_name": "Cameron",
                    "email": "acameron@example.com",
                    "username": "allisonxcameron",
                    "password": "password9",
                    "birth_date": "1815-12-10",
                    "gender": "F",
                }
            ]
        }
    }


class PersonCreate(PersonBase):
    """Creation payload for a User."""
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "first_name": "Robert",
                    "last_name": "Chase",
                    "email": "rchase@princetonplainsborough.com",
                    "username": "robertxchase",
                    "password": "password8",
                    "birth_date": "1906-12-09",
                    "gender": "M",                    
                }
            ]
        }
    }


class PersonUpdate(BaseModel):
    """Partial update for a Person; supply only fields to change."""
    first_name: Optional[str] = Field(None, json_schema_extra={"example": "Gregory"})
    last_name: Optional[str] = Field(None, json_schema_extra={"example": "House"})
    email: Optional[EmailStr] = Field(None, json_schema_extra={"example": "ghouse@princetonplainsborough.com"})
    username: Optional[str] = Field(None, json_schema_extra={"example": "house"})
    password: Optional[str] = Field(None, json_schema_extra={"example": "monsterTRUCKS!!"})
    birth_date: Optional[date] = Field(None, json_schema_extra={"example": "1815-12-10"})
    gender: Optional[str] = Field(None, json_schema_extra={"example": "M"})
    

    model_config = {
        "json_schema_extra": {
            "examples": [
                {"first_name": "Gregory", "last_name": "House"},
                {"password": "wilsonSUXXX2!"},
            ]
        }
    }
