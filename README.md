# Radio Operators

Radio Operators is an Odoo 18 module for recording and managing radio callsigns associated with contacts.

The module was originally developed for use by REACT and similar volunteer radio and emergency communications organizations, but is designed to support multiple types of radio operators and issuing organizations.

## Features

Radio Operators extends Odoo Contacts (`res.partner`) with support for multiple radio callsigns per person.

Each callsign can record:

* Callsign
* Operator
* Callsign type
* Issuing organization
* Issue date
* Expiry date
* Whether the callsign expires
* Active, expired, or inactive status
* Primary callsign
* Tags
* Notes

Supported callsign categories include:

* REACT
* Amateur / Ham Radio
* GMRS
* CB
* Commercial / Business Radio
* Marine
* Aviation
* Other radio services

## Issuing Organizations

Issuing authorities are represented using the `radio.organization` model rather than plain text.

Organizations may be arranged hierarchically.

For example:

```
REACT Trinidad & Tobago
├── Team 6006
├── Team XXXX
└── Team YYYY
```

A callsign may therefore be associated directly with the organization or team which issued it.

Example:

```
Callsign: R615
Type: REACT
Issued By: REACT Trinidad & Tobago / Team 6006
Status: Active
```

This structure allows callsigns to be searched, filtered, and grouped by issuing organization.

It can also represent organizations outside REACT, including regulators, licensing authorities, amateur radio clubs, agencies, and other institutions.

## Contact Integration

Radio operators remain normal Odoo contacts.

The module extends `res.partner` rather than creating a separate person database.

Contacts gain:

* A Radio Callsigns tab
* Primary Callsign
* Radio Operator status
* Callsign count
* Callsign search support

A single person may have multiple callsigns.

For example:

```
Operator
├── R615       REACT
├── 9Z4XXX     Amateur Radio
└── XXXXX      Other Service
```

This avoids assuming that one person can only belong to one radio service.

## Callsign Tags

Callsigns may also be classified using tags.

Initial tags include:

* REACT
* Amateur Radio
* GMRS
* Emergency Communications

Additional tags can be created as required.

## Installation

Copy the `radio_operators` directory into an Odoo addons directory.

For example:

```
/opt/odoo/custom-addons/radio_operators
```

Ensure the custom addons directory is included in Odoo's `addons_path`.

Restart Odoo and update the Apps list.

The module can then be installed from:

```
Apps → Radio Operators
```

Alternatively, it can be installed or upgraded from the command line:

```
odoo -d DATABASE_NAME -i radio_operators --stop-after-init
```

To upgrade an existing installation:

```
odoo -d DATABASE_NAME -u radio_operators --stop-after-init
```

Use the appropriate Odoo configuration file and executable path for your installation.

## Odoo Version

This branch targets:

```
Odoo 18
```

Module version:

```
18.0.2.0.0
```

Compatibility with other Odoo versions is not guaranteed.

## Intended Use

The module is suitable for organizations that need a simple registry of radio operators and callsigns, including:

* REACT teams
* Amateur radio clubs
* Emergency communications groups
* Volunteer organizations
* Community communications groups
* Search-and-rescue organizations
* Radio clubs
* Communications teams

The module is intentionally kept relatively small.

It is not intended to replace a complete membership-management, licensing, incident-management, or emergency-communications system.

Those functions should be implemented separately where appropriate rather than allowing this module to become an unmaintainable collection of unrelated features.

## Data Model

The primary models introduced by the module are:

```
radio.callsign
radio.callsign.tag
radio.organization
```

The module also extends:

```
res.partner
```

Relationships are used wherever practical instead of duplicating organization names and operator information as free text.

## Contributing

Contributions, bug fixes, documentation improvements, and useful extensions are welcome.

Changes should preserve the basic design philosophy of the module:

1. Keep radio operators attached to normal Odoo contacts.
2. Allow one operator to possess multiple callsigns.
3. Preserve historical callsign information where useful.
4. Represent issuing organizations relationally.
5. Avoid unnecessary complexity.
6. Prefer maintainable Odoo-native solutions.
7. Do not turn the module into a complete emergency-management platform.

When adding features intended for emergency or volunteer organizations, reliability and maintainability should take priority over novelty.

## License

Copyright © 2026 Joshua D

Radio Operators is free software licensed under the GNU Affero General Public License, version 3 or, at your option, any later version.

You may use, study, modify, and redistribute this software under the terms of that license.

Because this software is distributed under the GNU AGPL, modified versions remain subject to the license's copyleft requirements, including the provisions applicable when modified software is used to provide functionality over a network.

See the `LICENSE` file for the complete license terms.

SPDX-License-Identifier: AGPL-3.0-or-later