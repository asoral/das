# -*- coding: utf-8 -*-
# Copyright (c) 2019, VHRS and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from datetime import datetime, date

class SalarySummary(Document):
	pass

@frappe.whitelist()
def create_salary_summary(name,start_date):
	employees = frappe.db.sql("""select name,emp_category from `tabEmployee` where status = 'Active' """,as_dict=True)
	# salary_slip = frappe.db.sql("""select sum(gross_pay), net_pay from `tabSalary Slip` 
	# where start_date = %s """,(start_date), as_dict=True)
	# total = 0
	staff_gross = []
	boat_gross = []
	staff_g_total = 0
	staff_n_total = 0
	boat_g_total = 0
	ot_total = 0
	# c = frappe.db.sql("""select count(*) from "tabEmployee" where date_of_joining = '01-05-2019' """)
	# frappe.errprint(c)
	# for emp in employees:
	# 	if emp.emp_category == 'Staff':
	# 		staff = frappe.get_all("Salary Slip",fields =['gross_pay','net_pay'],filters={"employee":emp.name,'start_date':start_date})
	# 		salary_slip = frappe.get_doc("Salary Slip",{"employee":emp.name})
	# 		ot = frappe.get_value("Salary Detail",{'salary_component':'Overtime','parent':salary_slip.name},['amount'])
	# 		ot_total = ot_total + ot
	
	# 		for staff_g in staff:
	# 			# ot = frappe.get_value("Salary Detail",{"employee":staff_g.name,'salary_component':'Overtime','parent':slip.name},['amount'])
	# 			staff_g_total = staff_g_total + staff_g.gross_pay
	# 			staff_n_total = staff_n_total + staff_g.net_pay
	# frappe.errprint(ot_total)
	# frappe.db.set_value("Salary Summary",name,"current_month", staff_g_total)
	# frappe.db.set_value("Salary Summary",name,"current_month_net", staff_n_total)
	# frappe.db.set_value("Salary Summary",name,"current_month_staff_ot", ot_total)
	# 	elif emp.emp_category == 'BOAT':
	# 		boat = frappe.get_all("Salary Slip",fields =['gross_pay','net_pay'],filters={"employee":emp.name})
	# 		for boat_g in boat:
	# 			boat_g_total = boat_g_total + boat_g.gross_pay
	# 			boat_n_total = boat_n_total + boat_n.gross_pay
	# frappe.db.set_value("Salary Summary",name,"current_month", staff_g_total)
	# frappe.db.set_value("Salary Summary",name,"current_month_net", staff_n_total)

	emp_category = ["Staff","BOAT","emp"]
	calculate = []
	for emp in employees:
		for i in range(len(emp_category)):
			ot_total, gross_total, net_total = calculate(emp,emp_category[i])
	frappe.db.set_value("Salary Summary",name,"current_month", gross_total)
	frappe.db.set_value("Salary Summary",name,"current_month_net", net_total)
	frappe.db.set_value("Salary Summary",name,"current_month_staff_ot", ot_total)		
			
			
	def calculate(emp,cat):
		if emp.emp_category == cat:
			for slip in frappe.get_all("Salary Slip",fields =['gross_pay','net_pay','start_date'],filters={"employee":emp}):
				frappe.errprint(slip)
				slip_ot = frappe.get_doc("Salary Slip",{"employee":slip.name})
				ot = frappe.get_value("Salary Detail",{'salary_component':'Overtime','parent':slip_ot.name},['amount'])
				ot_total = ot_total + ot
				gross_total = gross_total + slip.gross_pay
				net_total = net_total + slip.net_pay
	return ot_total, gross_total, net_total


	