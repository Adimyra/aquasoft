# import frappe

# @frappe.whitelist()
# def create_first_visit_schedule(doc, *args, **kwargs):
#     doc = frappe.get_doc(frappe.parse_json(doc))  # Parse the doc passed from client-side
    
#     if doc.docstatus == 1 and doc.subscription:
#         subscription_doc = frappe.get_doc("Subscription", doc.subscription)
#         if subscription_doc.first_visit == 'Due':
#             maintenance_items = [
#                 {
#                     'item_code': item.item_code,
#                     'item_name': item.item_name,
#                     'start_date': doc.posting_date,
#                     'periodicity': 'Random',
#                     'no_of_visits': 1,
#                     'end_date': frappe.utils.add_days(doc.posting_date, 1)
#                 } for item in doc.items
#             ]
#             maintenance_schedule_doc = {
#                 'doctype': 'Maintenance Schedule',
#                 'customer': doc.customer,
#                 'customer_name': doc.customer_name,
#                 'customer_address': doc.customer_address,
#                 'address_display': doc.address_display,
#                 'territory': doc.territory,
#                 'customer_group': doc.customer_group,
#                 'transaction_date': doc.posting_date,
#                 'sales_invoice': doc.name,
#                 'visit_type': 'AMC',
#                 'subscription': doc.subscription,
#                 'items': maintenance_items
#             }
#             maintenance_schedule = frappe.get_doc(maintenance_schedule_doc)
#             maintenance_schedule.insert()
#             maintenance_schedule.submit()
#             frappe.msgprint(f"First Visit Maintenance Schedule {maintenance_schedule.name} created and submitted successfully for tomorrow because the first visit status was 'Due'.")