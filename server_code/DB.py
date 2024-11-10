import anvil.server

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
import anvil.secrets 

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def get_engine():
      return create_engine(
        f"postgresql://postgres.xelklrjeynkzpjhgergr:{anvil.secrets.get_secret('PG_PASSWORD')}@aws-0-eu-west-3.pooler.supabase.com:6543/postgres"
    )
    
Session = sessionmaker(bind=get_engine())
