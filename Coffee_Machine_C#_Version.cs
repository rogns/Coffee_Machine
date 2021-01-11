using System;

namespace ConsoleApp3
{
    class CoffeeMachine
    {
        static int cups = 9;
        static int water = 400; // ml
        static int milk = 540;  // grams
        static int cbeans = 120; // grams
        static float money;

        public void status()
        {
            Console.WriteLine("The coffee machine has:\n" +
                        water + " ml of water\n" + milk + " ml of milk\n" +
                        cbeans + " g of coffee beans\n" + cups + " of disposable cups\n" +
                        money + " of money");
        }

        public void necessary_suplies()
        {
            Console.WriteLine("Write how many cups of coffee you will need: ");
            int num_cups = Convert.ToInt32(Console.ReadLine());
            
            Console.WriteLine("For " + num_cups + " cups of coffee you will need:\n" +
                        num_cups * 200 + " ml of water\n" + num_cups * 50 + " ml of milk\n" +
                        num_cups * 15 + " g of coffee beans\n");
        }

        public void buy_espresso()
        {
            if (water >= 250)
            {
                if (cbeans >= 16)
                {
                    if (cups >= 1)
                    {
                        Console.WriteLine("I have enough resources, making you a coffee!");
                        water -= 250;
                        cbeans -= 16;
                        cups -= 1;
                        money += 4;
                    }
                    else
                    {
                        Console.WriteLine("Sorry, not enough cups!");
                    }
                }
                else
                {
                    Console.WriteLine("Sorry, not enough coffee beans!");
                }
            }
            else
            {
                Console.WriteLine("Sorry, not enough water!");
            }
        }

        public void buy_latte()
        {
            if (water >= 350)
            {
                if (cbeans >= 20)
                {
                    if (cups >= 1)
                    {
                        if (milk >= 75)
                        {
                            Console.WriteLine("I have enough resources, making you a coffee!");
                            water -= 350;
                            cbeans -= 20;
                            cups -= 1;
                            milk -= 75;
                            money += 7;
                        }
                        else
                        {
                            Console.WriteLine("Sorry, not enough milk!");
                        }
                    }
                    else
                    {
                        Console.WriteLine("Sorry, not enough cups!");
                    }
                }
                else
                {
                    Console.WriteLine("Sorry, not enough coffee beans!");
                }
            }
            else
            {
                Console.WriteLine("Sorry, not enough water!");
            }
        }

        public void buy_cappuccino()
        {
            if (water >= 200)
            {
                if (cbeans >= 12)
                {
                    if (cups >= 1)
                    {
                        if (milk >= 100)
                        {
                            Console.WriteLine("I have enough resources, making you a coffee!");
                            water -= 200;
                            cbeans -= 12;
                            cups -= 1;
                            milk -= 100;
                            money += 6;
                        }
                        else
                        {
                            Console.WriteLine("Sorry, not enough milk!");
                        }
                    }
                    else
                    {
                        Console.WriteLine("Sorry, not enough cups!");
                    }
                }
                else
                {
                    Console.WriteLine("Sorry, not enough coffee beans!");
                }
            }
            else
            {
                Console.WriteLine("Sorry, not enough water!");
            }
        }

        public void fill()
        {
            Console.WriteLine("Write how many ml of water do you want to add: ");
            water += Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Write how many ml of milk do you want to add: ");
            milk += Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Write how many grams of coffee beans do you want to add: ");
            cbeans += Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Write how many disposable cups of coffee do you want to add: ");
            cups += Convert.ToInt32(Console.ReadLine());
        }

        public void run()
        {
            string option;
            Console.WriteLine("Write action (buy, fill, take, remaining, exit): ");
            option = Console.ReadLine();

            if (option == "buy")
            {
                int option_buy;
                Console.WriteLine("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, 4 - back to main menu: ");
                option_buy = Convert.ToInt32(Console.ReadLine());
                if (option_buy == 1)
                {
                    buy_espresso();
                    run();
                }
                else if (option_buy == 2)
                {
                    buy_latte();
                    run();
                }
                else if (option_buy == 3)
                {
                    buy_cappuccino();
                    run();
                }
                else if (option_buy == 4)
                {
                    run();
                }
            }
            else if (option == "fill")
            {
                fill();
                run();
            }
            else if (option == "take")
            {
                Console.WriteLine("I gave you " + money);
                money = 0;
                run();

            }
            else if (option == "remaining")
            {
                status();
                run();
            }
            else if (option == "exit")
            {
                System.Environment.Exit(0);
            }
            else
            {
                Console.WriteLine("Error. Please try again.");
                run();
            }
        }

        static void Main(string[] args)
        {
            CoffeeMachine mycoffee = new CoffeeMachine();
            mycoffee.run();
                
        }
    }
}
