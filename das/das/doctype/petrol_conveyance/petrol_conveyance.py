# -*- coding: utf-8 -*-
# Copyright (c) 2019, VHRS and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class PetrolConveyance(Document):
    pass

@frappe.whitelist()
def create_petrol_allowance(start_date,end_date,employee):
    emp = frappe.get_doc("Employee",{"name":employee})
    frappe.errprint(emp.designation)
    if not frappe.db.exists("Petrol conveyance",{"employee":employee,"start_date":start_date,"end_date":end_date}):
        frappe.errprint(emp)
        # petrol_all = frappe.new_doc("Petrol Conveyance")
        # petrol_all.employee = emp.employee
        # petrol_all.save()
        # petrol_all.update({
        #     "employee":emp.employee,
        #     "employee_name":emp.employee_name,
        #     "designation":emp.desingation,
        #     "department":emp.department,
        #     "doj":date_of_joining,
        #     "start_date":start_date,
        #     "end_date":end_date
        # })
        # petrol_all.save(ignore_permissions=True)
        # frappe.db.commit()