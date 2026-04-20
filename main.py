owner_name = []
kilometre = []

def load_data():
    with open("services.txt", "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            name,km = line.split(",")
            owner_name.append(name.strip().lower())
            kilometre.append(km.strip())


def show_all():
    print(f"\n {'Name':<20}{'Kilometres':<15}{'Service Urgency'}")
    print("-" * 50)
    for name , km in zip(owner_name, kilometre):
        int_km = int(km)
        if int_km < 5000:
            urgency = "No Service Needed"
        elif int_km < 10000:
            urgency = "Service Due Soon"
        else:
            urgency = "Service Overdue"
        print(f"{name.title():<20}{km:<15}{urgency}")



def save_data():
    with open("services.txt", "w") as file:
        for name, km in zip(owner_name, kilometre):
            file.write(f"{name},{km}\n")

def add_customer():
    name = input("Enter name:").strip().lower()

    if name in owner_name:
        print(f"{name} is already exist in the list")
    else:
        km = input("Enter km:")
        owner_name.append(name)
        kilometre.append(km)
        save_data()
        print(f"{name.title()} added successfully")

def update_kilometre():
    name = input("Enter your name:").strip().lower()
    if name in owner_name:
        index = owner_name.index(name)
        print(f"Current Kilometres: {kilometre[index]}")
        km = int(input("Enter new km:"))
        kilometre[index] = km
        save_data()
        print(f"{name.title()} kilometres updated successfully.")
    else:
        print(f"{name} is not on the list")

def delete_customer():
    name = input("Enter name you would like to delete:").lower().strip()
    if name in owner_name:
        index = owner_name.index(name)
        km = kilometre[index]

        with open("deleted.txt", "a") as file:
            file.write(f"{name},{km}\n")

        owner_name.pop(index)
        kilometre.pop(index)

        save_data()

        print(f"{name.title()} deleted successfully!")
    else:
         print(f"{name.title()} not found. Please try again!")


def show_menu():
    print("\n===== MECHANIC SERVICE PROGRAM =====")
    print("1. Show all customers")
    print("2. Add new customer")
    print("3. Update kilometres")
    print("4. Delete customer")
    print("5. Exit")
    print("=====================================")

load_data()

while True:
    show_menu()
    choice = input("Enter your choice(1-5)").strip()

    if choice == "1":
        show_all()
    elif choice == "2":
        add_customer()
    elif choice == "3":
        update_kilometre()
    elif choice == "4":
        delete_customer()
    elif choice == "5":
        print("Goodbye")
        break
    else:
        print("Please enter invalid number")

