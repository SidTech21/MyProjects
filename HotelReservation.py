#Hotel Reservation  system

#it shows the condition of the rooms 
def summary(rooms):
    available = rooms.count("Available")
    booked = rooms.count("Booked")
    print("\nRoom Summary:")
    print(f"Available rooms: {available}")
    print(f"Booked rooms: {booked}")

#it shows the rooms are available or not 
def check_available(rooms):
    print("\nAvailable Rooms:")
    for room_number in range(len(rooms)):
        if rooms[room_number] == "Available":
            print(f"Room {room_number + 1} is Available")
        else:
            print("Rooms not available")


#use for booking 
def book_room(rooms):
    room_number = int(input("Enter the room number to book: ")) - 1
    if room_number >= 0 and room_number < len(rooms):
        if rooms[room_number] == "Available":
            rooms[room_number] = "Booked"
            print(f"Room {room_number + 1} is now booked!")
        else:
            print(f"Room {room_number + 1} is already booked.")
    else:
        print("Invalid room number.")


#for cancelation o
def cancel_room(rooms):
    room_number = int(input("Enter the room number to cancel booking: ")) - 1
    if room_number >= 0 and room_number < len(rooms):
        if rooms[room_number] == "Booked":
            rooms[room_number] = "Available"
            print(f"Booking for Room {room_number + 1} has been canceled.")
        else:
            print(f"Room {room_number + 1} is not currently booked.")
    else:
        print("Invalid room number.")



def main():
    num_rooms = int(input("Enter the number of rooms in the hotel: "))
    rooms = ["Available"] * num_rooms  

    while True:
        
        print("\nHotel reservation system")
        print("1. Check room availability")
        print("2. Book a room")
        print("3. Cancel a booking")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        
        if choice == "1":
            check_available(rooms)
        elif choice == "2":
            book_room(rooms)
        elif choice == "3":
            cancel_room(rooms)
        elif choice == "4":
            print("Thank you for using the Hotel Room Booking System!")
            break
        else:
            print("Invalid choice. Please try again.")

        summary(rooms)



if __name__ == "__main__":
    main()
