import multiprocessing
from multiprocessing import Process, Value
import time
import math
import sys

sys.set_int_max_str_digits(100000000) # increases the limit of digits in integer string


def is_prime_multi(multi_number):
    """Is it prime number?"""
    if multi_number <= 1:
        return False
    for i in range(2, int(multi_number**0.5) + 1):
        if multi_number % i == 0:
            return False
    return True

def HI_prime_multi(multi_num, prime_result):
    """Computes the highest prime number"""
    multi_init_time = time.time()
    HI_prime_num_multi = multi_num
    while time.time() - multi_init_time < 1:
        if is_prime_multi(multi_num):
            HI_prime_num_multi = multi_num
        multi_num += 1
    prime_result.value = HI_prime_num_multi

def fibonacci_HI_prime_multi(hi_prime_num_multi, Multifibonacci_result):
    """Calculates the fibonacci of the highest prime number"""
    if hi_prime_num_multi <= 1:
        Multifibonacci_result.value = hi_prime_num_multi
        return
    current_multi, next_multi = 0, 1
    for _ in range(2, hi_prime_num_multi + 1):
        current_multi, next_multi = next_multi, current_multi + next_multi
    Multifibonacci_result.value = next_multi

def factorial_of_HI_prime_multi(hi_prime_multi_num, Multifact_result):
    """Calculates the factorial of the highest prime number"""
    Multifact_result.value = math.factorial(hi_prime_multi_num)

def main():
    multi_HI_prime_value = multiprocessing.Value('i', 0)
    multi_fibonacci_value = multiprocessing.Value('i', 0)
    multi_factorial_value = multiprocessing.Value('i', 0)

    process_1 = multiprocessing.Process(target=HI_prime_multi, args=(2, multi_HI_prime_value))
    process_1.start()
    process_1.join()

    process_2 = multiprocessing.Process(target=fibonacci_HI_prime_multi, args=(multi_HI_prime_value.value, multi_fibonacci_value))
    process_3 = multiprocessing.Process(target=factorial_of_HI_prime_multi, args=(multi_HI_prime_value.value, multi_factorial_value))
    process_2.start()
    process_3.start()
    process_2.join()
    process_3.join()

    print(f"The Highest Prime Value: {multi_HI_prime_value.value}\n\nFibonacci Number: {multi_fibonacci_value.value}\n\nFactorial Number: {multi_factorial_value.value}")

if __name__ == "__main__":
    main()
