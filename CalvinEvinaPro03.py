def get_suffix(n):
    if 10 <= n % 100 <= 20:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    return suffix

def tribonacci(n, values):
    if n < len(values):
        if values[n] != 0:
            return values[n]
    ans = tribonacci(n - 1, values) + tribonacci(n - 2, values) + tribonacci(n - 3, values)
    values += [0] * (n - len(values) + 1)
    values[n] = ans
    return ans

def main():
    while True:
        try:
            user_input = int(input("Choose a positive integer (n): "))
            if user_input < 1:
                print("Exiting the program...")
                break

            values = [1, 1, 1]
            result = tribonacci(user_input - 1, values)  # n-1 to convert 1-based index to 0-based index
            suffix = get_suffix(user_input)
            print(f"The {user_input}{suffix} element of Tribonacci is {result}")
        except ValueError:
            print("Please enter a valid positive integer.")

if __name__ == "__main__":
    main()
