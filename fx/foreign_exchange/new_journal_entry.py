import frappe
import json
from frappe.utils.csvutils import read_csv_content, get_csv_content_from_google_sheets
from datetime import datetime
from frappe.utils import flt, add_to_date


@frappe.whitelist()
def get_data(url):
	content = get_csv_content_from_google_sheets(url)
	raw_data = read_csv_content(content)
	data = json.dumps(raw_data)
	new_data = json.loads(data)
	return new_data

@frappe.whitelist()
def create_new_journal_entry():
	data = get_data('https://docs.google.com/spreadsheets/d/1Id-1_SYEb8ZY_-rYQqown_9msjKD15RUrCszbVJzjc8/edit#gid=952708933')
	accounts = {
		'CC-COH': '10001-001-000-000 - COH - FX Cavite - GP', 
		'CC-CIV': '10203-007-000-000 - CIV-FX Reserve Branches - GP',
		'POB-COH': '10001-003-000-000 - COH - FX Poblacion - GP',
		'POB-CIV': '10203-003-000-000 - CIV - FX Reserve Poblacion - GP',
		'GTC-COH': '10001-004-000-000 - COH - FX Gen Trias - GP',
		'GTC-CIV': '10203-004-000-000 - CIV - FX Reserve Gen Trias - GP',
		'TNZ-COH': '10001-005-000-000 - COH - FX Tanza - GP',
		'TNZ-CIV': '10203-005-000-000 - CIV - FX Reserve Tanza - GP',
		'MOL-COH': '10001-006-000-000 - COH - FX Molino - GP',
		'MOL-CIV': '10203-006-000-000 - CIV - FX Reserve Molino - GP'
	}
	yesterday = add_to_date(datetime.now(), days=-1, as_string=True)
	for entry_no in range (2, len(data)):
		if data[entry_no][2] == yesterday: #today()
			if data[entry_no][3] == "CC":
				create_JE(data[entry_no][2], accounts.get("CC-COH"), accounts.get("CC-CIV"), data[entry_no][5], data[entry_no][6])
			elif data[entry_no][3] == "POB":
				create_JE(data[entry_no][2], accounts.get("POB-COH"), accounts.get("POB-CIV"), data[entry_no][5], data[entry_no][6])
			elif data[entry_no][3] == "GTC":
				create_JE(data[entry_no][2], accounts.get("GTC-COH"), accounts.get("GTC-CIV"), data[entry_no][5], data[entry_no][6])
			elif data[entry_no][3] == "TNZ":
				create_JE(data[entry_no][2], accounts.get("TNZ-COH"), accounts.get("TNZ-CIV"), data[entry_no][5], data[entry_no][6])
			elif data[entry_no][3] == "MOL":
				create_JE(data[entry_no][2], accounts.get("MOL-COH"), accounts.get("MOL-CIV"), data[entry_no][5], data[entry_no][6])
	
	return True
				
	

def create_JE(posting_date, coh_account, civ_account, additional_funds, peso_out):
	doc = frappe.new_doc('Journal Entry')
	doc.voucher_type = 'Journal Entry'
	doc.company = 'Garcia\'s Pawnshop'
	doc.posting_date = posting_date

	row_values1 = doc.append('accounts', {})
	row_values1.account = coh_account
	row_values1.credit_in_account_currency = flt(0)
	row_values1.debit_in_account_currency = flt(additional_funds)

	row_values2 = doc.append('accounts', {})
	row_values2.account = coh_account
	row_values2.credit_in_account_currency = flt(peso_out)
	row_values2.debit_in_account_currency = flt(0)

	row_values3 = doc.append('accounts', {})
	row_values3.account = civ_account
	row_values3.credit_in_account_currency = flt(additional_funds)
	row_values3.debit_in_account_currency = flt(0)

	row_values4 = doc.append('accounts', {})
	row_values4.account = 'Sales - GP'
	row_values4.credit_in_account_currency = flt(0)
	row_values4.debit_in_account_currency = flt(peso_out)

	doc.insert()
	doc.save()
	#doc.submit()