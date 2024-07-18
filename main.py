import random
heresies = ['pelagian', 'arian', 'nestorian', 'modalism', 'unitarian']
r = random.choice(heresies)
class Theologian:
    doTrinity = True
    doBible = True
    christian = True

class Calvin(Theologian):
    CALVINIST = True
    T = True
    U = True
    L = True
    I = True
    P = True

    def question(self):
        d = input("Do you believe the T.U.L.I.I.P? ").lower()
        if d == "yes":
            print("you're elect congrats")
        elif d == "no":
            print(f"you're not elect and anathema'd for being {r}")
        else:
            print("OOF")
c = Calvin()
c.question()