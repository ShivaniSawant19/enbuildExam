# 4. Consider one integer array. Update the array as per the following requirements:
# - If the element is negative number then make the square of the number
# - Keep the 0 as is
# - If the number is positive even number then add the same even number to that
# - If the number is positive odd number then print the next odd number to that
# Ex. {0, 13, 5, -4, 6} --> {0, 15, 7, 16, 12}



def sortSquare(arr, n):

	
	for i in range(n):
		arr[i]= arr[i] * arr[i]
	arr.sort()


arr = [0, 13, 5, -4, 6]
n = len(arr)

print("Before sort")
for i in range(n):
	print(arr[i], end = " ")

print("\n")

sortSquare(arr, n)

print("After sort")
for i in range(n):
	print(arr[i], end = " ")

