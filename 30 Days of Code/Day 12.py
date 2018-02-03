class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores) :
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores

    def calculate(self) :
        avg = sum(self.scores) / len(self.scores)
        if avg >= 90 :
            return 'O'
        elif avg >= 80 :
            return 'E'
        elif avg >= 70 :
            return 'A'
        elif avg >= 55 :
            return 'P'
        elif avg >= 40 :
            return 'D'
        else :
            return 'T'
