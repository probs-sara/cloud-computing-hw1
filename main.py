from __future__ import annotations

import os
import socket
from datetime import datetime

from typing import Dict, List
from uuid import UUID

from fastapi import FastAPI, HTTPException
from fastapi import Query, Path
from typing import Optional

from models.person import PersonCreate, PersonRead, PersonUpdate
from models.address import AddressCreate, AddressRead, AddressUpdate
from models.health import Health
from models.subscription import SubscriptionCreate, SubscriptionRead, SubscriptionUpdate
from models.user import UserCreate, UserUpdate, UserRead

port = int(os.environ.get("FASTAPIPORT", 8000))

# -----------------------------------------------------------------------------
# Fake in-memory "databases"
# -----------------------------------------------------------------------------

users: Dict[UUID, UserRead] = {}
subscriptions: Dict[UUID, SubscriptionRead] = {}

app = FastAPI(
    title="User/Subscription API",
    description="Demo FastAPI app using Pydantic v2 models for User and Subscription",
    version="0.1.0",
)

# -----------------------------------------------------------------------------
# User Endpoints
# -----------------------------------------------------------------------------

@app.get("/users", response_model=list[UserRead])
def list_users():
    raise HTTPException(status_code=501, detail="Not implemented")

@app.post("/users", response_model=UserRead)
def create_user(user: UserCreate):
    raise HTTPException(status_code=501, detail="Not implemented")

@app.get("/users/{user_id}", response_model=UserRead)
def get_user(user_id: UUID = Path(..., description="User ID")):
    raise HTTPException(status_code=501, detail="Not implemented")

@app.put("/users/{user_id}", response_model=UserRead)
def update_user(user_id: UUID, update: UserUpdate):
    raise HTTPException(status_code=501, detail="Not implemented")

@app.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: UUID):
    raise HTTPException(status_code=501, detail="Not implemented")

# -----------------------------------------------------------------------------
# Subscription endpoints
# -----------------------------------------------------------------------------

@app.get("/subscriptions", response_model=List[SubscriptionRead])
def list_subscriptions():
    """Get a list of all subscriptions available."""
    raise HTTPException(status_code=501, detail="Not implemented")

@app.post("/subscriptions", response_model=SubscriptionRead)
def create_subscription(subscription: SubscriptionCreate = Body(...)):
    """Create a new subscription."""
    raise HTTPException(status_code=501, detail="Not implemented")

@app.get("/subscriptions/{subscription_id}", response_model=SubscriptionRead)
def get_subscription(subscription_id: UUID = Path(..., description="Subscription to retrieve's ID")):
    raise HTTPException(status_code=501, detail="Not implemented")

@app.put("/subscriptions/{subscription_id}", response_model=SubscriptionRead)
def update_subscription(subscription_id: UUID, subscription: SubscriptionUpdate = Body(...)):
    raise HTTPException(status_code=501, detail="Not implemented")

@app.delete("/subscriptions/{subscription_id}")
def delete_subscription(subscription_id: UUID = Path(..., description="Subscription to delete's ID")):
    raise HTTPException(status_code=501, detail="Not implemented")

# -----------------------------------------------------------------------------
# Root
# -----------------------------------------------------------------------------
@app.get("/")
def root():
    return {"message": "Welcome to the Person/Address API. See /docs for OpenAPI UI."}

# -----------------------------------------------------------------------------
# Entrypoint for `python main.py`
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
