# -*- coding: utf-8 -*-

db.define_table('main_page',
                Field('paragraph_1','text',requires=IS_NOT_EMPTY()),
                Field('pic_1','upload',uploadfield='pic_file_1'),
                Field('pic_file_1','blob'),
                Field('pic_alt_1',requires=IS_NOT_EMPTY(),default='pic label'),
                Field('pic_2','upload'),
                Field('pic_file_2','blob'),
                Field('pic_alt_2',requires=IS_NOT_EMPTY(),default='fill me if pic is selected'),
                Field('paragraph_2','text'),
                Field('in_order','integer',requires=(IS_NOT_EMPTY(), IS_NOT_IN_DB(db, 'main_page.in_order'))),
                auth.signature)

db.define_table('about_us',
                Field('title'),
                Field('paragraph','text',requires=IS_NOT_EMPTY()),
                Field('image', 'upload',uploadfield='image_file'),
                Field('image_file','blob'),
                Field('is_active','boolean'),
                Field('in_order','integer',requires=(IS_NOT_EMPTY(), IS_NOT_IN_DB(db, 'about_us.in_order'))),
                auth.signature)

db.define_table('ministries',
                Field('title'),
                Field('paragraph','text',requires=IS_NOT_EMPTY()),
                Field('image', 'upload',uploadfield='image_file'),
                Field('image_file','blob'),
                Field('is_active','boolean'),
                Field('in_order','integer',requires=(IS_NOT_EMPTY(), IS_NOT_IN_DB(db, 'ministries.in_order'))),
                auth.signature)

db.define_table('staff',
                Field('name',requires=IS_NOT_EMPTY()),
                Field('job_post',requires=IS_NOT_EMPTY()),
                Field('image', 'upload',uploadfield='image_file'), #, default='static/images/cross.png'
                Field('image_file','blob'), #, default='static/images/cross.png'
                Field('is_active','boolean',default=True),
                Field('in_order','integer',requires=(IS_NOT_EMPTY(), IS_NOT_IN_DB(db, 'staff.in_order'))),
                auth.signature)

db.define_table('youth',
                Field('title'),
                Field('paragraph','text',requires=IS_NOT_EMPTY()),
                Field('image', 'upload',uploadfield='image_file'),
                Field('image_file','blob'),
                Field('is_active','boolean'),
                Field('in_order','integer',requires=(IS_NOT_EMPTY(), IS_NOT_IN_DB(db, 'youth.in_order'))),
                auth.signature)

db.define_table('rtr',
                Field('title'),
                Field('paragraph','text',requires=IS_NOT_EMPTY()),
                Field('image', 'upload',uploadfield='image_file'),
                Field('image_file','blob'),
                Field('is_active','boolean'),
                Field('in_order','integer',requires=(IS_NOT_EMPTY(), IS_NOT_IN_DB(db, 'rtr.in_order'))),
                auth.signature)

db.define_table('mp3',
                Field('name',requires=IS_NOT_EMPTY()),
                Field('pastor',requires=IS_NOT_EMPTY()),
                Field('datetime',requires=IS_NOT_EMPTY()),
                Field('mp3_file','upload'),
                Field('is_active','boolean'),
                Field('in_order','integer',requires=(IS_NOT_EMPTY(), IS_NOT_IN_DB(db, 'mp3.in_order'))),
                auth.signature)

db.define_table('link_categories',
                Field('category',requires=IS_NOT_EMPTY()),
                Field('is_active','boolean'),
                Field('in_order','integer',requires=(IS_NOT_EMPTY(), IS_NOT_IN_DB(db, 'link_categories.in_order'))),
                auth.signature)

db.define_table('links',
                Field('title',requires=IS_NOT_EMPTY()),
                Field('url',requires=IS_URL()),
                Field('pic','upload',uploadfield='pic_file'),
                Field('pic_file','blob'),
                Field('category','reference link_categories'),
                Field('is_active','boolean'),
                Field('in_order','integer',requires=(IS_NOT_EMPTY(), IS_NOT_IN_DB(db, 'links.in_order'))),
                auth.signature)

db.links.category.requires = IS_IN_DB(db,db.link_categories.id,'%(category)s')

db.define_table('contact',
                Field('title'),
                Field('paragraph','text',requires=IS_NOT_EMPTY()),
                Field('is_active','boolean'),
                Field('in_order','integer',requires=(IS_NOT_EMPTY(), IS_NOT_IN_DB(db, 'contact.in_order'))),
                auth.signature)

db.define_table('side_menu',
                Field('title'),
                Field('paragraph','text',requires=IS_NOT_EMPTY()),
                Field('is_active','boolean'),
                Field('in_order','integer',requires=(IS_NOT_EMPTY(), IS_NOT_IN_DB(db, 'side_menu.in_order'))),
                auth.signature)

db.define_table('directory',
                Field('man'),
                Field('woman'),
                Field('is_member_1','boolean'),
                Field('is_member_2','boolean'),
                Field('last_name',requires=IS_NOT_EMPTY()),
                Field('children','list:string'),
                Field('address'),
                Field('city'),
                Field('prov',requires=IS_IN_SET(('SK','MB'))),
                Field('postal_code'),
                Field('home_phone'),
                Field('cell_phone_1'),
                Field('cell_phone_2'),
                Field('mailbox_num','integer'),
                Field('is_active','boolean',default=True),
                Field('email_1',requires=IS_EMAIL()),
                Field('email_2',requires=IS_EMAIL()),
                Field('pic','upload'),
                auth.signature)
