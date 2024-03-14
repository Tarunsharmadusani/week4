class student:
    def check_pass_fail(self):
       if self.marks >= 40:
        return true
     else:
        return False

student1 = student()
student1.name = "Harry"
student1.marks = 85

did_pass = student1.check_pass_fail()
print(did_pass)

student2 = student()
student2.name = "janet"
student2.marks = 30


