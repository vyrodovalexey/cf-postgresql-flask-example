## CloudFoundry Example Application:  Python Flask, PostgreSQL

This is an example application which can be run on CloudFoundry. Application will create table ips (date varchar) in PostgreSQL. 
Every time when you will have an access to the application with browser, application will insert into the table ips your access time and show all users access times


### Usage

1. Login to CF

  ```bash
  cf login -a https://api.run.pivotal.io
  ```

2. Clone the app (i.e. this repo).

  ```bash
  git clone https://github.com/vyrodovalexey/cf-postgresql-flask-example.git
  cd cf-postgresql-flask-example
  ```

3. If you don't have one already, create a Postgres service.  With Pivotal Web Services, the following command will create a free Postgres database through [ElephantSQL].

  ```bash
  cf create-service elephantsql turtle pgsql
  ```

4. Push it to CloudFoundry.

  ```bash
  cf push
  ```

5. Bind service to App.

  ```bash
  cf bind-service cf-postgresql-flask-example pgsql
  ```

6. Find potgresql requisits (username, host, database, password).  Just run this command and look for the VCAP_SERVICES environment variable under the `System Provided` section.

  ```bash
  cf env cf-postgresql-flask-example
  ```
  
7. Replace postgres-2.0 to actuial in pgsql_env = services['postgres-2.0'] in cf-postgresql-flask-example.py

8. Push it again to CloudFoundry.
  ```bash
  cf push
  ```

## Enjoy!

