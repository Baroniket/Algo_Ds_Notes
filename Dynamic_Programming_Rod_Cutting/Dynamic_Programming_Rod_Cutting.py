INT_MIN = -32767



# Function for money calculation

def money(price, n):

    val = [0 for x in range(n+1)]

    val[0] = 0



    for i in range(1, n+1):

        max_val = INT_MIN

        for j in range(i):

             max_val = max(max_val, price[j] + val[i-j-1])

        val[i] = max_val



    return val[n]



# Testing the function

arr = [3, 5, 8, 9, 10, 17, 17, 20]

size = len(arr)



print("Maximum Money : " + str(money(arr, size)))





# Output

<<<<<<< HEAD
# Maximum Money : 24
=======
# Maximum Money : 24
>>>>>>> 178cbae9c8c7565ddbcfda39cd69422482d415f2
