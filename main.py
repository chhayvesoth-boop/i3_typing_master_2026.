def main():
    print("------------ Welcome to I3 Typing Master v2026 -----------")
    print("To begin, please select one of the following options:")
    print("1. Login")
    print("2. Register")
    print("3. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == '1':
        print("Redirecting to Login...")
    elif choice == '2':
        print("Redirecting to Registration...")
    elif choice == '3':
        print("Exiting. Goodbye!")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
