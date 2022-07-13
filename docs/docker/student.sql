BEGIN;
CREATE TABLE student(
    id serial,
    name text NOT NULL,
    course text NOT NULL,
    age integer NOT NULL,
    address text NOT NULL
);
COMMIT;