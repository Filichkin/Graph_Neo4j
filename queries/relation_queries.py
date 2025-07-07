employee_order = '''
LOAD CSV WITH HEADERS FROM
'file:///Order.csv'
AS line
MATCH (order:Order {orderID: line.OrderID})
MATCH (employee:Employee {employeeID: line.EmployeeID})
CREATE (employee)-[:SOLD]->(order);
'''
