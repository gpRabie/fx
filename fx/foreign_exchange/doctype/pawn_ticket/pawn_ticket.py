# Copyright (c) 2021, Garcia's Pawnshop and contributors
# For license information, please see license.txt

# import frappe


import frappe
from frappe.model.document import Document
from frappe import _
from frappe.utils import flt

import erpnext
from frappe.utils.csvutils import read_csv_content, get_csv_content_from_google_sheets
from erpnext.accounts.general_ledger import make_gl_entries
from erpnext.controllers.accounts_controller import AccountsController


class PawnTicket(AccountsController):

    def on_submit(self):
        self.make_gl_entries()

    def validate(self):
        pass

    #@frappe.whitelist()
    def make_gl_entries(self, cancel=0, adv_adj=0):

        content = get_csv_content_from_google_sheets('https://docs.google.com/spreadsheets/d/1Id-1_SYEb8ZY_-rYQqown_9msjKD15RUrCszbVJzjc8/edit#gid=952708933')
        data = read_csv_content(content)

        gle_map = []
            #debit_account = frappe.get_doc("Account", "COH-FX Branches")
            #credit_account = frappe.get_doc("Account", "CIV-FX Reserve Branches")
            #customer = frappe.get_doc("Customer", doc.customer_tracker_no)


        gle_map.append(
            self.get_gl_dict({
                "account": "10203-007-000-000 - CIV-FX Reserve Branches - GP",
                "posting_date": self.date_loan_granted,
                #"party_type": "Customer",
                #"party": self.customer_tracker_no,
                "credit": flt(data[6][5]),
                "debit": flt(0),
                "remarks": "Test"
            })
        )
        

        gle_map.append(
            self.get_gl_dict({
                "account": "10001-007-0000-0000 - COH-FX Branches - GP",
                "posting_date": self.date_loan_granted,
                "credit": flt(0),
                "debit": flt(data[6][5]),
                "remarks": "Test"
            })
        )

        gle_map.append(
            self.get_gl_dict({
                "account": "10001-007-0000-0000 - COH-FX Branches - GP",
                "posting_date": self.date_loan_granted,
                "credit": flt(data[6][6]),
                "debit": flt(0),
                "remarks": "Test"
            })
        )

        gle_map.append(
            self.get_gl_dict({
                "account": "Sales - GP",
                "posting_date": self.date_loan_granted,
                "cost_center": self.cost_center,
                "credit": flt(0),
                "debit": flt(data[6][6]),
                "remarks": "Test"
            })
        )


        if gle_map:
            make_gl_entries(gle_map, cancel=False, adv_adj=adv_adj)
            print("Done")

    #def format_date(date):
        #string_date = str(date)
        #format_list = []
        #for i in range (len(format_date)):
        #    if string_date[i] == "-" and format_list:
        #        format_list.append(string_date[:i])
        #    elif string_date[i] == "-" and not format_list:
        #        format_list.append(string_date[])