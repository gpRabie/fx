// Copyright (c) 2016, Garcia's Pawnshop and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Sample script report"] = {
	"filters": [
		{
			fieldname: "id_type",
			label: __("ID Type"),
			fieldtype: "Select",
			options: ["SSS ID", "TIN ID", "Postal ID", "Voter's ID"]
		}
	]
};
