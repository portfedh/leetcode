1689. Partitioning Into Minimum Number Of Deci-Binary Numbers

Python List

Setup 
-----

Companies

A decimal number is called deci-binary if each of its digits is either 0 or 1 without any leading zeros. For example, 101 and 1100 are deci-binary, while 112 and 3001 are not.

Given a string n that represents a positive decimal integer, return the minimum number of positive deci-binary numbers needed so that they sum up to n.

Example 1:

Input: n = "32"
Output: 3
Explanation: 10 + 11 + 11 = 32

Example 2:

Input: n = "82734"
Output: 8

Example 3:

Input: n = "27346209830709182346"
Output: 9

Constraints:

    1 <= n.length <= 105
    n consists of only digits.
    n does not contain any leading zeros and represents a positive integer.



Solution
--------

class Solution(object):

    def minPartitions(self, n):

        num_list = []

        for x in n:
            int(x)
            num_list.append(x)

        return int(max(num_list))


Test
----
n = "82734"
o1 = Solution()
a= o1.minPartitions(n)


Explanation
-----------

the other commenters mentioned practice which is definitely true for noticing patterns, but in my experience one of the best things you can do when trying to solve questions efficiently is thinking about things that you don't have to do as much as you think about things that you do have to do.
For this question, the naive solution or first solution that you think of is most likely generating all possible combinations of values and comparing their sums. Try working this out for a simple case: 4321 or something similar.
12 34
12 43
13 24
13 42
etc.
You'll probably start to notice that any combination with a number in the 40's is going to be useless and might not even write it out because you immediately know that it's bad. You get that feeling because humans are really good at noticing patterns even if we don't know why - getting to the next step is asking why we can immediately throw that number out. The answer is that every number with a 4 in it will always be better if the 4 is not in the 10's column. Now that we've figured that out, how can we generalize it?

This part is usually the hard bit. Finding a generalized rule is diffucult, and this is where pattern recognition from practice will help a lot, but in this case its pretty easy to see that any number that doesn't have its digits in increasing order will be non-optimal, and from there it's fairly easy to code that rule: sort the digits, then use the bigger ones first.

When I started programming (and still to this day) trying to figure out how to write optimal code is a pain. The optimal solution for one problem is rarely translatable to another problem, which can make lengthy explanations like this for one problem seem unhelpful for general programming. Most of the time for leetcode/interview questions, inefficiency comes in the form of calculating/evaluating things that don't need to be calculated. The (very generalized) process for figuring optimizing these is actually pretty similar for most problems, even if it doesn't seem like it. First, figure out the easy solution even if it isn't optimal. Then, figure out where that solution is inefficient, figure out why, and try to find a way to fix it.

I'll walk through using this formula on 2sum:

    find the naive solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
         for i in range(0, len(nums)):
                  for j in range(i, len(nums)):
                         if i + j == target:
                                 return [nums[i], nums[j]]

    This works, but it's inefficient. Lets try to figure out why.
    Where are we wasting time? lets go through an example and find out.
    [1, 2, 3, 4, 5], target = 8
    1 + 2 < 8
    1 + 3 < 8
    1 + 4 < 8
    1 + 5 < 8
    2 + 3 < 8
    2 + 4 < 8
    2 + 5 < 8
    3 + 4 < 8
    3 + 5 = 8

This might take a bit to think about, and a couple of examples but you can see that we're comparing 1 and 2 with every other number in the list when we're only looking for their complement. Let's try to not compare each number with each other number - how can we do that? Well, we're just looking for the number that complements the current number. How about instead of trying to find each complement in the rest of the list we kept track of the complements and checked if each new number is a complement to a previous number only once? Lets try our example again:

1's complement is 7
2 isn't 7, and its complement is 6
3 isn't 6 or 7. it's complement is 5
4 isn't 5, 6, or 7. It's complement is 4.
5 is a complement of 3.
return 5 and 3.

putting this generalized rule into practice we get:

def twoSum(self, nums: List[int], target: int) -> List[int]:
        targets = dict()
        for index, number in enumerate(nums):
            if number in targets:
                return [index, targets[number]]
            else:
                targets[target-number] = index

This solution is more efficient if you use an appropriate data structure like a dictionary that lets you check the current answer against the targets efficiently, but even if you don't use one it's still more efficient because the algorithm is better.
You can see how we got an easy solution, found the ways that its wasting time, and found a solution that avoids wasting that time.

Sorry this is a big essay but I hope this helps, good luck and keep practicing!
print(a)