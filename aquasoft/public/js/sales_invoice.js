// frappe.ui.form.on('Sales Invoice', {
//     on_submit: function(frm) {
//         if (frm.doc.subscription) {
//             frappe.call({
//                 method: 'frappe.client.get',
//                 args: {
//                     doctype: 'Subscription',
//                     name: frm.doc.subscription
//                 },
//                 callback: function(response) {
//                     let subscription_doc = response.message;
//                     if (subscription_doc && subscription_doc.first_visit === 'Due') {
//                         frappe.msgprint({
//                             title: __('First Visit Maintenance Schedule Required'),
//                             indicator: 'orange',
//                             message: __('The First Visit is due. Please create a Maintenance Schedule for the First Visit.')
//                         });
//                     } else {
//                         frappe.msgprint({
//                             title: __('Sales Invoice Submitted'),
//                             indicator: 'green',
//                             message: __('Sales Invoice has been successfully submitted.')
//                         });
//                     }
//                 }
//             });
//         }
//     }
// });