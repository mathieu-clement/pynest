# pynest: A no-frills interface to control Nest thermostats

## Usage

```python
from nest import *

# If you don't have an authentication token yet:
authorize() # Opens a browser where the user gets a PIN code
code = '...' # copy PIN code here
n = Nest(code=code)
print(n.access_token) # Your turn: save it somewhere for future use

# If you have a token:
n = Nest(access_token='c.azYfsYf...')

t = n.get_thermostat()
print(t.data) # view the JSON data for this thermostat
print(t.ambient_temperature) # ambient temperature in the room
print(t.target_temperature) # temperature thermostat is set to
t.target_temperature = 20 # same as turning the dial to 20 degrees Celsius
t.enable_heat(True)
t.refresh()
print(t.is_heating())

t.enable_eco(True)
t.refresh()
print(t.is_heating())
````
    
Make sure to check out [app.py](/app.py) which takes care of the authentication process and saves the credentials to the disk so the app is already authenticated on the next launch.

## Limitations

  * Cooling and fan related features are not implemented.
  * `Nest.get_thermostat()` assumes there is only one thermostat in the account.

