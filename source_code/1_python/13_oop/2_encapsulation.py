class Account:
    def __init__(self, owner, balance):
        self.owner = owner        # public
        self._balance = balance   # "internal" by convention
        self.__pin = "4471"       # name-mangled, hard to reach
 
acc = Account("Ahmed", 1000)
acc.owner          # "Ahmed" — fine, it's public
acc._balance       # works, but signals "you shouldn't"
# acc.__pin          # AttrsibuteError — mangled to _Account__pin
acc._Account__pin  # Would work: 4471