class CoffeeMachine:
    def __init__(self, water=0, milk=0, coffee_beans=0, disposable_cups=0, money=0):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.disposable_cups = disposable_cups
        self.money = money

    def __str__(self):
        return f'The coffee machine has:\n{self.water} ml of water\n{self.milk} ml of milk\n{self.coffee_beans} g of coffee beans\n{self.disposable_cups} disposable cups\n${self.money} of money\n'

    def action(self):
        action = input('Write action (buy, fill, take, remaining, exit):\n')
        if action == 'buy':
            self.buy()
        elif action == 'fill':
            self.fill()
        elif action == 'take':
            self.take()
        elif action == 'remaining':
            self.remaining()
        elif action == 'exit':
            self.exit()
        else:
            self.action()

    def buy(self):
        supplies_name = ['water', 'milk', 'coffee beans', 'disposable cups', 'money']
        supplies = ['water', 'milk', 'coffee_beans', 'disposable_cups', 'money']
        coffees = {'1': espresso, '2': latte, '3': cappuccino}
        kind = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        if kind == 'back':
            return self.action()
        else:
            trans = [vars(self)[i] - vars(coffees[kind])[i] for i in supplies]
            if any([i < 0 for i in trans]):
                lack = [supplies_name[i] for i in range(5) if trans[i] < 0]
                print(f'Sorry, not enough {lack[0]}!')
            else:
                print('I have enough resources, making you a coffee!')
                for i in supplies:
                    vars(self)[i] -= vars(coffees[kind])[i]
        return self.action()

    def fill(self):
        self.water += int(input('Write how many ml of water you want to add:'))
        self.milk += int(input('Write how many ml of milk you want to add:'))
        self.coffee_beans += int(input('Write how many grams of coffee beans you want to add:'))
        self.disposable_cups += int(input('Write how many disposable cups you want to add:'))
        return self.action()

    def take(self):
        print(f'I gave you ${self.money}\n')
        self.money = 0
        return self.action()

    def remaining(self):
        print(self.__str__())
        return self.action()

    def exit(self):
        pass


class Coffee:
    def __init__(self, water=0, milk=0, coffee_beans=0, disposable_cups=0, money=0):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.disposable_cups = disposable_cups
        self.money = money


coffee_machine = CoffeeMachine(water=400, milk=540, coffee_beans=120, disposable_cups=9, money=550)
espresso = Coffee(250, 0, 16, 1, -4)
latte = Coffee(350, 75, 20, 1, -7)
cappuccino = Coffee(200, 100, 12, 1, -6)

coffee_machine.action()
