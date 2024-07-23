import argparse
import logging


def logger_decorator(function):
    def wrapper(*args, **kwargs):
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(name)s - %(message)s')
        logger = logging.getLogger()
        logger.info(f"Function started")
        result = function(*args, **kwargs)
        logger.info(f"Function finished")
        return result

    return wrapper


@logger_decorator
def generate_primes(n):
    for i in range(2, n):
        if is_prime(i):
            yield i


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def print_primes(n):
    primes = generate_primes(n)
    print(f"Prime numbers less than {n}:")
    for prime in primes:
        print(prime)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate prime numbers less than a given integer and print them")
    parser.add_argument("-n", type=int, required=True, help="Specify the integer")
    args = parser.parse_args()

    print_primes(args.n)
