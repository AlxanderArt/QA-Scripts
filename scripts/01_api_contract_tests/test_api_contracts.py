from jsonschema import validate

from qa_scripts.demo_api import create_user, get_user, reset_users

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


def setup_function():
    reset_users()


def test_get_user_contract():
    response = get_user(1)
    assert response["status"] == 200
    validate(response["body"], USER_SCHEMA)


def test_get_missing_user_negative_path():
    assert get_user(999) == {"status": 404, "body": {"error": "not_found"}}


def test_create_user_validates_payload_and_prevents_duplicate_email():
    assert create_user({"name": "", "email": "bad"})["status"] == 400
    created = create_user({"name": "Katherine Johnson", "email": "Katherine@Example.Test"})
    assert created["status"] == 201
    assert created["body"]["email"] == "katherine@example.test"
    validate(created["body"], USER_SCHEMA)
    assert create_user({"name": "Katherine Johnson", "email": "katherine@example.test"}) == {"status": 409, "body": {"error": "duplicate_email"}}
