// frappe.ui.form.on('Subscription', {
//     first_visit: function(frm) {
//         frm.toggle_display('technician', frm.doc.first_visit !== 'Due');
//         frm.toggle_display('work_done', frm.doc.first_visit !== 'Due');
//     },
//     customer: function(frm) {
//         set_party_field(frm);
//     },
//     refresh: function(frm) {
//         // Ensure fields are shown/hidden on form load/refresh
//         frm.trigger('first_visit');
//     }
// });

// function set_party_field(frm) {
//     if (frm.doc.customer) {
//         frm.set_value('party', frm.doc.customer);
//     }
// }

frappe.ui.form.on('Subscription', {
    first_visit: function(frm) {
        frm.toggle_display('technician', frm.doc.first_visit !== 'Due');
        frm.toggle_display('work_done', frm.doc.first_visit !== 'Due');
    },
    customer: function(frm) {
        // Clear the serial_no field when the customer is changed
        frm.set_value('serial_no', null);
        set_party_field(frm);
        check_customer_type_and_serial_no(frm);
    },
    refresh: function(frm) {
        // Ensure fields are shown/hidden on form load/refresh
        frm.trigger('first_visit');
    }
});

function set_party_field(frm) {
    if (frm.doc.customer) {
        frm.set_value('party', frm.doc.customer);
    }
}

function check_customer_type_and_serial_no(frm) {
    // Check if the customer has serial numbers
    frappe.call({
        method: 'frappe.client.get_list',
        args: {
            doctype: 'Serial No',
            filters: {
                cust_id: frm.doc.customer
            },
            fields: ['name', 'serial_no']
        },
        callback: function(response) {
            if (response.message && response.message.length > 0) {
                let options = response.message.map(function(d) {
                    return { 'label': d.serial_no, 'value': d.serial_no };
                });
                frm.set_df_property('serial_no', 'options', options);
                frm.set_value('customer_type', 'Existing Customer');
                frm.set_df_property('machine_name', 'reqd', 0);
                frm.set_df_property('serial_no', 'reqd', 1);  // Make serial_no mandatory for existing customers
            } else {
                // If no serial numbers are found, check if the customer is in the Other Customer AMC doctype
                frappe.call({
                    method: 'frappe.client.get_list',
                    args: {
                        doctype: 'Other Customer AMC',
                        filters: {
                            customer: frm.doc.customer
                        },
                        fields: ['name']
                    },
                    callback: function(oc_response) {
                        if (oc_response.message && oc_response.message.length > 0) {
                            frm.set_value('customer_type', 'Other Customer');
                            frm.set_df_property('machine_name', 'reqd', 1);
                            frm.set_df_property('serial_no', 'reqd', 0);  // Remove mandatory requirement for serial_no
                        } else {
                            // If no records are found in either Serial No or Other Customer AMC
                            frm.set_value('customer_type', 'Other Customer');
                            frm.set_df_property('machine_name', 'reqd', 1);
                            frm.set_df_property('serial_no', 'reqd', 0);  // Remove mandatory requirement for serial_no
                            frappe.msgprint(__('No records found for this customer in Serial No or Other Customer AMC.'));
                        }
                    }
                });
            }
        }
    });
}
//2nd condition

// frappe.ui.form.on('Subscription', {
//     after_save: function(frm) {
//         frappe.msgprint({
//             title: __('AMC Saved'),
//             indicator: 'green',
//             message: __('Fetch Subscription Updates<br> from >> <b>Action</b> Menu')
//         })
//     }
// });
// -----------------------------------------
// create sales invoice button using this

frappe.ui.form.on('Subscription', {
    refresh: function(frm) {
        // Check if spare parts exist in the Subscription document
        if (!frm.is_new() && frm.doc.spare_parts && frm.doc.spare_parts.length > 0) {
            if (!frm.doc.amc_spare_parts_sales_invoice) {
                // Show "Create Sales Invoice" button if Sales Invoice is not created
                frm.add_custom_button(__('Create Sales Invoice'), function() {
                    // Call server-side method to create Sales Invoice
                    frappe.call({
                        method: 'aquasoft.custom_scripts.create_sales_invoice_from_subscription.create_sales_invoice',
                        args: {
                            subscription_name: frm.doc.name  // Pass the current subscription document name
                        },
                        callback: function(response) {
                            if (response.message) {
                                // Set the Sales Invoice number and save the form
                                frm.set_value('amc_spare_parts_sales_invoice', response.message);
                                frm.save();

                                // Show success message with a link to Sales Invoice
                                frappe.msgprint({
                                    title: __('Sales Invoice Created'),
                                    message: __('A Sales Invoice <a href="/app/sales-invoice/{0}" target="_blank">{0}</a> was created successfully.', [response.message]),
                                    indicator: 'green'
                                });

                                // Refresh the form to show the "View Sales Invoice" button
                                frm.refresh();
                            } else {
                                frappe.msgprint(__('Failed to create Sales Invoice.'));
                            }
                        }
                    });
                }).css('background-color', 'black').css('color', 'white');
            } else {
                // Show "View Sales Invoice" button if Sales Invoice is already created
                frm.add_custom_button(__('View Sales Invoice'), function() {
                    frappe.set_route('Form', 'Sales Invoice', frm.doc.amc_spare_parts_sales_invoice);
                }).css('background-color', 'black').css('color', 'white');
            }
        }
    }
});



// ----------------------------------------------
// filter item group in child table

frappe.ui.form.on('Subscription', {
    refresh: function(frm) {
        // Set filters for the spare parts item table to show only items in the 'Spare Part' group
        frm.fields_dict['spare_parts'].grid.get_field('item_code').get_query = function() {
            return {
                filters: {
                    item_group: 'Spare Part'
                }
            };
        };
    },
    
    is_spare_parts_changed_or_replaced: function(frm) {
        if (frm.doc.is_spare_parts_changed_or_replaced) {
            // Show a short, attentional message when the checkbox is checked
            frappe.msgprint({
                title: __('Reminder'),
                message: __('Spare parts have been changed or replaced. Don\'t forget to create a <b>Sales Invoice</b> for them separately.'),
                indicator: 'orange'
            });
        }
    }
});