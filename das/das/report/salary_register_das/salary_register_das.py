# Copyright (c) 2013, VHRS and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import flt
from frappe import _

def execute(filters=None):
	columns , data = [],[]
	columns = get_columns()
	row = []
	ss = get_salary_slips(filters)
	for s in ss:
		frappe.errprint(s)
		empid = frappe.get_value("Employee",{"name":s.employee},['employee_number','designation','first_name','date_of_joining','relieving_date'],as_dict=True)
		row = [s.employee]
		empname = frappe.get_value("Salary Slip",{"name":s.employee},['employee_name'])
		basic = frappe.get_value("Salary Detail",{'salary_component':'Basic','parent':s.name},['amount'])
		hra = frappe.get_value("Salary Detail",{'salary_component':'House Rent Allowance','parent':s.name},['amount'])
		con = frappe.get_value("Salary Detail",{'salary_component':'Conveyance Allowance','parent':s.name},['amount'])
		da = frappe.get_value("Salary Detail",{'salary_component':'Dearness Allowance','parent':s.name},['amount'])
		sa = frappe.get_value("Salary Detail",{'salary_component':'Special Allowance','parent':s.name},['amount'])
		ota = frappe.get_value("Salary Detail",{'salary_component':'Other Allowance','parent':s.name},['amount'])
		ma = frappe.get_value("Salary Detail",{'salary_component':'Medical Allowance','parent':s.name},['amount'])
		ot = frappe.get_value("Salary Detail",{'salary_component':'Overtime','parent':s.name},['amount'])
		ab = frappe.get_value("Salary Detail",{'salary_component':'Attendance Bonus','parent':s.name},['amount'])
		pf = frappe.get_value("Salary Detail",{'salary_component':'Provident Fund','parent':s.name},['amount'])
		esi = frappe.get_value("Salary Detail",{'salary_component':'Employee State Insurance','parent':s.name},['amount'])
		pt = frappe.get_value("Salary Detail",{'salary_component':'Professional Tax','parent':s.name},['amount'])
		tds = frappe.get_value("Salary Detail",{'salary_component':'Tax Deduction at source','parent':s.name},['amount'])
	    

  
		row += [s.name,empid['designation'],empid['first_name'],s.department,s.employee_category,empid['date_of_joining'],
		empid['relieving_date'],s.total_working_days,s.payment_days,s.leave_without_pay,basic,hra,con,da,sa,ota,ma,ot,s.gross_pay,ab,
		pf,esi,pt,tds,s.total_deduction,s.net_pay,s.bank_account_no]


		# frappe.errprint(s.name)
		data.append(row)
	return columns,data

# def get_salary_slip(filters):
	
# 	salary_slips = frappe.get_all("Salary Slip",{'start_date':filters.from_date,'end_date':filters.to_date,'docstatus':filters.docstatus},['employee','name','employee_name','department','total_working_days',
# 	'payment_days','leave_without_pay','gross_pay','total_deduction','net_pay','bank_account_no'])
# 	return salary_slips 

def get_columns():
	columns = [
		_("Employee Number") + ":Link/Employee:120",_("SSID") + ":Link/Employee:120", _("Designation") + ":Link/Employee:120" ,_("Emp Name") + ":Link/Employee:120", _("Department") + ":Link/Employee:120" 
		, _("Emp Category") + ":Data/Employee:120",_("DOJ") + ":Link/Employee:120", _("DOL") + ":Link/Employee:120", _("Working Days") + ":Link/Salary Slip:120", _("Payable") + ":Link/Salary Slip:120", _("LOP Days") + ":Link/Salary Slip:120", 
		_("Basic") + ":Link/Salary Slip:120", _("HRA") + ":Link/Salary Slip:120", _("Conveyance") + ":Link/Salary Slip:120", _("DA") + ":Link/Salary Slip:120", _("SPL.ALLO") + ":Link/Salary Slip:120", 
		_("Other Allowance") + ":Link/Salary Slip:120", _("Medical") + ":Link/Salary Slip:120", _("OT") + ":Link/Salary Slip:120", _("Gross Earnings") + ":Link/Salary Slip:120", _("Attendance Bonus") + ":Link/Salary Slip:120", _("PF") + ":Link/Salary Slip:120", 
		_("ESI") + ":Link/Salary Slip:120", _("PT") + ":Link/Salary Slip:120", _("TDS") + ":Link/Salary Slip:120", _("Gross Deduction") + ":Link/Salary Slip:120", _("Net") + ":Link/Salary Slip:120", _("Bank Account No") + ":Link/Salary Slip:120",
	]
	return columns

def get_salary_slips(filters):
	filters.update({"from_date": filters.get("from_date"), "to_date":filters.get("to_date")})
	conditions, filters = get_conditions(filters)
	salary_slips = frappe.db.sql("""select * from `tabSalary Slip` where %s
		order by employee""" % conditions, filters, as_dict=1)

	return salary_slips or []

def get_conditions(filters):
	conditions = ""
	doc_status = {"Draft": 0, "Submitted": 1, "Cancelled": 2}

	if filters.get("docstatus"):
		conditions += "docstatus = {0}".format(doc_status[filters.get("docstatus")])

	if filters.get("from_date"): conditions += " and start_date >= %(from_date)s"
	if filters.get("to_date"): conditions += " and end_date <= %(to_date)s"
	if filters.get("company"): conditions += " and company = %(company)s"
	if filters.get("employee"): conditions += " and employee = %(employee)s"

	return conditions, filters