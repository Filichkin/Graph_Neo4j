query_product = '''
LOAD CSV WITH HEADERS FROM
'file:///Product.csv'
AS line FIELDTERMINATOR ','
MERGE (product:Product {productID: line.ProductID})
  ON CREATE SET product.productName = line.ProductName,
  product.UnitPrice = toFloat(line.UnitPrice);
'''

query_order = '''
LOAD CSV WITH HEADERS FROM
'file:///Order.csv'
AS line FIELDTERMINATOR ','
CALL {
  WITH line
  MERGE (order:Order {orderID: line.OrderID})
  ON CREATE SET order.ShipName = line.ShipName, order.Quantity = line.Quantity
} IN TRANSACTIONS OF 10000 ROWS
'''

query_supplier = '''
LOAD CSV WITH HEADERS FROM
'file:///Supplier.csv'
AS line FIELDTERMINATOR ','
CALL {
  WITH line
  MERGE (supplier:Supplier {supplierID: line.SupplierID})
  ON CREATE SET supplier.companyName = line.CompanyName
} IN TRANSACTIONS OF 10000 ROWS
'''

query_category = '''
LOAD CSV WITH HEADERS FROM
'file:///Category.csv'
AS line FIELDTERMINATOR ','
CALL {
  WITH line
  MERGE (c:Category {categoryID: line.CategoryID})
  ON CREATE SET c.categoryName = line.CategoryName,
  c.description = line.Description
} IN TRANSACTIONS OF 10000 ROWS
'''

query_employee = '''
LOAD CSV WITH HEADERS FROM
'file:///Employee.csv'
AS line FIELDTERMINATOR ','
CALL {
  WITH line
  MERGE (e:Employee {employeeID:line.EmployeeID})
  ON CREATE SET e.firstName = line.FirstName,
  e.lastName = line.LastName, e.post = line.Post
} IN TRANSACTIONS OF 10000 ROWS
'''

queries_data_upload = [
    query_product,
    query_category,
    query_employee,
    query_order,
    query_supplier
    ]
