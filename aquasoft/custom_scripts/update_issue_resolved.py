# import frappe
# from frappe.model.document import Document

# def update_issue_status_on_visit_completion(doc, method):
#     if doc.completion_status == "Fully Completed" and doc.issue:
#         # Fetch the related Issue document
#         issue = frappe.get_doc("Issue", doc.issue)
#         issue.db_set("status", "Resolved")
#         frappe.msgprint(f"Issue {issue.name} status updated to 'Resolved'.")


import frappe
from frappe.model.document import Document

def update_issue_on_visit_completion(doc, method):
    if doc.completion_status == "Fully Completed" and doc.issue:
        # Fetch the related Issue document
        issue = frappe.get_doc("Issue", doc.issue)

        # Prepare the resolution details
        resolution_details = []
        for purpose in doc.purposes:
            details = f"""
                <b>Item Code:</b> {purpose.item_code}<br>
                <b>Item Name:</b> {purpose.item_name}<br>
                <b>Visited by Technician:</b> {purpose.service_person}<br>
                <b>Work Done:</b> {purpose.work_done}<br>
                <b>Visit Time:</b> {doc.mntc_time}<br>
                <b>Updated By:</b> {doc.modified_by}<br>
            """
            resolution_details.append(details)

        # Append the details to the existing resolution details in the Issue document
        issue.resolution_details = (issue.resolution_details or '') + "<br>".join(resolution_details)

        # Update the Issue status to "Resolved"
        issue.db_set("status", "Resolved")
        issue.db_set("resolution_details", issue.resolution_details)

        frappe.msgprint(f"Issue {issue.name} status updated to 'Resolved', with details added to Resolution Details.")