import select
import psycopg2

conn = psycopg2.connect(host="localhost", port="5432", user="postgres", password="kimysada6",dbname="myduka_db")
cur=conn.cursor()

cur.execute("SELECT * FROM products")

products = cur.fetchall()

print(products)

cur.execute("SELECT * FROM sales")

sales = cur.fetchall()

print(sales)