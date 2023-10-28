from flask import *
from database import *


admin=Blueprint('admin',__name__)

@admin.route('/category',methods=['get','post'])
def category():
    data={}
    if 'submit' in request.form:
        c_name=request.form['category_name']
        dt="insert into product_category values(null,'%s')" %(c_name)
        insert(dt)
    if 'action' in request.args:
        action=request.args['action']
        category_id=request.args['category_id']
    else:
        action=None 
    if action=='update':
        q="select* from product_category where category_id='%s'"%(category_id)
        data['up']=select(q)
    if 'update' in request.form:
         c_name=request.form['category_name']
         q="update product_category set category_name='%s' where category_id='%s'"%(c_name,category_id)
         update(q)
         return redirect(url_for('admin.category'))
    if action=='delete':
        q="delete from product_category where category_id='%s' "%(category_id)
        delete(q)
    a1="select *from product_category"
    a2=select(a1)
    data['catview']=a2
    return render_template('category.html',data=data)



@admin.route('/adminindex')
def admindex():
    return render_template('admindex.html')

@admin.route('/adminviewallproduct',methods=('get','post'))
def adminviewallproduct():
    data={}
    a="select *from product_category inner join products using (category_id)" 
    data['view']=select(a)
    return render_template('adminviewallproduct.html',data=data)



@admin.route('/adminviewproduct',methods=('get','post'))
def adminviewproductadm():
    data={}    
    if 'sid' in request.args:
        sid=request.args['sid']
    va="select * from product_category inner join products using (category_id) inner join shops using(shop_id) where shop_id='%s'"%(sid)
    data['view']=select(va)
    
    return render_template('adminviewproduct.html',data=data)

@admin.route('/adminviewshop',methods=('get','post'))
def viewshop():
    data={}
    v="select *from shops"
    data['view']=select(v)

    return render_template('adminviewshop.html',data=data)


@admin.route('/viewcustomer',methods=('get','post'))
def viewcustomer():
    data={}
    ve="select *from users"
    data['view']=select(ve)
    return render_template('viewcustomer.html',data=data)

@admin.route('/adminviewstock',methods=('get','post'))
def adminviewstock():
    data={}
    v="select *from products inner join stocks using(product_id)"                   
    data['view']=select(v)
    return render_template('adminviewstock.html',data=data)


@admin.route('/adminviewcomplaints')
def adminviewcomplaints():
    data={}
    v="select *from complaints inner join users using (user_id)"
    data['comp']=select(v)
   
    return render_template('adminviewcomplaints.html',data=data)