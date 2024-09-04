app_name = "aquasoft"
app_title = "Aquasoft"
app_publisher = "Adimyra Systems Private Limited"
app_description = "Aquasoft Maintenance Management Support System App"
app_email = "care@adimyra.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# In aquasoft/hooks.py
doc_events = {
    "Installation Note": {
        "on_submit": "aquasoft.installation_note_hooks.create_maintenance_visit_on_submit"
    },
    "Sales Invoice": {
        "on_submit": [
            # "aquasoft.custom_scripts.maintenance_visit.create_maintenance_visit_on_submit",
            "aquasoft.custom_scripts.maintenance_action.create_maintenance_action_on_submit",
            # "aquasoft.custom_scripts.first_visit_schedule.create_first_visit_schedule"
            "aquasoft.custom_scripts.regular_maintenance_schedule.create_maintenance_schedule"
        ]
    },
    "Subscription": {
        "on_update": "aquasoft.custom_scripts.amc_sync.create_or_update_other_customer_amc"
    },
    "Issue":{
        "on_update": "aquasoft.custom_scripts.create_mc_on_issue.create_maintenance_schedule_on_technician_update"
    },
    "Maintenance Visit": {
        "on_submit": [
            "aquasoft.custom_scripts.update_issue_resolved.update_issue_on_visit_completion"
            # "aquasoft.custom_scripts.create_sales_invoice_from_visit.create_sales_invoice_from_visit"
        ]
    }
    # "Maintenance Visit": {
    #     "on_save": "aquasoft.custom_scripts.create_sales_invoice_from_visit.validate_sales_invoice_on_save",
    # }
}

doctype_js = {
    "Installation Note": "public/js/installation_note_create_visit.js",
    "Subscription": "public/js/subscription.js",
    "Maintenance Visit": "public/js/create_sales_invoice_button.js",
    "subscription": "public/js/create_sales_invoice_btn_amc.js",

    # "Maintenance Visit": "public/js/create_sales_invoice_on_save.js"
    # "Sales Invoice": "public/js/create_maintenance_buttons.js"
    # "Sales Invoice": "public/js/sales_invoice.js"

    
}

after_migrate = "aquasoft.utils.add_shortcuts_to_support_team_workspace"


# include js, css files in header of desk.html
# app_include_css = "/assets/aquasoft/css/aquasoft.css"
# app_include_js = "/assets/aquasoft/js/aquasoft.js"

# include js, css files in header of web template
# web_include_css = "/assets/aquasoft/css/aquasoft.css"
# web_include_js = "/assets/aquasoft/js/aquasoft.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "aquasoft/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "aquasoft/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "aquasoft.utils.jinja_methods",
# 	"filters": "aquasoft.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "aquasoft.install.before_install"
# after_install = "aquasoft.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "aquasoft.uninstall.before_uninstall"
# after_uninstall = "aquasoft.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "aquasoft.utils.before_app_install"
# after_app_install = "aquasoft.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "aquasoft.utils.before_app_uninstall"
# after_app_uninstall = "aquasoft.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "aquasoft.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

#doc_events = {
   # "Delivery Note": {
  #      "on_submit": "aquasoft.delivery_note_hooks.update_serial_no_warranty"
 #   }
#}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"aquasoft.tasks.all"
# 	],
# 	"daily": [
# 		"aquasoft.tasks.daily"
# 	],
# 	"hourly": [
# 		"aquasoft.tasks.hourly"
# 	],
# 	"weekly": [
# 		"aquasoft.tasks.weekly"
# 	],
# 	"monthly": [
# 		"aquasoft.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "aquasoft.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "aquasoft.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "aquasoft.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["aquasoft.utils.before_request"]
# after_request = ["aquasoft.utils.after_request"]

# Job Events
# ----------
# before_job = ["aquasoft.utils.before_job"]
# after_job = ["aquasoft.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"aquasoft.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

