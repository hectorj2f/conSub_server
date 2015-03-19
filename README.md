

Ubuntu:
  apt-get build-dep python-psycopg2

Dependencies:
  You should install the pip packages detailed in the file subCon_requires

Packaging:
  Install docker PostgreSQL container:
    docker run -e POSTGRES_USER=consub -e POSTGRES_PASSWORD=password --name consub_db -p 5432:5432 -d postgres
