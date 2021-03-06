# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import cstr, cint, getdate
from frappe import msgprint, _
from calendar import monthrange
def execute(filters=None):
    if not filters:
        filters = {}

    conditions, filters = get_conditions(filters)
    columns = get_columns(filters)
    att_map = get_attendance_list(
        conditions, filters)
    emp_map = get_employee_details()

    holiday_list = [emp_map[d]["holiday_list"]
                    for d in emp_map if emp_map[d]["holiday_list"]]
    default_holiday_list = frappe.db.get_value(
        "Company", filters.get("company"), "default_holiday_list")
    holiday_list.append(default_holiday_list)
    holiday_list = list(set(holiday_list))
    holiday_map = get_holiday(holiday_list, filters["month"])

    data = []
    for emp in sorted(att_map):
        emp_det = emp_map.get(emp)
        if not emp_det:
            continue

        row = [emp, emp_det.employee_name, emp_det.biometric_no, emp_det.department,
               emp_det.designation, emp_det.emp_category]
        for day in range(filters["total_days_in_month"]):
            status = []
            status = att_map.get(emp).get(day + 1, "")
            # frappe.errprint(status)
            # in_time = in_time_map.get(emp).get(day + 1)
            # out_time = out_time_map.get(emp).get(day + 1)
            # status_map = {"Present":  cstr(in_time) + "/" + cstr(out_time), "On Duty": "OD", "Late": "P", "Absent": "A", "Half Day": "HD",
            #               "On Leave": "L", "None": "", "Holiday": "<b>H</b>"}
            # frappe.errprint(in_time) 
            # frappe.errprint(out_time)             
            if status == "" and holiday_map:
                emp_holiday_list = emp_det.holiday_list if emp_det.holiday_list else default_holiday_list
                if emp_holiday_list in holiday_map and (day + 1) in holiday_map[emp_holiday_list]:
                    status = "Holiday"
            row.append(status)

        data.append(row)

    return columns, data


def get_columns(filters):
    columns = [
        _("Employee") + ":Link/Employee:120", _("Employee Name") +
        "::140", _("ID") + "::120",
        _("Department") + ":Link/Department:120", _("Designation") +
        "::120", _("Employment Category") +
        ":Data:120"
    ]

    for day in range(filters["total_days_in_month"]):
        columns.append(cstr(day + 1) + "::120")

    return columns


def get_attendance_list(conditions, filters):
    checkin_list = frappe.db.sql("""select employee, day(time) as day_of_month,log_type,time from `tabEmployee Checkin` 
    where %s order by employee, date(log_date)""" % conditions,filters, as_dict=1)
    att_map = {}
    time = []
    for d in checkin_list:
        att_map.setdefault(d.employee, frappe._dict()
                           ).setdefault(d.day_of_month, "")
        time.append(cstr((d.time).time()))                
        att_map[d.employee][d.day_of_month] = time
    frappe.errprint(att_map)      
    return att_map


def get_conditions(filters):
    if not (filters.get("month") and filters.get("year")):
        msgprint(_("Please select month and year"), raise_exception=1)

    filters["month"] = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov",
                        "Dec"].index(filters.month) + 1

    filters["total_days_in_month"] = monthrange(
        cint(filters.year), filters.month)[1]

    conditions = " month(log_date) = %(month)s and year(log_date) = %(year)s"


    # if filters.get("emp_category"):
    #     conditions += " and company = %(company)s"
    if filters.get("employee"):
        conditions += " and employee = %(employee)s"

    return conditions, filters


def get_employee_details():
    emp_map = frappe._dict()
    for d in frappe.db.sql("""select name, employee_name, biometric_no,designation,emp_category, department,
        holiday_list from tabEmployee""", as_dict=1):
        emp_map.setdefault(d.name, d)

    return emp_map


def get_holiday(holiday_list, month):
    holiday_map = frappe._dict()
    for d in holiday_list:
        if d:
            holiday_map.setdefault(d, frappe.db.sql_list('''select day(holiday_date) from `tabHoliday`
                where parent=%s and month(holiday_date)=%s''', (d, month)))

    return holiday_map


@frappe.whitelist()
def get_attendance_years():
    year_list = frappe.db.sql_list(
        """select distinct YEAR(attendance_date) from tabAttendance ORDER BY YEAR(attendance_date) DESC""")
    if not year_list:
        year_list = [getdate().year]

    return "\n".join(str(year) for year in year_list)