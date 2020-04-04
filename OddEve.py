# ------Odd-Even-Cricket-Game------
import random

f_i = input("Enter s to start or q to exit: ").lower()

while f_i != "q":
    def play():
        usr_inp = int(input("Enter your number: "))
        cpu_inp = random.randint(1, 6)
        print(f'''your number is {usr_inp}, and the computer's number is {cpu_inp}''')
        return [usr_inp, cpu_inp]


    def toss():
        odd = input("Enter o for odd or e for even: ").lower()
        is_odd = odd == "o"
        vals = play()
        if (vals[0]+vals[1]) % 2 == 0:
            if is_odd:
                print("You have lost the toss :( ")
                return False
            else:
                print("You have won the toss! ")
                return True
        else:
            if is_odd:
                print("You have won the toss! ")
                return True
            else:
                print("You have lost the toss :( ")
                return False


    def bat_or_ball():
        if toss():
            b_o_b = int(input("Enter 1 to bat first or 0 to bowl first: "))
            bat = b_o_b == 1
            wickets = int(input("Enter the number of wickets: "))
            return [bat, wickets]
        else:
            select = bool(random.getrandbits(1))
            wickets = random.randint(1, 3)
            if select:
                bob = "bat"
            else:
                bob = "bowl"
            print(f"Computer chooses to {bob} for {wickets} wicket(s). ")
            return [bob != "bat", wickets]


    bob_ = bat_or_ball()


    class Player:

        def __init__(self, wickets, runs=0):
            self.runs = runs
            self.wickets = wickets

        def inn(self):
            while self.wickets > 0:
                turn = play()
                if turn[0] == turn[1]:
                    print("OUT!")
                    self.wickets -= 1
                else:
                    self.runs += turn[0]


    usr = Player(bob_[1])
    cpu = Player(bob_[1])

    for i in range(0, 2):
        if bob_[0]:
            usr.inn()
            print(f'''Your runs: {usr.runs}''')
            bob_[0] = False

        else:
            cpu.inn()
            print(f'''Computer's runs: {cpu.runs}''')
            bob_[0] = True
        print("End of innings")

    print(f'''Your runs are: {usr.runs} and the computer's runs are: {cpu.runs}''')
    if usr.runs > cpu.runs:
        print("YOU WIN! ")
    elif usr.runs == cpu.runs:
        print("Draw")
    else:
        print("You lose:( ")
    f_i = input("Enter q to quit or s to play again: ").lower()
