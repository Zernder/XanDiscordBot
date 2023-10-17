import os

def main():
    print("Welcome, Xanmal! Please select which bot you'd like to run:")
    print("1. Sakibot")
    print("2. Tamabot")
    
    choice = input("Enter the number of your choice: ")
    
    if choice == '1':
        os.system('python Sakibot.py')
    elif choice == '2':
        os.system('python Tamabot.py')
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
