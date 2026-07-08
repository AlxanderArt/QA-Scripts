"""Backward-compatible demo API shim for portfolio examples."""

from qa_scripts.demo_api import USERS, create_user, get_user, reset_users

__all__ = ["USERS", "create_user", "get_user", "reset_users"]
