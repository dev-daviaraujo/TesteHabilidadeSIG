QUERY_VENDAS = '''
SELECT 
    soh.SalesOrderID,
    soh.OrderDate,
    soh.TotalDue,
    sp.Name AS Region,
    p.Name AS ProductName,
    sod.OrderQty,
    sod.UnitPrice
FROM Sales.SalesOrderHeader AS soh
INNER JOIN Sales.SalesOrderDetail AS sod
    ON soh.SalesOrderID = sod.SalesOrderID
INNER JOIN Production.Product AS p
    ON sod.ProductID = p.ProductID
INNER JOIN Person.Address AS a
    ON soh.ShipToAddressID = a.AddressID
INNER JOIN Person.StateProvince AS sp
    ON a.StateProvinceID = sp.StateProvinceID
ORDER BY soh.OrderDate DESC;
'''