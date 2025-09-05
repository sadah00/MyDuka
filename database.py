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