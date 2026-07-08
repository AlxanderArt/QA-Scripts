from dataclasses import dataclass, asdict

@dataclass
class User:
    id: int
    name: str
    email: str
    active: bool = True

USERS = {
    1: User(1, "Ada Lovelace", "ada@example.test"),
    2: User(2, "Grace Hopper", "grace@example.test"),
}

def get_user(user_id: int):
    user = USERS.get(user_id)
    if not user:
        return {"status": 404, "body": {"error": "not_found"}}
    return {"status": 200, "body": asdict(user)}

def create_user(payload: dict):
    if not payload.get("name") or "@" not in payload.get("email", ""):
        return {"status": 400, "body": {"error": "invalid_user"}}
    new_id = max(USERS) + 1
    USERS[new_id] = User(new_id, payload["name"], payload["email"])
    return {"status": 201, "body": asdict(USERS[new_id])}
