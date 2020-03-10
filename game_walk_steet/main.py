import game

# make places details
arsen = game.Place("Arsen")
arsen.set_description("A big market with food in the center near Freedom square.")

lvivski_kruasany = game.Place("Lvivski kruasany")
lvivski_kruasany.set_description("A nice cafe near Freedom square.")

opera_theater = game.Place("Opera theater")
opera_theater.set_description("An exciting and cultural place near Freedom square.")

celentano = game.Place("pizza Celentano")
celentano.set_description("A nice cafe near Freedom square.")

fountain_near_Opera_theater = game.Place("Fountain near Opera theater")
fountain_near_Opera_theater.set_description("A fountain near Opera theater.")

zhorzh = game.Place("Hotel \"Zhorzh\"")
zhorzh.set_description("An expensive hotel near Freedom square.")

finish = game.Place("Finish")

# make link_place details
arsen.link_place(lvivski_kruasany, "north")

lvivski_kruasany.link_place(arsen, "south")
lvivski_kruasany.link_place(opera_theater, "west")

opera_theater.link_place(lvivski_kruasany, "east")
opera_theater.link_place(celentano, "west")

celentano.link_place(opera_theater, "south")
celentano.link_place(fountain_near_Opera_theater, "north")

fountain_near_Opera_theater.link_place(celentano, "south")
fountain_near_Opera_theater.link_place(zhorzh, "north")

zhorzh.link_place(fountain_near_Opera_theater, "south")
zhorzh.link_place(finish, "north")


# make characters details
dave = game.Walker("Dave", "Your friend from the university")
dave.set_conversation("Hello, guy! How are you ? Could you give me a chocolate ?")
# dave.set_weakness("cheese")
arsen.set_character(dave)

kavaler = game.Walker("Kavaler", "A man who entertains a woman in company, accompanies her during a walk, etc.")
kavaler.set_conversation("I am a polite man to girls.")
lvivski_kruasany.set_character(kavaler)

zbuy = game.Walker("Zbuy", "Robber, robber.")
zbuy.set_conversation("Give me your money or I will urge you to take Math exams!")
zbuy.set_weakness("karate")

zhorzh.set_character(zbuy)

batiar = game.Walker("Batiar", "Gravis, a drunkard, a popular late-19th-early-20th-century, brutal woman")
batiar.set_conversation("The last glass was enough.")
celentano.set_character(batiar)

laidak = game.Walker("Laidak", "Poor homeless man.")
laidak.set_conversation("Give me some money and I will start new busyness.")
fountain_near_Opera_theater.set_character(laidak)


# make items details
beer = game.Item("a glass of beer")
beer.set_description("Tool from batiar")
opera_theater.set_item(beer)

karate = game.Item("karate")
karate.set_description("Marshial art to protect yourself")
lvivski_kruasany.set_item(karate)

chocolate = game.Item("chocolate")
chocolate.set_description("Treatment for your friends")
arsen.set_item(chocolate)

money = game.Item("money")
money.set_description("Resource for new busyness")
fountain_near_Opera_theater.set_item(money)

current_place = arsen
backpack = []

dead = False

while dead == False:

    print("\n")
    if current_place.name == "Finish":
        print("Congratulations, you have finished the long road!")
        dead = True

    else:
        current_place.get_details()

        inhabitant = current_place.get_character()
        if inhabitant is not None:
            inhabitant.describe()

        item = current_place.get_item()
        if item is not None:
            item.describe()

        command = input("> ")

        if command in ["north", "south", "east", "west"] and command in current_place.link_place_directions:
            # Move in the given direction
            current_place = current_place.move(command)

        elif command == "talk":
            # Talk to the inhabitant - check whether there is one!
            if inhabitant is not None:
                inhabitant.talk()
        elif command == "fight":
            if inhabitant is not None:
                # Fight with the inhabitant, if there is one
                print("What will you fight with?")
                fight_with = input().lower()

                # Do I have this item?
                if fight_with in backpack:

                    if inhabitant.fight(fight_with) == True:
                        # What happens if you win?
                        print("Hooray, you won the fight!")
                        current_place.character = None

                    else:
                        # What happens if you lose?
                        print("Oh dear, you lost the fight.")
                        print("That's the end of the game")
                        dead = True
                else:
                    print("You don't have a " + fight_with + ' or you can not fight with him,'
                                                             ' because it is your friend')
            else:
                print("There is no one here to fight with")
        elif command == "take":
            if item is not None:
                print("You put the " + item.get_name() + " in your backpack")
                backpack.append(item.get_name())
                current_place.set_item(None)
            else:
                print("There's nothing here to take!")

        elif command == "give":
            # Give a thing to the inhabitant, if there is one
            print("What will you give ?")
            give_thing = input().lower()

            # Do I have this item?
            if give_thing in backpack:
                print("Oh dear, thank you!")
                backpack.remove(give_thing)

            else:
                print("You do not have this thing in your backpack")

        else:
            print("I don't know how to " + command)
            print("Or enter other direction from place information")
