CREATE TABLE departments (
    dname VARCHAR2(20),
    dnum NUMBER PRIMARY KEY,
    managerssn CHAR(20),
    managerstartdate DATE
);
CREATE TABLE employee(
    fname VARCHAR2(20),
    middleinitial CHAR(1),
    lname VARCHAR2(20),
    SSN CHAR(20) PRIMARY KEY,
    Bdate DATE,
    Address VARCHAR2(50),
    Sex CHAR(6),
    Salary NUMBER,
    supervisorssn NUMBER,
    dno NUMBER
);



CREATE TABLE department_locations (
    dnumber NUMBER,
    dlocation VARCHAR2(20)
);





CREATE TABLE project (
    pname VARCHAR2(20),
    pnumber NUMBER,
    plocation VARCHAR2(20),
    dnum NUMBER
);

CREATE TABLE works_on(
    essn CHAR(20),
    pno NUMBER,
    hours NUMBER
);

CREATE TABLE dependent(
    essn CHAR(20),
    Dependent_name VARCHAR2(20),
    sex CHAR(6),
    bdate DATE,
    relationship VARCHAR2(20)
);

--departments
INSERT INTO departments 
VALUES ('research',5,'333445555',TO_DATE('1988-05-22', 'YYYY-MM-DD'));

INSERT INTO departments 
VALUES ('administration',4,'987654321',TO_DATE('1995-01-01', 'YYYY-MM-DD'));

INSERT INTO departments 
VALUES ('headquarters',1,'888665555',TO_DATE('1981-06-19', 'YYYY-MM-DD'));

--end departments




--debug stuff here idk
SELECT * FROM departments WHERE dnumber = 5;
DELETE FROM departments WHERE dnumber = 5;
SELECT * FROM employee WHERE SSN = '123456789';
DELETE FROM employee WHERE SSN = '123456789';
--end dfebug


--employee
INSERT INTO employee 
VALUES ('john', 'b', 'smith', '123456789', TO_DATE('1965-01-09', 'YYYY-MM-DD'), '731 Fondren, Houston,TX', 'm', 30000,333445555,5); --og line: VALUES ('john', 'b', 'smith', '123456789', TO_DATE('1965-01-09', 'YYYY-MM-DD'), '731 Fondren, Houston,TX', 'm', 30000,'333445555', 5);

INSERT INTO employee
VALUES ('franklin', 't', 'wong', '333445555', TO_DATE('1955-12-08', 'YYYY-MM-DD'), '638 voss, houston,tx', 'm', 40000,888665555,5);

INSERT INTO employee
VALUES ('alicia', 'j', 'zelaya', '999887777', DATE '1968-07-19', '3321 castle,spring,tx', 'f', 25000,987654321,4);

INSERT INTO employee
VALUES ('jennifer', 's', 'wallace', '987654321', DATE '1941-06-20', '291 berry, bellaire, tx', 'f', 43000,888665555,4);

INSERT INTO employee 
VALUES ('ramesh', 'k', 'narayan', '666884444', DATE '1962-09-15', '975 fire oak, humble,tx', 'm', 38000,333445555,5);

INSERT INTO employee
VALUES ('joyce', 'a', 'english', '453453453', DATE '1972-07-31', '5631 rice, Houston, tx', 'f', 25000,333445555,5);

INSERT INTO employee
VALUES ('ahmad', 'v', 'jabbar', '987987987', DATE '1969-03-29', '980 dallas, houston tx', 'm', 25000,987654321,4);

INSERT INTO employee
VALUES ('james', 'e', 'borg', '888665555', DATE '1937-11-10', '450 stone, houston,tx', 'm', 55000,NULL,1);
--end employee



--department locations
INSERT INTO department_locations 
VALUES (1,'Houston');

INSERT INTO department_locations 
VALUES (4,'Stafford');

INSERT INTO department_locations 
VALUES (5,'Bellaire');

INSERT INTO department_locations 
VALUES (5,'Sugarland');

INSERT INTO department_locations
VALUES (5,'Houston');


--end department locations

--project but need to ask dugan abt foreign key
INSERT INTO project
VALUES ('ProductX',1,'Bellaire',5)

INSERT INTO project
VALUES ('ProductY',2,'Sugarland',5)

INSERT INTO project
VALUES ('ProductZ',3,'Houston',5)

INSERT INTO project
VALUES ('Computerization',10,'Stafford',4)

INSERT INTO project
VALUES ('Reorganization',20,'Houston',1)

INSERT INTO project
VALUES ('Newbenefits',30,'Stafford',4)
--end project

SELECT * FROM DEPARTMENTS WHERE DNUMBER =5






--need dugan
INSERT INTO WORKS_ON
VALUES ('123456789',1,32.5)

INSERT INTO WORKS_ON
VALUES ('123456789',2,7.5)

INSERT INTO WORKS_ON
VALUES ('666884444',3,40.0)

INSERT INTO WORKS_ON
VALUES ('453453453',1,20)

INSERT INTO WORKS_ON
VALUES ('453453453',2,20)

INSERT INTO WORKS_ON
VALUES ('333445555',2,10)

INSERT INTO WORKS_ON
VALUES ('333445555',3,10)

INSERT INTO WORKS_ON
VALUES ('333445555',10,10)

INSERT INTO WORKS_ON
VALUES ('333445555',20,10)

INSERT INTO WORKS_ON
VALUES ('999887777',30,30)

INSERT INTO WORKS_ON
VALUES ('999887777',10,10)

INSERT INTO WORKS_ON
VALUES ('987987987',10,35)

INSERT INTO WORKS_ON
VALUES ('987987987',30,5)

INSERT INTO WORKS_ON
VALUES ('987654321',30,20)

INSERT INTO WORKS_ON
VALUES ('987654321',20,15)

INSERT INTO WORKS_ON
VALUES ('123456789',20,NULL)

--end works on

--dependent
INSERT INTO DEPENDENT
VALUES ('333445555','Alice','F',TO_DATE('1988-04-05', 'YYYY-MM-DD'),'daughter')

INSERT INTO DEPENDENT
VALUES ('333445555','Theodore','M',TO_DATE('1983-10-25', 'YYYY-MM-DD'),'son')

INSERT INTO DEPENDENT
VALUES ('333445555','Joy','F',TO_DATE('1958-05-03', 'YYYY-MM-DD'),'spouse')

INSERT INTO DEPENDENT
VALUES ('987654321','Abner','M',TO_DATE('1942-02-28', 'YYYY-MM-DD'),'spouse')

INSERT INTO DEPENDENT
VALUES ('123456789','Michael','M',TO_DATE('1988-01-03', 'YYYY-MM-DD'),'son')

INSERT INTO DEPENDENT
VALUES ('123456789','Alice','F',TO_DATE('1988-12-30', 'YYYY-MM-DD'),'daughter')

INSERT INTO DEPENDENT
VALUES ('123456789','Elizabeth','F',TO_DATE('1967-05-05', 'YYYY-MM-DD'),'spouse')








--PRINT TABLES
SELECT * FROM EMPLOYEE;
SELECT * FROM DEPARTMENTS;
SELECT * FROM DEPARTMENT_LOCATIONS;
SELECT * FROM WORKS_ON;
SELECT * FROM DEPENDENT;
SELECT * FROM PROJECT;
--just need works on and dep locations too


--A
SELECT fname, lname
FROM employee, works_on, project
WHERE dno = 5
AND SSN = essn
AND pno = pnumber
AND pname = 'ProductX'
AND hours > 10;

--B
SELECT fname, lname
FROM employee , dependent 
WHERE fname = dependent_name;

--C
SELECT fname, lname
FROM employee 
WHERE supervisorssn = '333445555';

--D
SELECT pname, SUM(hours)
FROM project, works_on 
WHERE pnumber = pno
GROUP BY pname;

--E
SELECT dname, AVG(salary)
FROM departments, employee 
WHERE dnum = dno
GROUP BY dname;

--F
SELECT fname
FROM EMPLOYEE, (SELECT ESSN,COUNT(PNO) AS TOTAL
FROM WORKS_ON
GROUP BY ESSN)
WHERE TOTAL = (SELECT COUNT(PNAME) FROM PROJECT) AND SSN = ESSN

--G
SELECT AVG(salary) AS avg_salary
FROM employee
WHERE sex = 'f';


--H
SELECT fname, address, dno
FROM employee, DEPARTMENT_LOCATIONS
WHERE dno = dnumber AND dnumber NOT IN(SELECT dnumber 
FROM DEPARTMENT_LOCATIONS
WHERE dlocation = 'Houston')

--I
SELECT lname
FROM employee 
WHERE SSN = SUPERVISORSSN 
AND NOT EXISTS (
    SELECT *
    FROM dependent 
    WHERE essn = eSSN
);
--J
SELECT fname, lname
FROM employee
WHERE SSN NOT IN (SELECT essn FROM works_on);













