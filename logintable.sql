BEGIN;
CREATE TABLE login (username TEXT, fullname TEXT, email TEXT, password TEXT);
COMMIT;

BEGIN;
INSERT INTO login values('belleten', 'Albert Ruiz Bellet', 'albert.rb@gmail.com', 'maxpower');
INSERT INTO login values('erik', 'Eric Mas Moncusi', 'eric.mas@gmail.com', 'papitolover');
INSERT INTO login values('maikel', 'Maik Mika Mikael', 'mikaelmi@gmail.com', 'pitufosmakineros');
COMMIT;
