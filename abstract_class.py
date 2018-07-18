from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def Cal_sal(self, sal):
        pass

class Developer(Employee):

    def Cal_sal(self,sal):
        sal=sal+10
        return sal


emp = Developer()
print(emp.Cal_sal(10000))
