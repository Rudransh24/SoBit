In this question, we need to find list of all transaction ids which lead to maximum fee with total weight of block to be less than 4,000,000...

1)Approach 1: Greedy Knapsack approach which is the naive approach to solve this question. We need to first find all valid ids that can be added in the block which means no ids should be present before their parent ids.

Now, we just sort the dataframe in terms of weight, then fees, and finally ratio of fee and weight. Thus, we now have 3 different options to choose from and we require the maximum fees we can get. Thus, we find maximum out of 3 and store all the ids related to it using concept of dictionary.

2)Appraoch 2: 0-1 Knapsack is one of the more efficient solutions to the problem but the main reason we can't use it here is because of the capacity of the knapsack, that is, the maximum weight the block can store which is 4,000,000. Thus creating a two dimensional array (for dynamic programming) can be an issue of the space memory and also time complexity.
But, we can also use one dimensional array which would be of linear time complexity. Even then, we need to iterate every possible situation which will only occur in time: O(capacity * number of ids) which is an n^2 approach and cannot be used with capacity C = 4,000,000 due to higher time complexity issues.

Thus, greedy approach is the sole answer to the problem statement.