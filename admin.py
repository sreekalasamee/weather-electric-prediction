from flask import*
from database import*
admin=Blueprint('admin',__name__)

@admin.route('/adminhome')
def admin_home():
 if not session.get('logid')is None:
    return redirect(url_for('public.login'))
 else:
    return render_template('adminhome.html')
    

@admin.route('/manageemp',methods=['GET','POST'])
def manageemp():
    if not session.get('login')is None:
        data={}
        qry="select * from employees "
        data['c']=select(qry)

        if 'submit' in request.form:
            fname=request.form['rfname']
            lname=request.form['rlname']
            joined_date=request.form['rjoinda']
            dob=request.form['rdob']
            gender=request.form['gender']
            house_name=request.form['rhname']
            place=request.form['rplace']
            pincode=request.form['rpin']
            phoneno=request.form['rphoneno']
            email=request.form['remail']
            username=request.form['user']
            password=request.form['pass']
            qry1="insert into login values(null,'%s','%s','employee')"%(username,password)
            lid=insert(qry1)
            qry2="insert into employees values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(lid,fname,lname,joined_date,dob,gender,house_name,place,pincode,phoneno,email)
            insert(qry2)
        if 'action' in request.args:
            action=request.args['action']
            id=request.args['id']
        else:
            action=None
        if action=='delete':
            qry="delete from employees where employee_id='%s'"%(id)
            delete(qry)
            return redirect(url_for('admin.manageemp'))
        return render_template('employees.html',data=data)
    else:
        return redirect(url_for('public.login'))
 
@admin.route('/updateemp',methods=['GET','POST'])
def updateemp():
    id=request.args['id']
    data={}
    qry="select * from employees where employee_id='%s'"%(id)
    data['manage']=select(qry)
    if 'submit' in request.form:
        fname=request.form['rfname']
        lname=request.form['rlname']
        joined_date=request.form['rjoinda']
        dob=request.form['rdob']
        gender=request.form['gender']
        house_name=request.form['rhname']
        place=request.form['rplace']
        pincode=request.form['rpin']
        phoneno=request.form['rphoneno']
        email=request.form['remail']
        username=request.form['user']
        password=request.form['pass']
        qry1="update employees set fname='%s',lname='%s',joined_date='%s',dob='%s',gender='%s',house_name='%s',place='%s',pincode='%s',phoneno='%s',email='%s',username='%s',password='%s'"
        update(qry1)
        return '''<script>alert('update successful');window.location="/manageemp"</script>'''
    return render_template('updateemp.html',data=data)


@admin.route('/assignemp',methods=['GET','POST'])
def assignemp():
    data={}
    qry1="select * from duty"
    data['duty']=select(qry1)
    qry="select * from employees"
    data['emp']=select(qry)
    if 'duty' in request.form:
        employee_id=request.form['emp']
        duty_title=request.form['title']
        duty_description=request.form['desc']
        qry="insert into duty values(null,'%s','%s','%s',curdate(),'status')"%(employee_id,duty_title,duty_description)
        insert(qry)
        return redirect(url_for('admin.assignemp'))

    return render_template('duty.html',data=data)


@admin.route('/viewattendance',methods=['GET','POST'])
def viewattendance():
    data={}
    qry="select * from employees inner join attendance using(employee_id)"
    data['viewatt']=select(qry)
    return render_template('attendance.html',data=data)


@admin.route('/manageconsumer',methods=['GET','POST'])
def manageconsumer():
    data={}
    qry="select * from consumers"
    data['user']=select(qry)

    if 'submit' in request.form:
        consumer_no=request.form['rconsno']
        first_name=request.form['rfname']
        last_name=request.form['rlname']
        house_name=request.form['rhname']
        place=request.form['rplace']
        pincode=request.form['rpin']
        connecttype=request.form['rconnect']
        depamt=request.form['rdeposit']
        phone=request.form['rphone']
        email=request.form['remail']
        username=request.form['user']
        password=request.form['pass']
        qry1="insert into login values(null,'%s','%s','consumer')"%(username,password)
        res=insert(qry1)
        qry="insert into consumers values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(res,consumer_no,first_name,last_name,house_name,place,pincode,connecttype,depamt,phone,email)
        insert(qry)
        if 'action' in request.args:
            action=request.args['action']
            id=request.args['id']
        else:
            action=None
        if action=='delete':
            qry="delete from consumers where cosumer_id='%s'"%(id)
            delete(qry)
            return redirect(url_for('admin.manageconsumer'))
    

    return render_template('consumer.html',data=data)


@admin.route('/updateconsumer',methods=['GET','POST'])

def updateconsumer():
    id=request.args['id']
    data={}
    qry="select * from consumers where consumer_id='%s'"%(id)
    data['up']=select(qry)
    if 'submit' in request.form:
        consumer_no=request.form['rconsno']
        first_name=request.form['rfname']
        last_name=request.form['rlname']
        house_name=request.form['rhname']
        place=request.form['rplace']
        pincode=request.form['rpin']
        connecttype=request.form['rconnection']
        depamt=request.form['rdeposit']
        phone=request.form['rphone']
        email=request.form['remail']
        username=request.form['user']
        password=request.form['pass']
        qry1="update consumer set consumer_no='%s',first_name='%s',last_name='%s',house_name='%s',place='%s',pincode='%s',connecttype='%s',depamt='%s',phone='%s',email='%s',username='%s',password='%s'"
        update(qry1)
        return '''<script>alert('update successful');window.location="/manageconsumer"</script>'''
    return render_template('consumer.html',data=data)

@admin.route('/viewcomplaint',methods=['GET','POST'])
def viewcomplaint():
    data={}
    qry="select * from complaints"
    data['user']=select(qry)
    return render_template('viewcomplaint.html',data=data)

@admin.route('/viewconnectionreq',methods=['GET','POST'])
def viewconnectionreq():
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
    return render_template('viewconnectionreq.html',data=data)

@admin.route('/viewmeterread',methods=['GET','POST'])
def viewmeterread():
    data={}
    qry="select * from readings"
    data['user']=select(qry)
    return render_template('/viewmeterread.html',data=data)


@admin.route('/viewleavereq',methods=['GET','POST'])
def viewleavereq():
    data={}
    qry="select * from leave_request"
    data['user']=select(qry)
    return render_template('/viewleavereq.html',data=data)

from predict import *
@admin.route('/viewbillpayment',methods=['get','post'])
def predict():
    data={}
    qry="select * from payments"
    data['user']=select(qry)
    if 'submit' in request.form:
        xxx=[]

        fan=request.form['fan']
        refr=request.form['refr']
        ac=request.form['ac']
        tv=request.form['tv']
        monitor=request.form['monitor']
        motor=request.form['motor']
        temp=request.form['temp']
        hum=request.form['humidity']
        monthly=request.form['monthly']
        tariff=request.form['tariff']


        xxx = [float(request.form[field]) for field in ['fan', 'refr', 'ac', 'tv', 'monitor', 'motor', 'temp', 'humidity', 'monthly', 'tariff']]
        print("//////////////////",xxx)
        

        
        predictions = predict_elec(xxx)
        predictionss = round(predictions, 2)

        print(predictions)
        return render_template('viewbillpayment.html',predictionss=predictionss,data=data)

        # Pass predictions to template for rendering
    return render_template('viewbillpayment.html',data=data)

             
