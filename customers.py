from admin import*
from database import*
customers=Blueprint('customers',__name__)

@customers.route('/cust_home')
def cust_home():
    return render_template('cust_home.html')


@customers.route('/viewconnectreq2',methods=['GET','POST'])
def viewconnectreq2():
    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
    else:
        action=None
        if action=="accept":
         qry="update connection_req set request_status='accept' where request_id='%s'"%(id)
         update(qry)
        if action=="reject":
         qry3="update connection_req set request_status='reject' where request_id='%s'"%(id)
         update(qry3)
    data={}
    qry1="select * from connection_request"
    data['user']=select(qry1)
    return render_template('viewconnectreq2.html',data=data)

@customers.route('/viewmeterread2',methods=['GET','POST'])
def viewmeterread2():
    data={}
    qry="select * from readings"
    data['user']=select(qry)
    return render_template('/viewmeterread2.html',data=data)

@customers.route('/viewbillhistory',methods=['GET','POST'])
def viewbillhistory():
    data={}
    qry="select * from bills"
    data['user']=select(qry)

    if 'submit' in request.form:
       usage_unit=request.form['rusage_unit']
       amount=request.form['ramount']
       qry="insert into bills values(null,'%s','%s','%s','%s','%s','%s')"%(usage_unit,amount)
       insert(qry)
    return render_template('/viewbillhistory.html',data=data)

@customers.route('/makepayment',methods=['GET','POST'])
def makepayment():
   data={}
   qry="select * from payments"
   data['user']=select(qry)
   if 'submit' in request.form:
      bill_id=request.form['bill_id']
      amount=request.form['amount']
      pay_type=request.form['pay_type']
      qry="insert into payments values(null,'%s','%s','%s')"%(bill_id,amount,pay_type)
      insert(qry)
   return render_template('makepayment.html',data=data)


@customers.route('/paynowbil',methods=['GET','POST'])
def paynowbil():
   data={}
   id=request.args['id']
   qry="select * from payments"
   data['user']=select(qry)
   if 'submit' in request.form:

      amount=request.form['amount']
      pay_type=request.form['pay_type']
      qry="insert into payments values(null,'%s','%s','%s',curdate())"%(id,amount,pay_type)
      insert(qry)
   return render_template('paynowbil.html',data=data)

@customers.route('/complaintreg',methods=['GET','POST'])
def complaintreg():
    data={}
    qry="select * from complaints"
    data['user']=select(qry)
    if 'submit' in request.form:
       complaint_description=request.form['rcomplaint_desc']
       qry="insert into complaints values(null,'%s','%s',curdate(),'pending')"%(session['con'],complaint_description)
       insert(qry)
    return render_template('complaintreg.html',data=data)

