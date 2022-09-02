from time import sleep
import os

frame1 = """
                ,,,,,,,,,,---''''---,,,,,,,,,,
      --''''''''          ````][''''          ''''''''--
                           _3'''':.
 _                  .,---------------.
 \\    / _________./  |[__]| o   |J@"\\__
  \\==o=========:;    |____|[IL__|''''/_/')
     /            `'-,._____===\=_____.,-'
                          \         \     ,
                    \"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\\"\"\"\"
"""

frame2 = """
      --'''''''',,,,,,,,,,---''''---,,,,,,,,,,''''''''--
                          ````][''''          
                           _3'''':.
 _                  .,---------------.
 \\  \   _________./  |[__]| o   |J@"\\__
  \\==o=========:;    |____|[IL__|''''/_/')
        \         `'-,._____===\=_____.,-'
                          \         \     ,
                    \"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\\"\"\"\"
"""

# Clear Console Window
def clearConsole():
  command = 'clear'
  if os.name in ('nt', 'dos'):
      command = 'cls'
  os.system(command)

  
# Prints Both Frame 1000 Times 
for x in range(1000):
  clearConsole()
  print(frame1)
  sleep(0.1)
  clearConsole()
  print(frame2)
  sleep(0.1)