import random

CABS = {
    1: ("Auto", 12),
    2: ("Sedan", 18),
    3: ("SUV", 25),
}

ROUTES = {
    1: ("Pune Station", "Shivajinagar", 5),
    2: ("Swargate", "Kothrud", 8),
    3: ("Hinjawadi", "Wakad", 10),
}


def read_choice(prompt):
    value = input(prompt).strip()
    if value.isdigit():
        return int(value)
    return None


def book_ride():
    print("\n--- Choose Cab Type ---")
    for num, (name, rate) in CABS.items():
        print(f"{num}. {name} (Rs.{rate}/km)")
    cab_choice = read_choice("Enter cab choice: ")
    if cab_choice not in CABS:
        print("Invalid cab choice. Returning to main menu.")
        return
    cab_name, rate = CABS[cab_choice]

    print("\n--- Choose Route ---")
    for num, (src, dest, km) in ROUTES.items():
        print(f"{num}. {src} -> {dest} ({km} km)")
    route_choice = read_choice("Enter route number: ")
    if route_choice not in ROUTES:
        print("Invalid route choice. Returning to main menu.")
        return
    source, destination, distance = ROUTES[route_choice]

    fare = rate * distance
    print("\n--- Ride Summary ---")
    print(f"Cab Type    : {cab_name}")
    print(f"Source      : {source}")
    print(f"Destination : {destination}")
    print(f"Distance    : {distance} km")
    print(f"Rate        : Rs.{rate}/km")
    print(f"Total Fare  : Rs.{fare}")

    while True:
        print("\n1. Confirm & Share OTP")
        print("2. Cancel Ride")
        confirm = read_choice("Enter choice: ")
        if confirm == 1:
            break
        elif confirm == 2:
            print("Ride cancelled. No OTP was shared. Returning to main menu.")
            return
        else:
            print("Invalid choice. Please enter 1 or 2.")

    otp = random.randint(1000, 9999)
    print(f"\nOTP shared with you: {otp}")
    print("NOTE: Ride cannot be cancelled after OTP is shared.")
    print("Booking confirmed! Your cab is on the way.")


def main():
    print("=== Welcome to Cab Booking Chatbot ===")
    while True:
        print("\n--- Main Menu ---")
        print("1. Book Ride")
        print("2. Exit")
        choice = read_choice("Enter your choice: ")

        if choice == 1:
            book_ride()
        elif choice == 2:
            print("Thank you for using Cab Booking Chatbot. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
