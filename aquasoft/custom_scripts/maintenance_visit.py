# import frappe
# from frappe.utils import nowtime

# def create_maintenance_visit_on_submit(doc, method):
#     if doc.subscription:
#         subscription_doc = frappe.get_doc("Subscription", doc.subscription)
#         if subscription_doc.first_visit != 'Due':
#             maintenance_visit = frappe.get_doc({
#                 "doctype": "Maintenance Visit",
#                 "customer": doc.customer,
#                 "customer_name": doc.customer_name,
#                 "customer_address": doc.customer_address,
#                 "address_display": doc.address_display,
#                 "territory": doc.territory,
#                 "customer_group": doc.customer_group,
#                 "mntc_date": doc.posting_date,
#                 "mntc_time": nowtime(),
#                 "visit_type": "AMC",
#                 "repeat_visit": "No",
#                 "completion_status": subscription_doc.first_visit,
#                 "maintenance_type": "Scheduled",
#                 "status": "Draft",
#                 "company": doc.company,
#                 "sales_invoice": doc.name,
#                 "subscription": doc.subscription,
#                 "purposes": [
#                     {
#                         "item_code": item.item_code,
#                         "item_name": frappe.db.get_value("Item", item.item_code, "item_name"),
#                         "service_person": subscription_doc.technician,
#                         "work_done": subscription_doc.work_done,
#                         "description": item.description
#                     } for item in doc.items
#                 ]
#             })
#             maintenance_visit.insert()
#             maintenance_visit.submit()
#             frappe.msgprint(f"AMC Maintenance Visit {maintenance_visit.name} created and submitted successfully")

# import frappe
# from frappe.utils import nowtime

# def create_maintenance_visit_on_submit(doc, method):
#     if doc.subscription:
#         subscription_doc = frappe.get_doc("Subscription", doc.subscription)
#         if subscription_doc.first_visit != 'Due':
#             maintenance_visit = frappe.get_doc({
#                 "doctype": "Maintenance Visit",
#                 "customer": doc.customer,
#                 "customer_name": doc.customer_name,
#                 "customer_address": doc.customer_address,
#                 "address_display": doc.address_display,
#                 "territory": doc.territory,
#                 "customer_group": doc.customer_group,
#                 "mntc_date": doc.posting_date,
#                 "mntc_time": nowtime(),
#                 "visit_type": "AMC",
#                 "repeat_visit": "No",
#                 "completion_status": subscription_doc.first_visit,
#                 "maintenance_type": "Scheduled",
#                 "status": "Draft",
#                 "company": doc.company,
#                 "sales_invoice": doc.name,
#                 "subscription": doc.subscription,
#                 "purposes": [
#                     {
#                         "item_code": item.item_code,
#                         "item_name": frappe.db.get_value("Item", item.item_code, "item_name"),
#                         "service_person": subscription_doc.technician,
#                         "work_done": subscription_doc.work_done,
#                         "description": item.description
#                     } for item in doc.items
#                 ]
#             })
#             maintenance_visit.insert()
#             maintenance_visit.submit()
#             frappe.msgprint(f"AMC Maintenance Visit {maintenance_visit.name} created and submitted successfully")



