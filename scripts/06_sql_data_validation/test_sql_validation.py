from qa_scripts.sql_validation import build_db, run_validation


def test_sql_validation_checks_pass():
    assert run_validation() == {
        "no_negative_order_totals": True,
        "all_orders_have_customers": True,
        "unique_customer_emails": True,
    }


def test_sql_validation_models_money_as_integer_cents():
    with build_db() as conn:
        columns = {row[1]: row[2] for row in conn.execute("PRAGMA table_info(orders)")}
        assert columns["total_cents"] == "INTEGER"
        assert "total" not in columns
