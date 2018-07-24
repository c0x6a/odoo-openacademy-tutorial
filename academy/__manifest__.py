# -*- coding: utf-8 -*-
{
    'name': 'Academy',
    'summary': """Website Module""",
    'author': 'CJ',
    'website': 'https://carlosjoel.net',
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'website'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/academy_templates.xml',
        'views/templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
