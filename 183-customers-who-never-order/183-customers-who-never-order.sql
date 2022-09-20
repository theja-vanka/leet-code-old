# Write your MySQL query statement below

SELECT cust.name as Customers FROM Customers AS cust
WHERE cust.id NOT in (
    SELECT ord.customerId FROM Orders AS ord
);