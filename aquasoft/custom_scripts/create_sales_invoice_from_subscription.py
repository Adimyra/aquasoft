# import frappe

# @frappe.whitelist()
# def create_sales_invoice(subscription_name):
#     subscription = frappe.get_doc('Subscription', subscription_name)

#     if subscription.spare_parts:
#         invoice_items = []
#         for spare in subscription.spare_parts:
#             invoice_items.append({
#                 'item_code': spare.item_code,
#                 'item_name': spare.item_name,
#                 'qty': spare.qty,
#                 'warehouse': subscription.warehouse  # Ensure warehouse is taken from Subscription
#             })

#         # Create Sales Invoice document
#         sales_invoice = frappe.get_doc({
#             'doctype': 'Sales Invoice',
#             'customer': subscription.customer,
#             'customer_name': subscription.customer_name,
#             'posting_date': subscription.start_date,  # Use appropriate date field
#             'items': invoice_items,
#             'company': subscription.company,
#             'set_warehouse': subscription.warehouse,  # Set warehouse for all items
#             'update_stock': 1  # Enable stock update
#         })
#         sales_invoice.insert()
#         frappe.db.commit()

#         return sales_invoice.name
import frappe
from frappe.utils import add_days

@frappe.whitelist()
def create_sales_invoice(subscription_name):
    subscription = frappe.get_doc('Subscription', subscription_name)
    
    # Define default payment term in days (e.g., 30 days)
    payment_term_days = 30  # This can be adjusted based on your business logic

    if subscription.spare_parts:
        invoice_items = []
        for spare in subscription.spare_parts:
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
                'warehouse': subscription.warehouse,  # Ensure warehouse is taken from Subscription
                'discount_percentage': discount_percentage,
                'description': description  # Add description for the discount reason
            })

        # Calculate posting date and due date
        posting_date = subscription.start_date  # Use start_date as posting_date
        due_date = add_days(posting_date, payment_term_days)  # Set due date as 30 days from start_date

        # Create Sales Invoice document
        sales_invoice = frappe.get_doc({
            'doctype': 'Sales Invoice',
            'customer': subscription.customer,
            'customer_name': subscription.customer_name,
            'posting_date': posting_date,  # Set the posting date as the subscription start date
            'due_date': due_date,  # Set the due date 30 days from the start date
            'items': invoice_items,
            'company': subscription.company,
            'set_warehouse': subscription.warehouse,  # Set warehouse for all items
            'update_stock': 1,  # Enable stock update
            'set_posting_time': 1  # Enable posting time to allow posting date change
        })
        sales_invoice.insert()
        frappe.db.commit()

        return sales_invoice.name

    return None