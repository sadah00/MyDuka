import select
import psycopg2

conn = psycopg2.connect(host="localhost", port="5432", user="postgres", password="kimysada6",dbname="myduka_db")
cur=conn.cursor()

# displaying products
def get_products():
    cur.execute("SELECT * FROM products")
    products = cur.fetchall()
    return products

# products = get_products()
# print(products)

# displaying sales
def get_sales():
    cur.execute("SELECT * FROM sales")
    sales = cur.fetchall()
    return sales

# sales=get_sales()
# print(sales)

# insert products
def insert_products(product_values):
    cur.execute(f"INSERT INTO products (name,buying_price,selling_price) VALUES{product_values}")
    conn.commit()
# input from user
# name= input("Enter product name: ")
# buying_price= float(input("Enter buying price: "))
# selling_price= float(input("Enter selling price: "))

# product_values=(name,buying_price,selling_price)

# insert_products(product_values)

# inserting more products

# products1=('flour',140,180)
# products2=('sugar',120,150)
# insert_products(products1)
# insert_products(products2)

# insert sales
def insert_sales(sale_values):
    cur.execute(f"INSERT INTO sales (pid, quantity) VALUES {sale_values}")
    conn.commit()

# pid=int(input("Enter product id: "))
# quantity=int(input("Enter quantity: "))

# sale_values=(pid,quantity)

# insert_sales(sale_values)

def get_stock():
    cur.execute("SELECT * FROM stock")
    stock = cur.fetchall()
    return stock

def insert_stock(stock_values):
    cur.execute(f"INSERT INTO stock (pid,stock_quantity) VALUES{stock_values}")
    conn.commit()

def available_stock(pid):
    cur.execute(f"select sum(stock_quantity) from stock where pid = {pid}")
    total_stock = cur.fetchone()[0] or 0

    cur.execute(f"select sum(quantity) from sales where pid = {pid}")
    total_sales = cur.fetchone()[0] or 0

    return total_stock - total_sales

def insert_user(user_details):
    cur.execute(f"INSERT INTO users (full_name,phone_number,email,password) VALUES{user_details}")
    conn.commit()


def check_user(email):
    cur.execute("select * from users where email = %s",(email,))
    user = cur.fetchone()   
    return user
# test = check_user('john@gmail.com')
# print(test)

def sales_per_day():
    cur.execute("""
    select date(sales.created_at) as date, sum(products.selling_price * sales.quantity) as
    total_sales from products inner join sales on sales.pid = products.id group by(date);
    """)
    daily_sales = cur.fetchall()
    return daily_sales

def profit_per_day():
    cur.execute("""
        select date(sales.created_at) as date, sum((products.selling_price - products.buying_price)* sales.quantity) as 
        profit from sales join products on products.id = sales.pid group by(date);
    """)
    daily_profit = cur.fetchall()
    return daily_profit

def sales_per_product():
    cur.execute("""
        select products.name as p_name, sum(sales.quantity * products.selling_price) as tota_sales
        from products join sales on products.id = sales.pid group by(p_name);
    """)
    product_sales = cur.fetchall()
    return product_sales

def profit_per_product():
    cur.execute("""
    select products.name as p_name ,sum((products.selling_price - products.buying_price) * sales.quantity) as profit from
    sales join products on sales.pid = products.id group by(p_name);
    """)
    product_profit = cur.fetchall()
    return product_profit

test1=sales_per_product()
product_names = [i[0] for i in test1]
sales_made = [i[1] for i in test1]
print (product_names)
print(sales_made)