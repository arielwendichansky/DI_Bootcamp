create database Week11_Day1

CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50),
    location_id INT
);

CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department_id INT,
    salary DECIMAL(10, 2),
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

CREATE TABLE locations (
    location_id INT PRIMARY KEY,
    city VARCHAR(50),
    country VARCHAR(50)
);

INSERT INTO departments (department_id, department_name, location_id) VALUES
(1, 'HR', 100),
(2, 'Finance', 200),
(3, 'IT', 300),
(4, 'Marketing', 400),
(5, 'Sales', 500);

INSERT INTO employees (employee_id, first_name, last_name, department_id, salary) VALUES
(1, 'John', 'Doe', 1, 60000),
(2, 'Jane', 'Smith', 2, 80000),
(3, 'Jim', 'Brown', 3, 90000),
(4, 'Jake', 'White', 4, 70000),
(5, 'Jill', 'Green', 5, 75000),
(6, 'Jack', 'Black', 3, 95000),
(7, 'Jerry', 'Gray', 2, 82000);

INSERT INTO locations (location_id, city, country) VALUES
(100, 'New York', 'USA'),
(200, 'London', 'UK'),
(300, 'San Francisco', 'USA'),
(400, 'Berlin', 'Germany'),
(500, 'Paris', 'France');

-- Task: Find the employee details who have the highest salary in each department.

SELECT e.employee_id, e.first_name, e.last_name, e.salary, e.department_id
FROM (SELECT department_id, MAX(salary) as max_salary
							FROM employees 
							GROUP BY department_id)t
JOIN employees e ON e.department_id = t.department_id AND e.salary = t.max_salary
JOIN departments d ON e.department_id = d.department_id;


					   
