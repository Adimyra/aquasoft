# import frappe
# from frappe.utils import nowtime

# def create_maintenance_action_on_submit(doc, method):
#     if doc.subscription:
#         subscription_doc = frappe.get_doc("Subscription", doc.subscription)
        
#         if subscription_doc.first_visit == 'Due':
#             # Create a Maintenance Schedule for the first visit
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
        
#         else:
#             # Create a Maintenance Visit if the first visit is not 'Due'
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
#             frappe.msgprint(f"AMC Maintenance Visit {maintenance_visit.name} created and submitted successfully.")


import frappe
from frappe.utils import nowtime

def create_maintenance_action_on_submit(doc, method):
    if doc.subscription:
        subscription_doc = frappe.get_doc("Subscription", doc.subscription)
        
        # Check if all items belong to the 'Water Purifier' group
        all_items_are_water_purifiers = all(frappe.db.get_value('Item', item.item_code, 'item_group') == 'Water Purifier' for item in doc.items)
        
        if not all_items_are_water_purifiers:
            # frappe.msgprint("Maintenance Schedule not created. All items must belong to the 'Water Purifier' group.")
            frappe.msgprint("Maintenance Schedule not created")

        else:
            if subscription_doc.first_visit == 'Due':
                # Create a Maintenance Schedule for the first visit
                maintenance_items = [
                    {
                        'item_code': item.item_code,
                        'item_name': item.item_name,
                        'start_date': doc.posting_date,
                        'periodicity': 'Random',
                        'no_of_visits': 1,
                        'end_date': frappe.utils.add_days(doc.posting_date, 1)
                    } for item in doc.items
                ]
                maintenance_schedule_doc = {
                    'doctype': 'Maintenance Schedule',
                    'customer': doc.customer,
                    'customer_name': doc.customer_name,
                    'customer_address': doc.customer_address,
                    'address_display': doc.address_display,
                    'territory': doc.territory,
                    'customer_group': doc.customer_group,
                    'transaction_date': doc.posting_date,
                    'sales_invoice': doc.name,
                    'visit_type': 'AMC',
                    'subscription': doc.subscription,
                    'items': maintenance_items
                }
                maintenance_schedule = frappe.get_doc(maintenance_schedule_doc)
                maintenance_schedule.insert()
                maintenance_schedule.submit()
                frappe.msgprint(f"First Visit Maintenance Schedule {maintenance_schedule.name} created and submitted successfully for tomorrow because the first visit status was 'Due'.")
            
            elif subscription_doc.first_visit in ['Fully Completed', 'Partially Completed']:
                # Create a Maintenance Visit if the first visit is either 'Fully Completed' or 'Partially Completed'
                maintenance_visit = frappe.get_doc({
                    "doctype": "Maintenance Visit",
                    "customer": doc.customer,
                    "customer_name": doc.customer_name,
                    "customer_address": doc.customer_address,
                    "address_display": doc.address_display,
                    "territory": doc.territory,
                    "customer_group": doc.customer_group,
                    "mntc_date": doc.posting_date,
                    "mntc_time": nowtime(),
                    "visit_type": "AMC",
                    "repeat_visit": "No",
                    "completion_status": subscription_doc.first_visit,
                    "maintenance_type": "Scheduled",
                    "status": "Draft",
                    "company": doc.company,
                    "sales_invoice": doc.name,
                    "subscription": doc.subscription,
                    "purposes": [
                        {
                            "item_code": item.item_code,
                            "item_name": frappe.db.get_value("Item", item.item_code, "item_name"),
                            "service_person": subscription_doc.technician,
                            "work_done": subscription_doc.work_done,
                            "description": item.description
                        } for item in doc.items
                    ]
                })
                maintenance_visit.insert()
                maintenance_visit.submit()
                frappe.msgprint(f"AMC Maintenance Visit {maintenance_visit.name} created and submitted successfully.")