# Sal's Shipping Weight Distribution

# Global Variables
# Note: (If you are trying to use user input in Codeacademy, it won't let you so hard code a number in instead!)
weight = float(input("Enter weight of the package: "))
costG = 0
costD = 0

# Static Variable
premium_shipping = 125

# Functions
def calc_ground(costG):
  # Total cost for ground shipping
  print("Ground Shipping Cost: $", round(costG, 2))
  print("------------------------------------------------------")

def calc_p_ground(premium_shipping):
  # Total cost for premium ground shipping
  print("Premium Ground Shipping Cost: $", premium_shipping)
  print("------------------------------------------------------")

def calc_drone(costD):
  # Total cost for drone shipping
  print("Drone Shipping Cost: $", round(costD,2))
  print("------------------------------------------------------")

def cheapest(costD, premium_shipping, costG):
  if round(costD, 2) == round(costG, 2):
    # A test case I found when two prices intersect
    print("You found a test case!")
  elif costD < premium_shipping and costD < costG:
    print("Drone shipping is the cheapest!")
  elif costG < premium_shipping and costG < costD:
    print("Ground shipping is the cheapest!")
  elif premium_shipping < costD and premium_shipping < costG:
    print("Premium ground shipping is the cheapest!")

# Outputs
#----------------------------------------------------------------
# Test Cases. (Weight check)
if isinstance(weight, str):
  # Test Case. (Wrong datatype being used)
    print("Wrong Datatype")
    exit()
if weight <= 0:
  # Test case. (Weight is too small)
    print("You cannot ship anything with negative or no weight")
    exit()

# Ground shipping
if weight <= 2:
  costG = 1.50 * weight + 20
elif weight >= 2 and weight <= 6:
  costG = 3 * weight + 20
elif weight >= 6 and weight <= 10:
  costG = 4 * weight + 20
elif weight > 10:
  costG = 4.75 * weight + 20
else:
  # Test case. (Unpredicated Error)
    print("Unexpected Error")
    exit()
calc_ground(costG)

# Premimum ground shipping
calc_p_ground(premium_shipping)

# Drone shipping
if weight <= 2:
  costD = 4.50 * weight
elif weight >= 2 and weight <= 6:
  costD = 9 * weight
elif weight >= 6 and weight <= 10:
  costD = 12 * weight
elif weight > 10:
  costD = 14.25 * weight
else:
  # Test case. (Unpredicated Error)
    print("Unexpected Error")
    exit()
calc_drone(costD)

# Final Calculation
cheapest(costD, premium_shipping, costG)


