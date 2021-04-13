# memoization
# this memo to make the recursive count 1 time only
# first take the memo
def fib(n, memo={}):
    # if the n is inside the memo that has been passed in inside the function it will auto return the result value
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    # so every value will be stored and wont count 2 time
    # store the value of the fibonnanci count inside the memo with n value stored
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

# same as prior this use memoization take the n and m position and store inside memo to remove duplicate count inside the recursive function


def gridTraveler(m, n, memo={}):
    key = f'{str(m)},{str(n)}'
    if key in memo:
        return memo[key]
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    memo[key] = gridTraveler(m-1, n, memo) + gridTraveler(m, n-1, memo)
    return memo[key]

# on this one store the true and false for each targetsum that has been count and store the true and false value so when they reach the same data the result is already there
# cache all the data that has been looped inside the value


def canSum(targetSum, numbers, memo={}):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False
    for num in numbers:
        remainder = targetSum - num
        if canSum(remainder, numbers, memo) == True:
            memo[targetSum] = True
            return True
    memo[targetSum] = False
    return False


print(canSum(300, [7, 14]))
print(canSum(7, [2, 2, 3, 1]))
print(gridTraveler(2, 3))
print(gridTraveler(3, 3))
print(gridTraveler(18, 18))


print(fib(100))
