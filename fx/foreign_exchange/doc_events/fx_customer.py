import frappe

def validate(doc, method):
    frappe.msgprint("hello customer {}".format(doc.first_name))