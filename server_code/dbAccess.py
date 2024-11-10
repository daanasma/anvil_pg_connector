import anvil.secrets
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

from sqlalchemy.inspection import inspect

from .DB import Session
from .Models import Employee



@anvil.server.callable(require_user=True)
def get_or_create_employee():
  with Session() as session:
      # Execute a raw SQL query using the session
      result = session.execute('SELECT * FROM your_table')
  
      # Optionally, fetch the results
      rows = result.fetchall()
  
      # Do something with the rows
              
    
  return rows
