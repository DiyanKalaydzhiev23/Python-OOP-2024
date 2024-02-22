class Employee:
    MONTHS = 12

    def __init__(self, _id: int, first_name: str, last_name: str, salary: float):
        self.id = _id
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_full_name(self) -> str:
        return self.first_name + " " + self.last_name

    def get_annual_salary(self) -> float:
        return self.salary * Employee.MONTHS

    def raise_salary(self, amount: float) -> float:
        self.salary += amount
        return self.salary


employee = Employee(744423129, "John", "Smith", 1000)
print(employee.get_full_name())
print(employee.raise_salary(500))
print(employee.get_annual_salary())

