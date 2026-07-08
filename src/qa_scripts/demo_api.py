from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any, TypedDict


class ApiResponse(TypedDict):
    status: int
    body: dict[str, Any]


@dataclass(frozen=True)
class User:
    id: int
    name: str
    email: str
    active: bool = True


_INITIAL_USERS: dict[int, User] = {
    1: User(1, "Ada Lovelace", "ada@example.test"),
    2: User(2, "Grace Hopper", "grace@example.test"),
}
USERS: dict[int, User] = dict(_INITIAL_USERS)


def reset_users() -> None:
    """Reset the in-memory demo API so tests remain isolated and repeatable."""
    USERS.clear()
    USERS.update(_INITIAL_USERS)


def get_user(user_id: int) -> ApiResponse:
    user = USERS.get(user_id)
    if user is None:
        return {"status": 404, "body": {"error": "not_found"}}
    return {"status": 200, "body": asdict(user)}


def create_user(payload: dict[str, Any]) -> ApiResponse:
    name = str(payload.get("name", "")).strip()
    email = str(payload.get("email", "")).strip().lower()
    if not name or "@" not in email:
        return {"status": 400, "body": {"error": "invalid_user"}}
    if any(user.email == email for user in USERS.values()):
        return {"status": 409, "body": {"error": "duplicate_email"}}
    new_id = max(USERS, default=0) + 1
    USERS[new_id] = User(new_id, name, email)
    return {"status": 201, "body": asdict(USERS[new_id])}
