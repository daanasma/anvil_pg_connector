import anvil.server
import psycopg2
# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#

conn = psycopg2.connect(
  host="aws-0-eu-west-3.pooler.supabase.com",
  user="postgres.xelklrjeynkzpjhgergr",
  password="jnT8iXwbzDZLX3wz",
  port=6543
  )

# Automatically commit transactions
conn.set_session(autocommit=True)

cur = conn.cursor()

def get_items():
  # Run a query
  cur.execute('SELECT * FROM poi;')
  
  # Get all the rows for that query
  items = cur.fetchall()
  
  # Convert the result into a list of dictionaries (useful later)
  return items

print(get_items())