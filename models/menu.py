# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

# response.logo = A(B('web',SPAN(2),'py'),XML('&trade;&nbsp;'),
                  # _class="brand",_href="http://www.web2py.com/")
# response.title = ' '.join(
    # word.capitalize() for word in request.application.split('_'))
# response.subtitle = T('customize me!')

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Wayne Stickwood <you@example.com>'
response.meta.description = 'a cool new Heritage App'
response.meta.keywords = 'web2py, python, framework'
response.meta.generator = 'Web2py Web Framework'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################
if request.controller == 'manage':
    response.menu = [
        (T('Home'), False, URL('manage','index'), [])
    ]
    rows = db(db.auth_user.registration_key!='').select()
    if rows:
        if auth.has_membership('secretary'):
            response.menu += [
                (T('New Users'), False, URL('manage','new_user'), [])
            ]
    if auth.has_membership('master'):
        response.menu += [
            (T('Users'), False, URL('manage','edit',args='auth_user'), []),
            (T('Groups'), False, URL('manage','edit',args='auth_group'), []),
            (T('Memberships'), False, URL('manage','edit',args='auth_membership'), []),
            (T('Permissions'), False, URL('manage','edit',args='auth_permission'), []),
            (T('Events'), False, URL('manage','edit',args='auth_event'), []),
            (T('CAS'), False, URL('manage','edit',args='auth_CAS'), []),
            (T(''), False, A(T('Admin'), _href="/admin/default/index.html",_target='_blank'), []) #URL('admin','default','index'), [])
        ]
    elif auth.has_membership('secretary'):
        response.menu += [
            (T('Users'), False, URL('manage','edit',args='auth_user'), []),
            (T('Events'), False, URL('manage','edit',args='auth_event'), [])
            ]
    response.menu += [
        (T('Log Out'), False, URL('manage','logout'), [
            (T('Profile'), False, URL('manage','profile'), []),
            (T('Password'), False, URL('manage','change_password'), [])
        ])
    ]
else:
    response.menu = [
        (T('Home'), False, URL('default','index'), []),
        (T('About Us'), False, URL('default','about'), []),
        (T('Find Us'), False, URL('default','map'), []),
        (T('Calendar'), False, URL('default','calendar'), []),
        (T('Ministries'), False, URL('default','ministries'), []),
        (T('Staff'), False, URL('default','staff'), []),
        (T('Youth'), False, URL('default','youth'), [
            (T('RTR'), False, URL('default','rtr'), [])
        ]),
        (T('Useful Links'), False, URL('default','links'), []),
        (T('Contact Us'), False, URL('default','contact'), [])
    ]
    if auth.is_logged_in():
        response.menu += [
            (T('Media'), False, URL('default','media'), []),
            (T('Directory'), False, URL('default','directory'), [])
        ]
    if auth.has_membership('secretary'):
        response.menu += [
            (T(''), False, A(T('Manage Site'), _href="/manage/index.html",_target='_blank'), [])
        ]
    if auth.is_logged_in():
        response.menu += [
            (T('Logout'), False, URL('default','logout'), [
                (T('profile'), False, URL('default','profile'), []),
                (T('Password'), False, URL('default','change_password'), [])
            ])
        ]
    else:
        response.menu += [
            (T('Login'), False, URL('default','login'), [
                (T('Register'), False, URL('default','register'), [])
            ])
            #(T('Forgot Username'), False, URL('default','retrieve_username'), []),
            #(T('Forgot Password'), False, URL('default','request_reset_password'), [])
        ]

    #auth.navbar(mode="dropdown",referrer_actions=None)
    #'auth' in globals() and
DEVELOPMENT_MENU = True

#########################################################################
## provide shortcuts for development. remove in production
#########################################################################

# def _():
    #shortcuts
    # app = request.application
    # ctr = request.controller
    #useful links to internal and external resources
    # response.menu += [
        # (SPAN('web2py', _class='highlighted'), False, 'http://web2py.com', [
        # (T('My Sites'), False, URL('admin', 'default', 'site')),
        # (T('This App'), False, URL('admin', 'default', 'design/%s' % app), [
        # (T('Controller'), False,
         # URL(
         # 'admin', 'default', 'edit/%s/controllers/%s.py' % (app, ctr))),
        # (T('View'), False,
         # URL(
         # 'admin', 'default', 'edit/%s/views/%s' % (app, response.view))),
        # (T('Layout'), False,
         # URL(
         # 'admin', 'default', 'edit/%s/views/layout.html' % app)),
        # (T('Stylesheet'), False,
         # URL(
         # 'admin', 'default', 'edit/%s/static/css/web2py.css' % app)),
        # (T('DB Model'), False,
         # URL(
         # 'admin', 'default', 'edit/%s/models/db.py' % app)),
        # (T('Menu Model'), False,
         # URL(
         # 'admin', 'default', 'edit/%s/models/menu.py' % app)),
        # (T('Database'), False, URL(app, 'appadmin', 'index')),
        # (T('Errors'), False, URL(
         # 'admin', 'default', 'errors/' + app)),
        # (T('About'), False, URL(
         # 'admin', 'default', 'about/' + app)),
        # ]),
            # ('web2py.com', False, 'http://www.web2py.com', [
             # (T('Download'), False,
              # 'http://www.web2py.com/examples/default/download'),
             # (T('Support'), False,
              # 'http://www.web2py.com/examples/default/support'),
             # (T('Demo'), False, 'http://web2py.com/demo_admin'),
             # (T('Quick Examples'), False,
              # 'http://web2py.com/examples/default/examples'),
             # (T('FAQ'), False, 'http://web2py.com/AlterEgo'),
             # (T('Videos'), False,
              # 'http://www.web2py.com/examples/default/videos/'),
             # (T('Free Applications'),
              # False, 'http://web2py.com/appliances'),
             # (T('Plugins'), False, 'http://web2py.com/plugins'),
             # (T('Layouts'), False, 'http://web2py.com/layouts'),
             # (T('Recipes'), False, 'http://web2pyslices.com/'),
             # (T('Semantic'), False, 'http://web2py.com/semantic'),
             # ]),
            # (T('Documentation'), False, 'http://www.web2py.com/book', [
             # (T('Preface'), False,
              # 'http://www.web2py.com/book/default/chapter/00'),
             # (T('Introduction'), False,
              # 'http://www.web2py.com/book/default/chapter/01'),
             # (T('Python'), False,
              # 'http://www.web2py.com/book/default/chapter/02'),
             # (T('Overview'), False,
              # 'http://www.web2py.com/book/default/chapter/03'),
             # (T('The Core'), False,
              # 'http://www.web2py.com/book/default/chapter/04'),
             # (T('The Views'), False,
              # 'http://www.web2py.com/book/default/chapter/05'),
             # (T('Database'), False,
              # 'http://www.web2py.com/book/default/chapter/06'),
             # (T('Forms and Validators'), False,
              # 'http://www.web2py.com/book/default/chapter/07'),
             # (T('Email and SMS'), False,
              # 'http://www.web2py.com/book/default/chapter/08'),
             # (T('Access Control'), False,
              # 'http://www.web2py.com/book/default/chapter/09'),
             # (T('Services'), False,
              # 'http://www.web2py.com/book/default/chapter/10'),
             # (T('Ajax Recipes'), False,
              # 'http://www.web2py.com/book/default/chapter/11'),
             # (T('Components and Plugins'), False,
              # 'http://www.web2py.com/book/default/chapter/12'),
             # (T('Deployment Recipes'), False,
              # 'http://www.web2py.com/book/default/chapter/13'),
             # (T('Other Recipes'), False,
              # 'http://www.web2py.com/book/default/chapter/14'),
             # (T('Buy this book'), False,
              # 'http://stores.lulu.com/web2py'),
             # ]),
            # (T('Community'), False, None, [
             # (T('Groups'), False,
              # 'http://www.web2py.com/examples/default/usergroups'),
                        # (T('Twitter'), False, 'http://twitter.com/web2py'),
                        # (T('Live Chat'), False,
                         # 'http://webchat.freenode.net/?channels=web2py'),
                        # ]),
                # (T('Plugins'), False, None, [
                        # ('plugin_wiki', False,
                         # 'http://web2py.com/examples/default/download'),
                        # (T('Other Plugins'), False,
                         # 'http://web2py.com/plugins'),
                        # (T('Layout Plugins'),
                         # False, 'http://web2py.com/layouts'),
                        # ])
                # ]
         # )]
# if DEVELOPMENT_MENU: _()
