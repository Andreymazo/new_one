create table employee
(
	employee_id int PRIMARY KEY,
	first_name varchar(100) NOT NULL,
	last_name varchar(100) NOT NULL,
	title varchar(100) NOT NULL,
	birth_date date,
	notes text
);
create table customers(
    customer_id varchar(100) PRIMARY KEY,
    company_name varchar(100) NOT NULL,
    contact_name varchar(100) NOT NULL
    );

create table orders(
    order_id int PRIMARY KEY,
    customer_id varchar(100)  REFERENCES customers(customer_id) NOT NULL,
    employee_id int REFERENCES employee(employee_id) NOT NULL,
    order_date date,
    ship_city varchar(100) NOT NULL
	);