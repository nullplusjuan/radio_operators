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
