# -*- coding: utf-8 -*-

from odoo import fields, models


class Teacher(models.Model):
    _name = 'academy.teacher'

    name = fields.Char()
    biography = fields.Html()

    course_ids = fields.One2many('academy.course', inverse_name='teacher_id', string='Course')


class Course(models.Model):
    _name = 'academy.course'
    _inherit = 'mail.thread'

    name = fields.Char()
    teacher_id = fields.Many2one('academy.teacher', string='Teacher')
