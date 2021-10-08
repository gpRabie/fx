import frappe
from datetime import datetime
from frappe.utils import add_to_date

@frappe.whitelist()
def hello():
    yesterday = add_to_date(datetime.now(), days=-1, as_string=True)
    return "Today is {}".format(yesterday)

@frappe.whitelist()
def reminder():
    print("Hi")
    frappe.msgprint("The time now is {}".format(now()))
    
    