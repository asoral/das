from __future__ import unicode_literals
from frappe.utils import formatdate, add_months, add_days,flt
from frappe.utils.data import today
import frappe
import datetime
from datetime import date
from dateutil.relativedelta import relativedelta
from frappe.model.mapper import get_mapped_doc
from frappe.model.document import Document
from frappe import _
from frappe.utils.data import get_link_to_form

def stt_one_year_alert():
    stt = frappe.get_all("Employee",filters ={'emp_category':'STT','status':'Active'})
    # print(stt)
    for st in stt:
        s = frappe.get_doc('Employee',st)
        doj = s.date_of_joining
        one_year = add_months(doj,11)
        two_year = add_months(doj,23)
        three_year = add_months(doj,35)
        today = date.today()
        # print(s.employee_name)
        if one_year == today:
            send_alert(one_year,s.employee_name,s.department,s.designation)
            # print(s.employee_name)
        if two_year == today:
            send_alert(two_year,s.employee_name,s.department,s.designation)
        if three_year == today:
            send_alert(three_year,s.employee_name,s.department,s.designation)
        
def send_alert(date,name,dept,des):
    content="""anniversary reminder for %s of %s department"""%(name,dept) 
    # print(content)
    
    # frappe.sendmail(
    #             recipients=["suganya.b@voltechgroup.com"],
    #             subject = "hello",
    #             message = """%s"""%(content)
    #         )
    
            
def work_anniversary():
    work_ann = frappe.get_all("Employee",filters = {'status':'Active'})
    # print(work_ann)
    for work in work_ann:
        w = frappe.get_doc('Employee',work)
        doj = w.date_of_joining
        one_year = add_months(doj,12)
        two_year = add_months(doj,24)
        today = date.today()
        if one_year == today:
            anniversary_alert(one_year,w.employee_name,w.department)
        if two_year == today:
            anniversary_alert(two_year,w.employee_name,w.department)
def anniversary_alert(date,name,dept):
      content="""Work anniversary for %s of %s department"""%(name,dept) 
      print(content)
        
    # frappe.sendmail(
    #             recipients=["suganya.b@voltechgroup.com"],
    #             subject = "hello",
    #             message = """%s"""%(content)
    #         )

def wedding_anniversary():
    wed_day =  get_employees_wedding_anniversary_today()
    if wed_day:
        print(wed_day)
    for e in wed_day:
         frappe.sendmail(recipients=filter(lambda u: u not in (e.company_email, e.personal_email, e.user_id), users),
                            subject=_("Birthday Reminder for {0}").format(
                                e.employee_name),
                            message=_("""Today is {0}'s birthday!""").format(
                                e.employee_name),
                            reply_to=e.company_email or e.personal_email or e.user_id)

   
def birthday_reminder():
    birthday = get_employees_who_are_born_today()
    if birthday:
        print(birthday)
    for e in birthday:
         frappe.sendmail(recipients=filter(lambda u: u not in (e.company_email, e.personal_email, e.user_id), users),
                            subject=_("Birthday Reminder for {0}").format(
                                e.employee_name),
                            message=_("""Today is {0}'s birthday!""").format(
                                e.employee_name),
                            reply_to=e.company_email or e.personal_email or e.user_id)


    
       
def get_employees_who_are_born_today():
    """Get Employee properties whose birthday is today."""
    return frappe.db.sql("""select name, personal_email, company_email, user_id, employee_name
		from tabEmployee where day(date_of_birth) = day(%(date)s)
		and month(date_of_birth) = month(%(date)s)
		and status = 'Active'""", {"date": today()}, as_dict=True)
def get_employees_wedding_anniversary_today():
    """Get Employee properties whose birthday is today."""
    return frappe.db.sql("""select name, personal_email, company_email, user_id, employee_name
		from tabEmployee where day(date_of_marriage) = day(%(date)s)
		and month(date_of_marriage) = month(%(date)s)
		and status = 'Active'""", {"date": today()}, as_dict=True)
@frappe.whitelist()
def make_employee(name):
 
    app = frappe.get_doc("Job Applicant",name)
    return app
    # if status == 'Accepted':
    #     emp = frappe.new_doc("Employee")
    #     # frappe.set_route('Form','Employee',{'applicant_name':frm.doc.name})
    #     emp.update({
    #         "first_name":app.applicant_name, 
    #         "date_of_joining":app.joining_date   
    #         "employment_type":app.employment_type
    #         "emp_category":app.emp_category
    #         "date_of_birth":app.date_of_birth
    #     })
    #     emp.save(ignore_permissions=True)
    #     frappe.errprint(emp.first_name)
    #     frappe.db.commit()
        # frappe.errprint(emp)

     
	




    
    





    

# def update_cat():
#     employees = frappe.db.sql("""select name,emp_category from `tabEmployee` where status = 'Active' """,as_dict=True)
#     for emp in employees:
#         if frappe.db.exists("Salary Slip",{"employee":emp.name}):
#             salary_slip = frappe.get_doc("Salary Slip",{"employee":emp.name})
#             salary_slip.employee_category = emp.emp_category
#             print salary_slip.employee_name
#             salary_slip.db_update()
#             frappe.db.commit()
            





    
    






