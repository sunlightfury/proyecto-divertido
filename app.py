# Python program to print
# Hello Python

# a = 3
# b = 2

# c = a + b
# print("sum:", c)

# for i in range(3, 101, 3):
#     print("multiples of 3:", i)

# for j in range(5, 101, 5):
#     print("multiplees of 5:", j)


# Set the range of numbers
start_range = 3
end_range = 100

for i in range(start_range, end_range):

    # Check for multiples of 3
    if i % 3 == 0 or i % 5 == 0:
        print("multiples of 3 and 5", i)

    # # Check for multiples of 5
    # if i % 5 == 0:
    #     print("multiples of 5", i)
