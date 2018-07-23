# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Teacher(models.Model):
    _name = 'academy.teacher'

    name = fields.Char()
