from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    radio_callsign_ids = fields.One2many(
        "radio.callsign",
        "partner_id",
        string="Radio Callsigns",
    )

    radio_callsign_count = fields.Integer(
        string="Callsign Count",
        compute="_compute_radio_callsign_count",
    )

    primary_callsign = fields.Char(
        string="Primary Callsign",
        compute="_compute_primary_callsign",
        store=True,
        index="trigram",
    )

    radio_operator = fields.Boolean(
        string="Radio Operator",
        compute="_compute_radio_operator",
        store=True,
        index=True,
    )

    radio_operator_tag_ids = fields.Many2many(
        "radio.callsign.tag",
        string="Radio Operator Tags",
        compute="_compute_radio_operator_tags",
        store=False,
    )

    @api.depends("radio_callsign_ids")
    def _compute_radio_callsign_count(self):
        for partner in self:
            partner.radio_callsign_count = len(partner.radio_callsign_ids)

    @api.depends(
        "radio_callsign_ids.callsign",
        "radio_callsign_ids.is_primary",
        "radio_callsign_ids.active",
    )
    def _compute_primary_callsign(self):
        for partner in self:
            callsigns = partner.radio_callsign_ids.filtered(lambda c: c.active)
            primary = callsigns.filtered("is_primary")[:1]
            if not primary:
                primary = callsigns[:1]
            partner.primary_callsign = primary.callsign if primary else False

    @api.depends("radio_callsign_ids", "radio_callsign_ids.active")
    def _compute_radio_operator(self):
        for partner in self:
            partner.radio_operator = bool(
                partner.radio_callsign_ids.filtered(lambda c: c.active)
            )

    def _compute_radio_operator_tags(self):
        for partner in self:
            partner.radio_operator_tag_ids = partner.radio_callsign_ids.tag_ids
