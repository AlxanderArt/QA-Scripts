from jsonschema import validate
from apps.demo_api.demo_api import get_user, create_user

USER_SCHEMA = {
    "type": "object",
    "required": ["id", "name", "email", "active"],
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string", "minLength": 1},
        "email": {"type": "string", "pattern": "@"},
        "active": {"type": "boolean"},
    },
}

def test_get_user_contract():
    response = get_user(1)
    assert response["status"] == 200
    validate(response["body"], USER_SCHEMA)

def test_get_missing_user_negative_path():
    assert get_user(999) == {"status": 404, "body": {"error": "not_found"}}

def test_create_user_validates_payload():
    assert create_user({"name": "", "email": "bad"})["status"] == 400
    created = create_user({"name": "Katherine Johnson", "email": "katherine@example.test"})
    assert created["status"] == 201
    validate(created["body"], USER_SCHEMA)
