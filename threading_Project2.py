import threading
import queue
import math
import time

def is_prime_thread(thr_number):
    """Is it prime number?"""
    if thr_number<=1:
        return False
    for i in range(2,int(thr_number**0.5)+1):
        if thr_number % i == 0:
            return False
        
    return True

def HI_prime_thread(PrimeQueue):
    """Computes the highest prime number in a given amount of time 
        (3 min in this application)"""
    init_time = time.time()
    thread_num = 0

    while time.time()-init_time< 1:
        if is_prime_thread(thread_num):
            thread_HI_prime_num = thread_num
            
        thread_num += 1
    
    PrimeQueue.put(thread_HI_prime_num)

def fibonacci_HI_prime_thr (thr_hi_prime,FibQueue):
    """Calculates the fibonacci of the highest prime number"""
    if thr_hi_prime <= 1:
        FibQueue.put(thr_hi_prime)
    current_thr, next_thr = 0 , 1
    for _ in range(2,thr_hi_prime + 1):
        current_thr, next_thr = next_thr, current_thr + next_thr
        
    
    FibQueue.put(next_thr)


def factorial_of_HI_prime_thr (thr_hi_prime_num,FactQueue):
    """calculates the factorial of the highest prime number"""
    

    FactQueue.put(math.factorial(thr_hi_prime_num))

if __name__ == "__main__":

    HI_prime_queue = queue.Queue()
    fibonacci_queue = queue.Queue()
    factorial_queue = queue.Queue()


    thr1 = threading.Thread(target=HI_prime_thread,args=(HI_prime_queue))
    
    thr1.start()
    thr1.join()
    
    thr2 = threading.Thread(target=fibonacci_HI_prime_thr,args=(HI_prime_queue,fibonacci_queue))
    
    thr3 = threading.Thread(target=factorial_of_HI_prime_thr,args=(HI_prime_queue,factorial_queue))
    

    thr2.start()
    thr3.start()

    thr2.join()
    thr3.join()

    thr_HIprime_number = HI_prime_queue.get()
    thr_fibonacci_number = fibonacci_queue.get()
    thr_factorial_number = factorial_queue.get()


    
    print(f"The Highest Prime Number: {thr_HIprime_number}\n\nFibonacci Number:{thr_fibonacci_number}\n\nFactorial:{thr_factorial_number}")
    
    
