
from flask import *
from database import *

public=Blueprint('public',__name__)

@public.route('/',methods=('get','post'))
def index():
    return render_template('index.html')



@public.route('/signup',methods=('get','post'))
def signup():
    if 'submit' in request.form:
        fname=request.form['firstname']
        lname=request.form['lastname']
        hname=request.form['housename']
        pincode=request.form['pincode']
        phone=request.form['phone']
        place=request.form['place']
        email=request.form['email']
        username=request.form['username']
        password=request.form['password']
        qu="insert into login values(null,'%s','%s','user')" %(username,password)
        insert(qu)
        que="insert into users values(null,null,'%s','%s','%s','%s','%s','%s','%s','%s','%s')"  %(fname,lname,hname,pincode,phone,place,email,username,password)
        insert(que)  
        return render_template('product.html')

    return render_template('signup.html')


@public.route('/login',methods=('get','post'))
def login():
    if 'submit' in request.form:
        username=request.form['username']
        password=request.form['password']
        sel="select * from login where username = '%s' and  password = '%s' " %(username,password)
        res=select(sel)
        
        if res:
            session['login']=res[0]['login_id']
            print("my log_id",session['login'])
            
            if res[0]['user_type']=='shop':
                qw="select * from shops where login_id='%s'"%(session['login'])
                res1=select(qw)
                if res1:
                    session['shop_id']=res1[0]['shop_id']
                    print("my shop_id",session['shop_id'])


                return redirect(url_for('shop.shopindex'))
            
            if res[0]['user_type']=='admin':
                return redirect(url_for('admin.admindex'))
            



            # if res[0]['user_type']=='user':
            #     return redirect(url_for('public.userpage'))
    return render_template('login.html')

@public.route('/userhome')
def userhome():
    return render_template('userhome.html')


@public.route('/dummy')
def dummy():
    return render_template('dummy.html')