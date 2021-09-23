# Copyright (c) 2013, Garcia's Pawnshop and contributors
# For license information, please see license.txt

import frappe
from frappe import _ # _ for to set the string into literal string

def execute(filters=None):
	columns, data = [], []
	columns = get_columns()
	data = frappe.get_all("FX Customer", filters=filters, fields=['customer_tracker', 'first_name', 'last_name', 'gender', 'date_of_birth','id_type', 'money_borrowed'])
	message = 'Total Number of Customers:<span class="font-weight-bold primary">{}</span>'.format(len(data))

	chart = {
		'data': {
			'labels': [
				'asymptomatic',
				'mild',
				'severe',
				'critical'
			],
			'datasets': [
				{
					'name': 'Fully Vaccinated',
					'values': [45, 80, 22, 33]
				},
				{
					'name': 'Not Vaccinated',
					'values':[45, 80, 22, 10]
				}
			]
		},
		'type': 'bar'
	}

	report_summary = [
		{
			"label": "cases",
			"value":len(data),
			"indicator": "Blue"
		},

		{
			"label": "positivity rate",
			"value":254,
			"indicator": "Red"
		}
	]
	return columns, data, message, chart, report_summary

def get_columns():
	columns = [
		{
			'fieldname': 'customer_tracker',
			'label': _('Tracker Number'),
			'fieldtype': 'Link',
			'options': 'FX Customer',
			'width': 200
		},

		{
			'fieldname': 'first_name',
			'label': _('First Name'),
			'fieldtype': 'Data',
			'width': 120
		},

		{
			'fieldname': 'last_name',
			'label': _('Last Name'),
			'fieldtype': 'Data',
			'width': 120
		},

		{
			'fieldname': 'gender',
			'label': _('Gender'),
			'fieldtype': 'Data',
			'width': 120
		},

		{
			'fieldname': 'date_of_birth',
			'label': _('Date of Birth'),
			'fieldtype': 'Data',
			'width': 120
		},

		{
			'fieldname': 'id_type',
			'label': _('Date of Birth'),
			'fieldtype': 'Data',
			'width': 120
		},

		{
			'fieldname': 'money_borrowed',
			'label': _('Money Borrowed'),
			'fieldtype': 'Currency',
			'width': 120
		}
	]
	return columns
