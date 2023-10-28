from flask import *
from database import *
import uuid

shop=Blueprint('shop',__name__)



@shop.route('/product',methods=('get','post'))
def product():
    data={}
    qs="select *from product_category"
    data['catview']=select(qs)
    if 'submit' in request.form:
        drop=request.form['drop']
        product_name=request.form['product_name']
        product_details=request.form['product_details']
        product_price=request.form['product_rate']
        image=request.files['img']
        path="static/image"+str(uuid.uuid4())+image.filename
        image.save(path)
        product_quantity=request.form['product_quantity']

        db="insert into products values(null,'%s','0','%s','%s','%s','%s','%s','%s')" %(drop,session['shop_id'],product_name,product_details,product_price,path,product_quantity)
        res=insert(db)

        qd="insert into stocks values(null,'%s','%s',now())" %(res,product_quantity)
        insert(qd)

    if 'action' in request.args:
        action=request.args['action']
        product_id=request.args['product_id']
    else:
        action=None
    if action=='update':
        q="select *from products where product_id='%s'" %(product_id)
        data['up']=select(q)
    if action=='delete':
        q="delete from products where product_id='%s'"%(product_id)
        delete(q)

    if 'update' in request.form:
        product_name=request.form['product_name']
        product_details=request.form['product_details']
        product_price=request.form['product_rate']
        product_image=request.files['img']
        path="static/product_image"+str(uuid.uuid4())+product_image.filename
        product_image.save(path)
        category_up=request.form['drop']
        q="update products set product_name='%s',details='%s',price='%s',product_image='%s',category_id='%s' where product_id='%s'" %(product_name,product_details,product_price,path,category_up,product_id)
        update(q)
        return redirect(url_for('shop.product'))
    va="select * from products inner join product_category on(product_category.category_id=products.category_id) where shop_id='%s' "%(session['shop_id'])     # using(c_id)  
    mvar=select(va)
    data['view']=mvar
    return render_template('product.html',data=data)


@shop.route('/shopsignup',methods=('get','post'))
def shopsignup():
    if 'submit' in request.form:
        shopname=request.form['shopname']
        shopplace=request.form['shopplace']
        shoplandmark=request.form['shoplandmark']
        shopphone=request.form['shopphone']
        shopemail=request.form['shopemail']
        shop_image=request.files['shop_image']
        path="static/shop_image"+str(uuid.uuid4())+shop_image.filename
        shop_image.save(path)
        username=request.form['username']
        password=request.form['password']
        qu="insert into login values(null,'%s','%s','shop')" %(username,password)
        log=insert(qu)
        ve="insert into shops values(null,'%s','%s','%s','%s','%s','%s','Pending','0','0','%s','%s','%s')" %(log,shopname,shopplace,shoplandmark,shopphone,shopemail,path,username,password)
        insert(ve)
        return redirect(url_for('public.login'))
        
        # sel="select * from login where username = '%s' and  password = '%s' " %(username,password)
        # res=select(sel)
        # if res:
        #     session['login']=res[0]['login_id']
        #     print("my log_id",session['login'])
            
        #     if res[0]['user_type']=='shop':
        #         qw="select * from shops where login_id='%s'"%(session['login'])
        #         res1=select(qw)
        #         if res1:
        #             session['shop_id']=res1[0]['shop_id']
        #             print("my shop_id",session['shop_id'])
        




        
    return render_template('shopsignup.html')

@shop.route('/shopindex',methods=('get','post'))
def shopindex():
    return render_template('shopindex.html')


@shop.route('/shopviewstock')
def viewstock():
    data={}
    v="select *from products inner join stocks using(product_id) where shop_id= '%s'" %(session['shop_id'])
    data['view']=select(v)
    return render_template('shopviewstock.html',data=data)


@shop.route('/shopaddstock',methods=('get','post'))
def shopaddstock():
    data={}
    a="select *from stocks"
    data['view']=select(a)
    if 'submit' in request.form:
        product_id=request.args['product_id']
        quantity=request.form['stock_quantity']
        q="update stocks set quantity = '%s' where product_id='%s' " %(quantity,product_id)
        update(q)
    return render_template('shopaddstock.html',data=data)