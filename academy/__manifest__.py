# -*- coding: utf-8 -*-
{
    'name': 'Academy',
    'summary': """Website Module""",
    'author': 'CJ',
    'website': 'https://carlosjoel.net',
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'website', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/academy_templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
