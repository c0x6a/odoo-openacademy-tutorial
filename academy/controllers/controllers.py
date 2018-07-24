# -*- coding: utf-8 -*-
from odoo import http


class Academy(http.Controller):
    @http.route('/academy/academy/', auth='public', website=True)
    def index(self, **kwargs):
        teachers = http.request.env['academy.teacher']
        return http.request.render('academy.index', {
            'teachers': teachers.search([])
        })
