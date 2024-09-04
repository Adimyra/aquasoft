# import frappe
# from frappe.model.document import Document

# def create_maintenance_schedule_on_technician_update(doc, method):
#     if doc.technician:
#         # Check if a Maintenance Schedule has already been created for this issue
#         existing_schedule = frappe.db.exists('Maintenance Schedule', {'issue': doc.name})
#         if existing_schedule:
#             frappe.msgprint(f'A Maintenance Schedule has already been created for this issue: {doc.name}', alert=True)
#             return

#         # Determine the item to use based on the issue type
#         if doc.issue_type == 'AMC Complaint':
#             item_code = doc.amc_item
#             item_name = doc.amc_item
#         elif doc.issue_type == 'Warranty Complaint':
#             item_code = doc.warranty_item
#             item_name = doc.warranty_item
#         elif doc.issue_type == 'Paid':
#             item_code = 'PV001'  # Fixed item code for Paid issues
#             item_name = 'PV001'
#         else:
#             frappe.msgprint('Maintenance Schedule not created. Unsupported issue type.', alert=True)
#             return  # Do not create a schedule for unsupported issue types

#         maintenance_items = [
#             {
#                 'item_code': item_code,
#                 'item_name': item_name,
#                 'start_date': doc.opening_date,
#                 'periodicity': 'Random',
#                 'no_of_visits': 1,
#                 'end_date': frappe.utils.add_days(doc.opening_date, 1),
#                 'sales_person': doc.technician
#             }
#         ]
#         maintenance_schedule_doc = {
#             'doctype': 'Maintenance Schedule',
#             'customer': doc.customer,
#             'customer_name': doc.customer_name,
#             'transaction_date': doc.opening_date,
#             'visit_type': 'Paid' if doc.issue_type == 'Paid' else doc.issue_type,
#             'issue': doc.name,
#             'items': maintenance_items,
#             'technician': doc.technician
#         }

#         # Insert and submit the Maintenance Schedule
#         maintenance_schedule = frappe.get_doc(maintenance_schedule_doc)
#         maintenance_schedule.insert()
#         maintenance_schedule.submit()
#         frappe.msgprint(f'Maintenance Schedule {maintenance_schedule.name} created successfully.')

#         # Update the Issue status to "Forwarded to Technician"
#         doc.db_set('status', 'Forwarded to Technician')

#         # Organized message with technician's name
#         frappe.msgprint(
#             f'<b>Issue Forwarded to Technician:</b> {doc.technician}<br>'
#             f'<b>Status Updated:</b> Forwarded to Technician'
#         )


###2nd

# import frappe
# from frappe.model.document import Document

# def create_maintenance_schedule_on_technician_update(doc, method):
#     if doc.technician:
#         # Check if a Maintenance Schedule has already been created for this issue
#         existing_schedule = frappe.db.exists('Maintenance Schedule', {'issue': doc.name})
#         if existing_schedule:
#             frappe.msgprint(f'A Maintenance Schedule has already been created for this issue: {doc.name}', alert=True)
#             return

#         # Determine the item to use based on the issue type
#         if doc.issue_type == 'AMC Complaint':
#             item_code = doc.amc_item
#             item_name = doc.amc_item
#         elif doc.issue_type == 'Warranty Complaint':
#             item_code = doc.warranty_item
#             item_name = doc.warranty_item
#         elif doc.issue_type == 'Paid Visit':
#             # Create a Sales Invoice instead of a Maintenance Schedule for "Paid Visit"
#             create_sales_invoice_for_paid_visit(doc)
#             return
#         else:
#             frappe.msgprint('Maintenance Schedule not created. Unsupported issue type.', alert=True)
#             return  # Do not create a schedule for unsupported issue types

#         maintenance_items = [
#             {
#                 'item_code': item_code,
#                 'item_name': item_name,
#                 'start_date': doc.opening_date,
#                 'periodicity': 'Random',
#                 'no_of_visits': 1,
#                 'end_date': frappe.utils.add_days(doc.opening_date, 1),
#                 'sales_person': doc.technician
#             }
#         ]
#         maintenance_schedule_doc = {
#             'doctype': 'Maintenance Schedule',
#             'customer': doc.customer,
#             'customer_name': doc.customer_name,
#             'transaction_date': doc.opening_date,
#             'visit_type': doc.issue_type,
#             'issue': doc.name,
#             'items': maintenance_items,
#             'technician': doc.technician
#         }

#         # Insert and submit the Maintenance Schedule
#         maintenance_schedule = frappe.get_doc(maintenance_schedule_doc)
#         maintenance_schedule.insert()
#         maintenance_schedule.submit()
#         frappe.msgprint(f'Maintenance Schedule {maintenance_schedule.name} created successfully.')

#         # Update the Issue status to "Forwarded to Technician"
#         doc.db_set('status', 'Forwarded to Technician')

#         # Organized message with technician's name
#         frappe.msgprint(
#             f'<b>Issue Forwarded to Technician:</b> {doc.technician}<br>'
#             f'<b>Status Updated:</b> Forwarded to Technician'
#         )

# def create_sales_invoice_for_paid_visit(doc):
#     # Check if a Sales Invoice is already linked to this issue
#     existing_invoice = frappe.db.exists('Sales Invoice', {'custom_issue': doc.name})
#     if existing_invoice:
#         frappe.msgprint(f'A Sales Invoice has already been created for this issue: {existing_invoice}', alert=True)
#         return

#     sales_invoice_doc = {
#         'doctype': 'Sales Invoice',
#         'customer': doc.customer,
#         'posting_date': frappe.utils.today(),
#         'due_date': frappe.utils.add_days(frappe.utils.today(), 30),
#         'custom_issue': doc.name,  # Link the issue to the Sales Invoice
#         'items': [
#             {
#                 'item_code': 'PV001',
#                 'qty': 1,
#                 'description': f'Service charge for {doc.issue_type}'
#             }
#         ]
#     }

#     # Insert and submit the Sales Invoice
#     sales_invoice = frappe.get_doc(sales_invoice_doc)
#     sales_invoice.insert()
#     sales_invoice.submit()
#     frappe.msgprint(f'Sales Invoice {sales_invoice.name} created successfully.')

#     # Update the Issue with the Sales Invoice ID
#     doc.db_set('sales_invoice', sales_invoice.name)

#     # Redirect to the Sales Invoice
#     frappe.msgprint(f'<a href="/app/sales-invoice/{sales_invoice.name}" target="_blank">View Sales Invoice {sales_invoice.name}</a>')



#3nd one

import frappe
from frappe.model.document import Document

def create_maintenance_schedule_on_technician_update(doc, method):
    if doc.technician:
        # Check if a Maintenance Schedule has already been created for this issue
        existing_schedule = frappe.db.exists('Maintenance Schedule', {'issue': doc.name})
        if existing_schedule:
            frappe.msgprint(f'A Maintenance Schedule has already been created for this issue: {doc.name}', alert=True)
            return

        # If issue type is 'Paid Visit' but Sales Invoice not created, create Sales Invoice first
        if doc.issue_type == 'Paid Visit':
            if not doc.sales_invoice:  # Check if Sales Invoice is already linked
                create_sales_invoice_for_paid_visit(doc)
                # Check again if the Sales Invoice is created before proceeding
                if not doc.sales_invoice:
                    frappe.msgprint('Failed to create Sales Invoice. Maintenance Schedule will not be created.', alert=True)
                    return
        
        # Now create Maintenance Schedule after Sales Invoice is done for 'Paid Visit'
        if doc.issue_type in ['AMC Complaint', 'Warranty Complaint', 'Paid Visit']:
            if doc.issue_type == 'AMC Complaint':
                item_code = doc.amc_item
                item_name = doc.amc_item
            elif doc.issue_type == 'Warranty Complaint':
                item_code = doc.warranty_item
                item_name = doc.warranty_item
            elif doc.issue_type == 'Paid Visit':
                item_code = 'PV001'
                item_name = 'Service Charge'  # You can adjust this as needed

            maintenance_items = [
                {
                    'item_code': item_code,
                    'item_name': item_name,
                    'start_date': doc.opening_date,
                    'periodicity': 'Random',
                    'no_of_visits': 1,
                    'end_date': frappe.utils.add_days(doc.opening_date, 1),
                    'sales_person': doc.technician
                }
            ]
            maintenance_schedule_doc = {
                'doctype': 'Maintenance Schedule',
                'customer': doc.customer,
                'customer_name': doc.customer_name,
                'transaction_date': doc.opening_date,
                'visit_type': doc.issue_type,
                'issue': doc.name,
                'items': maintenance_items,
                'technician': doc.technician
            }

            # Insert and submit the Maintenance Schedule
            maintenance_schedule = frappe.get_doc(maintenance_schedule_doc)
            maintenance_schedule.insert()
            maintenance_schedule.submit()
            frappe.msgprint(f'Maintenance Schedule {maintenance_schedule.name} created successfully.')

            # Update the Issue status to "Forwarded to Technician"
            doc.db_set('status', 'Forwarded to Technician')

            # Organized message with technician's name
            frappe.msgprint(
                f'<b>Issue Forwarded to Technician:</b> {doc.technician}<br>'
                f'<b>Status Updated:</b> Forwarded to Technician'
            )
        else:
            frappe.msgprint('Maintenance Schedule not created. Unsupported issue type.', alert=True)
            return

def create_sales_invoice_for_paid_visit(doc):
    # Check if a Sales Invoice is already linked to this issue
    existing_invoice = frappe.db.exists('Sales Invoice', {'custom_issue': doc.name})
    if existing_invoice:
        frappe.msgprint(f'A Sales Invoice has already been created for this issue: {existing_invoice}', alert=True)
        return

    sales_invoice_doc = {
        'doctype': 'Sales Invoice',
        'customer': doc.customer,
        'posting_date': frappe.utils.today(),
        'due_date': frappe.utils.add_days(frappe.utils.today(), 30),
        'custom_issue': doc.name,  # Link the issue to the Sales Invoice
        'items': [
            {
                'item_code': 'PV001',
                'qty': 1,
                'rate': 1000,  # Example rate; adjust as necessary
                'description': f'Service charge for {doc.issue_type}'
            }
        ]
    }

    # Insert and submit the Sales Invoice
    sales_invoice = frappe.get_doc(sales_invoice_doc)
    sales_invoice.insert()
    sales_invoice.submit()
    frappe.msgprint(f'Sales Invoice {sales_invoice.name} created successfully.')

    # Update the Issue with the Sales Invoice ID
    doc.db_set('sales_invoice', sales_invoice.name)

    # Redirect to the Sales Invoice
    frappe.msgprint(f'<a href="/app/sales-invoice/{sales_invoice.name}" target="_blank">View Sales Invoice {sales_invoice.name}</a>')