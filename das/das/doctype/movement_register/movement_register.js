// Copyright (c) 2019, VHRS and contributors
// For license information, please see license.txt

frappe.ui.form.on('Movement Register', {
	// refresh: function(frm) {

	// }
	setup: function(frm) {
		frm.set_query("approver", function() {
			return {
				query: "erpnext.hr.doctype.department_approver.department_approver.get_approvers",
				filters: {
					employee: frm.doc.employee,
					doctype: frm.doc.doctype
				}
			};
		});

		frm.set_query("employee", erpnext.queries.employee);
	},
});
