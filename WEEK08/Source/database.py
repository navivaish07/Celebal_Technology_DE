from pathlib import Path
import csv
import sqlite3

ROOT = Path(__file__).resolve().parents[1]
CLEAN_DIR = ROOT / 'data' / 'cleaned'
DB_DIR = ROOT / 'database'
DB_PATH = DB_DIR / 'ecommerce.db'

TABLE_CONFIG = {
    'customers': {
        'schema': [
            ('customer_id', 'INTEGER'),
            ('customer_name', 'TEXT'),
            ('email', 'TEXT'),
            ('registration_date', 'TEXT'),
            ('customer_type', 'TEXT'),
        ],
        'csv_path': CLEAN_DIR / 'customers_cleaned.csv',
    },
    'products': {
        'schema': [
            ('product_id', 'INTEGER'),
            ('product_name', 'TEXT'),
            ('category', 'TEXT'),
            ('subcategory', 'TEXT'),
            ('cost_price', 'REAL'),
        ],
        'csv_path': CLEAN_DIR / 'products_cleaned.csv',
    },
    'orders': {
        'schema': [
            ('order_id', 'INTEGER'),
            ('customer_id', 'INTEGER'),
            ('order_date', 'TEXT'),
            ('status', 'TEXT'),
            ('region_code', 'TEXT'),
        ],
        'csv_path': CLEAN_DIR / 'orders_cleaned.csv',
    },
    'order_items': {
        'schema': [
            ('item_id', 'INTEGER'),
            ('order_id', 'INTEGER'),
            ('product_id', 'INTEGER'),
            ('quantity', 'INTEGER'),
            ('unit_price', 'REAL'),
            ('discount_percent', 'REAL'),
        ],
        'csv_path': CLEAN_DIR / 'order_items_cleaned.csv',
    },
}


def connect_db():
    DB_DIR.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def create_schema(conn):
    cursor = conn.cursor()
    for table_name, config in TABLE_CONFIG.items():
        columns = ', '.join(f'{column} {dtype}' for column, dtype in config['schema'])
        cursor.execute(f'DROP TABLE IF EXISTS {table_name}')
        cursor.execute(f'CREATE TABLE {table_name} ({columns})')
    conn.commit()


def load_csv_to_table(conn, table_name, csv_path):
    if not csv_path.exists():
        raise FileNotFoundError(f'Expected CSV file not found: {csv_path}')

    with csv_path.open(newline='', encoding='utf-8') as handle:
        reader = csv.DictReader(handle)
        fieldnames = reader.fieldnames or []
        placeholders = ', '.join('?' for _ in fieldnames)
        insert_sql = f'INSERT INTO {table_name} ({", ".join(fieldnames)}) VALUES ({placeholders})'
        rows = []
        for row in reader:
            values = [None if value == '' else value for value in (row.get(col) for col in fieldnames)]
            rows.append(tuple(values))
        if rows:
            conn.executemany(insert_sql, rows)


def load_cleaned_data():
    DB_DIR.mkdir(parents=True, exist_ok=True)
    conn = connect_db()
    create_schema(conn)

    for table_name, config in TABLE_CONFIG.items():
        load_csv_to_table(conn, table_name, config['csv_path'])

    conn.commit()
    conn.close()
    return DB_PATH


if __name__ == '__main__':
    load_cleaned_data()
    print(f'Loaded cleaned data into SQLite database at {DB_PATH}')
