from __future__ import unicode_literals
from frappe import _
def get_data():
    config = [
        {
            "label": _("Finance"),
            "items": [
                {
					"type": "doctype",
					"name": "Sales Order",
					"description": _("Confirmed orders from Customers."),
					"onboard": 1,
					"dependencies": ["Item", "Customer"],
				},
                {
					"type": "doctype",
					"name": "Sales Invoice",
                    "label": "Invoice",
					"description": _("Bills raised to Customers."),
					"onboard": 2,
				},
                {
                    "type": "doctype",
                    "name": "HRD Corp Grant",
                    "label": "HRD Corp Grant",
                    "onboard": 3,
                },
            ]
        },
        {
            "label": _("Operation"),
            "items": [
                {
					"type": "doctype",
					"name": "Room",
                    "label": "Room Booking",
					"onboard": 1,
				},
                {
                    "type": "doctype",
                    "name": "HRD Corp Grant",
                    "label": "HRD Corp Grant",
                    "onboard": 2,
                },
                {
                    "type": "doctype",
                    "name": "Manual",
                    "label": "E-Manual",
                    "onboard": 3, 
                },      
            ]
        },
        {
            "label": _("Course Instructor"),
            "items": [
                {
                    "type": "doctype",
                    "name": "Instructor",
                    "label": "Instructor",
                    "onboard": 1,
                },
                {
                    "type": "doctype",
                    "name": "Trainer Schedule",
                    "label": "Trainer Schedule",
                    "onboard": 2,
                },
                {
                    "type": "doctype",
                    "name": "Trainer Kit",
                    "label": "Trainer Kit",
                    "onboard": 3,
                },     
            ]
        },
        {
            "label": _("Settings"),
            "items": [
                 {
                    "type": "doctype",
                    "name": "Short Courses Settings",
                    "label": "Short Courses Settings",
                    "onboard": 1,
                }, 
                {
					"type": "doctype",
					"name": "Course Schedule",
                    "label": "Course Schedule"
					
                    
				},
                          
            ]

        }

    ]
    return config