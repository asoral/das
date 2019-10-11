# -*- coding: utf-8 -*-
# Copyright (c) 2019, VHRS and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import add_days
from frappe.utils.data import today
from datetime import datetime, timedelta, date

class PetrolConveyance(Document):
    pass

@frappe.whitelist()
def create_petrol_allowance():
    day = add_days(date.today(),-1)
    start_date = get_first_day(day)
    end_date = get_last_day(day)
    employees = frappe.get_list("Employee",{'petrol':1})
    for employee in employees:
        emp = frappe.get_doc("Employee",{"name":employee.name})
        if not frappe.db.exists("Petrol conveyance",{"employee":employee,"start_date":start_date,"end_date":end_date}):
            petrol_all = frappe.new_doc("Petrol Conveyance")
            petrol_all.employee = emp.employee
            petrol_all.save()
            petrol_all.update({
                "employee":emp.employee,
                "employee_name":emp.employee_name,
                "designation":emp.designation,
                "department":emp.department,
                "doj":emp.date_of_joining,
                "petrol_conveyance":emp.petrol_conveyance,
                "start_date":start_date,
                "end_date":end_date
            })
            petrol_all.save(ignore_permissions=True)
            frappe.db.commit()

def get_first_day(dt, d_years=0, d_months=0):
    y, m = dt.year + d_years, dt.month + d_months
    a, m = divmod(m - 1, 12)
    return date(y + a, m + 1, 1)


def get_last_day(dt):
    return get_first_day(dt, 0, 1) + timedelta(-1)