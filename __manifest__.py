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
{
    "name": "Radio Operators",
    "version": "18.0.2.0.0",
    "license": "AGPL-3",
    "summary": "Track radio operator callsigns on contacts",
    "description": """
Radio Operators
===============

Adds radio operator callsign tracking to Odoo contacts.

Features:
- Multiple callsigns per contact
- Callsign type (REACT, Amateur/Ham, GMRS, CB, Other)
- Issuing authority / organization
- Issue and expiry dates
- Non-expiring callsigns
- Active/expired status
- Callsign tags
- Primary callsign displayed and searchable on contacts
""",
    "author": "REACT Team 6006",
    "category": "Contacts",
    "license": "AGPL-3",
    "depends": ["contacts"],
    "data": [
        "security/ir.model.access.csv",
        "data/radio_organization_data.xml",
        "views/radio_operator_views.xml",
        "views/res_partner_views.xml",
        "data/radio_operator_tag_data.xml",
    ],
    "installable": True,
    "application": False,
}
