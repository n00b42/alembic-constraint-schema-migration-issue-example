-- CREATE USER legacy WITH PASSWORD 'legacy'; -- already done by docker image
-- CREATE DATABASE mydatabase WITH OWNER legacy; -- already done by docker image
-- GRANT ALL PRIVILEGES ON DATABASE mydatabase to legacy; -- already done by docker image

CREATE TABLE users (id int PRIMARY KEY, name varchar NOT NULL);
INSERT INTO users VALUES (1, 'Aaa'), (2, 'Bbb');
CREATE USER myuser WITH PASSWORD 'myuser';
CREATE SCHEMA myschema AUTHORIZATION myuser;
GRANT REFERENCES (id) ON public.users TO myuser;