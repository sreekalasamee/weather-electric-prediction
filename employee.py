from flask import*
from database import*
employee=Blueprint('employee',__name__)

@employee.route('/employee_home')
def employee_home():
    return render_template('emp_home.html')


@employee.route('/viewdutiesassign',methods=['GET','POST'])
def viewdutiesassign():
    data={}
    qry="select * from duty where employee_id='%s'"%(id)
    res=select(qry)
    print(res)
    data['view']=res
    return render_template('viewdutiesassign.html',data=data)


@employee.route('/managepayments',methods=['GET','POST'])
def managepayments():
    data={}
    qry="select * from payments"
    data['pay']=select(qry)

    if 'submit' in request.form:
        amount=request.form['ramount']
        pay_type=request.form['rpaytype']
        qry1="insert into payments values(null,'%s','%s')"%(amount,pay_type)
        insert(qry1)
    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
    else:
        action=None
    if action=='delete':
        qry="delete from payments where payment_id='%s'"%(id)
        delete(qry)
        return redirect(url_for('employee.managepayments'))
    
    return render_template('payments.html',data=data)  


@employee.route('/updatepayments',methods=['GET','POST'])
def updatepayments():
    data={}
    qry="select * from payments where payment_id='%s'"%(id)
    data['pay']=select(qry)
    if 'submit' in request.form:
        amount=request.form['ramount']
        pay_type=request.form['rpaytype']
        qry1="update payments set amount='%s',pay_type='%s'"
        update(qry1)
        return '''<script>alert('update successful');window.location="/managepayments"</script>'''
    return render_template('updatepayments.html',data=data)


@employee.route('/managemeterreading',methods=['GET','POST'])
def managemeterreading():
    data={}
    qry="select * from readings"
    data['read']=select(qry)
    if 'submit' in request.form:
        current_reading=request.form['rcurrent_reading']
        qry1="insert into readings values(null,'%s')"%(current_reading)
        insert(qry1)
    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
    else:
        action=None
    if action=='delete':
        qry="delete from readings where reading_id='%s'"%(id)
        delete(qry)
        return redirect(url_for('employee.managemeterreading'))
    return render_template("reading.html",data=data)


@employee.route('/updatereading',methods=['GET','POST'])
def updatereading():
    data={}
    qry="select * from readings where reading_id='%s'"%(id)
    data['read']=select(qry)
    if 'submit' in request.form:
        current_reading=request.form['rcurrent_reading']
        qry1="update readings set current_reading='%s'"
        update(qry1)
        return '''<script>alert('update successful');window.location="/managemeterreading"</script>'''
    return render_template('updatereading.html',data=data)


@employee.route('/leaverequest',methods=['GET','POST'])
def leaverequest():
    data={}
    if 'submit' in request.form:
        date_requested=request.form['date_requested']
        leave_reason=request.form['leave_reason']
        request_status=request.form['request_status']
        qry="insert into leave_request values(null,'%s','%s','%s','%s','%s')"%(date_requested,leave_reason,request_status)
        insert(qry)
    return render_template('leave_request.html',data=data)

