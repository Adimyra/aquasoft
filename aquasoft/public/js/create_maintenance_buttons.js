frappe.ui.form.on('Sales Invoice', {
    refresh: function(frm) {
        frm.add_custom_button(__('Create Maintenance Schedule'), function() {
            frappe.call({
                method: 'aquasoft.custom_scripts.regular_maintenance_schedule.create_maintenance_schedule',
                args: { doc: frm.doc }
            });
        });

        frm.add_custom_button(__('First Visit M Schedule'), function() {
            frappe.call({
                method: 'aquasoft.custom_scripts.first_visit_schedule.create_first_visit_schedule',
                args: { doc: frm.doc }
            });
        });
    }
});