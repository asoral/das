# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Documents"),
            "icon": "fa fa-star",
            "items":[
                {
                    "type":"doctype",
                    "name":"Salary Summary"
            }
            ]
		},
        {
			"label": _("Documents"),
            "icon": "fa fa-star",
            "items":[
                {
                    "type":"doctype",
                    "name":"On Duty Application"
            }
            ]
		},
        {
			"label": _("Documents"),
            "icon": "fa fa-star",
            "items":[
                {
                    "type":"doctype",
                    "name":"Full and final settlement sheet"
            }
            ]
		},
        {
			"label": _("Documents"),
            "icon": "fa fa-star",
            "items":[
                {
                    "type":"doctype",
                    "name":"NO DUE DECLARATION FORM"
            }
            ]
		},
        {
			"label": _("Documents"),
            "icon": "fa fa-star",
            "items":[
                {
                    "type":"doctype",
                    "name":"Training and feedback form"
            }
            ]
		},
        {
			"label": _("Documents"),
            "icon": "fa fa-star",
            "items":[
                {
                    "type":"doctype",
                    "name":"Appraisal Form"
            }
            ]
		},
	]