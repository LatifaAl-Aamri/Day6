"""
Problem
Chef wants to give a burger party to all his N friends
i.e. he wants to buy one burger for each of his friends.
The cost of each burger is X rupees while Chef has a total of K rupees.

Determine whether he has enough money to buy a burger for each of his friends or not

Explanation:

Test case
1: Chef has 5 friends. The cost of buying a burger for each of them
will be 10×5=50 while Chef has 70 rupees.
Therefore, he can buy a burger for all of them.

Test case
2: Chef has 5 friends. The cost of buying a burger for each of them
will be 10×5=50 while Chef has 40 rupees.
Therefore, he can not buy a burger for all of them.

Test case
3: Chef has 10 friends. The cost of buying a burger for each of them
will be 40×10=400 and Chef has 400 rupees.
Therefore, he can buy a burger for all of them.

Test case
4: Chef has 14 friends. The cost of buying a burger for each of them
will be 14×14=196 while Chef has 150 rupees.
Therefore, he can not buy a burger for all of them.
"""

# X = cost of each burger
#  K = Chef has a total
# N = number of friends
def can_buy_burgers(N, X, K):
    required_cost = N * X
    
    if K >= required_cost:
        return "YES"  # Chef can buy burgers for all friends
    else:
        return "NO"   # Chef cannot buy burgers for all friends
    
# Input: Number of friends (N), Cost of each burger (X), Chef's total money (K)
N = int(input("Enter the number of friends: "))
X = int(input("Enter the cost of each burger: "))
K = int(input("Enter Chef's total money: "))

result = can_buy_burgers(N, X, K)
print("Chef can buy burgers for all friends:", result)






















