frappe.ui.form.on("Journal Entry", {
    refresh:function(frm){
        frm.add_custom_button('Import Data', () =>{
            frappe.call({
                method: 'fx.foreign_exchange.test.hello',

                callback: function(r){
                    frappe.msgprint(r)
                },

                /*method: 'fx.foreign_exchange.new_journal_entry.create_new_journal_entry',

                callback: function(r){
                    frappe.show_alert({
                        message: 'Import Succesful',
                        indicator: 'green'
                    })
                },*/

                error: function(r){
                    //frappe.show_alert({
                    //    message: 'Import failed',
                    //    indicator: 'red'
                    //})
                }
            })
        })
    }
})