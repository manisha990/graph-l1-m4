# ************** Correct **************************

# Importing the deque class from the collections module
from collections import deque

# Function to perform Breadth-First Search to find a solution for the Water Jug problem
def BFS(a, b, target):
    m = {} # Dictionary to keep track of visited states
    isSolvable = False   # Flag to indicate if a solution is found
    path = []    # List to store the sequence of actions taken to reach the solution

    q = deque()   # Creating a deque data structure for implementing the

    q.append((0, 0))   # Adding the initial state (0, 0) to the queue

    # Loop until the queue is empty or a solution is found
    while len(q) > 0:

        u = q.popleft()   # Dequeue the first element from the queue

        # Check if the current state has been visited before
        if (u[0], u[1]) in m:
            continue   # Skip this state if already visited

        # Check if the current state violates the jug capacities
        if u[0] > a or u[1] > b or u[0] < 0 or u[1] < 0:
            continue   # Skip this state if it's invalid

        path.append([u[0], u[1]]) # Append the current state to the path

        m[(u[0], u[1])] = 1   # Mark the current state as visited

        # Check if the target amount is reached in either jug
        if u[0] == target or u[1] == target:
            isSolvable = True   # Update the flag indicating solution is found


            # Adjust the path for displaying the solution
            if u[0] == target:
                if u[1] != 0:
                    path.append([u[0], 0])
            else:
                if u[0] != 0:
                    path.append([0, u[1]])


            # Display the sequence of actions taken to reach the solution
            sz = len(path)
            for i in range(sz):
                print("(", path[i][0], ",", path[i][1], ")")
            break

        q.append([u[0], b])  # Fill Jug2
        q.append([a, u[1]])  # Fill Jug1

        # Explore all possible pouring combinations of water between jugs
        for ap in range(max(a, b) + 1):

            # Pour water from Jug1 to Jug2
            c = u[0] + ap
            d = u[1] - ap

            if c == a or (d == 0 and d >= 0):
                q.append([c, d])

            # Pour water from Jug2 to Jug1
            c = u[0] - ap
            d = u[1] + ap

            if (c == 0 and c >= 0) or d == b:
                q.append([c, d])

        q.append([a, 0])   # Action: Empty Jug1

        q.append([0, b])   # Action: Empty Jug2


    # If no solution is found, print a message
    if not isSolvable:
        print("No solution")

# Call the BFS function with jug capacities and target amount, and store the result in variable 'a'
a = BFS(4, 3, 2)
print(a)
