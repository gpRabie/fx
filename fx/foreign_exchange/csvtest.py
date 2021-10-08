import frappe
import json
from frappe.utils.csvutils import read_csv_content, get_csv_content_from_google_sheets
from frappe.core.doctype.data_import.importer import Importer
from frappe.utils import flt


@frappe.whitelist()
def get_data(url):
	content = get_csv_content_from_google_sheets(url)
	data = read_csv_content(content)
	return data

