from flask import Flask , render_template ,request ,redirect ,url_for,flash,session
from database import get_products ,get_sales,get_stock,insert_products,insert_sales,insert_stock,available_stock,insert_user,check_user,sales_per_day,sales_per_product,profit_per_day,profit_per_product
from flask_bcrypt import Bcrypt
from functools import wraps

# creating a flask instance
app = Flask(__name__)

bcrypt = Bcrypt(app)

app.secret_key = 'delicate88'

@app.route('/')  # unique routes
def home():  # must have a unique name
    return render_template("index.html")

def login_required(f):
    @wraps(f)
    def protected(*args,**kwargs):
        if 'email' not in session:
            return redirect(url_for('login'))
        return f(*args,**kwargs)
    return protected

@app.route('/dashboard') # decorator function
@login_required
def dashboard(): # View function - giving back data
    product_sales = sales_per_product()
    daily_sales = sales_per_day()
    product_profit = profit_per_product()
    daily_profit = profit_per_day()
    
    product_names = [i[0] for i in product_sales]
    sales_per_p = [i[1] for i in product_sales]
    profit_per_p = [i[1] for i in product_profit]

    date = [i[0] for i in daily_sales]
    sales_per_d = [i[1] for i in daily_sales]
    profit_per_d = [i[1] for i in daily_profit]



    return render_template("dashboard.html",
                product_names = product_names,sales_per_p = sales_per_p,profit_per_p = profit_per_p,     
                date = date,sales_per_d = sales_per_d,profit_per_d = profit_per_d     
               )

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        registered_user = check_user(email)
        print(registered_user)
        if not registered_user:
            flash("User doesn't exist,Please Register","danger")
            return redirect(url_for('register'))
        else:
            if bcrypt.check_password_hash(registered_user[-1],password):
                flash("Logged in Successfully","Success")
                session["email"]=email
                return redirect(url_for("dashboard"))
            else:
                flash("Password incorrect,try again","danger")
        
    return render_template("login.html")

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        full_name = request.form['full_name']
        phone_number = request.form['phone_number']
        email = request.form['email']
        password = request.form['password']
        existing_user = check_user(email)

        if not existing_user:
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            new_user = (full_name,phone_number,email,hashed_password)
            insert_user(new_user)
            flash("User registered successfully","success")
            return redirect(url_for('register'))
        
        else:
            flash("User already exists,please login","danger")
    return render_template("register.html")    

@app.route('/stock')
@login_required
def stock():
    stock = get_stock()
    products = get_products()
    return render_template("stock.html",stock = stock, products = products)

@app.route('/manage_stock',methods=['GET','POST'])
def manage_stock():
    pid = request.form["pid"]
    stock_quantity= request.form["stockquantity"]

    new_stock=(pid,stock_quantity)
    insert_stock(new_stock)
    flash("Stock updated successfully","success")
    return redirect(url_for('stock'))

@app.route('/products')
@login_required
def products():
    products = get_products()
    return render_template("products.html",products = products )

@app.route('/add_products',methods=['GET','POST'])
def add_products():
    product_name = request.form["product_name"]
    buying_price = request.form["buying_price"]
    selling_price = request.form["selling_price"]

    new_products = (product_name,buying_price,selling_price)
    insert_products(new_products)
    flash("Product added successfully","success")
    return redirect(url_for('products'))

@app.route('/sales')
@login_required
def sales():
    sales = get_sales()
    products = get_products()
    return render_template("sales.html", sales = sales, products = products)

@app.route('/make_sale', methods=['GET','POST'])
def make_sale():
    pid= request.form["pid"]
    quantity= request.form["quantity"]

    new_sale=(pid,quantity)
    check_stock = available_stock(pid)
    if check_stock < float(quantity):
        print("Insufficient stock")
        return redirect(url_for('sales'))
    insert_sales(new_sale)
    flash("Sale made successfully","success")
    return redirect(url_for('sales'))

@app.route('/logout')
def logout():
    session.pop('email',None)
    flash("Logged out Successfully")
    return redirect(url_for('login'))




app.run(debug=True)