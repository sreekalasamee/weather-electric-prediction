from flask import*
from public import*
from admin import*
from employee import*
from customers import*
app=Flask(__name__)
app.register_blueprint(public)
app.register_blueprint(admin)
app.secret_key='3ruer'
app.register_blueprint(employee)
app.register_blueprint(customers)
app.run(debug=True,port=5050)