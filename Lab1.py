''' TASK - 1 '''
import matplotlib.pyplot as plt
import numpy as np
# hard code variables
def quadratic_model(time):
  a=2
  b=4
  c=9
  temperature = a*time*time + b*time + c
  return temperature

time_values=np.linspace(0,10,100)
temperature_hardcoded = quadratic_model(time_values)

plt.plot(time_values,temperature_hardcoded, label='temperature with hard coded coefficients')
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.legend()
plt.title('weather modeling with quadratic equation(Hard-coded coefficient)')
plt.show()

#------------------------------------------------------------------------------------------

''' TASK - 2 '''
import matplotlib.pyplot as plt
import numpy as np
# hard code variables
def quadratic_model(a,b,c,time):
  temperature = a*time*time + b*time + c
  return temperature

time_values=np.linspace(0,10,100)
a=int(input("Enter value of a : "))
b=int(input("Enter value of b : "))
c=int(input("Enter value of c : "))
temperature_hardcoded = quadratic_model(a,b,c,time_values)

plt.plot(time_values,temperature_hardcoded, label='temperature with hard coded coefficients')
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.legend()
plt.title('weather modeling with quadratic equation(keyboard input)')
plt.show()

#------------------------------------------------------------------------------------------

''' TASK - 3 '''
f = open("a.txt", "r")

import matplotlib.pyplot as plt
import numpy as np
# hard code variables
def quadratic_model(f,time):
  a=int(f.readline())
  b=int(f.readline())
  c=int(f.readline())
  temperature = a*time*time + b*time + c
  return temperature

time_values=np.linspace(0,10,50)
temperature_hardcoded = quadratic_model(f,time_values)

plt.plot(time_values,temperature_hardcoded, label='temperature with hard coded coefficients')
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.legend()
plt.title('weather modeling with quadratic equation(read from file)')
plt.show()

#------------------------------------------------------------------------------------------

''' TASK - 4 '''
import matplotlib.pyplot as plt
import numpy as np
# hard code variables
def quadratic_model(time,a,b,c):
  temperature = a*time*time + b*time + c
  return temperature
list = [(20,3,4),(4,3,1),(2,5,1)]
time_values=np.arange(0,51,1)

for i,(a,b,c) in enumerate(list):
  temperature_values = quadratic_model(time_values,a,b,c)
  label=f'Set{i+1}: a={a},b={b},c={c}'
  plt.plot(time_values,temperature_values, label=label)


plt.xlabel('Time')
plt.ylabel('Temperature')
plt.legend()
plt.grid(True)
plt.title('weather modeling with quadratic equation(multiple set)')
plt.show()

#------------------------------------------------------------------------------------------

''' TASK - 5 '''
import matplotlib.pyplot as plt
import numpy as np

# Function to calculate temperature using the quadratic model
def quadratic_model(time, a, b, c):
    temperature = a * time**2 + b * time + c
    return temperature

# Hard-coded coefficients
a_hardcoded = 2
b_hardcoded = 5
c_hardcoded = 3

# User input for additional coefficients
a_user = float(input("Enter the value for coefficient 'a': "))
b_user = float(input("Enter the value for coefficient 'b': "))
c_user = float(input("Enter the value for coefficient 'c': "))

# Combine hard-coded and user-input coefficients
a_combined = a_hardcoded + a_user
b_combined = b_hardcoded + b_user
c_combined = c_hardcoded + c_user

# Generate time values
time_values = np.linspace(0, 10, 50)

# Calculate temperatures using the combined coefficients
temperature_combined = quadratic_model(time_values, a_combined, b_combined, c_combined)

# Plotting a line graph
plt.plot(time_values, temperature_combined, label='Combined Coefficients', linestyle='-', color='blue', marker='o')

# Add labels and title
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.legend()
plt.title('Weather Modeling with Quadratic Equation')

# Show the plot
plt.show()

