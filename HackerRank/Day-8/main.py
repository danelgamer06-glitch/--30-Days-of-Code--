import sys


def solve():
    # Read all input data at once
    input_data = sys.stdin.read().split()

    if not input_data:
        return

    # First value is the number of contacts
    n = int(input_data[0])
    phone_book = {}

    idx = 1

    # Store n contacts
    for _ in range(n):
        name = input_data[idx]
        phone = input_data[idx + 1]
        phone_book[name] = phone
        idx += 2

    # Process queries until End of File (EOF)
    while idx < len(input_data):
        query = input_data[idx]
        if query in phone_book:
            print(f"{query}={phone_book[query]}")
        else:
            print("Not found")
        idx += 1


if __name__ == "__main__":
    solve()

