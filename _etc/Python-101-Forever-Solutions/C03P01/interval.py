import sys
from pprint import pprint

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def is_inside(self, value):
        return self.start <= value <=  self.end

    def stringify(self):
        start_symbol = "["
        end_symbol = "]"

        return f"{start_symbol}{self.start}, {self.end}{end_symbol}"

    def __str__(self):
        return self.stringify() 

    def __repr__(self) -> str:
        return self.stringify()


interval_1 = Interval(1,20)
# pprint(sys.path[0])
pprint(interval_1.stringify())
# pprint(interval_1.is_inside(15))
pprint(interval_1.__str__())
pprint(str(interval_1))
pprint(interval_1)




