
# app.py

def greet(name):
    return f"Hello, {name}! Welcome to AWS CI/CD Pipeline 🚀"

def add_numbers(a, b):
    return a + b

def main():
    print(greet("Anish"))

    result = add_numbers(5, 7)
    print(f"Addition Result: {result}")

if __name__ == "__main__":
    main()
