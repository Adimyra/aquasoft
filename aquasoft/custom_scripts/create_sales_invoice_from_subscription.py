import frappe

@frappe.whitelist()
def create_sales_invoice(subscription_name):
    subscription = frappe.get_doc('Subscription', subscription_name)

    if subscription.spare_parts:
        invoice_items = []
        for spare in subscription.spare_parts:
            invoice_items.append({
                'item_code': spare.item_code,
                'item_name': spare.item_name,
                'qty': spare.qty,
                'warehouse': subscription.warehouse  # Ensure warehouse is taken from Subscription
            })

        # Create Sales Invoice document
        sales_invoice = frappe.get_doc({
            'doctype': 'Sales Invoice',
            'customer': subscription.customer,
            'customer_name': subscription.customer_name,
            'posting_date': subscription.start_date,  # Use appropriate date field
            'items': invoice_items,
            'company': subscription.company,
            'set_warehouse': subscription.warehouse,  # Set warehouse for all items
            'update_stock': 1  # Enable stock update
        })
        sales_invoice.insert()
        frappe.db.commit()

        return sales_invoice.name

    return None