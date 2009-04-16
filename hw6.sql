Part1

CREATE TABLE MOVIE(
 movie_name VARCHAR(100) PRIMARY KEY,
 director_name VARCHAR(100),
 gross_sales DECIMAL(20,2)
);

CREATE TABLE ACTOR(
 actor_name VARCHAR(100) PRIMARY KEY,
 actor_sex CHAR(1) CHECK (actor_sex in ('M', 'F')),
 actor_age INTEGER CHECK (actor_age BETWEEN 0 and 200)
);

CREATE TABLE STARS(
 movie_name VARCHAR(100),
 actor_name VARCHAR(100),
 star_category VARCHAR(100),
 CONSTRAINT movie_fk FOREIGN KEY (movie_name) REFERENCES MOVIE(movie_name),
 CONSTRAINT actor_fk FOREIGN KEY (actor_name) REFERENCES ACTOR(actor_name),
 CONSTRAINT check_category CHECK (star_category in ('Best Actor', 'Best Supporting actor', 'Best Actress', 'Best Supporting Actress')),
 CONSTRAINT stars_pk PRIMARY KEY (movie_name, actor_name)
);
