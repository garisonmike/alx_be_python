# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Draw the pattern using while and for loops
row = 0
while row < size:
    # Use for loop to print asterisks in the current row
    for col in range(size):
        print("*", end="")
    
    # Move to the next line after completing the row
    print()
    
    # Move to the next row
    row += 1