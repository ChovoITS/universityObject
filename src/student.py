class student ():
    def __init__ (self, name, surname, hours, qpoints):
        self.name = name
        self.surname = surname
        self.hours = float(hours)
        self.qpoints = float(qpoints)
    
    def __str__(self):
        return f""
    
    def __repr__(self):
        return f""
    
    def getName (self):
        return self.name
    
    def setName (self, name):
        self.name = name
    
    def getSurname (self):
        return self.surname
    
    def setSurname (self, surname):
        self.surname = surname

    def getHours (self):
        return self.hours
    
    def setHours (self, hours):
        self.hours = hours
    
    def getQPoints (self):
        return self.qpoints
    
    def setQPoints (self, qpoints):
        self.qpoints = qpoints
    
    def getGPA(self):
        return self.qpoints/self.hours