#!/usr/bin/env python3

# Created by: Marcus Wehbi
# Created on: Dec 16 2022
# This program asks the user to enter a list of numbers and a target number
# The program then prints the first and last occurrence of this number

import random
import os

# Function to compare the player's and computer's choices
# ...for a game of rock paper scissors
def compare_choices(player, computer):
    # Create a list of possible choices
    choices = ["rock", "paper", "scissors"]
    # Check who wins the game
    if player == computer:
        print("It's a tie!")
    elif (
        (player == "rock" and computer == "scissors")
        or (player == "paper" and computer == "rock")
        or (player == "scissors" and computer == "paper")
    ):
        print("You win!")
    else:
        print("Computer wins!")


# Function to find the first and last occurrence of the target number
def find_occurrences(numbers_list, target):
    # Find the first occurrence of the target number
    # Set the first occurrence to -1 for when the target number is absent
    # ... from the list
    first_occurrence = -1
    # Iterate through the list of numbers and assign each index to the value
    # ... at its spot
    for index, counter in enumerate(numbers_list):
        # If the target number is seen, assign it to the first target number
        if counter == target:
            first_occurrence = index
            # Exit the loop
            break

    # Find the last occurrence of the target number
    # Set the last occurrence to -1 for when the target number is absent
    # ... from the list
    last_occurrence = -1
    # Reverse the list and then iterate through the list of numbers and assign
    # ...  each index to the value at its spot
    for index, counter in enumerate(numbers_list[::-1]):
        # If the target number is seen, assign it to the last target number
        if counter == target:
            # Calculate the index of the last occurrence
            last_occurrence = len(numbers_list) - index - 1
            # Exit the loop
            break
    # Return the indices of the first and last occurrences
    return [first_occurrence, last_occurrence]


# Function to find all indices of several target numbers
def find_all_occurrences(numbers_list, target_numbers):
    # Create an empty dictionary to store all the results (indices/occurrences)
    occurrences = {}
    # Iterate through the target numbers
    for target in target_numbers:
        # Initialize an empty list to store the indices of the occurrences
        indices = []
        # Iterate through the list of numbers and add the index to the list
        # ...if the number is equal to the target
        for index, number in enumerate(numbers_list):
            if number == target:
                indices.append(index)
        # Add the list of indices to the dictionary with the target as the key
        occurrences[target] = indices
    # Return the list of all occurrences
    return occurrences


# Function to get the input and return the results
def main():
    # Explain what the program does
    print("You are currently in the waiting lobby. While you are here, ")
    print("you can play rock paper scissors. When you are ready to use ")
    print("the program, simply type in 'exit'.")
    print()
    print()
    # Loop to repeat the game as many times as the user would like
    while True:
        # Get the player's choice for rock, paper, scissors
        player = input("Enter your choice (rock, paper, scissors): ")
        # If they have not exited the game yet, continue
        if player.upper() != "EXIT":
            # Generate a random choice for the computer
            computer = random.choice(["rock", "paper", "scissors"])
            # Compare the player's and computer's choices
            compare_choices(player, computer)
            continue
        # Otherwise, leave the loop
        else:
            break
    # Use another loop to repeat the program as many times as the user
    # ...would like
    while True:
        # Clear the terminal
        os.system("clear")
        # Explain how the program works
        print(
            "This program allows you to find the first and last occurrences of an integer "
        )
        print("in a list or all occurrences of multiple integers. Make sure you are ")
        print("entering a sorted list, and each integer is separated by spaces. ")
        print("Here is a sample input: 1 5 6 6 6 7")
        # Get the sorted list, search type, and target number from the user
        numbers = input("Enter a sorted list of numbers: ")
        search_type = input(
            "Enter 'single' to search for a single target or 'multiple' to search for multiple targets: "
        )
        target = input("Enter the targeted numbers separated by spaces: ")
        # Use a try catch
        try:
            # Convert the input strings to lists of integers
            # ...using list comprehension
            numbers = [int(x) for x in numbers.split()]
            target = [int(x) for x in target.split()]
        except:
            # If an error is met, notify the user
            print("Remember to separate the numbers with spaces.")
        else:
            # Otherwise, continue with the program
            # Execute if user inputs "single"
            if search_type.lower() == "single":
                # Find the first and last occurrences of the target number
                occurrences = find_occurrences(numbers, target[0])
                # Print the results
                print(
                    "The first occurrence of {} is at index {}.".format(
                        target[0], occurrences[0]
                    )
                )
                print(
                    "The last occurrence of {} is at index {}.".format(
                        target[0], occurrences[1]
                    )
                )
            # Execute if user inputs "multiple"
            elif search_type.lower() == "multiple":
                # Find all occurrences of the target numbers
                occurrences = find_all_occurrences(numbers, target)
                # Print the results
                # Loop to iterate over the items in a dictionary
                # The dictionary has keys that are integers (integer)
                # ...and values that are lists of integers (indices)
                for integer, indices in occurrences.items():
                    print(
                        "The occurrences of {} are at indices {}.".format(
                            integer, indices
                        )
                    )
            else:
                # Otherwise, print error message
                print("Invalid search type. Please enter 'single' or 'multiple'.")
        # Variable to ask the user if they want to play again
        play_again = input(
            "Do you want to use this program (enter 'y' if you would like to): "
        )
        # If they dont say yes, exit the loop
        if play_again.upper() != "Y":
            # Break out of the loop
            break


if __name__ == "__main__":
    main()
