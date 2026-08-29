from odoo import fields, models


class RadioOrganization(models.Model):
    _name = "radio.organization"
    _description = "Radio Issuing Organization"
    _parent_name = "parent_id"
    _parent_store = True
    _order = "complete_name"

    name = fields.Char(required=True, index=True)
    code = fields.Char(
        string="Code",
        index=True,
        help="Optional short identifier, e.g. 6006.",
    )

    organization_type = fields.Selection(
        [
            ("national", "National Organization"),
            ("team", "Team / Local Unit"),
            ("regulator", "Regulator / Licensing Authority"),
            ("club", "Radio Club"),
            ("agency", "Agency / Institution"),
            ("other", "Other"),
        ],
        string="Type",
        default="team",
        required=True,
        index=True,
    )

    parent_id = fields.Many2one(
        "radio.organization",
        string="Parent Organization",
        index=True,
        ondelete="restrict",
    )

    parent_path = fields.Char(index=True)

    child_ids = fields.One2many(
        "radio.organization",
        "parent_id",
        string="Child Organizations",
    )

    complete_name = fields.Char(
        string="Organization",
        compute="_compute_complete_name",
        recursive=True,
        store=True,
        index=True,
    )

    notes = fields.Text()
    active = fields.Boolean(default=True)

    def _compute_complete_name(self):
        for record in self:
            if record.parent_id:
                record.complete_name = f"{record.parent_id.complete_name} / {record.name}"
            else:
                record.complete_name = record.name

    def name_get(self):
        return [(record.id, record.complete_name or record.name) for record in self]
