from pathlib import Path
import csv
import random
from faker import Faker

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / 'data' / 'raw'
RAW_DIR.mkdir(parents=True, exist_ok=True)

fake = Faker()
Faker.seed(2026)
random.seed(2026)

ORDER_STATUS = ['PLACED', 'SHIPPED', 'DELIVERED', 'CANCELLED', 'RETURNED']
REGIONS = ['US-W', 'US-E', 'EU', 'APAC', 'LATAM']
CATEGORIES = ['Electronics', 'Clothing', 'Home', 'Books', 'Toys']
SUBCATEGORIES = {
    'Electronics': ['Audio', 'Computers', 'Wearables'],
    'Clothing': ['Men', 'Women', 'Kids'],
    'Home': ['Kitchen', 'Furniture', 'Decor'],
    'Books': ['Fiction', 'Nonfiction', 'Education'],
    'Toys': ['Action', 'Learning', 'Outdoor'],
}
CUSTOMER_TYPES = ['REGULAR', 'PREMIUM', 'VIP']

NUM_CUSTOMERS = 520
NUM_PRODUCTS = 260
NUM_ORDERS = 620
NUM_ORDER_ITEMS = 1420


def generate_customers():
    customers = []
    for customer_id in range(1, NUM_CUSTOMERS + 1):
        name = fake.name()
        email = fake.email()
        if random.random() < 0.02:
            email = email.replace('@', '', 1) if random.random() < 0.5 else email.split('@')[0] + '@'
        registration_date = fake.date_between(start_date='-3y', end_date='today').strftime('%Y-%m-%d')
        customers.append({
            'customer_id': customer_id,
            'customer_name': name,
            'email': email,
            'registration_date': registration_date,
            'customer_type': random.choices(CUSTOMER_TYPES, [0.7, 0.2, 0.1])[0],
        })
    return customers


def generate_products():
    products = []
    for product_id in range(1, NUM_PRODUCTS + 1):
        category = random.choice(CATEGORIES)
        subcategory = random.choice(SUBCATEGORIES[category])
        base_name = f'{subcategory} {fake.word()}'
        if random.random() < 0.15:
            base_name = f'  {base_name.upper()}  ' if random.random() < 0.5 else f'{base_name.title()}  '
        cost_price = round(random.uniform(5, 450), 2)
        products.append({
            'product_id': product_id,
            'product_name': base_name,
            'category': category,
            'subcategory': subcategory,
            'cost_price': cost_price,
        })
    return products


def generate_orders(customers):
    orders = []
    for order_id in range(1, NUM_ORDERS + 1):
        customer = random.choice(customers)
        order_date = fake.date_time_between(start_date='-18M', end_date='now')
        order_date = order_date.strftime('%d-%m-%Y %H:%M:%S') if random.random() < 0.08 else order_date.strftime('%Y-%m-%d %H:%M:%S')
        status = random.choices(ORDER_STATUS, [0.3, 0.25, 0.3, 0.1, 0.05])[0]
        region_code = random.choice(REGIONS)
        customer_id = customer['customer_id']
        if random.random() < 0.05:
            customer_id = ''
        orders.append({
            'order_id': order_id,
            'customer_id': customer_id,
            'order_date': order_date,
            'status': status,
            'region_code': region_code,
        })
    return orders


def generate_order_items(orders, products):
    order_items = []
    item_id = 1
    order_ids = [order['order_id'] for order in orders]
    for _ in range(NUM_ORDER_ITEMS):
        order_id = random.choice(order_ids)
        if random.random() < 0.01:
            order_id = max(order_ids) + random.randint(1, 20)
        product = random.choice(products)
        quantity = random.randint(1, 6)
        if random.random() < 0.03:
            quantity = -random.randint(1, 4)
        unit_price = round(product['cost_price'] * random.uniform(1.1, 2.2), 2)
        discount_percent = round(random.uniform(0, 40), 2)
        order_items.append({
            'item_id': item_id,
            'order_id': order_id,
            'product_id': product['product_id'],
            'quantity': quantity,
            'unit_price': unit_price,
            'discount_percent': discount_percent,
        })
        item_id += 1
    return order_items


def write_csv(path, rows, fieldnames):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


if __name__ == '__main__':
    customers = generate_customers()
    products = generate_products()
    orders = generate_orders(customers)
    order_items = generate_order_items(orders, products)

    write_csv(RAW_DIR / 'customers.csv', customers, ['customer_id', 'customer_name', 'email', 'registration_date', 'customer_type'])
    write_csv(RAW_DIR / 'products.csv', products, ['product_id', 'product_name', 'category', 'subcategory', 'cost_price'])
    write_csv(RAW_DIR / 'orders.csv', orders, ['order_id', 'customer_id', 'order_date', 'status', 'region_code'])
    write_csv(RAW_DIR / 'order_items.csv', order_items, ['item_id', 'order_id', 'product_id', 'quantity', 'unit_price', 'discount_percent'])

    print(f'Generated raw CSV files in {RAW_DIR}')
