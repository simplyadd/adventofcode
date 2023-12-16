Day 9: https://adventofcode.com/2023/day/9

Part 1 gets the sum of the extrapolated values.
  Each line in the input file contains the history of a single value. Predict the next value for each history by making a sequence from the difference at each step of your history. If that sequence is not all zeroes, repeat this process. 

  Once the latest sequence has all zeroes, extrapolate by adding a new zero to the end of your list. Next, add the 0 to the last value of the previous list. Use the sum to add to the one before the list until reaching the original list.