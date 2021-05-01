# while <conditional statement> :
#   <action>

count = 0
print("Starting a while Loop")
while count <= 3:
    # Loop Body
    # Print if the condition is still true
    print("Loop Iteration - count <= 3 is still true")
    # Print the current value of count
    print("Count is currently " + str(count))
    # Increment count
    count += 1
    print(" ----- ")
print("While Loop ended")
# Elegant Loop (One Line) seperated with ;
# count = 0
# while count <= 3: print(count); count += 1
#
