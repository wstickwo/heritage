# -*- coding: utf-8 -*-

import os
import socket
import datetime
import copy
import gluon.contenttype
import gluon.fileutils

response.view = 'manage.html'

@auth.requires(lambda: auth.has_membership('master') or auth.has_membership('secretary'))
def index():
    tables = db.tables
    side = db(db.side_menu.is_active==True).select(orderby=db.side_menu.in_order)
    return locals()

#testing 1 2 3, testing again....
@auth.requires(lambda: auth.has_membership('master') or auth.has_membership('secretary'))
def edit():
    fields=[]
    table = request.args(0)
    if request.args(1) != "":
        id = request.args(1)
    if not table in db.tables():
        session.flash = 'no table found'
        redirect(URL('index'))
    for f in db[table].fields:
        fields.append(f)
    if table[0:4] != 'auth':
        if db[table].fields[-5] == 'in_order':
            orderby=db[table].in_order
        else:
            orderby=db[table].id
    elif table == 'auth_membership':
        orderby=db[table].user_id
    elif table == 'directory':
        orderby=db[table].last_name
    else:
        orderby=db[table].id
    rows = db(db[table]).select(orderby=orderby)
    count = db(db[table]).count()
    side = db(db.side_menu.is_active==True).select(orderby=db.side_menu.in_order)
    if table == 'auth_user':
        rows = db(db.auth_user.registration_key=='').select(orderby=orderby)
        count = db(db.auth_user.registration_key=='').count()
    return locals()


@auth.requires(lambda: auth.has_membership('master') or auth.has_membership('secretary'))
def update():
    table = request.args(0)
    id = request.args(1)
    min = db[table].id.min()   # this is to grab the record with the lowest id
    lowest = db(db[table]).select(min)
    if table == 'auth_user':
		table2 = db(db.auth_membership.user_id==id).select(orderby=db.auth_membership.group_id)
    else:
        table2 = False
    now = request.now
    record = db(db[table].id == id).select()
    if table[0:4] != 'auth':
        db[table].modified_on.default = now
        db[table].modified_by.default = auth.user_id
    if table == 'main_page' and id == str(lowest[0][min]):
        deletable = False
    elif db(db[table]).count() > 1:
        deletable = True
    else:
        deletable = False
    form = SQLFORM(db[table],id,deletable=deletable,
                   showid=False,upload=URL('download')).process()
    if form.deleted:
       	db.auth_event.insert(time_stamp=now,client_ip='127.0.0.1',user_id=auth.user_id,origin='auth',description=table.capitalize() + ' ID ' + id + ' Deleted')
        session.flash = 'record deleted'
        if table == 'auth_user':
            rows = db(db.auth_membership.user_id==id).select()
            for row in rows:
                row.delete()
        redirect(URL('edit',args=table))

    elif form.accepted:
        db.auth_event.insert(time_stamp=now,client_ip='127.0.0.1',user_id=auth.user_id,origin='auth',description=table.capitalize() + ' ID ' + id + ' Edited')
        session.flash = 'record updated'
        redirect(URL('edit',args=table))
    side = db(db.side_menu.is_active==True).select(orderby=db.side_menu.in_order)
    return locals()


@auth.requires(lambda: auth.has_membership('master') or auth.has_membership('secretary'))
def membership_update():
    table = request.args(0)
    id = request.args(1)
    user = request.args(2)
    db[table].user_id.writable = False
    record = db(db[table].id == id).select()
    now = request.now
    if table[0:4] != 'auth':
        db[table].modified_on.default = now
        db[table].modified_by.default = auth.user_id
    if db(db[table]).count() > 1:
        deletable = True
    else:
        deletable = False
    form = SQLFORM(db[table],id,deletable=deletable,
                   showid=False,upload=URL('download')).process()
    if form.deleted:
       	db.auth_event.insert(time_stamp=now,client_ip='127.0.0.1',user_id=auth.user_id,origin='auth',description=table.capitalize() + ' ID ' + id + ' Deleted')
        session.flash = 'record deleted'
        redirect(URL('update',args=('auth_user',user)))

    elif form.accepted:
        db.auth_event.insert(time_stamp=now,client_ip='127.0.0.1',user_id=auth.user_id,origin='auth',description=table.capitalize() + ' ID ' + id + ' Edited')
        session.flash = 'record updated'
        redirect(URL('update',args=('auth_user',user)))
    side = db(db.side_menu.is_active==True).select(orderby=db.side_menu.in_order)
    return locals()


@auth.requires(lambda: auth.has_membership('master') or auth.has_membership('secretary'))
def new():
    table = request.args(0)
    if request.args(1):
        g = []
        id = request.args(1)
        db[table].user_id.default = id
        db[table].user_id.writable = False
        group = db(db.auth_group.id!=2).select(db.auth_group.id)
        for row in group:
            g.append(str(row.id))
        #db.auth_membership.group_id.default = IS_IN_SET(g)
    now = request.now
    if table[0:4] != 'auth':
        db[table].created_on.default = now
        db[table].modified_on.default = now
        db[table].created_by.default = auth.user_id
        db[table].modified_by.default = auth.user_id
    if request.args(1):
                    form = SQLFORM.factory(Field('user_id',requires=IS_IN_DB(db,'auth_user.id','%(username)s'),default=id,writable=False),
                                Field('group_id',requires=IS_IN_DB(db(db.auth_group.id!=2),'auth_group.id','%(role)s')),
                                submit_button='Add New Membership')
                #form.vars.user_id = db(db.auth_user.id==id).select(db.auth_user.username)
                    form.process()
    else:
        form = SQLFORM(db[table],showid=False,submit_button='Add New Record').process()
    #form.vars.group_id = IS_IN_SET(g)
    if form.accepted:
        id1 = str(form.vars.id)
        if table == 'auth_user':
            db.auth_membership.insert(user_id=id1,group_id=3)
        db.auth_event.insert(time_stamp=now,client_ip='127.0.0.1',user_id=auth.user_id,origin='auth',description=table.capitalize() + ' ID ' + id1 + ' Added')
        session.flash = 'Record in ' + table.capitalize() + ' Created.'
        if table == 'auth_membership':
            redirect(URL('update',args=('auth_user',id)))
        else:
            redirect(URL('edit',args=table))
    side = db(db.side_menu.is_active==True).select(orderby=db.side_menu.in_order)
    return locals()


@auth.requires(lambda: auth.has_membership('master') or auth.has_membership('secretary'))
def new_user():
    rows = db(db.auth_user.registration_key!='').select()
    now = request.now
    side = db(db.side_menu.is_active==True).select(orderby=db.side_menu.in_order)
    return locals()


@auth.requires(lambda: auth.has_membership('master') or auth.has_membership('secretary'))
def accept_new_user():
    now = request.now
    id = request.args(0)
    user = db(db.auth_user.id==id).select().first()
    user.update_record(registration_key='')
    db.auth_membership.insert(user_id=id,group_id=3)
    redirect(URL('edit',args='auth_user'))
    #side = db(db.side_menu.is_active==True).select(orderby=db.side_menu.in_order)
    return locals()


@auth.requires(lambda: auth.has_membership('master') or auth.has_membership('secretary'))
def delete_new_user():
    #now = request.now
    id = request.args(0)
    db(db.auth_user.id==id).delete()
    redirect(URL('edit',args='auth_user'))
    #side = db(db.side_menu.is_active==True).select(orderby=db.side_menu.in_order)
    return locals()


@auth.requires(lambda: auth.has_membership('master') or auth.has_membership('secretary'))
def view():
    table = request.args(0)
    id = request.args(1)
    form = SQLFORM(db[table],id,showid=False,readonly=True)
    side = db(db.side_menu.is_active==True).select(orderby=db.side_menu.in_order)
    return locals()


@auth.requires(lambda: auth.has_membership('master') or auth.has_membership('secretary'))
def delete():
    table = request.args(0)
    string_list = request.args(1)
    sub = ''
    delete_list = []
    for each in string_list:
        if each == "_":
            delete_list.append(sub)
            sub = ''
        else:
            sub += each
    delete_list.append(sub)
    for id in delete_list:
        db(db[table].id == id).delete()
    redirect(URL('edit',args=(table)),client_side=True)
    side = db(db.side_menu.is_active==True).select(orderby=db.side_menu.in_order)
    return locals()


@auth.requires_login()
def logout():
    response.view = 'auth.html'
    side = db(db.side_menu.is_active==True).select(orderby=db.side_menu.in_order)
    return dict(form=auth.logout(),side=side)


@auth.requires_login()
def profile():
    response.view = 'auth.html'
    side = db(db.side_menu.is_active==True).select(orderby=db.side_menu.in_order)
    return dict(form=auth.profile(),side=side)


@auth.requires_login()
def change_password():
    response.view = 'auth.html'
    side = db(db.side_menu.is_active==True).select(orderby=db.side_menu.in_order)
    return dict(form=auth.change_password(),side=side)


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())

@cache.action()
def download():
    return response.download(request, db)
