import argparse
import sqlite3
from datetime import datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / 'database' / 'ecommerce.db'


def parse_date(value):
    return datetime.strptime(value, '%Y-%m-%d')


def connect_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def pct_change(current, previous):
    if previous in (None, 0):
        return None
    return round((current - previous) / previous * 100, 2)


def build_report(conn, from_date, to_date):
    summary_query = '''
        SELECT
            COUNT(DISTINCT o.order_id) AS total_orders,
            ROUND(SUM(oi.quantity * oi.unit_price * (1 - oi.discount_percent / 100.0)), 2) AS revenue,
            COUNT(DISTINCT o.customer_id) AS unique_customers
        FROM orders o
        JOIN order_items oi ON o.order_id = oi.order_id
        WHERE o.order_date >= ? AND o.order_date <= ?
    '''
    summary = conn.execute(summary_query, (from_date, to_date)).fetchone()

    top_products = conn.execute(
        '''
            SELECT p.product_name,
                   ROUND(SUM(oi.quantity * oi.unit_price * (1 - oi.discount_percent / 100.0)), 2) AS revenue
            FROM order_items oi
            JOIN products p ON oi.product_id = p.product_id
            JOIN orders o ON oi.order_id = o.order_id
            WHERE o.order_date >= ? AND o.order_date <= ?
            GROUP BY p.product_name
            ORDER BY revenue DESC
            LIMIT 3
        ''',
        (from_date, to_date),
    ).fetchall()

    prev_from = parse_date(from_date) - (parse_date(to_date) - parse_date(from_date)) - timedelta(days=1)
    prev_to = parse_date(from_date) - timedelta(days=1)
    prev_summary = conn.execute(summary_query, (prev_from.strftime('%Y-%m-%d'), prev_to.strftime('%Y-%m-%d'))).fetchone()

    def fmt_pct(value):
        return f'{value}%' if value is not None else 'N/A'

    print(f'Report period: {from_date} to {to_date}')
    print(f"Total orders: {summary['total_orders']}")
    print(f"Total revenue: {summary['revenue']}")
    print(f"Unique customers: {summary['unique_customers']}")
    print('Top 3 products:')
    for row in top_products:
        print(f"- {row['product_name']}: {row['revenue']}")
    print('\nComparison with previous period:')
    print(f"- Orders change: {fmt_pct(pct_change(summary['total_orders'], prev_summary['total_orders']))}")
    print(f"- Revenue change: {fmt_pct(pct_change(summary['revenue'], prev_summary['revenue']))}")
    print(f"- Customers change: {fmt_pct(pct_change(summary['unique_customers'], prev_summary['unique_customers']))}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate order analytics summary.')
    parser.add_argument('--report-type', choices=['daily', 'weekly', 'monthly'], required=True)
    parser.add_argument('--from-date', required=True, help='Start date YYYY-MM-DD')
    parser.add_argument('--to-date', required=True, help='End date YYYY-MM-DD')
    args = parser.parse_args()

    if not DB_PATH.exists():
        raise FileNotFoundError('Database not found. Run src/database.py first.')

    conn = connect_db()
    build_report(conn, args.from_date, args.to_date)
    conn.close()
