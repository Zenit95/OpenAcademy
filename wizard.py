# -*- coding: utf8 -*-

from openerp import models, fields, api

class Wizard(models.TransientModel):
    _name = 'openacademy.wizard'
    
    def _default_sessions(self):
        return self.env['openacademy.session'].browse(self._context.get('active_id'))
    
    session_id = fields.Many2one('openacademy.session',
        string="Session", required=True, default=_default_sessions)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")
    
    @api.multi
    def subscribe(self):
        for session in self.session_ids:
            session.attendee_ids |= self.attendee_ids
        return {}
    