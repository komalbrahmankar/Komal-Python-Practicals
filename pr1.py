Assignment No : 1 
 Problem Statement: Design and implement a simple reflex agent for the Vacuum Cleaner world and analyze its rational behaviour in given environment. 
 
def display_rooms(roomA, roomB, location): 
 
    print("\n----------------------------") 
    print("Current Environment") 
    print("----------------------------") 
    print("Room A :", roomA) 
    print("Room B :", roomB) 
    print("Vacuum Location :", location) 
    print("----------------------------") 
 
 
roomA = input("Enter Room A Status (Clean/Dirty): ").capitalize() 
roomB = input("Enter Room B Status (Clean/Dirty): ").capitalize() 
location = input("Enter Vacuum Location (A/B): ").upper() 
count = 0 
 
display_rooms(roomA, roomB, location) 
 
print("\nActions Performed") 
 
while roomA == "Dirty" or roomB == "Dirty": 
 
    if location == "A": 
        if roomA == "Dirty": 
            print("Room A is Dirty -> clean") 
            count += 1 
            roomA = "Clean" 
        else: 
            print("Room A is Clean -> Move Right") 
            count += 1 
            location = "B" 
    elif location == "B": 
        if roomB == "Dirty": 
            print("Room B is Dirty -> clean") 
            count += 1 
            roomB = "Clean" 
        else: 
            print("Room B is Clean -> Move Left") 
            count += 1 
 
            location = "A" 
display_rooms(roomA, roomB, location) 
 
print("Both rooms are clean.") 
print("Action: NO OP (Stop)") 
print("Total Actions Performed:", count) 
 
 
