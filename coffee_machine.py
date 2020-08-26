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
        self.run()

    def buy_espresso(self):
        if self.water >= 250:
            if self.cbeans >= 16:
                if self.disp_cups >= 1:
                    print("I have enough resources, making you a coffee!")
                    self.water -= 250;
                    self.cbeans -= 16;
                    self.money += 4;
                    self.disp_cups -= 1;
                    self.run()
                else:
                    print("Sorry, not enough cups!"); self.run()
            else:
                print("Sorry, not enough coffee beans!"); self.run()
        else:
            print("Sorry, not enough water!"); self.run()

    def buy_latte(self):
        if self.water >= 350:
            if self.milk >= 75:
                if self.cbeans >= 20:
                    if self.disp_cups >= 1:
                        print("I have enough resources, making you a coffee!")
                        self.water -= 350;
                        self.milk -= 75;
                        self.cbeans -= 20;
                        self.money += 7;
                        self.disp_cups -= 1;
                        self.run()
                    else:
                        print("Sorry, not enough cups!"); self.run()
                else:
                    print("Sorry, not enough coffee beans!"); self.run()
            else:
                print("Sorry, not enough milk!"); self.run()
        else:
            print("Sorry, not enough water!"); self.run()

    def buy_cappuccino(self):
        if self.water >= 200:
            if self.milk >= 100:
                if self.cbeans >= 12:
                    if self.disp_cups >= 1:
                        print("I have enough resources, making you a coffee!")
                        self.water -= 200;
                        self.milk -= 100;
                        self.cbeans -= 12;
                        self.money += 6;
                        self.disp_cups -= 1;
                        self.run()
                    else:
                        print("Sorry, not enough cups!"); self.run()
                else:
                    print("Sorry, not enough coffee beans!"); self.run()
            else:
                print("Sorry, not enough milk!"); self.run()
        else:
            print("Sorry, not enough water!"); self.run()

    def fill(self):
        add_water = int(input("Write how many ml of water do you want to add: "))
        self.water += add_water
        add_milk = int(input("Write how many ml of milk do you want to add: "))
        self.milk += add_milk
        add_cbeans = int(input("Write how many grams of coffee beans do you want to add:"))
        self.cbeans += add_cbeans
        add_cups = int(input("Write how many disposable cups of coffee do you want to add:"))
        self.disp_cups += add_cups
        self.run()

    def run(self):
        x = str(input("Write action (buy, fill, take, remaining, exit): "))
        if x == "buy":
            opt = str(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:"))
            if opt == "1":
                self.buy_espresso()
            elif opt == "2":
                self.buy_latte()
            elif opt == "3":
                self.buy_cappuccino()
            elif opt == "back":
                self.run()
            else:
                print("Invalid Option.")
                self.run()
        elif x == "fill":
            self.fill()
        elif x == "take":
            print("I gave you", self.money); self.money = 0; self.run()
        elif x == "remaining":
            self.print_status()
        elif x == "exit":
            return 0
        else:
            print("Invalid option. Try again."), self.run()


your_coffee = CoffeeMachine()
your_coffee.run()
