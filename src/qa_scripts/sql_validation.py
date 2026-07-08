from __future__ import annotations

import sqlite3
from collections.abc import Mapping
from contextlib import closing

SCHEMA_AND_DATA = """
PRAGMA foreign_keys = ON;
CREATE TABLE customers(id INTEGER PRIMARY KEY, email TEXT NOT NULL UNIQUE);
CREATE TABLE orders(
    id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    total REAL NOT NULL CHECK(total >= 0),
    FOREIGN KEY(customer_id) REFERENCES customers(id)
);
INSERT INTO customers VALUES (1, 'ada@example.test'), (2, 'grace@example.test');
INSERT INTO orders VALUES (101, 1, 25.50), (102, 2, 99.99);
"""

VALIDATION_QUERIES: Mapping[str, str] = {
    "no_negative_order_totals": "SELECT COUNT(*) FROM orders WHERE total < 0",
    "all_orders_have_customers": "SELECT COUNT(*) FROM orders o LEFT JOIN customers c ON c.id=o.customer_id WHERE c.id IS NULL",
    "unique_customer_emails": "SELECT COUNT(*) - COUNT(DISTINCT email) FROM customers",
}


def build_db() -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    conn.executescript(SCHEMA_AND_DATA)
    return conn


def validate(conn: sqlite3.Connection) -> dict[str, bool]:
    return {name: conn.execute(query).fetchone()[0] == 0 for name, query in VALIDATION_QUERIES.items()}


def run_validation() -> dict[str, bool]:
    with closing(build_db()) as conn:
        return validate(conn)


def format_checks(checks: dict[str, bool]) -> str:
    return "\n".join(f"{'PASS' if passed else 'FAIL'} - {name}" for name, passed in checks.items())
