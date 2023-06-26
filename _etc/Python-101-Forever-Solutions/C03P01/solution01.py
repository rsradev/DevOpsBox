class Interval:
    def __init__(self, start, end, start_opened=False, end_opened=False):
        self.start =  start
        self.end = end
        self.start_opened = start_opened
        self.end_opened = end_opened
    
    def is_inside(self, value):
        if self.start_opened and self.end_opened:
            return self.start < value < self.end
        elif self.start_opened:
            return self.start <= value < self.end
        elif self.end_opened:
            return self.start < value <= self.end
        return self.start <= value <= self.end
    
    def stringify(self):
        start = "["
        end =  "]"
        if self.start_opened:
            start = "("
        elif self.end_opened:
            end_opened = ")"
        return f"{start}{self.start},{self.end}{end}"

        



test_interval = Interval(1,10)

print(test_interval.is_inside(1))

print(test_interval.stringify()=="[1,10]")
