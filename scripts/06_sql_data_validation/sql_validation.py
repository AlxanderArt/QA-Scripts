import sqlite3

def build_db():
    conn = sqlite3.connect(":memory:")
    conn.executescript("""
    CREATE TABLE customers(id INTEGER PRIMARY KEY, email TEXT NOT NULL UNIQUE);
    CREATE TABLE orders(id INTEGER PRIMARY KEY, customer_id INTEGER NOT NULL, total REAL NOT NULL,
      FOREIGN KEY(customer_id) REFERENCES customers(id));
    INSERT INTO customers VALUES (1, 'ada@example.test'), (2, 'grace@example.test');
    INSERT INTO orders VALUES (101, 1, 25.50), (102, 2, 99.99);
    """)
    return conn

def validate(conn):
    return {
        "no_negative_order_totals": conn.execute("SELECT COUNT(*) FROM orders WHERE total < 0").fetchone()[0] == 0,
        "all_orders_have_customers": conn.execute("SELECT COUNT(*) FROM orders o LEFT JOIN customers c ON c.id=o.customer_id WHERE c.id IS NULL").fetchone()[0] == 0,
        "unique_customer_emails": conn.execute("SELECT COUNT(*) = COUNT(DISTINCT email) FROM customers").fetchone()[0] == 1,
    }

if __name__ == "__main__":
    checks = validate(build_db())
    for name, passed in checks.items():
        print(f"{'PASS' if passed else 'FAIL'} - {name}")
    raise SystemExit(0 if all(checks.values()) else 1)
