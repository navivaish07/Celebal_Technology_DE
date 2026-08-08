from datetime import datetime
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / 'data' / 'raw'
CLEAN_DIR = ROOT / 'data' / 'cleaned'
REPORTS_DIR = ROOT / 'reports'

INPUT_FILES = {
    'orders': RAW_DIR / 'orders.csv',
    'products': RAW_DIR / 'products.csv',
    'customers': RAW_DIR / 'customers.csv',
    'order_items': RAW_DIR / 'order_items.csv',
}

OUTPUT_FILES = {
    'orders': CLEAN_DIR / 'orders_cleaned.csv',
    'products': CLEAN_DIR / 'products_cleaned.csv',
    'customers': CLEAN_DIR / 'customers_cleaned.csv',
    'order_items': CLEAN_DIR / 'order_items_cleaned.csv',
}


def parse_order_date(value):
    if pd.isna(value):
        return None
    for fmt in ['%Y-%m-%d %H:%M:%S', '%d-%m-%Y %H:%M:%S', '%Y/%m/%d %H:%M:%S']:
        try:
            return datetime.strptime(str(value).strip(), fmt)
        except ValueError:
            continue
    return None


def clean_orders(df_orders):
    issues = []
    df = df_orders.copy()
    df['order_date_parsed'] = df['order_date'].apply(parse_order_date)
    invalid_dates = df[df['order_date_parsed'].isna()]
    if not invalid_dates.empty:
        issues.append(f'{len(invalid_dates)} orders have invalid or unparseable order_date')
    df['order_date'] = df['order_date_parsed'].apply(lambda dt: dt.strftime('%Y-%m-%d %H:%M:%S') if dt else '')
    df.drop(columns=['order_date_parsed'], inplace=True)

    missing_customers = df['customer_id'].isna() | (df['customer_id'].astype(str).str.strip() == '')
    if missing_customers.any():
        issues.append(f'{missing_customers.sum()} orders have missing customer_id')
        df.loc[missing_customers, 'customer_id'] = 0
    df['customer_id'] = df['customer_id'].astype(int)
    return df, issues


def clean_products(df_products):
    issues = []
    df = df_products.copy()
    df['product_name'] = (
        df['product_name'].astype(str)
        .str.strip()
        .replace(r'\s+', ' ', regex=True)
        .str.title()
    )
    invalid_names = df['product_name'].str.contains(r'^\s|\s$', regex=True)
    if invalid_names.any():
        issues.append(f'{invalid_names.sum()} products required product_name normalization')
    return df, issues


def validate_emails(df_customers):
    invalid = df_customers[~df_customers['email'].astype(str).str.match(r'^[^@\s]+@[^@\s]+\.[^@\s]+$')]
    return invalid[['customer_id', 'email']]


def check_referential_integrity(df_orders, df_order_items):
    valid_order_ids = set(df_orders['order_id'].astype(int).tolist())
    invalid_items = df_order_items[~df_order_items['order_id'].astype(int).isin(valid_order_ids)]
    return invalid_items


def save_csv(path, df):
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)


def save_report(text):
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    report_path = REPORTS_DIR / 'data_quality_report.txt'
    report_path.write_text(text, encoding='utf-8')
    return report_path


if __name__ == '__main__':
    CLEAN_DIR.mkdir(parents=True, exist_ok=True)
    orders = pd.read_csv(INPUT_FILES['orders'], dtype=str)
    products = pd.read_csv(INPUT_FILES['products'], dtype=str)
    customers = pd.read_csv(INPUT_FILES['customers'], dtype=str)
    order_items = pd.read_csv(INPUT_FILES['order_items'], dtype=str)

    orders_cleaned, order_issues = clean_orders(orders)
    products_cleaned, product_issues = clean_products(products)
    invalid_emails = validate_emails(customers)
    invalid_order_items = check_referential_integrity(orders_cleaned, order_items)

    save_csv(OUTPUT_FILES['orders'], orders_cleaned)
    save_csv(OUTPUT_FILES['products'], products_cleaned)
    save_csv(OUTPUT_FILES['customers'], customers)
    save_csv(OUTPUT_FILES['order_items'], order_items)

    report_lines = [
        'Data Quality Report',
        '===================',
        f'Raw orders rows: {len(orders)}',
        f'Raw products rows: {len(products)}',
        f'Raw customers rows: {len(customers)}',
        f'Raw order_items rows: {len(order_items)}',
        '',
        'Cleaning Issues',
        '--------------',
    ]
    report_lines.extend(order_issues or ['No order date or missing customer issues found.'])
    report_lines.extend(product_issues or ['No product name normalization issues found.'])
    report_lines.append(f'Invalid emails found: {len(invalid_emails)}')
    report_lines.append(f'Invalid order_items references: {len(invalid_order_items)}')
    if not invalid_emails.empty:
        report_lines.append('Sample invalid emails:')
        for _, row in invalid_emails.head(10).iterrows():
            report_lines.append(f" - customer_id={row['customer_id']} email={row['email']}")
    if not invalid_order_items.empty:
        report_lines.append('Sample invalid order_items rows:')
        for _, row in invalid_order_items.head(10).iterrows():
            report_lines.append(f" - item_id={row['item_id']} order_id={row['order_id']}")

    report_path = save_report('\n'.join(report_lines))
    print(f'Cleaned files written to {CLEAN_DIR}')
    print(f'Report written to {report_path}')
