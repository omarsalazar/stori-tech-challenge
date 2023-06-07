FROM postgres:latest
ENV POSTGRES_PASSWORD=secret
ENV POSTGRES_USER=postgres
ENV POSTGRES_DB=stori
ENV POSTGRES_HOST=db
ENV POSTGRES_PORT=5432
COPY dump-stori-202306062027.sql /docker-entrypoint-initdb.d/dump-stori-202306062027.sql