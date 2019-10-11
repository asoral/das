# Copyright (c) 2013, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import flt

def execute(filters=None):
    columns, data = [], []
    # if not filters: filters = {}
    conditions = get_conditions(filters)
    columns = get_columns()
    opening = get_openings(conditions,filters)
    addition = get_additions(conditions,filters)
    left = get_lefts(conditions,filters)
    closing = opening + addition - left
    departments = get_department(filters)
    row = [departments,opening,addition,left,closing]
    data.append(row)

    return columns, data

def get_department(filters):
	return frappe.db.sql("""select name from `tabDepartment`""" , as_list=1)


def get_columns():
    columns = [
        _("Department") + ":Link/Department:120", _("Opening") + ":Data:120" , _("Addition") + ":Data:120" , _("Left") + ":Data:120" , _("Closing") + ":Data:120"
    ]
    return columns

def get_openings(conditions,filters):
    opening = 0
    query = """select count(name) as count,department from tabEmployee where status = 'Active' and date_of_joining < '%s' or relieving_date < '%s' %s group by department""" % (filters.from_date,filters.from_date,conditions)
    openings = frappe.db.sql(query, as_dict=1)
    frappe.errprint(openings)
    for o in openings:
        opening = o.count
    return opening

def get_additions(conditions,filters):
    addition = 0
    query = """select count(name) as count from tabEmployee where status = 'Active' and date_of_joining between '%s' and '%s' %s""" % (filters.from_date,filters.to_date,conditions)
    additions = frappe.db.sql(query, as_dict=1)
    for a in additions:
        addition = a.count
    return addition

def get_lefts(conditions,filters):
    left = 0
    query = """select count(name) as count from tabEmployee where status = 'Left' and relieving_date between '%s' and '%s' %s""" % (filters.from_date,filters.to_date,conditions)
    lefts = frappe.db.sql(query, as_dict=1)
    for l in lefts:
        left = l.count
    return left


def get_conditions(filters):
    conditions = ""
    if filters.get("department"):
        conditions += "and department = '%s'" % filters.get("department")

    # if filters.get("company"): conditions += " and company = '%s'" % \
    # 	filters["company"].replace("'", "\\'")

    return conditions