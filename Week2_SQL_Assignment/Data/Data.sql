BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "customers" (
	"customer_id"	INT,
	"first_name"	VARCHAR(50) NOT NULL,
	"last_name"	VARCHAR(50) NOT NULL,
	"email"	VARCHAR(100) NOT NULL UNIQUE,
	"city"	VARCHAR(50) NOT NULL,
	"state"	VARCHAR(50) NOT NULL,
	"join_date"	DATE NOT NULL,
	"is_premium"	BOOLEAN DEFAULT FALSE,
	PRIMARY KEY("customer_id")
);
CREATE TABLE IF NOT EXISTS "order_items" (
	"item_id"	INT,
	"order_id"	INT NOT NULL,
	"product_id"	INT NOT NULL,
	"quantity"	INT NOT NULL CHECK("quantity" > 0),
	"unit_price"	DECIMAL(10, 2) NOT NULL CHECK("unit_price" > 0),
	"discount_pct"	DECIMAL(5, 2) DEFAULT 0 CHECK("discount_pct" BETWEEN 0 AND 100),
	PRIMARY KEY("item_id"),
	FOREIGN KEY("order_id") REFERENCES "orders"("order_id"),
	FOREIGN KEY("product_id") REFERENCES "products"("product_id")
);
CREATE TABLE IF NOT EXISTS "orders" (
	"order_id"	INT,
	"customer_id"	INT NOT NULL,
	"order_date"	DATE NOT NULL,
	"status"	VARCHAR(20) NOT NULL DEFAULT 'Pending' CHECK("status" IN ('Pending', 'Shipped', 'Delivered', 'Cancelled')),
	"total_amount"	DECIMAL(12, 2) NOT NULL CHECK("total_amount" >= 0),
	PRIMARY KEY("order_id"),
	FOREIGN KEY("customer_id") REFERENCES "customers"("customer_id")
);
CREATE TABLE IF NOT EXISTS "products" (
	"product_id"	INT,
	"product_name"	VARCHAR(100) NOT NULL,
	"category"	VARCHAR(50) NOT NULL,
	"brand"	VARCHAR(50) NOT NULL,
	"unit_price"	DECIMAL(10, 2) NOT NULL CHECK("unit_price" > 0),
	"stock_qty"	INT NOT NULL DEFAULT 0 CHECK("stock_qty" >= 0),
	PRIMARY KEY("product_id")
);
INSERT INTO "customers" VALUES (101,'Aarav','Sharma','aarav.s@email.com','Mumbai','Maharashtra','2024-01-15',1);
INSERT INTO "customers" VALUES (102,'Priya','Patel','priya.p@email.com','Ahmedabad','Gujarat','2024-02-20',0);
INSERT INTO "customers" VALUES (103,'Rohan','Gupta','rohan.g@email.com','Delhi','Delhi','2024-03-10',1);
INSERT INTO "customers" VALUES (104,'Sneha','Reddy','sneha.r@email.com','Hyderabad','Telangana','2024-04-05',0);
INSERT INTO "customers" VALUES (105,'Vikram','Singh','vikram.s@email.com','Jaipur','Rajasthan','2024-05-12',1);
INSERT INTO "customers" VALUES (106,'Ananya','Iyer','ananya.i@email.com','Chennai','Tamil Nadu','2024-06-18',0);
INSERT INTO "customers" VALUES (107,'Karan','Mehta','karan.m@email.com','Pune','Maharashtra','2024-07-22',1);
INSERT INTO "customers" VALUES (108,'Divya','Nair','divya.n@email.com','Kochi','Kerala','2024-08-30',0);
INSERT INTO "order_items" VALUES (5001,1001,201,2,1499,0);
INSERT INTO "order_items" VALUES (5002,1001,207,1,899,10);
INSERT INTO "order_items" VALUES (5003,1002,202,1,799,0);
INSERT INTO "order_items" VALUES (5004,1003,203,1,2999,0);
INSERT INTO "order_items" VALUES (5005,1003,204,1,4599,5);
INSERT INTO "order_items" VALUES (5006,1004,205,1,3499,0);
INSERT INTO "order_items" VALUES (5007,1005,203,1,2999,0);
INSERT INTO "order_items" VALUES (5008,1006,201,1,1499,10);
INSERT INTO "order_items" VALUES (5009,1006,204,1,4599,5);
INSERT INTO "order_items" VALUES (5010,1007,206,1,1299,0);
INSERT INTO "order_items" VALUES (5011,1008,207,1,899,0);
INSERT INTO "order_items" VALUES (5012,1009,205,1,3499,0);
INSERT INTO "order_items" VALUES (5013,1009,208,2,599,15);
INSERT INTO "order_items" VALUES (5014,1010,206,1,1299,0);
INSERT INTO "order_items" VALUES (5015,1010,208,1,599,0);
INSERT INTO "orders" VALUES (1001,101,'2024-08-01','Delivered',4498);
INSERT INTO "orders" VALUES (1002,102,'2024-08-03','Delivered',799);
INSERT INTO "orders" VALUES (1003,103,'2024-08-05','Shipped',7498);
INSERT INTO "orders" VALUES (1004,101,'2024-08-10','Delivered',3499);
INSERT INTO "orders" VALUES (1005,104,'2024-08-12','Cancelled',2999);
INSERT INTO "orders" VALUES (1006,105,'2024-08-15','Delivered',5898);
INSERT INTO "orders" VALUES (1007,106,'2024-08-18','Pending',1299);
INSERT INTO "orders" VALUES (1008,103,'2024-08-20','Delivered',899);
INSERT INTO "orders" VALUES (1009,107,'2024-08-25','Shipped',6098);
INSERT INTO "orders" VALUES (1010,108,'2024-08-28','Delivered',1598);
INSERT INTO "products" VALUES (201,'Wireless Earbuds','Electronics','BoAt',1499,250);
INSERT INTO "products" VALUES (202,'Cotton T-Shirt','Clothing','Levis',799,500);
INSERT INTO "products" VALUES (203,'Smart Watch','Electronics','Noise',2999,150);
INSERT INTO "products" VALUES (204,'Running Shoes','Clothing','Nike',4599,120);
INSERT INTO "products" VALUES (205,'Bluetooth Speaker','Electronics','JBL',3499,200);
INSERT INTO "products" VALUES (206,'Bedsheet Set','Home','Spaces',1299,300);
INSERT INTO "products" VALUES (207,'Laptop Stand','Electronics','AmazonBasics',899,180);
INSERT INTO "products" VALUES (208,'Cushion Covers (Set)','Home','HomeCenter',599,400);
CREATE INDEX IF NOT EXISTS "idx_customers_city" ON "customers" (
	"city"
);
CREATE INDEX IF NOT EXISTS "idx_customers_state" ON "customers" (
	"state"
);
CREATE INDEX IF NOT EXISTS "idx_orders_date" ON "orders" (
	"order_date"
);
CREATE INDEX IF NOT EXISTS "idx_orders_status" ON "orders" (
	"status"
);
CREATE INDEX IF NOT EXISTS "idx_products_category" ON "products" (
	"category"
);
COMMIT;
