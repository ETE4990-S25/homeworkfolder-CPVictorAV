#asynchronous modules

import asyncio
import time
import nest_asyncio
import sys
import math


sys.set_int_max_str_digits(100000000) # increases the limit of digits in integer string

nest_asyncio.apply() # allows async main to run

async def is_prime(number):
    """Is it prime number?"""
    # this is from the given code in the prompt
    if number<=1:
        return False
    for i in range(2,int(number**0.5)+1):
        if number % i == 0:
            return False
        
    return True

async def HI_prime():
    """Computes the highest prime number in a given amount of time 
        (3 min in this application)"""
    init_time = time.time()
    asynch_num = 0

    while time.time()-init_time<1: # runtime of 3 min is too big to compute
        if await is_prime(asynch_num):
            HI_prime_num = asynch_num
            
        asynch_num += 1
    
    return HI_prime_num

async def fibonacci_HI_prime (hi_prime):
    """Calculates the fibonacci of the highest prime number"""
    if hi_prime <= 1:
        return hi_prime
    current, next = 0 , 1
    for _ in range(2,hi_prime + 1):
        current, next = next, current + next
        
    await asyncio.sleep(0)
    return next


async def factorial_of_HI_prime (hi_prime_num):
    """calculates the factorial of the highest prime number"""
    await asyncio.sleep(0)

    return math.factorial(hi_prime_num)


async def main():

    prime_task = asyncio.create_task(HI_prime()) #async task list 1
    prime_HI = await prime_task # outputs function output
    fib_task = asyncio.create_task(fibonacci_HI_prime(prime_HI)) # async task list 2
    fact_task = asyncio.create_task(factorial_of_HI_prime(prime_HI)) # async task list 3
    
    if prime_HI > 0: #when prime_HI is done it can compute list 2 and 3
        fib_number = await fib_task
        factorial_calc = await fact_task

    print(f"The Highest Prime Number: {prime_HI}\n\nFibonacci Number:{fib_number}\n\nFactorial:{factorial_calc}")


         

    
    
asyncio.run(main())

