import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / 'database' / 'ecommerce.db'


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def test_missing_order_reference():
    conn = get_connection()
    result = conn.execute(
        'SELECT COUNT(1) AS missing_refs FROM order_items oi LEFT JOIN orders o ON oi.order_id = o.order_id WHERE o.order_id IS NULL'
    ).fetchone()
    print(f"Missing order references: {result['missing_refs']}")
    conn.close()


def test_discount_gt_100():
    conn = get_connection()
    result = conn.execute(
        'SELECT COUNT(1) AS invalid_discounts FROM order_items WHERE discount_percent > 100'
    ).fetchone()
    print(f'Discount > 100 rows: {result['invalid_discounts']}')
    conn.close()


def test_zero_quantity():
    conn = get_connection()
    result = conn.execute(
        'SELECT COUNT(1) AS zero_quantity FROM order_items WHERE quantity = 0'
    ).fetchone()
    print(f'Zero quantity rows: {result['zero_quantity']}')
    conn.close()


def test_future_order_date():
    conn = get_connection()
    result = conn.execute(
        "SELECT COUNT(1) AS future_orders FROM orders WHERE order_date > DATE('now')"
    ).fetchone()
    print(f'Future order_date rows: {result['future_orders']}')
    conn.close()


if __name__ == '__main__':
    if not DB_PATH.exists():
        raise FileNotFoundError('Database not found. Run src/database.py first.')

    print('Running edge-case tests')
    test_missing_order_reference()
    test_discount_gt_100()
    test_zero_quantity()
    test_future_order_date()
