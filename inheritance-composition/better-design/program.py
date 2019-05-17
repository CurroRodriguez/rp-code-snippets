import hr
import employee
import productivity
import contacts

manager = employee.Manager(1, 'Mary Poppins', 3000)
manager.address = contacts.Address('121 Admin Rd', 'Concord', 'NH', '03301')
secretary = employee.Secretary(2, 'John Smith', 1500)
secretary.address = contacts.Address('67 Paperwork Ave.', 'Manchester', 'NH', '03101')
sales_guy = employee.SalesPerson(3, 'Kevin Bacon', 1000, 250)
factory_worker = employee.FactoryWorker(4, 'Jane Doe', 40, 15)
temporary_secretary = employee.TemporarySecretary(5, 'Robin Williams', 40, 9)
employees = [
    manager,
    secretary,
    sales_guy,
    factory_worker,
    temporary_secretary,
]
productivity_system = productivity.ProductivitySystem()
productivity_system.track(employees, 40)
payroll_system = hr.PayrollSystem()
payroll_system.calculate_payroll(employees)
