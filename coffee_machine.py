class CoffeeMachine:

    water = int(400)
    milk = int(540)
    cbeans = int(120)
    disp_cups = int(9)
    money = int(550)

    def print_status(self):
        print("The coffee machine has:\n",
              self.water, "ml of water\n", self.milk, "ml of milk\n",
              self.cbeans, "g of coffee beans\n", self.disp_cups, "of disposable cups\n",
              "$", self.money, "of money")

    def purchase(self):
        x = str(input("Write action (buy, fill, take, remaining, exit): "))
        if x == "buy":
            opt = str(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:"))
            if opt == "1":
                if self.water >= 250:
                    if self.cbeans >= 16:
                        if self.disp_cups >= 1:
                            print("I have enough resources, making you a coffee!")
                            self.water -= 250; self.cbeans -= 16; self.money += 4; self.disp_cups -= 1; self.purchase()
                        else: print("Sorry, not enough cups!"); self.purchase()
                    else: print("Sorry, not enough coffee beans!"); self.purchase()
                else: print("Sorry, not enough water!"); self.purchase()
            elif opt == "2":
                if self.water >= 350:
                    if self.milk >= 75:
                        if self.cbeans >= 20:
                            if self.disp_cups >= 1:
                                print("I have enough resources, making you a coffee!")
                                self.water -= 350; self.milk -= 75; self.cbeans -= 20; self.money += 7;
                                self.disp_cups -= 1; self.purchase()
                            else: print("Sorry, not enough cups!"); self.purchase()
                        else: print("Sorry, not enough coffee beans!"); self.purchase()
                    else: print("Sorry, not enough milk!"); self.purchase()
                else: print("Sorry, not enough water!"); self.purchase()
            elif opt == "3":
                if self.water >= 200:
                    if self.milk >= 100:
                        if self.cbeans >= 12:
                            if self.disp_cups >= 1:
                                print("I have enough resources, making you a coffee!")
                                self.water -= 200; self.milk -= 100; self.cbeans -= 12; self.money += 6;
                                self.disp_cups -= 1; self.purchase()
                            else: print("Sorry, not enough cups!"); self.purchase()
                        else: print("Sorry, not enough coffee beans!"); self.purchase()
                    else: print("Sorry, not enough milk!"); self.purchase()
                else: print("Sorry, not enough water!"); self.purchase()
            elif opt == "back":
                self.purchase()
            else:
                print("Invalid Option.")
                self.purchase()
        elif x == "fill":
            add_water = int(input("Write how many ml of water do you want to add: "))
            self.water += add_water
            add_milk = int(input("Write how many ml of milk do you want to add: "))
            self.milk += add_milk
            add_cbeans = int(input("Write how many grams of coffee beans do you want to add:"))
            self.cbeans += add_cbeans
            add_cups = int(input("Write how many disposable cups of coffee do you want to add:"))
            self.disp_cups += add_cups
            self.purchase()
        elif x == "take":
            print("I gave you", self.money); self.money = 0; self.purchase()
        elif x == "remaining":
            self.print_status(), self.purchase()
        elif x == "exit":
            return 0
        else:
            print("Invalid option. Try again."), self.purchase()


your_coffee = CoffeeMachine()
your_coffee.purchase()
