DROP TABLE IF EXISTS vacancies;
CREATE TABLE vacancies (
  id integer primary key autoincrement,
  company text not null,
  dev text not null,
  city_business text not null,
  salary text not null,
  hashtags text not null,
  description text not null,
  contacts blob not null
);
