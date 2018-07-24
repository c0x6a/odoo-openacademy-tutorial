# -*- coding: utf-8 -*-

from odoo import fields, models


class Teacher(models.Model):
    _name = 'academy.teacher'

    name = fields.Char()
