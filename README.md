# largest-number-generated-from-combination-of-a-list-of-integers

In this code, I have solved a problem, where the input is a list of integers and the output will be the maximum number that can be generated by the permutation of the integers present in the list.

For example, [394,71,40,792,517] will give output 7927151740394 

To solve this problem, I have defined a function named: IsGreaterOrEqual(digit, max_digit). Which will take digit and max_digit as input and will return True if the permutation of digit and max_digit generates a bigger number than the permutation of max_digit and digit. Otherwise it will return False.

Now, I have defined a function largest_number which will take the list of integers as input. And it will iterate through the list and will check if all the sequential elements return True for the function IsGreaterOrEqual. For example, this will check IsGreaterOrEqual(a[0],a[1]), then IsGreaterOrEqual(a[1],a[2]) where a is the input list.
So if all the checkings return True, then the list will stay as is, which is the best case here. But when it will return False for any sequence, it will swap the sequence so that it returns True the next time. So it will keep swaping the elements as long as any of the sequences returns False and will continue this until all the sequences return True, giving us the required sequence.

Another function is defined as largest_numbercopied. Which is basically another way of solving this problem and which I found in the github repo of 'anoubhav'. Where he iterated through the input list and stored the present maximum value (Which will be the first element of the output list) in a variable named max_digit and removed that element from the input list. Thus looping through the input list until it gets totally empty, will eventually give the correct and required output.

To turn this output list into a concatenated string, we just create and empty list, iterate through the output list and add the elements as str typecasting and append the newly created stringlist.

stresstest function:

I have created a stresstest function here to check that both of the algorithms are working correctly and giving the same outputs. So in this function I have generated a random list of integers using random.randint and returned 'ok' if both algorithms give same result. I have checked it for 100 times and those two returned the same results. The constraints are: The size of the list will be in between 1 and 100 (including) and the elements of the list will be at most 1000 and at least 1.

timecounter function:

The timecounter function that I have created here creates random list of integers same as the stresstest function and outputs the time consumed to run both of the algorithms along with a comparison of which one is faster for a variable number of times which is an input to the timeit function with a variable named 'number'. In my code I have run it for 1000 times to compare the results and seems like the second algorithm is the faster one.
