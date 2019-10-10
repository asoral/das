from __future__ import unicode_literals
from frappe.utils import formatdate, add_months, add_days,flt
from frappe.utils.data import today
import frappe
import datetime
from datetime import date
from frappe import _

def mark_contract_att():
    checkins = frappe.db.sql(""" select ec.* from `tabEmployee Checkin` ec inner join `tabEmployee` e on e.employee = ec.employee  where e.employment_type = 'Contract'""",as_dict=1)
    for checkin in checkins:
        print(checkin)

def reset_password():
    frappe.errprint("hi")