# Copyright (c) 2018, Frappe Technologies Pvt. Ltd. and Contributors
# See license.txt

import unittest

import frappe

test_dependencies = ["Employee Onboarding"]


class TestEmployeeSeparation(unittest.TestCase):
	def test_employee_separation(self):
		employee = frappe.db.get_value("Employee", {"status": "Active"})
		separation = frappe.new_doc("Employee Separation")
		separation.employee = employee
		separation.company = "_Test Company"
		separation.append("activities", {"activity_name": "Deactivate Employee", "role": "HR User"})
		separation.boarding_status = "Pending"
		separation.insert()
		separation.submit()
		self.assertEqual(separation.docstatus, 1)
		separation.cancel()
		self.assertEqual(separation.project, "")
