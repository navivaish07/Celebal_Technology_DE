
--print all columns from the table 
select * from customers; 

--print specific columns from the table 
select first_name , last_name , city from customers ;

--print the UNIQUE categories in the table 
select * from products;
select DISTINCT category from products ;

--identifying primary key in the tables
PRAGMA table_info(products);
PRAGMA table_info(orders);
pragma table_info(order_items);
PRAGMA table_info(customers);
PRAGMA index_list(customers);

--Entering Duplicate records for the not null and UNIQUE CONSTRAINT columns 
insert into customers values ( 109 , 'Vaishh' , 'Dhanwate' , 'aarav.s@email.com' , 'Nagpur' , 'Maharashtra' , '2024-12-12' , TRUE );

--Entering the Negative value againts the contraint
SELECT sql FROM sqlite_master WHERE type = 'table' AND name = 'products';
insert into products 
values (209 , 'USB Cable' , 'Electronics' , 'Boat' , -50 ,100);


