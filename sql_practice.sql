CREATE TABLE IF NOT EXISTS regions    (
    id uuid PRIMARY KEY,
    name VARCHAR
);

CREATE TABLE IF NOT EXISTS locations    (
    id uuid PRIMARY KEY,
    address VARCHAR,
    region_id uuid NOT NULL,
    FOREIGN KEY(region_id) REFERENCES regions(id)
);

CREATE TABLE IF NOT EXISTS departments   (
    id uuid PRIMARY KEY,
    name VARCHAR,
    location_id uuid NOT NULL,
    manager_id uuid NOT NULL,
    FOREIGN KEY(location_id) REFERENCES locations (id)
);

CREATE TABLE IF NOT EXISTS employees  (
    id uuid PRIMARY KEY,
    name VARCHAR,
    last_name VARCHAR,
    hire_date DATE,
    email VARCHAR,
    salary INTEGER,
    manager_id uuid NOT NULL,
    department_id uuid NOT NULL,
    FOREIGN KEY(department_id) REFERENCES departments (id),
    FOREIGN KEY(manager_id) REFERENCES employees (id)
);

Alter TABLE departments add FOREIGN KEY (manager_id) REFERENCES employees (id);

-- Показать работников у которых нет почты или почта не в корпоративном домене (домен dualbootpartners.com)
Select * from Employees
where Employees.Email is null or Employees.Email not like '%dualbootpartners.com';

-- Получить список работников нанятых в последние 30 дней
SELECT * from employees
where employees.hire_date > (CURRENT_DATE - INTERVAL '30 day');

-- Найти максимальную и минимальную зарплату по каждому департаменту
SELECT min(salary) as minimum, max(salary) as maximum from employees
GROUP by employees.department_id;

-- Посчитать количество работников в каждом регионе
SELECT count(*), regions.name FROM employees
left join departments on departments.id = employees.department_id
left join locations on locations.id = departments.location_id
left join regions on regions.id = locations.region_id
group by regions.name;

-- Показать сотрудников у которых фамилия длиннее 10 символов
SELECT last_name from employees
where LENGTH(last_name) > 9

-- Показать сотрудников с зарплатой выше средней по всей компании
SELECT employees.* from employees
where employees.salary >= ((SELECT sum(salary) from employees) / (SELECT COUNT(id) from employees))
