
q = True
while q:
    dir = input("You are in a room. Choose a direction to move in (north, south, east, west): ")


    match dir:
        case "north":
            ans =input("You move north and find a river. What will you do? (swim/build a raft): ")
            if ans == "swim":
                print("You swim across the river and find a hidden treasure.")
                x = input("Would you like to continue playing?")
                if x == "no":
                    break
            if ans == "build a raft":
                print("You build a raft and discover a mysterious lake.")
                x = input("Would you like to continue playing?")
                if x == "no":
                    break
        case "south":
            ans = input("You move south and discover a dense forest. What will you do? (climb a tree/walk deeper): ")
            if ans == "climb a tree":
                print("You climb a tree and discover a hidden village.")
                x = input("Would you like to continue playing?")
                if x == "no":
                    break
            if ans == "walk deeper":
                print("You walk deeper into the forest and find an abandoned cabin.")
                x = input("Would you like to continue playing?")
                if x == "no":
                    break
        case "east":
            ans = input("You move east and encounter a mountain. What will you do? (climb the mountain/go around it): ")
            if ans == "climb the mountain":
                print("You climb the mountain and talk to a wizard.")
                x = input("Would you like to continue playing?")
                if x == "no":
                    break
            if ans == "go around it":
                print("You go around it into a eerie cavern.")
                x = input("Would you like to continue playing?")
                if x == "no":
                    break
        case "west":
            ans = input("You move west and stumble upon a cave. What will you do? (enter the cave/walk past it): ")
            if ans == "enter the cave":
                print("You enter the cave and find a sleeping dragon.")
                x = input("Would you like to continue playing?")
                if x == "no":
                    break
            if ans == "walk past it":
                print("You see a troll near a bridge and walk past it.")
                x = input("Would you like to continue playing?")
                if x == "no":
                    break


print("Thank you for playing!")