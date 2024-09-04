import frappe
from frappe.utils import today

def update_serial_no_warranty(doc, method):
    today_date = today()
    frappe.log_error(message="Update Serial No Warranty Triggered", title="Delivery Note Hook Log")

    for item in doc.items:
        if item.serial_no:
            serial_nos = item.serial_no.split('\n')
            for serial_no in serial_nos:
                try:
                    serial_doc = frappe.get_doc('Serial No', serial_no)
                    frappe.log_error(message=f"Fetched Serial No: {serial_no}", title="Delivery Note Hook Log")
                    
                    # Update the warranty expiry date
                    serial_doc.db_set('warranty_expiry_date', today_date)
                    frappe.log_error(message=f"Set Warranty Expiry Date for {serial_no} to {today_date}", title="Delivery Note Hook Log")
                    
                    # Update the status
                    serial_doc.db_set('status', 'Delivered')
                    
                    # Log each successful update
                    frappe.log_error(message=f"Updated Serial No: {serial_no} with expiry date {today_date}", title="Delivery Note Hook Log")

                    # Notify the user
                    frappe.msgprint(f'Warranty expiry date updated for Serial No: {serial_no}', alert=True)
                except Exception as e:
                    frappe.log_error(message=f"Error updating Serial No: {serial_no} - {str(e)}", title="Delivery Note Hook Error")
