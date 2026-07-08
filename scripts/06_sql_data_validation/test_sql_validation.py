from qa_scripts.sql_validation import run_validation


def test_sql_validation_checks_pass():
    assert run_validation() == {
        "no_negative_order_totals": True,
        "all_orders_have_customers": True,
        "unique_customer_emails": True,
    }
