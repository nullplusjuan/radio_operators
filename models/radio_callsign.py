# Copyright 2026 Joshua D
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# SPDX-License-Identifier: AGPL-3.0-or-later
from odoo import api, fields, models


class RadioCallsign(models.Model):
    _name = "radio.callsign"
    _description = "Radio Operator Callsign"
    _rec_name = "callsign"
    _order = "active desc, callsign"

    callsign = fields.Char(
        string="Callsign",
        required=True,
        index="trigram",
        help="The operator's assigned radio callsign, e.g. R615, 9Z4ABC, W1ABC.",
    )

    partner_id = fields.Many2one(
        "res.partner",
        string="Operator",
        required=True,
        ondelete="cascade",
        index=True,
    )

    callsign_type = fields.Selection(
        [
            ("react", "REACT"),
            ("amateur", "Amateur / Ham"),
            ("gmrs", "GMRS"),
            ("cb", "CB"),
            ("commercial", "Commercial / Business"),
            ("marine", "Marine"),
            ("aviation", "Aviation"),
            ("other", "Other"),
        ],
        string="Type",
        required=True,
        default="react",
        index=True,
    )

    issuing_organization_id = fields.Many2one(
        "radio.organization",
        string="Issued By",
        index=True,
        ondelete="restrict",
        help="Organization, team, regulator, or other authority that issued this callsign.",
    )

    issue_date = fields.Date(string="Issue Date")

    expires = fields.Boolean(
        string="Expires",
        default=False,
        help="Enable if the callsign/license has an expiry date.",
    )

    expiry_date = fields.Date(
        string="Expiry Date",
        help="Leave empty for callsigns that do not expire.",
    )

    status = fields.Selection(
        [
            ("active", "Active"),
            ("expired", "Expired"),
            ("inactive", "Inactive"),
        ],
        compute="_compute_status",
        store=True,
        index=True,
    )

    is_primary = fields.Boolean(
        string="Primary Callsign",
        help="Marks this as the operator's main callsign.",
    )

    tag_ids = fields.Many2many(
        "radio.callsign.tag",
        "radio_callsign_tag_rel",
        "callsign_id",
        "tag_id",
        string="Tags",
    )

    notes = fields.Text()
    active = fields.Boolean(default=True)

    @api.depends("active", "expires", "expiry_date")
    def _compute_status(self):
        today = fields.Date.context_today(self)
        for record in self:
            if not record.active:
                record.status = "inactive"
            elif record.expires and record.expiry_date and record.expiry_date < today:
                record.status = "expired"
            else:
                record.status = "active"

    @api.onchange("expires")
    def _onchange_expires(self):
        if not self.expires:
            self.expiry_date = False

    @api.onchange("is_primary")
    def _onchange_is_primary(self):
        if self.is_primary and self.partner_id:
            for callsign in self.partner_id.radio_callsign_ids:
                if callsign != self:
                    callsign.is_primary = False

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        for record in records.filtered("is_primary"):
            others = self.search([
                ("partner_id", "=", record.partner_id.id),
                ("id", "!=", record.id),
                ("is_primary", "=", True),
            ])
            others.write({"is_primary": False})
        return records

    def write(self, vals):
        result = super().write(vals)
        if vals.get("is_primary"):
            for record in self:
                others = self.search([
                    ("partner_id", "=", record.partner_id.id),
                    ("id", "!=", record.id),
                    ("is_primary", "=", True),
                ])
                others.write({"is_primary": False})
        return result
