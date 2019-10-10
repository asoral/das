# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "das"
app_title = "DAS"
app_publisher = "VHRS"
app_description = "Customizations for DAS"
app_icon = "octicon octicon-organization"
app_color = "blue"
app_email = "abdulla.pi@voltechgroup.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/das/css/das.css"
# app_include_js = "/assets/das/js/das.js"

# include js, css files in header of web template
# web_include_css = "/assets/das/css/das.css"
# web_include_js = "/assets/das/js/das.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Appraisal" : "public/js/appraisal.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "das.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "das.install.before_install"
# after_install = "das.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "das.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events
# on_session_creation = [
# 	"das.utils.reset_password"
# ]

doc_events = {
	"Salary Slip": {
		"after_insert": "das.custom.add_leave_balance",
	},
	"Attendance Request": {
		"before_submit":"das.custom.cancel_attendance",
	},
	"Canteen Checkin":{
		"after_insert":"das.custom.add_meal_rate",
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"das.tasks.all"
# 	],
# 	"daily": [
# 		"das.tasks.daily"
# 	],
# 	"hourly": [
# 		"das.tasks.hourly"
# 	],
# 	"weekly": [
# 		"das.tasks.weekly"
# 	]
# 	"monthly": [
# 		"das.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "das.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "das.event.get_events"
# }

