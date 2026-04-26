use northwind;
show tables;
select * from customers;
select distinct Country from customers;
select distinct CustomerName, ContactName, Address from customers;
select count(distinct Country) from customers;
select * from customers where Country = 'Mexico';
select CustomerName from customers where CustomerID = 1;
select * from customers where CustomerID >= 50;
select * from customers where CustomerID between 50 and 60;
select * from customers where City LIKE 's%';
select * from customers where City IN ('Paris', 'London');
select * from products order by Price, CategoryID, SupplierID;
select * from products order by Price desc, CategoryID desc, SupplierID desc;
select * from products order by Price desc;
select * from customers where Country = 'UK' and City = 'London';
select * from customers where Country = 'Germany' and (City = 'Berlin' or City = 'Stuttgart');
select count(*) from customers where not Country = 'Germany';
select * from customers where not Country = 'Germany';
select * from customers where Country is not null;
select * from customers where not Country = 'Germany' and not Country = 'USA';
select * from customers where CustomerName not like 'A%';
select * from customers where CustomerID NOT between 10 and 100;
select * from customers where City not in ('Paris','London');
select * from customers where not CustomerID > 50;
-- INSERT INTO "keyword"
/* THis is a multi line comment.
This is the second line comment. */
-- The INSERT INTO statement is used to insert new records in a table.
insert into customers
values (92, 'Aarush Singh', 'ROBOT X', 'localhost', 'Patna', '811105', 'India');
select count(*) from customers;
select * from customers where CustomerID = 92;
insert into customers
values ('93', 'Aarush Singh', 'ROBOT X', 'localhost', 'Patna', '811105', 'India');
select * from customers where CustomerID = 93;
insert into Customers (CustomerName, City, Country) values ('Cardinal', 'Stavangar', 'Norway');
select * from customers;
-- inserting multiple values
insert into Customers (CustomerName, ContactName, Address, City, PostalCode, Country)
values
("Rahul Kumar", 'Golu', 'R.K Nagar', 'Patna', '800027', 'India'),
('Golu Prasad', 'Rahul', 'R.K Nagar', 'BiharSharif', 803101, 'India');

select * from Customers;
select * from Customers order by CustomerID desc limit 3;
select * from customers where PostalCode is null;
update customers set CustomerName = 'Aarush X', City = 'Patliputra' where CustomerID = 92;
commit;
select * from Customers;
update Customers set PostalCode = 0000 where CustomerId = 92;
select * from Customers;
commit;
delete from Customers where CustomerID = 92;
select * from Customers;
rollback;
update Customers set CustomerName = 'Aarush X' where CustomerID = 92;
select * from customers;
rollback;
commit;
select * from customers;
-- delete from table_name     ---> deletes all records
-- drop table table_name ====>> delete the entire table along with schema
commit;
select CustomerName from customers where CustomerID = 92;
select * from customers limit 3;
select * from customers limit 3 offset 3;
select * from customers where Country = 'Germany' limit 3;
select * from customers order by Country limit 3;
select min(Price) as smallestprice from products;
select min(Price) from products;
select min(BirthDate) as earliestbirthday from employees;
select max(Price) as largestPrice from Products;
select max(BirthDate) as LatestBirthDate from employees;
select * from customers order by CustomerID desc limit 1;
select count(*) from customers;
select count(distinct City) from customers;
select count(City) from customers;
select count(ProductID) from Products where Price > 20;
select sum(Quantity) from OrderDetails;
select sum(Quantity) from OrderDetails where ProductId = 11;
select avg(Price) from Products;
select avg(Price) from Products where CategoryID = 1;
select * from Products where price > (select avg(price) from Products);
select * from Customers where CustomerName LIKE 'aa%';
select * from Customers where Country in ('Germany', 'France', 'UK');
select * from Customers where Country not in ('Germany', 'France', 'UK');
select * from Customers where CustomerID in (select CustomerID from Orders);
SELECT * FROM Customers WHERE CustomerID NOT IN (SELECT CustomerID FROM Orders);
select * from Products where Price BETWEEN 10 and 20;
select * from Products where Price between 10 and 20 and CategoryID in (1,2,3);
select CustomerID as ID, CustomerName as Customer from Customers;
select CustomerName as Customer, ContactName as "Contact Person" from Customers;
select CustomerName, concat_ws(', ',Address, PostalCode, City, Country) as Address from Customers;
select CustomerName, concat(' ',Address, PostalCode, City, Country) as Address from Customers;
-- fetching data from multiple tables using alias
select o.OrderID, o.OrderDate, c.CustomerName from Customers as c, Orders as o where c.CustomerName='Around the Horn' and c.CustomerID = o.CustomerID;
select orders.OrderID, orders.OrderDate, customers.CustomerName from customers, orders where customers.CustomersName = 'Around the Horn' and customers.CustomerID = orders.CustomerID;
select Orders.OrderID, Customers.CustomerName, Orders.OrderDate from Orders inner join Customers on Orders.CustomerID=Customers.CustomerID;
select Orders.OrderID, Customers.CustomerName, Orders.OrderDate from customers inner join orders on Orders.CustomerID=Customers.CustomerID;
select orders.OrderID, customers.CustomerName, shippers.ShipperName from orders inner join customers on orders.CustomerID = customers.CustomerID inner join shippers on orders.ShipperID = shippers.ShipperID;

-- The LEFT JOIN clause returns all rows from the left table (table1), and only the matched rows from the right table. If there is no match in the right table, the result for the columns from the right table will be NULL.
select customers.CustomerName, orders.OrderDate from customers left join orders on customers.CustomerID = orders.CustomerID order by customers.CustomerName;
select * from customers left join orders on customers.CustomerID = orders.CustomerID order by customers.CustomerName;
select customers.CustomerName, orders.OrderID from customers left join orders on customers.CustomerID = orders.CustomerID where orders.CustomerID is null;
select orders.OrderDate, employees.FirstName, employees.LastName from orders right join employees on orders.EmployeeID = employees.EmployeeID order by orders.OrderID;
-- cross join
select customers.CustomerName, orders.OrderID from customers cross join orders;
select customers.CustomerName, orders.OrderID from customers cross join orders where customers.CustomerID = orders.CustomerID;
select A.CustomerName as CustomerName1, B.CustomerName as CustomerName2, A.City from Customers A, Customers B where A.CustomerID <> B.CustomerID and A.City = B.City order by A.City;
-- UNION
select city from customers
union
select city from suppliers
order by city;

select city, country from customers where country = 'Germany'
union
select city, country from suppliers
where country = 'Germany'
order by city;

select 'Customer' as Type, ContactName, City, Country from Customers
UNION
select 'Supplier', ContactName, City, Country
FROM Suppliers;

select city from customers
union all
select city from suppliers
order by city;

select city, country from customers where country='Germany' union all select city, country from suppliers where country='Germany' order by City;

select country, count(customerid) as 'number of customers' from customers group by country;
select country, count(customerid) as 'Number of Customers' from customers group by country order by count(customerid) desc;
select shippers.shippername, count(orders.orderid) as 'Number of Orders' from orders left join shippers on orders.shipperid = shippers.shipperid group by shippername;

select country, count(customerid) as 'number of customers' from customers group by country having count(customerid) > 5 order by count(customerid) desc;
select employees.lastname, count(orders.orderid) as numberOfOrders from (orders inner join employees on orders.EmployeeID = Employees.employeeid) group by lastname having count(orders.orderid) > 10;