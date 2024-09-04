import frappe

@frappe.whitelist()
def create_maintenance_schedule(doc, method=None):
    doc = frappe.get_doc(frappe.parse_json(doc)) if isinstance(doc, str) else doc  # Handle both JSON strings and document objects

    if doc.docstatus == 1:
        visit_type = 'AMC' if doc.subscription else 'Warranty'

        # Filter items to include only those with item_group 'Water Purifier'
        maintenance_items = [
            {
                'item_code': item.item_code,
                'item_name': item.item_name,
                'start_date': doc.posting_date,
                'periodicity': 'Quarterly',
                'no_of_visits': 3,
                'end_date': frappe.utils.add_days(doc.posting_date, 274)
            } for item in doc.items if frappe.db.get_value('Item', item.item_code, 'item_group') == 'Water Purifier'
        ]

        # Only proceed if all items are from 'Water Purifier' and no other item groups are present
        all_items_are_water_purifiers = all(frappe.db.get_value('Item', item.item_code, 'item_group') == 'Water Purifier' for item in doc.items)

        if all_items_are_water_purifiers and maintenance_items:
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
                'visit_type': visit_type,
                'items': maintenance_items
            }
            if visit_type == 'AMC':
                maintenance_schedule_doc['subscription'] = doc.subscription
            
            # Insert and submit the Maintenance Schedule
            maintenance_schedule = frappe.get_doc(maintenance_schedule_doc)
            maintenance_schedule.insert()
            maintenance_schedule.submit()
            frappe.msgprint(f"{visit_type} Maintenance Schedule {maintenance_schedule.name} created and submitted successfully.")
        else:
            frappe.msgprint("Maintenance Schedule not created. All items must belong to the 'Water Purifier' group.")

# import frappe

# @frappe.whitelist()
# def create_maintenance_schedule(doc, method=None):
#     doc = frappe.get_doc(frappe.parse_json(doc)) if isinstance(doc, str) else doc  # Handle both JSON strings and document objects

#     if doc.docstatus == 1:
#         visit_type = 'AMC' if doc.subscription else 'Warranty'

#         # Filter items to exclude those with item_group 'Spare Part'
#         maintenance_items = [
#             {
#                 'item_code': item.item_code,
#                 'item_name': item.item_name,
#                 'start_date': doc.posting_date,
#                 'periodicity': 'Quarterly',
#                 'no_of_visits': 3,
#                 'end_date': frappe.utils.add_days(doc.posting_date, 274)
#             } for item in doc.items if frappe.db.get_value('Item', item.item_code, 'item_group') not in ['Spare Part', 'Services']
#         ]

#         # Only proceed if there are items eligible for the maintenance schedule
#         if maintenance_items:
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
#                 'visit_type': visit_type,
#                 'items': maintenance_items
#             }
#             if visit_type == 'AMC':
#                 maintenance_schedule_doc['subscription'] = doc.subscription
            
#             # Insert and submit the Maintenance Schedule
#             maintenance_schedule = frappe.get_doc(maintenance_schedule_doc)
#             maintenance_schedule.insert()
#             maintenance_schedule.submit()
#             frappe.msgprint(f"{visit_type} Maintenance Schedule {maintenance_schedule.name} created and submitted successfully.")
#         else:
#             frappe.msgprint("No eligible items for maintenance schedule creation.")