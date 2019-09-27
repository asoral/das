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
    # overtime = frappe.db.sql(""" select sum(amount) from `tabSalary Detail` as sd, `tabSalary Structure` as ss where ss.name = sd.name and sd.salary_component = "Overtime" and ss.start_date = %s group by employee_category """, (start_date), as_dict=1)
    # frappe.errprint(overtime)
    # employees = frappe.db.sql("""select name,emp_category from `tabEmployee` where status = 'Active' """,as_dict=True)
    # salary_slip = frappe.db.sql("""select sum(gross_pay), net_pay from `tabSalary Slip` 
    # where start_date = %s """,(start_date), as_dict=True)
    # total = 0
    
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
    
    salary_slip = frappe.db.sql("""select name,employee_category,designation, sum(gross_pay) , sum(net_pay) from `tabSalary Slip`  where start_date = '2019-05-01' group by employee_category""", as_dict=True)
    # frappe.errprint(salary_slip)
    # over_time = frappe.db.sql("""select salary_component from `tabSalary Detail` ,""")
    ot_total = 0
    for i in salary_slip:
        if i["employee_category"] == "Staff" and i["designation"] != "OPERATING ENGINEER" :
            frappe.db.set_value("Salary Summary",name,"current_month",i["sum(gross_pay)"] )
            frappe.db.set_value("Salary Summary",name,"current_month_net", i["sum(net_pay)"])
            
            
        if i["employee_category"] == "OE" :
            frappe.db.set_value("Salary Summary",name,"cur_gross_oe",i["sum(gross_pay)"] )
            frappe.db.set_value("Salary Summary",name,"cur_net_oe", i["sum(net_pay)"])
            # frappe.db.set_value("Salary Summary",name,"current_month_staff_ot", ot_total)
        
        if i["employee_category"] == "Emp" :
            frappe.db.set_value("Salary Summary",name,"cur_gross_emp",i["sum(gross_pay)"] )
            frappe.db.set_value("Salary Summary",name,"cur_net_emp", i["sum(net_pay)"])

        if i["employee_category"] == "STT" :
            frappe.db.set_value("Salary Summary",name,"cur_gross_stt",i["sum(gross_pay)"] )
            frappe.db.set_value("Salary Summary",name,"cur_net_stt", i["sum(net_pay)"])
            
        if i["employee_category"] == "BOAT" :
            frappe.db.set_value("Salary Summary",name,"cur_gross_boat",i["sum(gross_pay)"] )
            frappe.db.set_value("Salary Summary",name,"cur_net_boat", i["sum(net_pay)"])

        if i["employee_category"] == "Driver" :
            frappe.db.set_value("Salary Summary",name,"cur_gross_driver",i["sum(gross_pay)"] )
            frappe.db.set_value("Salary Summary",name,"cur_net_driver", i["sum(net_pay)"])

        if i["employee_category"] == "Cook" :
            frappe.db.set_value("Salary Summary",name,"cur_gross_cook",i["sum(gross_pay)"] )
            frappe.db.set_value("Salary Summary",name,"cur_net_cook", i["sum(net_pay)"])
        
        if i["employee_category"] == "Korean" :
            frappe.db.set_value("Salary Summary",name,"cur_gross_korean",i["sum(gross_pay)"] )
            frappe.db.set_value("Salary Summary",name,"cur_net_korean", i["sum(net_pay)"])

    query = """ select ss.designation,sum(sd.amount) from `tabSalary Detail` as sd inner join `tabSalary Slip` ss on sd.parent = ss.name where ss.start_date = '2019-05-01' and sd.salary_component = "Overtime" group by ss.designation"""
    overtime = frappe.db.sql(query, as_dict=1)
    frappe.errprint(overtime)
    
    # emp_category = ["Staff","BOAT","emp"]
    # for cat in emp_category:
    # 	employees = frappe.db.sql("""select name,emp_category from `tabEmployee` where status = 'Active' and emp_category = %s """,(cat),as_dict=True)
    # 	for emp in employees:

    
    # for emp in employees:
# 	for i in range(len(emp_category)):
# 		ot_total, gross_total, net_total = calculate(start_date,emp_category[i])
# 	frappe.errprint(gross_total)
# 	frappe.db.set_value("Salary Summary",name,"current_month", gross_total)
# 	frappe.db.set_value("Salary Summary",name,"current_month_net", net_total)
# 	frappe.db.set_value("Salary Summary",name,"current_month_staff_ot", ot_total)
            
            
# def calculate(start_date,cat):
# 	ot_total = gross_total = net_total = 0
# 	# if emp.emp_category == cat:
# 	for slip in frappe.get_all("Salary Slip",fields =['name','gross_pay','net_pay','start_date']):
# 		ot = frappe.get_value("Salary Detail",{'salary_component':'Overtime','parent':slip.name},['amount'])
# 		ot_total = ot_total + ot
# 		gross_total = gross_total + slip.gross_pay
# 		net_total = net_total + slip.net_pay
# 	frappe.errprint(net_total)
# 	return ot_total, gross_total, net_total

    staff_count = frappe.db.count('Employee', {'emp_category':"Staff",'status': 'Active'})
    frappe.db.set_value("Salary Summary",name,"no_of_staff_cur_mon", staff_count)

    oe_count = frappe.db.count('Employee', {'designation':"OPERATION ENGINEER",'status': 'Active'})
    frappe.db.set_value("Salary Summary",name,"cur_mon_oe", oe_count)

    boat_count = frappe.db.count('Employee', {'designation':"BOAT",'status': 'Active'})
    frappe.db.set_value("Salary Summary",name,"cur_mon_boat", boat_count)

    emp_count = frappe.db.count('Employee', {'emp_category':"emp",'status': 'Active'})
    frappe.db.set_value("Salary Summary",name,"cur_mon_emp", emp_count)

    stt_count = frappe.db.count('Employee', {'emp_category':"STT",'status': 'Active'})
    frappe.db.set_value("Salary Summary",name,"cur_mon_stt", stt_count)

    driver_count = frappe.db.count('Employee', {'emp_category':"Driver",'status': 'Active'})
    frappe.db.set_value("Salary Summary",name,"cur_mon_driver", driver_count)

    cook_count = frappe.db.count('Employee', {'designation':"Cook",'status': 'Active'})
    frappe.db.set_value("Salary Summary",name,"cur_mon_cook", cook_count)

    korean_count = frappe.db.count('Employee', {'emp_category':"Korean",'status': 'Active'})
    frappe.db.set_value("Salary Summary",name,"cur_korean", korean_count)