CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department_id INT,
    salary DECIMAL(10, 2)
);

CREATE TABLE sales_data (
    sale_id INT PRIMARY KEY,
    employee_id INT,
    sales DECIMAL(10, 2),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);

INSERT INTO employees (employee_id, first_name, last_name, department_id, salary) VALUES
(1, 'John', 'Doe', 1, 60000),
(2, 'Jane', 'Smith', 2, 80000),
(3, 'Jim', 'Brown', 3, 90000),
(4, 'Jake', 'White', 4, 70000),
(5, 'Jill', 'Green', 5, 75000),
(6, 'Jack', 'Black', 3, 95000),
(7, 'Jerry', 'Gray', 2, 82000);

INSERT INTO sales_data (sale_id, employee_id, sales) VALUES
(1, 1, 1000),
(2, 2, 1500),
(3, 3, 2000),
(4, 4, 700),
(5, 5, 1300),
(6, 6, 1750),
(7, 7, 1200);

INSERT INTO employees (employee_id, first_name, last_name, department_id, salary) VALUES
(8, 'Sarah', 'Miller', 1, 62000),
(9, 'Michael', 'Johnson', 1, 58000),
(10, 'Linda', 'Lee', 2, 83000),
(11, 'David', 'Wilson', 3, 88000),
(12, 'Richard', 'Moore', 3, 92000),
(13, 'Karen', 'Taylor', 4, 65000),
(14, 'Nancy', 'Anderson', 4, 68000),
(15, 'Steven', 'Thomas', 5, 72000),
(16, 'Laura', 'Jackson', 5, 78000),
(17, 'Robert', 'White', 1, 61000),
(18, 'Susan', 'Harris', 2, 80000),
(19, 'James', 'Clark', 3, 96000),
(20, 'Patricia', 'Lewis', 4, 69000),
(21, 'Charles', 'Robinson', 5, 74000);


INSERT INTO sales_data (sale_id, employee_id, sales) VALUES
(8, 8, 1100),
(9, 9, 1050),
(10, 10, 1450),
(11, 11, 1900),
(12, 12, 1800),
(13, 13, 750),
(14, 14, 800),
(15, 15, 1250),
(16, 16, 1350),
(17, 17, 950),
(18, 18, 1150),
(19, 19, 1950),
(20, 20, 700),
(21, 21, 1300),
(22, 1, 500),
(23, 2, 1200),
(24, 3, 1600),
(25, 4, 300),
(26, 5, 1100),
(27, 6, 1500),
(28, 7, 900),
(29, 8, 1200),
(30, 9, 1150),
(31, 10, 1400),
(32, 11, 2100);

-- 1. Task: Use the ROW_NUMBER() function to list employees in each department, ordered by their salary in descending order. Display the department, employee name, and their salary rank within the department.

Select e.first_name, e.last_name, e.department_id, e.salary,
	row_number()Over(Partition By department_id order by salary Desc) as salary_rank
From employees as e;

-- 2. Task: Calculate the cumulative salary for employees in each department using the SUM() function with windowing.

Select e.first_name, e.last_name, e.department_id, e.salary,
	Sum(salary) over(partition by department_id order by salary desc) as salary_per_department
From employees as e;

-- 1. Task: Rank the sales performance of employees within each department using the DENSE_RANK() function. Display the department, employee name, and their sales rank.

Select e.first_name, e.last_name, e.department_id, e.salary,
	dense_rank() over (partition by department_id order by s.sales desc) as sales_rank
from employees as e 
join sales_data s on e.employee_id = s.employee_id					   


-- 2. Task: Calculate the total sales for each employee and the running total of sales across all employees using the SUM() function with windowing.





-- Exercise 1: Advanced Employee Analysis
-- 1. Task: Use the LAG() function to identify employees whose salary is less than their previous colleague's salary in the sorted list.

Select e.first_name, e.last_name, e.department_id, e.salary,
	LAG(e.salary, 1) over (Order BY salary DESC) as prevoius_salary
From employees e;

-- 2. Task: Use the SUM() function to calculate the cumulative salary for employees in each department using the ROWS frame specification.

Select e.first_name, e.last_name, e.department_id, e.salary,
	Sum(salary) over (order by salary rows between unbounded preceding and current row) as cumulative_salary
From employees e;

-- 3. Task: Create a CTE to rank employees by their sales performance within each department and filter out the top performers.

WITH EmployeesRank AS(
	Select e.first_name, e.last_name, e.department_id, e.salary, s.sales,
	Rank() OVER (Partition BY e.department_id order BY s.sales DESC) as sales_rank
	From employees e
	Join sales_data s ON e.employee_id = s.employee_id
)
Select * from EmployeesRank
Where sales_rank != 1;


-- Exercise 2: Sales Data Insights

-- 1. Task: Use the LEAD() function to identify employees who have lower sales compared to their next colleague in the sorted list.

Select e.first_name, e.last_name, e.department_id, e.salary,s.sales,
	LEAD(s.sales, 1) over (Order BY e.employee_id) as next_sale
From employees e
Join sales_data s on e.employee_id = s.employee_id;

-- 2. Task: Calculate the running total of sales for each employee using the SUM() function with the RANGE frame specification.

Select e.first_name, e.last_name, e.department_id, e.salary, s.sales,
	Sum(s.sales) over (order by e.employee_id range between unbounded preceding and current row) as running_total
From employees e
Join sales_data s on e.employee_id = s.employee_id;
