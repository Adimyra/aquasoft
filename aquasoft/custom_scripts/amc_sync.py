import frappe
from frappe.utils import now, getdate, add_days

def create_or_update_other_customer_amc(doc, method):
    if doc.customer_type == "Other Customer":
        # Check if an Other Customer AMC record already exists for this Subscription
        amc_name = frappe.db.get_value("Other Customer AMC", {"subscription": doc.name})

        if amc_name:
            # If it exists, fetch it
            amc_doc = frappe.get_doc("Other Customer AMC", amc_name)
        else:
            # If it doesn't exist, create a new one
            amc_doc = frappe.new_doc("Other Customer AMC")
            amc_doc.subscription = doc.name

        # Update the fields
        amc_doc.customer = doc.customer
        amc_doc.customer_name = doc.customer_name
        amc_doc.machine_name = doc.machine_name
        amc_doc.amc_plan = doc.plans[0].plan if doc.plans else None
        amc_doc.sales_person = doc.sales_person
        amc_doc.start_date = doc.start_date
        amc_doc.end_date = add_days(doc.end_date, -1)  # Show the date minus one day
        amc_doc.first_visit_status = doc.first_visit
        amc_doc.technician = doc.technician
        amc_doc.work_done = doc.work_done
        amc_doc.status = doc.status  # AMC Subscription Status

        # Determine the AMC Maintenance Status
        current_date = getdate(now())
        adjusted_end_date = getdate(amc_doc.end_date)

        if adjusted_end_date < current_date:
            amc_doc.amc_maintenance_status = "Out of AMC"
        else:
            amc_doc.amc_maintenance_status = "Under AMC"

        # Save the document
        amc_doc.save(ignore_permissions=True)
        frappe.msgprint(f"Other Customer AMC for {doc.customer_name} has been created/updated successfully.")