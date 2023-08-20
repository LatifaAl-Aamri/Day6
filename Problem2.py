"""
Problem 2
Chef has recently started playing chess, and wants to play as many games as possible.
He calculated that playing one game of chess takes at least 20 minutes of his time.

Chef has
N hours of free time. What is the maximum number of complete chess games he can play in that time?

Explanation:
Test case
1: If every game Chef plays takes 20 minutes, he can play 3 games in one hour.

Test case
2: If every game Chef plays takes 20 minutes, he can play 30 games in 10 hours.

Test case
3: If every game Chef plays takes 20 minutes, he can play 21 games in 7 hours.

Test case
4: If every game Chef plays takes 20 minutes, he can play 9 games in 3 hours.
"""

def max_chess_games(hours):
    game_duration = 20  # Duration of a single chess game in minutes
    total_time_in_minutes = hours * 60  # Convert hours to minutes
    """
    The // operator ensures that the division result is always rounded
    down to the nearest whole number, which is suitable for counting
    how many complete chess games Chef can play within his available time.
    """
    max_games = total_time_in_minutes // game_duration
    return max_games

# Input: Number of hours of free time
hours = int(input("Enter the number of hours of free time: "))
max_games = max_chess_games(hours)
print("Maximum number of complete chess games Chef can play:", max_games)