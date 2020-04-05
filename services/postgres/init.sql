DO
$do$
BEGIN
   IF NOT EXISTS (
      SELECT                       -- SELECT list can stay empty for this
      FROM   pg_catalog.pg_roles
      WHERE  rolname = 'drumrose_user') THEN

      CREATE ROLE drumrose_user LOGIN PASSWORD 'drumrose_password';
   END IF;
END
$do$;
CREATE DATABASE drumrose_db;
GRANT ALL PRIVILEGES ON DATABASE drumrose_db TO drumrose_user;
