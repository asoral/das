# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "DAS",
			# "category": "Modules",
			"label": _("DAS"),
			"color": "#1abc9c",
			"icon": "octicon octicon-organization",
			"type": "module",
			"description": "DAS Specific Requirements",
			
		}
	]
