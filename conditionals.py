# The Following are "if " statements in doffrent scenarios

enemy = "goblin"

#On the bottom the "!=" means not equal to or if is NOT
if enemy != "dragon":
    print("charge forward")


player_health = 75

if player_health <= 100:
    print("drink a health posion")



magic_stones = 12

if 10 <= magic_stones <= 20:
    print("you've unlocked the elven chest")


is_daytime = False
dragon_asleep = True

if not is_daytime and dragon_asleep:
    print("sneak into the dragon's lair to retrive the golden chalice!")
