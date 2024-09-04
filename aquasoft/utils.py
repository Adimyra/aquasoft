import frappe

def add_shortcuts_to_support_team_workspace():
    # Load the workspace document
    workspace = frappe.get_doc('Workspace', 'Support Team')

    # Add shortcuts
    shortcuts = [
        {
            "type": "DocType",  # Corrected the type value to "DocType"
            "label": "Add Issue",
            "name": "Issue",
            "link_type": "list",
            "onboard": 0,
            "idx": 1
        },
        {
            "type": "DocType",  # Corrected the type value to "DocType"
            "label": "Open Issues",
            "name": "Issue",
            "link_type": "list",
            "filters": [["status", "=", "Open"]],
            "onboard": 0,
            "idx": 2
        },
        {
            "type": "DocType",  # Corrected the type value to "DocType"
            "label": "Resolved Issues",
            "name": "Issue",
            "link_type": "list",
            "filters": [["status", "=", "Resolved"]],
            "onboard": 0,
            "idx": 3
        }
    ]

    # Clear existing shortcuts and add new ones
    workspace.shortcuts = []
    for shortcut in shortcuts:
        workspace.append("shortcuts", shortcut)

    # Save the workspace
    workspace.save()
    frappe.msgprint(f'Shortcuts added to the {workspace.title} workspace successfully.')

# Call the function to update the workspace
add_shortcuts_to_support_team_workspace()