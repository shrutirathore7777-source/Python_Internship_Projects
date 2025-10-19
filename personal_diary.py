import os 
def diary_app():
    filename = "mydiary.txt"
    while True:
        print("\n Personal diary")
        print("1. Add New Entry")
        print("2.View All entries")
        print("3.Search Enteries by word")
        print("4.Delete all enteries")
        print("5.Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            date = input("Enter date (DD/MM/YYYY): ")
            entry = input("Write your diary entry: ")
            with open(filename,"a") as f:
                f.write(f"\n Date : {date} \nEntry: {entry}\n{'-'*40}\n")
        elif choice == "2":
            print("Your diary enteries:")
            try:
                with open(filename, "r") as f :
                    content = f.read()
                    if content.strip() == "":
                        print("No enteries yet!")
                    else:
                        print(content)
            except FileNotFoundError:
                print("Diary not found yet!")
        elif choice == "3":
            keyword = input("Enter keyword to search: ")
            try:
                with open(filename , "r") as f:
                    found = False
                    for line in f:
                        if keyword.lower() in line.lower():
                            print(line.strip())
                            found = True
                        if not found :
                            print("No matching entry found")
            except FileNotFoundError:
                print("Diary not found!")
        elif choice == "4":
            confirm = input("Are you sure you want to delete all enteries?")
            if confirm == "yes":
                if os.path.exists(filename):
                    os.remove(filename)
                    print("All entries deleted!")
            else :
                print("deletion cancelled")
        elif choice == "5":
            print("Goodbye! Exiting Diary....")
            break
        else :
            print("Invalid choice! Try agian.")
diary_app()