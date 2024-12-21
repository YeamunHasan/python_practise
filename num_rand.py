import numpy as np
np.random.seed(123)
print(np.random.rand())
# NumPy is imported, seed is set
import numpy as np
np.random.seed(123)
# Starting step
step = 50

# Roll the dice

dice = np.random.randint(1, 7)
# Finish the control construct
if dice <= 2:  # If dice is 1 or 2
    step = step - 1
elif 3 <= dice <= 5:  # If dice is 3, 4, or 5
    step = step + 1
else:  # If dice is 6
    step = step + np.random.randint(1, 7)

# Print out dice and step
print("Dice:", dice)
print("Step:", step)