import frappe
from frappe.utils import add_days

@frappe.whitelist()
def create_sales_invoice(maintenance_visit_name):
    maintenance_visit = frappe.get_doc('Maintenance Visit', maintenance_visit_name)

    if maintenance_visit.spare_parts:
        invoice_items = []
        for spare in maintenance_visit.spare_parts:
            discount_percentage = 0
            description = ""

            # Check item status and apply discount accordingly
            if spare.item_status == "Under AMC":
                discount_percentage = 100
                description = "Item covered under AMC"
            elif spare.item_status == "Under Warranty":
                discount_percentage = 100
                description = "Item covered under Warranty"
            else:
                discount_percentage = 0
                description = "Paid Item"

            invoice_items.append({
                'item_code': spare.item_code,
                'item_name': spare.item_name,
                'qty': spare.qty,
                'warehouse': maintenance_visit.warehouse,  # Ensure warehouse is set from the maintenance visit
                'discount_percentage': discount_percentage,
                'description': description  # Add description for the discount reason
            })

        # Set the posting date to the maintenance visit date
        posting_date = maintenance_visit.mntc_date
        
        # Calculate due date (30 days from posting date)
        due_date = add_days(posting_date, 30)

        # Create Sales Invoice document with set_posting_time enabled
        sales_invoice = frappe.get_doc({
            'doctype': 'Sales Invoice',
            'customer': maintenance_visit.customer,
            'customer_name': maintenance_visit.customer_name,
            'posting_date': posting_date,  # Use maintenance visit date as posting date
            'due_date': due_date,  # Set due date 30 days after posting date
            'items': invoice_items,
            'company': maintenance_visit.company,
            'update_stock': 1,  # Ensure stock is updated
            'set_warehouse': maintenance_visit.warehouse,  # Set warehouse globally
            'set_posting_time': 1  # Enable posting time to allow posting date change
        })
        sales_invoice.insert()
        frappe.db.commit()

        return sales_invoice.name

    return None

@frappe.whitelist()
def update_sales_invoice(maintenance_visit_name, sales_invoice_name):
    maintenance_visit = frappe.get_doc('Maintenance Visit', maintenance_visit_name)
    sales_invoice = frappe.get_doc('Sales Invoice', sales_invoice_name)

    # Clear existing items in the Sales Invoice and add the updated ones
    sales_invoice.items = []
    for spare in maintenance_visit.spare_parts:
        discount_percentage = 0
        description = ""

        # Check item status and apply discount accordingly
        if spare.item_status == "Under AMC":
            discount_percentage = 100
            description = "Item covered under AMC"
        elif spare.item_status == "Under Warranty":
            discount_percentage = 100
            description = "Item covered under Warranty"
        else:
            discount_percentage = 0
            description = "Paid Item"

        sales_invoice.append('items', {
            'item_code': spare.item_code,
            'item_name': spare.item_name,
            'qty': spare.qty,
            'warehouse': maintenance_visit.warehouse,  # Ensure warehouse is set from the maintenance visit
            'discount_percentage': discount_percentage,
            'description': description  # Add description for the discount reason
        })

    # Update posting date and due date in the updated Sales Invoice
    sales_invoice.posting_date = maintenance_visit.mntc_date
    sales_invoice.due_date = add_days(maintenance_visit.mntc_date, 30)

    # Enable posting time to allow posting date change
    sales_invoice.set_posting_time = 1

    # Save and commit the updated Sales Invoice
    sales_invoice.save()
    frappe.db.commit()

    return sales_invoice.name
# import frappe

# @frappe.whitelist()
# def create_sales_invoice(maintenance_visit_name):
#     maintenance_visit = frappe.get_doc('Maintenance Visit', maintenance_visit_name)

#     if maintenance_visit.spare_parts:
#         invoice_items = []
#         for spare in maintenance_visit.spare_parts:
#             invoice_items.append({
#                 'item_code': spare.item_code,
#                 'item_name': spare.item_name,
#                 'qty': spare.qty,
#                 'warehouse': maintenance_visit.warehouse  # Ensure warehouse is set from the maintenance visit
#             })

#         sales_invoice = frappe.get_doc({
#             'doctype': 'Sales Invoice',
#             'customer': maintenance_visit.customer,
#             'customer_name': maintenance_visit.customer_name,
#             'posting_date': maintenance_visit.mntc_date,
#             'items': invoice_items,
#             'company': maintenance_visit.company,
#             'update_stock': 1,  # Ensure stock is updated
#             'set_warehouse': maintenance_visit.warehouse  # Set warehouse globally
#         })
#         sales_invoice.insert()
#         frappe.db.commit()

#         return sales_invoice.name

#     return None

# @frappe.whitelist()
# def update_sales_invoice(maintenance_visit_name, sales_invoice_name):
#     maintenance_visit = frappe.get_doc('Maintenance Visit', maintenance_visit_name)
#     sales_invoice = frappe.get_doc('Sales Invoice', sales_invoice_name)

#     # Clear existing items in the Sales Invoice and add the updated ones
#     sales_invoice.items = []
#     for spare in maintenance_visit.spare_parts:
#         sales_invoice.append('items', {
#             'item_code': spare.item_code,
#             'item_name': spare.item_name,
#             'qty': spare.qty,
#             'warehouse': maintenance_visit.warehouse  # Ensure warehouse is set from the maintenance visit
#         })

#     sales_invoice.save()
#     frappe.db.commit()

#     return sales_invoice.name

# @frappe.whitelist()
# def cancel_sales_invoice(sales_invoice_name):
#     try:
#         sales_invoice = frappe.get_doc('Sales Invoice', sales_invoice_name)
#         if sales_invoice.docstatus == 1:  # Only cancel if the Sales Invoice is submitted
#             sales_invoice.cancel()
#             frappe.msgprint(f'Sales Invoice {sales_invoice_name} has been canceled.')
#         else:
#             frappe.msgprint(f'Sales Invoice {sales_invoice_name} is not submitted, so it cannot be canceled.')
#     except Exception as e:
#         frappe.msgprint(f'Failed to cancel Sales Invoice {sales_invoice_name}: {str(e)}')