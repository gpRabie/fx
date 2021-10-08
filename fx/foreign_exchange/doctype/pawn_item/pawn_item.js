// Copyright (c) 2021, Garcia's Pawnshop and contributors
// For license information, please see license.txt


frappe.ui.form.on('Pawn Item', {
	refresh: function(frm) {
		frm.call('Pawn Ticket', { throw_if_missing: true })
		.then(r => {
			if (r.message) {
				let linked_doc = r.message;
				frappe.msgprint({
					title: linked_doc.pawn_item,
					indicator: 'green',
					message: __(pawn_type)
				});
			}
		});
	}
});
