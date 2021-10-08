// Copyright (c) 2021, Garcia's Pawnshop and contributors
// For license information, please see license.txt

frappe.ui.form.on('Pawn Ticket', {
	refresh: function(frm) {
		set_total_appraised_amount(frm);
		frm.set_query("pawn_item", "pawn_ticket_items", function() {
        	return {
				"filters": {
					"pawn_type": frm.doc.pawn_type
				}
			};
    	});
	},

	customers_tracker_no: function(frm){
		frappe.call({
			method: 'fx.foreign_exchange.test.hello',
			args: {
				customer_name: frm.doc.customers_tracker_no
			},

			callback: function(r){
				frm.set_value('notes', r.message);
				refresh_fields('notes');
				console.log(r.message);
			},
			
			error: function(r){
				console.log(r);
			}
		});
	},

	pawn_type: function(frm){
		set_total_appraised_amount(frm);

		frappe.confirm('Are you sure you want to proceed?',
		() => {
			// action to perform if Yes is selected
			frm.clear_table("pawn_ticket_items");
			frm.refresh_fields();
		}, () => {
			// action to perform if No is selected
		})	
	},

	date_loan_granted: function(frm){
		let default_maturity_date = frappe.datetime.add_days(cur_frm.doc.date_loan_granted, 30);
		cur_frm.set_value('maturity_date', default_maturity_date);

		let default_expiry_date = frappe.datetime.add_days(cur_frm.doc.date_loan_granted, 120);
		cur_frm.set_value('expiry_date', default_expiry_date);
	},	

});

frappe.ui.form.on('Pawn Ticket Item', {
	
    appraised_amount: function(frm, cdt, cdn){
		set_total_appraised_amount(frm, cdt, cdn);
	},

	pawn_ticket_items_remove: function(frm, cdt, cdn) {
		set_total_appraised_amount(frm, cdt, cdn);
    }

})


function set_total_appraised_amount(frm, cdt, cdn){ // Calculate Principal Amount
	let temp_principal = 0.00;
	$.each(frm.doc.pawn_ticket_items, function(index, item){
		temp_principal += parseFloat(item.appraised_amount);
	});
	frm.set_value('desired_principal', temp_principal);
	let interest = set_item_interest(frm, temp_principal);

}

function set_item_interest(frm, temp_principal){ //Calculate Interest and Net Proceeds
	var interest = 0.00;
	var net_proceeds = 0.00;
	if (frm.doc.pawn_type == 'Gadget'){
		frappe.db.get_single_value('Pawnshop Management Settings', 'gadget').then(value => {
			interest = parseFloat(value)/100 * temp_principal;
			frm.set_value('interest', interest);
			net_proceeds = temp_principal - interest;
			frm.set_value('net_proceeds', net_proceeds)
		});

	} else {
		frappe.db.get_single_value('Pawnshop Management Settings', 'jewelry').then((value) => {
			interest = parseFloat(value)/100 * temp_principal;
			frm.set_value('interest', interest);
			net_proceeds = temp_principal - interest;
			frm.set_value('net_proceeds', net_proceeds)
		});
	}

	
}

