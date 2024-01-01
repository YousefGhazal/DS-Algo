# Define the size of the list
N = 10

# Create a list of size N
A = [0]*N

# Print the size of the list
print("Size of the list:", len(A))

# Implement the selection sort algorithm
for i in range(N):
    print("i", i)
    for j in range(i + 1, N):
        print("j", j)  
        
        if A[i] > A[j]:
            A[i], A[j] = A[j], A[i]  # Swap elements
