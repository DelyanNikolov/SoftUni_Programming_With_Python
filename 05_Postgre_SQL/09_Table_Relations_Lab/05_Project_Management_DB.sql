CREATE TABLE clients(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE projects(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    client_id INT,
    project_lead_id INT
);

CREATE TABLE employees(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    project_id INT
);

ALTER TABLE projects
ADD CONSTRAINT fk_client
FOREIGN KEY (client_id) REFERENCES clients(id);

ALTER TABLE projects
ADD CONSTRAINT fk_project_lead
FOREIGN KEY (project_lead_id) REFERENCES employees(id);

ALTER TABLE employees
ADD CONSTRAINT fk_project_id
FOREIGN KEY (project_id) REFERENCES projects(id);