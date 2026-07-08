from __future__ import annotations

from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class TestUser:
    id: str
    email: str
    role: str
    active: bool


def build_user(sequence: int, *, role: str = "customer", active: bool = True) -> dict[str, str | bool]:
    if sequence < 1:
        raise ValueError("sequence must be positive")
    user = TestUser(
        id=f"user_{sequence:04d}",
        email=f"qa-user-{sequence:04d}@example.test",
        role=role,
        active=active,
    )
    return asdict(user)


def build_user_batch(count: int, *, role: str = "customer") -> list[dict[str, str | bool]]:
    if count < 0:
        raise ValueError("count cannot be negative")
    return [build_user(index, role=role) for index in range(1, count + 1)]
