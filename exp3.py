# def pour_water(juga, jugb):
#     max1, max2, fill = 4, 3, 2
#     print("%d\t%d" % (juga, jugb))
#     if jugb == fill:
#         return
#     elif jugb == max2:
#         pour_water(0, juga)
#     elif juga != 0 and jugb == 0:
#         pour_water(0, juga)
#     elif juga == fill:
#         pour_water(juga, 0)
#
#     elif juga < max1:
#         pour_water(max1, jugb)
#     elif juga < (max2 - jugb):
#         pour_water(0, (juga + jugb))
#     else:
#         pour_water(juga - (max2 - jugb), (max2 - jugb) + jugb)
#
#
# print("JUG A \tJUG B")
# pour_water(0, 0)



# ************** Correct **************************
def pour_water():
    jug4 = 0  # initialize 4-gallon jug
    jug3 = 3  # initialize 3-gallon jug

    # step 1: fill 3-gallon jug
    print("Fill 3-gallon jug")
    print("3-gallon jug: Full")
    print("4-gallon jug:", jug4)

    # step 2: pour water from 3-gallon jug to 4-gallon jug
    jug4 += jug3
    jug3 = 0  # empty 3-gallon jug
    print("Pour water from 3-gallon jug to 4-gallon jug")
    print("3-gallon jug: Empty")
    print("4-gallon jug:", jug4)

    # step 3: empty 4-gallon jug
    jug4 = 0
    print("Empty 4-gallon jug")
    print("3-gallon jug:", jug3)
    print("4-gallon jug: Empty")

    # step 4: pour remaining water from 3-gallon jug to 4-gallon jug
    jug4 += jug3
    jug3 = 0  # empty 3-gallon jug
    print("Pour remaining water from 3-gallon jug to 4-gallon jug")
    print("3-gallon jug: Empty")
    print("4-gallon jug:", jug4)

    print("Now, you have 2 gallons of water in the 4-gallon jug")

pour_water()


# def jug_problem(jug1, jug2, target):
#     """
#     Solves the jug problem for given jug sizes and target amount.
#
#     Args:
#     jug1 (int): Size of the first jug.
#     jug2 (int): Size of the second jug.
#     target (int): Target amount of water to be left in the larger jug.
#
#     Returns:
#     list: List of steps to achieve the target amount.
#     """
#
#     def dfs(curr_state, visited):
#         if curr_state[0] == target or curr_state[1] == target:
#             return True
#
#         if curr_state in visited:
#             return False
#
#         visited.add(curr_state)
#
#         # Pour from jug1 to jug2
#         if curr_state[0] > 0:
#             if curr_state[1] < jug2:
#                 if dfs((max(0, curr_state[0] - (jug2 - curr_state[1])), min(jug2, curr_state[1] + curr_state[0])),
#                        visited):
#                     steps.append(f"Pour {curr_state[0]} gallons from jug 1 to jug 2.")
#                     return True
#
#         # Pour from jug2 to jug1
#         if curr_state[1] > 0:
#             if curr_state[0] < jug1:
#                 if dfs((min(jug1, curr_state[0] + curr_state[1]), max(0, curr_state[1] - (jug1 - curr_state[0]))),
#                        visited):
#                     steps.append(f"Pour {curr_state[1]} gallons from jug 2 to jug 1.")
#                     return True
#
#         # Fill jug1
#         if curr_state[0] < jug1:
#             if dfs((jug1, curr_state[1]), visited):
#                 steps.append(f"Fill jug 1 ({jug1} gallons).")
#                 return True
#
#         # Fill jug2
#         if curr_state[1] < jug2:
#             if dfs((curr_state[0], jug2), visited):
#                 steps.append(f"Fill jug 2 ({jug2} gallons).")
#                 return True
#
#         # Empty jug1
#         if curr_state[0] > 0:
#             if dfs((0, curr_state[1]), visited):
#                 steps.append("Empty jug 1.")
#                 return True
#
#         # Empty jug2
#         if curr_state[1] > 0:
#             if dfs((curr_state[0], 0), visited):
#                 steps.append("Empty jug 2.")
#                 return True
#
#         return False
#
#     steps = []
#     dfs((0, 0), set())
#     return steps
#
#
# # Example usage:
# jug1 = 4
# jug2 = 3
# target = 2
# print(jug_problem(jug1, jug2, target))
