import frappe
from frappe import _
from frappe.model.document import Document


class SiSopDocument(Document):

    def validate(self):
        self.validate_document_type()
        self.validate_dates()
        self.validate_departments()
        self.validate_users()
        self.validate_content()
        self.validate_approved_person()

		
    def validate_approved_person(self):
        if self.status != "Approved":
            return

        approved_users = [user for user in self.users if user.role=="Approved By"]

        if len(approved_users) == 0:
            frappe.throw(
                _("An approved document must have one approved person.")
            )

    def validate_document_type(self):
        if self.document_type not in ("SOP", "SI"):
            frappe.throw(_("Document Type must be SOP or SI."))

    def validate_dates(self):
        if self.issue_date and self.approval_date:
            if self.approval_date < self.issue_date:
                frappe.throw(_("Approval Date cannot be before Issue Date."))

        if self.status == "Approved" and not self.approval_date:
            frappe.throw(_("Approval Date is mandatory for approved documents."))

    def validate_departments(self):
        if not self.departments:
            frappe.throw(_("Please add at least one Department."))

    def validate_users(self):
        if not self.users:
            frappe.throw(_("Please add at least one User."))

    def validate_content(self):
        if self.status == "Approved" and not self.content:
            frappe.throw(_("Content is mandatory before approving the document."))