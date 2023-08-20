"""
Problem 1
Chef has recently moved into an apartment. It takes 30
30 minutes for Chef to reach office from the apartment.
Chef left for the office
X minutes before Chef was supposed to reach. Determine whether or not Chef will be able to reach on time.

Explanation:
Test case 1: Chef leaves
30 minutes before he is supposed to reach, so he will reach the office exactly on time since it takes
30 minutes to commute.
Test case 2: Chef will reach
30 minutes early.

Test case 3: Chef will reach 16 minutes late
"""

def determine_chef_status(total_time, leave_before):
    commute_time = 30
    
    if leave_before == commute_time:
        return "On Time"
    elif leave_before < commute_time:
        return "Early"
    else:
        if total_time - leave_before >= commute_time:
            return "On Time"
        else:
            return "Late"

# Input: Total time Chef has to reach (in minutes), Minutes Chef leaves before reaching
total_time = int(input("Enter the total time Chef has to reach (in minutes): "))
leave_before = int(input("Enter minutes Chef leaves before reaching: "))

chef_status = determine_chef_status(total_time, leave_before)
print("Chef will be:", chef_status)