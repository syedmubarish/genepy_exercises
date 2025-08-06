class Parent:
    def __init__(self,name):
        self.name = name
        self.child_list = []

    def add_child(self,value):
        self.child_list.append(value)
    
    def get_mean_child(self):
        mean = 0
        for value in self.child_list:
            mean += value.get_mean()
        
        return mean/len(self.child_list)
        
    def get_best(self):
        max = 0
        best = None
        for i in self.child_list:
            mean = i.get_mean()
            if mean>max:
                best = i
        
        return best
    

class Student(Parent):
    
    
    def add_exam(self,grade:float):
        self.add_child(grade)
    
    def get_mean(self):
        return sum(self.child_list)/len(self.child_list)
    

class School(Parent):
    
    def add_student(self,student):
        self.add_child(student)
        
    def get_mean(self):
        return self.get_mean_child()
        
    def get_best_student(self):
        return self.get_best()
    
    

class City(Parent):
    
    def add_school(self,school):
        self.add_child(school)
        
    def get_mean(self):
        return self.get_mean_child()
        
    def get_best_school(self):
        return self.get_best()
        
    def get_best_student(self):
        current_best = self.child_list[0]
        for school in self.child_list:
            current_best_student_mean = current_best.get_best_student().get_mean()
            iterating_best_student_mean = school.get_best_student().get_mean()
            if current_best_student_mean < iterating_best_student_mean:
                current_best = school
        
        return school.get_best_student()