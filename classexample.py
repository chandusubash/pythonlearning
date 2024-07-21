class Human:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    def do_work(self):
        if self.occupation=="tennis player":
            print(self.name, " : Plays tennis")
        elif self.occupation=="actor":
            print(self.name, " : is an actor")
        else:
            print("we dont know what ", self.name, " does")

    def speaks(self):
        print(self.name, " says hello")


tom = Human("tom cruise", "actor")
nadal = Human("rafael nadal", "tennis player")
chandu = Human("chandu subash", "IT professional")

tom.do_work()
nadal.do_work()
chandu.do_work()

tom.speaks()
nadal.speaks()
chandu.speaks()
