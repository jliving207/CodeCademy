# A temporary variable’s name is arbitrary and does not need to be defined beforehand.
ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]

# for i in ingredients:
#    print(i)
# These for loops are the exact same
for ingredient in ingredients:
    # Any code at this level of indentation
  # will run on each iteration of the loop
    print(ingredient)
# for loop using range to iterate


six_steps = range(6)
# six_steps is now a collection with 6 elements:
# 0, 1, 2, 3, 4, 5


for temp in range(6):
    print("Learning Loops Baby!")
# which loop iteration (step) we are on, we can use temp


for temp in range(6):
    print("Loop is on iteration number " + str(temp + 1))

promise = "I will finish the python loops module!"

for p in range(5):
    print(promise)
