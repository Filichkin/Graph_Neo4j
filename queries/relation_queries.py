employee_order = '''
LOAD CSV WITH HEADERS FROM
'file:///Order.csv'
AS line
MATCH (order:Order {orderID: line.OrderID})
MATCH (employee:Employee {employeeID: line.EmployeeID})
CREATE (employee)-[:SOLD]->(order);
'''

order_product = '''
LOAD CSV WITH HEADERS FROM
'file:///Order.csv'
AS line
MATCH (order:Order {orderID: line.OrderID})
MATCH (product:Product {productID: line.ProductID})
MERGE (order)-[op:PURCHASED]->(product)
  ON CREATE SET op.quantity = toFloat(line.Quantity);
'''

supplier_product = '''
LOAD CSV WITH HEADERS FROM
'file:///Product.csv'
AS line
MATCH (product:Product {productID: line.ProductID})
MATCH (supplier:Supplier {supplierID: line.SupplierID})
MERGE (supplier)-[:SUPPLIES]->(product);
'''

product_category = '''
LOAD CSV WITH HEADERS FROM
'file:///Product.csv'
AS line
MATCH (product:Product {productID: line.ProductID})
MATCH (category:Category {categoryID: line.CategoryID})
MERGE (product)-[:IS_CATEGORY]->(category);
'''
