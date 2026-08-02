app_name = "si_sop"
app_title = "si_sop"
app_publisher = "volt"
app_description = "new"
app_email = "volt@gmail.com"
app_license = "mit"





fixtures = [
    {
        "dt": "Workspace",
        "filters": [["module", "=", "si_sop"]]
    },
    {
        "dt": "Workspace Sidebar",
        "filters": [["module", "=", "si_sop"]]
    },
    {
        "dt": "Desktop Icon",
        "filters": [["label", "=", "si_sop"]]
    },
    {
        "dt": "Dashboard Chart",
        "filters": [["module", "=", "si_sop"]]
    },
    {
        "dt": "Number Card",
        "filters": [["module", "=", "si_sop"]]
    },
    {
        "dt": "Notification",
        "filters": [["module", "=", "si_sop"]]
    },
    {
        "dt": "Role",
        "filters": [
            [
                "role_name",
                "in",
                [
                    "SI SOP Manager",
                    "SI SOP User"
                ]
            ]
        ]
    },
    {
        "dt": "Custom DocPerm",
        "filters": [
            [
                "role",
                "in",
                [
                    "SI SOP Manager",
                    "SI SOP User"
                ]
            ]
        ]
    },
    {
        "dt": "Client Script"
    },
    {
        "dt": "Custom Field"
    },
    {
        "dt": "Property Setter"
    }
]

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "si_sop",
# 		"logo": "/assets/si_sop/logo.png",
# 		"title": "si_sop",
# 		"route": "/si_sop",
# 		"has_permission": "si_sop.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/si_sop/css/si_sop.css"
# app_include_js = "/assets/si_sop/js/si_sop.js"

# include js, css files in header of web template
# web_include_css = "/assets/si_sop/css/si_sop.css"
# web_include_js = "/assets/si_sop/js/si_sop.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "si_sop/public/scss/website"

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
# app_include_icons = "si_sop/public/icons.svg"

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

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "si_sop.utils.jinja_methods",
# 	"filters": "si_sop.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "si_sop.install.before_install"
# after_install = "si_sop.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "si_sop.uninstall.before_uninstall"
# after_uninstall = "si_sop.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "si_sop.utils.before_app_install"
# after_app_install = "si_sop.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "si_sop.utils.before_app_uninstall"
# after_app_uninstall = "si_sop.utils.after_app_uninstall"

# Build
# ------------------
# To hook into the build process

# after_build = "si_sop.build.after_build"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "si_sop.notifications.get_notification_config"

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

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"si_sop.tasks.all"
# 	],
# 	"daily": [
# 		"si_sop.tasks.daily"
# 	],
# 	"hourly": [
# 		"si_sop.tasks.hourly"
# 	],
# 	"weekly": [
# 		"si_sop.tasks.weekly"
# 	],
# 	"monthly": [
# 		"si_sop.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "si_sop.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "si_sop.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "si_sop.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "si_sop.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["si_sop.utils.before_request"]
# after_request = ["si_sop.utils.after_request"]

# Job Events
# ----------
# before_job = ["si_sop.utils.before_job"]
# after_job = ["si_sop.utils.after_job"]

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
# 	"si_sop.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

