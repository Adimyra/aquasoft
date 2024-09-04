frappe.ui.form.on('Installation Note', {
    refresh: function(frm) {
        // Add custom button to create Maintenance Visit manually
        frm.add_custom_button(__('Create Maintenance Visit'), function() {
            frappe.call({
                method: 'aquasoft.installation_note_hooks.create_maintenance_visit_manually',
                args: {
                    docname: frm.doc.name
                },
                callback: function(r) {
                    if (r.message) {
                        frappe.msgprint(__('Maintenance Visit {0} created and submitted successfully', [r.message]));
                    }
                }
            });
        });
    }
});