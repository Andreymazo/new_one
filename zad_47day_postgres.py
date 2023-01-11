import psycopg2
import csv

conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='12345')
try:
    with conn:
        with conn.cursor() as cur:
            conn.autocommit = True

            with open('customers_data.csv', 'r') as f:
                 next(f)  # Skip the header row.
                 #f , <database name>, Comma-Seperated
                 cur.copy_from(f, 'customers', sep=',')
            with open('employees_data.csv', 'r', encoding='utf-8') as f:
                data_empl = csv.DictReader(f);
                index = 1
                for i in data_empl:
                    cur.execute('INSERT INTO employee VALUES (%s, %s, %s, %s, %s, %s)',
                                (index, i['first_name'], i['last_name'], i['title'], i['birth_date'], i['notes']))
                    index += 1
            with open('orders_data.csv', 'r', encoding='utf-8') as f:
                next(f)  # Skip the header row.
                #      #f , <database name>, Comma-Seperated
                cur.copy_from(f, 'orders', sep=',')
                # data_order = csv.DictReader(f)
                # for i in data_order:
                #     cur.execute('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)', (i['order_id'], i['customer_id'], i['employee_id'], i['order_date'], i['ship_city']))

                    # # next(f)  # Skip the header row.

finally:
    conn.close()