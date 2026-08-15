import frappe
from frappe import _
from frappe.model.document import Document


class SiSopDocument(Document):

    def validate(self):
        self.validate_document_type()
        self.validate_dates()
        self.validate_departments()
        self.validate_users()


    def validate_document_type(self):
        if not self.document_type:
            frappe.throw(_("Document Type is required."))

        if not frappe.db.exists(
            "SISOP Document Type",
            self.document_type
        ):
            frappe.throw(
                _("Document Type '{0}' does not exist.").format(
                    self.document_type
                )
            )

    def validate_dates(self):
        if self.issue_date and self.approval_date:
            if self.approval_date < self.issue_date:
                frappe.throw(_("Approval Date cannot be before Issue Date."))

        if self.status == "Approved" and not self.unknown_approval_date and not self.approval_date:
            frappe.throw(_("Approval Date is mandatory for approved documents."))

    def validate_departments(self):
        if not self.departments:
            frappe.throw(_("Please add at least one Department."))

    def validate_users(self):
        if not self.users:
            frappe.throw(_("Please add at least one User."))