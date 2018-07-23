# -*- coding: utf-8 -*-
from odoo import http


class Academy(http.Controller):
    @http.route('/academy/academy/', auth='public')
    def index(self, **kwargs):
        return http.request.render('academy.index', {
            'teachers': ['Pepito Grillo', 'Clark Kent', 'Tony Stark']
        })
