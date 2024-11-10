from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form1(Form1Template):
    def __init__(self, **properties):
        # Initialize the form components and set up initial properties.
        self.init_components(**properties)

        # Fetch employee data when the form is initialized
        self.all_employees = anvil.server.call('get_or_create_employee')

        # Initialize a DataGrid or RepeatingPanel if needed
        self.repeating_panel_employees.items = []

        # Any code you write here will run before the form opens.

    def button_show_employees_click(self, **event_args):
        """This method is called when the button is clicked"""
        # Update the items of the RepeatingPanel with employee data
        self.repeating_panel_employees.items = self.all_employees