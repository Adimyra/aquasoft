

// frappe.ui.form.on('Maintenance Visit', {
//     refresh: function(frm) {
//         // Check if the document is saved (not new) and spare parts exist
//         if (!frm.is_new() && frm.doc.spare_parts && frm.doc.spare_parts.length > 0 && !frm.doc.custom_spare_parts_sales_invoice) {
//             frm.add_custom_button(__('Create Sales Invoice'), function() {
//                 frappe.call({
//                     method: 'aquasoft.custom_scripts.create_sales_invoice_from_visit.create_sales_invoice',
//                     args: {
//                         maintenance_visit_name: frm.doc.name
//                     },
//                     callback: function(response) {
//                         if (response.message) {
//                             frm.set_value('custom_spare_parts_sales_invoice', response.message);
//                             frm.set_value('custom_parts_sales_invoice_created', 1);
//                             frm.save_or_update();
//                             frappe.msgprint({
//                                 title: __('Sales Invoice Created'),
//                                 message: __('A Sales Invoice <a href="/app/sales-invoice/{0}" target="_blank">{0}</a> was created successfully.', [response.message]),
//                                 indicator: 'green'
//                             });
//                         } else {
//                             frappe.msgprint(__('Failed to create Sales Invoice.'));
//                         }
//                     }
//                 });
//             }).css('background-color', 'black').css('color', 'white');
//         }

//         // If the Sales Invoice has already been created, show the "View Sales Invoice" button
//         if (frm.doc.custom_spare_parts_sales_invoice) {
//             frm.add_custom_button(__('View Sales Invoice'), function() {
//                 frappe.set_route('Form', 'Sales Invoice', frm.doc.custom_spare_parts_sales_invoice);
//             }).css('background-color', 'black').css('color', 'white');
//         }
//     }
// });

frappe.ui.form.on('Maintenance Visit', {
    refresh: function(frm) {
        // Remove any buttons and messages if there are no spare parts
        if (!frm.doc.spare_parts || frm.doc.spare_parts.length === 0) {
            return; // No spare parts, do nothing
        }

        // If spare parts exist but no Sales Invoice has been created, show the "Create Sales Invoice" button
        if (frm.doc.spare_parts && frm.doc.spare_parts.length > 0 && !frm.doc.custom_spare_parts_sales_invoice) {
            frm.add_custom_button(__('Create Sales Invoice'), function() {
                frappe.call({
                    method: 'aquasoft.custom_scripts.create_sales_invoice_from_visit.create_sales_invoice',
                    args: {
                        maintenance_visit_name: frm.doc.name
                    },
                    callback: function(response) {
                        if (response.message) {
                            frm.set_value('custom_spare_parts_sales_invoice', response.message);
                            frm.set_value('custom_parts_sales_invoice_created', 1);
                            frm.save_or_update();
                            frappe.msgprint({
                                title: __('Sales Invoice Created'),
                                message: __('A Sales Invoice <a href="/app/sales-invoice/{0}" target="_blank">{0}</a> was created successfully.', [response.message]),
                                indicator: 'green'
                            });
                        } else {
                            frappe.msgprint(__('Failed to create Sales Invoice.'));
                        }
                    }
                });
            }).css('background-color', 'black').css('color', 'white');
        }

        // If the Sales Invoice has already been created, show the "View Sales Invoice" button
        if (frm.doc.custom_spare_parts_sales_invoice) {
            frm.add_custom_button(__('View Sales Invoice'), function() {
                frappe.set_route('Form', 'Sales Invoice', frm.doc.custom_spare_parts_sales_invoice);
            }).css('background-color', 'black').css('color', 'white');
        }
    },

    after_save: function(frm) {
        if (frm.doc.spare_parts && frm.doc.spare_parts.length > 0 && frm.doc.custom_spare_parts_sales_invoice) {
            // If the spare parts were modified and Sales Invoice already exists, update the Sales Invoice
            frappe.call({
                method: 'aquasoft.custom_scripts.create_sales_invoice_from_visit.update_sales_invoice',
                args: {
                    maintenance_visit_name: frm.doc.name,
                    sales_invoice_name: frm.doc.custom_spare_parts_sales_invoice
                },
                callback: function(response) {
                    if (response.message) {
                        frappe.msgprint({
                            title: __('Sales Invoice Updated'),
                            message: __('The existing Sales Invoice <a href="/app/sales-invoice/{0}" target="_blank">{0}</a> has been updated.', [response.message]),
                            indicator: 'green'
                        });
                    } else {
                        frappe.msgprint(__('Failed to update Sales Invoice.'));
                    }
                }
            });
        }
    },

    // before_cancel: function(frm) {
    //     if (frm.doc.custom_spare_parts_sales_invoice) {
    //         frappe.call({
    //             method: 'aquasoft.custom_scripts.create_sales_invoice_from_visit.cancel_sales_invoice',
    //             args: {
    //                 sales_invoice_name: frm.doc.custom_spare_parts_sales_invoice
    //             },
    //             callback: function(response) {
    //                 if (response.message) {
    //                     frappe.msgprint({
    //                         title: __('Sales Invoice Canceled'),
    //                         message: __('The associated Sales Invoice {0} has been canceled.', [frm.doc.custom_spare_parts_sales_invoice]),
    //                         indicator: 'red'
    //                     });
    //                 }
    //             }
    //         });
    //     }
    // }
});

// print msg for sale invoice
frappe.ui.form.on('Maintenance Visit', {
    after_save: function(frm) {
        // Check if there are spare parts in the Maintenance Visit
        if (frm.doc.spare_parts && frm.doc.spare_parts.length > 0) {
            // Show a custom message after saving
            frappe.msgprint({
                title: __('Attention'),
                message: __('This Maintenance Visit contains spare parts. Please create a <b>Sales Invoice</b> for the spare parts if you have not done so already.'),
                indicator: 'orange'
            });
        }
    }
});