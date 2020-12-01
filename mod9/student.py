class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)
    
    def __eq__(self, comp):
        if self.name == comp.name:
            return True
        else:
            return False

    def __lt__(self, comp):
        if self.name < comp.name:
            return True
        else:
            return False
        
    def __ge__(self, comp):
        if self.name >= comp.name:
            return True
        else:
            return False

    def getName(self):
        """Returns the student's name."""
        return self.name
  
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]
   
    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self._scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)
 
    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))

def main():
    """A simple test."""
    student = Student("Ken", 5)
    student2 = Student("Sam", 6)
    student3 = Student("Sam", 7)
    student4 = Student("Liz", 8)
    
    # should return false
    print(student.__eq__(student2))
    # should return true
    print(student2.__eq__(student3))
    # should return false
    print(student3.__lt__(student4))
    # should return true
    print(student4.__ge__(student))
if __name__ == "__main__":
    main()