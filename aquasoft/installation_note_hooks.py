# import frappe
# from frappe.utils import nowtime

# def create_maintenance_visit_on_submit(doc, method):
#     # Create a new Maintenance Visit document
#     maintenance_visit = frappe.get_doc({
#         "doctype": "Maintenance Visit",
#         "customer": doc.customer,
#         "customer_name": doc.customer_name,
#         "customer_address": doc.customer_address,
#         "address_display": doc.address_display,
#         "territory": doc.territory,
#         "customer_group": doc.customer_group,
#         "mntc_date": doc.inst_date,
#         "mntc_time": nowtime(),
#         "visit_type": "Warranty",
#         "repeat_visit": "No",
#         "completion_status": "Fully Completed",
#         "maintenance_type": "Scheduled",
#         "status": "Draft",
#         "company": doc.company,
#         "installation_note": doc.name,
#         "purposes": [
#             {
#                 "item_code": item.item_code,
#                 "item_name": frappe.db.get_value("Item", item.item_code, "item_name"),
#                 "service_person": doc.installation_by,
#                 "work_done": "Installation",
#                 "description": item.description
#             } for item in doc.items
#         ]
#     })
    
#     # Insert and submit the Maintenance Visit document
#     maintenance_visit.insert()
#     maintenance_visit.submit()
    
#     frappe.msgprint(f"Maintenance Visit {maintenance_visit.name} created and submitted successfully")

import frappe
from frappe.utils import nowtime

def create_maintenance_visit_on_submit(doc, method):
    create_maintenance_visit(doc)

@frappe.whitelist()
def create_maintenance_visit_manually(docname):
    doc = frappe.get_doc("Installation Note", docname)
    maintenance_visit_name = create_maintenance_visit(doc)
    return maintenance_visit_name

def create_maintenance_visit(doc):
    # Create a new Maintenance Visit document
    maintenance_visit = frappe.get_doc({
        "doctype": "Maintenance Visit",
        "customer": doc.customer,
        "customer_name": doc.customer_name,
        "customer_address": doc.customer_address,
        "address_display": doc.address_display,
        "territory": doc.territory,
        "customer_group": doc.customer_group,
        "mntc_date": doc.inst_date,
        "mntc_time": nowtime(),
        "visit_type": "Warranty",
        "repeat_visit": "No",
        "completion_status": "Fully Completed",
        "maintenance_type": "Scheduled",
        "status": "Draft",
        "company": doc.company,
        "installation_note": doc.name,
        "purposes": [
            {
                "item_code": item.item_code,
                "item_name": frappe.db.get_value("Item", item.item_code, "item_name"),
                "service_person": doc.installation_by,
                "work_done": "Installation",
                "description": item.description
            } for item in doc.items
        ]
    })
    
    # Insert and submit the Maintenance Visit document
    maintenance_visit.insert()
    maintenance_visit.submit()
    
    frappe.msgprint(f"Maintenance Visit {maintenance_visit.name} created and submitted successfully")
    return maintenance_visit.name