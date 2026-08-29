from odoo import fields, models


class RadioCallsignTag(models.Model):
    _name = "radio.callsign.tag"
    _description = "Radio Callsign Tag"
    _order = "name"

    name = fields.Char(required=True, index=True)
    color = fields.Integer()
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ("name_unique", "unique(name)", "A callsign tag with this name already exists."),
    ]
