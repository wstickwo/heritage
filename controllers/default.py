# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations


def index():
    main = db().select(orderby=db.main_page.in_order).first()
    side = db(db.side_menu.is_active==True).select(orderby=db.side_menu.in_order)
    return locals()


def about():
    abouts = db(db.about_us.is_active==True).select(orderby=db.about_us.in_order)
    side = db(db.side_menu.is_active==True).select(orderby=db.side_menu.in_order)
    return locals()


def map():
    side = db(db.side_menu.is_active==True).select(orderby=db.side_menu.in_order)
    return locals()


def calendar():
    side = db(db.side_menu.is_active==True).select(orderby=db.side_menu.in_order)
    return locals()


def ministries():
    ministries = db(db.ministries.is_active==True).select(orderby=db.ministries.in_order)
    side = db(db.side_menu.is_active==True).select(orderby=db.side_menu.in_order)
    return locals()


def staff():
    staff = db(db.staff.is_active==True).select(orderby=db.staff.in_order)
    side = db(db.side_menu.is_active==True).select(orderby=db.side_menu.in_order)
    return locals()


def youth():
    youths = db(db.youth.is_active==True).select(orderby=db.youth.in_order)
    side = db(db.side_menu.is_active==True).select(orderby=db.side_menu.in_order)
    return locals()


def media():
    side = db(db.side_menu.is_active==True).select(orderby=db.side_menu.in_order)
    return locals()


def links():
    categories = db().select(db.link_categories.ALL,orderby=db.link_categories.id)
    links = db(db.links.is_active==True).select(orderby=db.links.in_order)
    side = db(db.side_menu.is_active==True).select(orderby=db.side_menu.in_order)
    return locals()


def contact():
    contacts = db(db.contact.is_active==True).select(orderby=db.contact.in_order)
    side = db(db.side_menu.is_active==True).select(orderby=db.side_menu.in_order)
    return locals()


def rtr():
    rtrs = db(db.rtr.is_active==True).select(orderby=db.rtr.in_order)
    side = db(db.side_menu.is_active==True).select(orderby=db.side_menu.in_order)
    return locals()


def directory():
    side = db(db.side_menu.is_active==True).select(orderby=db.side_menu.in_order)
    grid = SQLFORM.grid(db.directory,editable=False,create=False,deletable=False,csv=False,paginate=10,orderby=db.directory.last_name)
    grid.element('.web2py_grid')['_id'] = 'root' #giving an id to the grid container for personal purposes
    grid.element('.web2py_grid')['_class'] = 'row'  #giving a class name to the grid container for personal purposes
    #grid.element('.web2py_counter')[0] = '' #i dont want the 'X results found' message
    grid[0].element('.web2py_console')['_class'] = '' #full width search input
    grid[0][1][0][1] = '' #remove search button
    #grid[0][1][0][2] = '' #remove clear button
    grid[0][1][0][0]['_onfocus'] = None #remove event from input
    grid[0][1][0][0]['_placeholder'] = T('Search Directory...')
    grid[0][1][1] = ''
    table_div = grid.element('.web2py_table')
    table_div[0] = ''
    table_div['_class'] = 'row'
    for row in grid.rows:
        if row.man and row.woman:
            name = row.man.capitalize()
            if row.is_member_1:
                name += '* '
            name += 'and ' + row.woman.capitalize()
            if row.is_member_2:
                name += '* '
            name += row.last_name.capitalize()
        elif row.man:
            name = row.man.capitalize() + ' ' + row.last_name.capitalize()
            if row.is_member_1:
                name += '*'
        else:
            name = row.woman.capitalize() + ' ' + row.last_name.capitalize()
            if row.is_member_2:
                name += '*'
        if row.mailbox_num:
                name += ' ' + str(row.mailbox_num)
        children = ''
        if row.children:
            clist = []
            for each in row.children:
                clist.append(each.capitalize())
            children = ', '.join(clist)
        address = ''
        if row.address:
            address = row.address
        city = ''
        if row.city:
            city = row.city
        prov = ''
        if row.prov:
            prov = row.prov
        postal_code = ''
        if row.postal_code:
            postal_code = row.postal_code
        home_phone = ''
        if row.home_phone:
            home_phone = row.home_phone
        table_div.insert(-1,
            TR(
                TR(
                    TD(name)
                ),
                TR(
                    TD(children)
                ),
                TR(
                    TD(address)
                ),
                TR(
                    TD(city + ', ' + prov)
                ),
                TR(
                    TD(postal_code)
                ),
                BR()
            )
        )
    return dict(grid=grid,side=side)


def test():
    youths = db(db.youth.is_active==True).select(orderby=db.youth.in_order)
    side = db(db.side_menu.is_active==True).select(orderby=db.side_menu.in_order)
    return locals()


def login():
    response.view = 'auth.html'
    side = db(db.side_menu.is_active==True).select(orderby=db.side_menu.in_order)
    return dict(form=auth.login(),side=side)


def register():
    response.view = 'auth.html'
    side = db(db.side_menu.is_active==True).select(orderby=db.side_menu.in_order)
    return dict(form=auth.register(),side=side)


def retrieve_username():
    response.view = 'auth.html'
    side = db(db.side_menu.is_active==True).select(orderby=db.side_menu.in_order)
    return dict(form=auth.retrieve_username(),side=side)


def request_reset_password():
    response.view = 'auth.html'
    side = db(db.side_menu.is_active==True).select(orderby=db.side_menu.in_order)
    return dict(form=auth.request_reset_password(),side=side)


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
    side = db(db.side_menu.is_active==True).select(orderby=db.side_menu.in_order)
    return dict(form=auth(),side=side)


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_login()
def api():
    """
    this is example of API with access control
    WEB2PY provides Hypermedia API (Collection+JSON) Experimental
    """
    from gluon.contrib.hypermedia import Collection
    rules = {
        '<tablename>': {'GET':{},'POST':{},'PUT':{},'DELETE':{}},
        }
    return Collection(db).process(request,response,rules)
