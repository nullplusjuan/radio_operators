{
    "name": "Radio Operators",
    "version": "18.0.2.0.0",
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
    "license": "LGPL-3",
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
