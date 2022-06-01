import uvicorn
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from typing import Optional, List
app = FastAPI(
    title="Blake's cool app",
    description="LMS for managing students and courses.",
    version="0.0.1"
)
users = []


class User(BaseModel):
    id: int
    email: str
    is_active: bool
    bio: Optional[str]


@app.get("/users",
         response_model=List[User],
         name="get_users",
         description="Returns the list of users.")
async def get_users():
    return users


@app.post("/users")
async def create_users(user: User):
    users.append(user)
    return {"message": "Hello world"}


@app.get("/users/{id}",  # {id} is the path variable referenced by Path()
         name="get_user",
         description="Gets a user by the ID")
async def get_user(
    id: int =
        Path(..., description="The ID of the user you want to look up.", gt=2),
        query: str = Query(None, max_length=5)
        ):
    return users[id]


def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("fastapp.main:app", host="0.0.0.0", port=8001, reload=True)
