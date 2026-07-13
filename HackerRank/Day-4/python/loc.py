class Person:
    def __init__(self, initialAge):
        # Check if initialAge is valid
        if initialAge < 0:
            print("Age is not valid, setting age to 0.")
            self.age = 0
        else:
            self.age = initialAge

    def amIOld(self):
        # Classify the person's age category
        if self.age < 13:
            print("You are young.")
        elif 13 <= self.age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")

    def yearPasses(self):
        # Increment the age of the person
        self.age += 1

# --- Code to execute in Visual Studio Code ---
if __name__ == "__main__":
    print("--- HackerRank: Day 4 - Classes vs. Instances ---")
    try:
        t = int(input("Enter the number of test cases (e.g., 2): "))
        for i in range(0, t):
            age = int(input(f"Enter age for person {i+1}: "))         
            p = Person(age)  
            p.amIOld()
            for j in range(0, 3):
                p.yearPasses()       
            p.amIOld()
            print("")
    except ValueError:
        print("Please enter valid numbers.")
