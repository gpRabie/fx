import frappe

@frappe.whitelist()
def hello():
    return "Hellow world"