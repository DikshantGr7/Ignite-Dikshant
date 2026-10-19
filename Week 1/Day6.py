import time
from contextlib import contextmanager
from datetime import datetime, timedelta

raw_date = "2026-03-15 14:30:00"
parsed_date = datetime.strptime(raw_date, "%Y-%m-%d %H:%M:%S")
formatted_date = parsed_date.strftime("%B %d, %Y at %I:%M %p")
print(f"1A. Datetime (Format) - Raw: '{raw_date}' -> Formatted: '{formatted_date}'")

now = datetime.now()
future_deadline = now + timedelta(days=7, hours=3)
days_remaining = (future_deadline - now).days
print(f"1B. Datetime (Timedelta) - Target Date: {future_deadline.strftime('%Y-%m-%d')}, Days ahead: {days_remaining}")


def make_multiplier(factor: int):
    def multiplier(number: int) -> int:
        return number * factor

    return multiplier


double = make_multiplier(2)
triple = make_multiplier(3)
print(f"2A. Closures - Double 5: {double(5)}, Triple 5: {triple(5)}")


def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start_time
        print(f"    [Decorator] {func.__name__} took {elapsed:.6f}s")
        return result

    return wrapper


@timer_decorator
def process_data(n: int):
    return sum(i * i for i in range(n))


computation_result = process_data(100000)
print(f"2B. Decorators - Execution Result: {computation_result}")


def fibonacci_generator(limit: int):
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1


fib_sequence = list(fibonacci_generator(6))
print(f"3A. Generators (Yield) - First 6 Fibonacci numbers: {fib_sequence}")

numbers = [10, 20, 30]
num_iterator = iter(numbers)
first_val = next(num_iterator)
second_val = next(num_iterator)
print(f"3B. Iterators (Manual Traversal) - Next 1: {first_val}, Next 2: {second_val}")


class ManagedFile:

    def __init__(self, filename: str, mode: str):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        print(f"    [Class Context] Opened file '{self.filename}'")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
            print(f"    [Class Context] Closed file '{self.filename}' safely")


with ManagedFile("demo_class.txt", "w") as f:
    f.write("Class-based context manager execution.")
print("4A. Context Manager (Class) - Write operation finished")


@contextmanager
def execution_block(label: str):
    print(f"    [Generator Context] Starting block: {label}")
    try:
        yield
    finally:
        print(f"    [Generator Context] Exiting block: {label}")


with execution_block("Database Transaction Simulation"):
    print("    [Inside Block] Performing query operations...")

print("4B. Context Manager (Generator) - Block finished")