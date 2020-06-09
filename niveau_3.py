tickets = [
            "t#### #i### ####r 1##",
            "r##### d##### ###### ####0",
            "### ane ### ###0",
            "### ### ### 1#",
            "####e #####y r## ###0",
            "r##### r## r## ###"
          ]

animals = ["ane", "baleine", "caribou", "chat", "cheval", "chien", "coq", "daim", "lapin", "lion", "loutre", "rat", "tigre"]

prices = [5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]

class Calculator():
    def __init__(self, tickets, animals):
        self.tickets = tickets
        self.animals = animals
        self.winnings = 0
        self.result_list = []
        self.prices = prices


    def splitter(self):
        self.tickets = [x.split(" ") for x in self.tickets]

    def len_checker(self):
        self.splitter()
        self.tickets = [x for x in self.tickets if len(x[0]) == len(x[1]) == len(x[2])]
        self.prices = [x.pop() for x in self.tickets]
        print(self.tickets)
    def animal_checker(self):
        self.len_checker()
        for i in self.tickets:
            stripped = ""
            fitting_animals = [animal for animal in self.animals if len(animal) == len(i[0])]
            for zone in i:
                stripped += zone.strip("#")
            self.result_list.append(self.is_true(stripped, fitting_animals))

    def is_true(self, stripped, fitting_values):
        stripped = list(stripped)
        fitting_values = [str(i) for i in fitting_values]
        for fits in fitting_values:
            if all(x in fits for x in stripped):
                return True
        return False

    def money_time(self):
        won_misterious = []

        for i in range(len(self.result_list)):
            if self.result_list[i] == True:
                won_misterious.append(self.prices[i])

        for moneys in won_misterious:
            possible_money = [x for x in prices if len(str(x)) == len(moneys)]
            for price in possible_money:
                if moneys[0] == str(price)[0] and moneys[0] != "#":
                    self.winnings += price
            if moneys[0] == "#":
                self.winnings += max(possible_money)

        print(self.winnings)



calc = Calculator(tickets, animals)

calc.animal_checker()
calc.money_time()
