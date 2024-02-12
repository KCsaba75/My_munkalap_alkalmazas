CREATE TABLE "Itallap" (
  "ital_id" INT PRIMARY KEY,
  "ital_nev" VARCHAR(255) NOT NULL,
  "kiszereles_id" INT,
  "ital_ar" "decimal" ,
  "kategoria_id" int
);

CREATE TABLE "Felhasznalok" (
  "user_id" INT PRIMARY KEY,
  "user_nev" VARCHAR(255) NOT NULL,
  "user_email" VARCHAR(255) NOT NULL
);

CREATE TABLE "Asztalok" (
  "asztal_id" INT PRIMARY KEY,
  "asztal_szam" VARCHAR(50) NOT NULL
);

CREATE TABLE "Rendelesek" (
  "rendeles_id" INT PRIMARY KEY,
  "user_id" INT,
  "asztal_id" INT,
  "datum" timestamp,
  "statusz_id" INT
);

CREATE TABLE "KedvencItalok" (
  "kedvenc_id" INT PRIMARY KEY,
  "user_id" INT,
  "ital_id" INT
);

CREATE TABLE "RendelesTetelek" (
  "tetel_id" INT PRIMARY KEY,
  "rendeles_id" INT,
  "ital_id" INT,
  "mennyiseg" INT
);

CREATE TABLE "Kiszerelesek" (
  "kiszereles_id" INT PRIMARY KEY,
  "kiszereles_nev" VARCHAR(50) NOT NULL
);

CREATE TABLE "Statuszok" (
  "statusz_id" INT PRIMARY KEY,
  "statusz_nev" VARCHAR(50)
);
CREATE TABLE "Kategoriak" (
  "kategoria_id" INT PRIMARY KEY,
  "kategoria_nev" VARCHAR(50) NOT NULL
);

ALTER TABLE "Rendelesek" ADD FOREIGN KEY ("asztal_id") REFERENCES "Asztalok" ("asztal_id");

ALTER TABLE "KedvencItalok" ADD FOREIGN KEY ("user_id") REFERENCES "Felhasznalok" ("user_id");

ALTER TABLE "KedvencItalok" ADD FOREIGN KEY ("ital_id") REFERENCES "Itallap" ("ital_id");

ALTER TABLE "Felhasznalok" ADD FOREIGN KEY ("user_id") REFERENCES "Rendelesek" ("user_id");

ALTER TABLE "RendelesTetelek" ADD FOREIGN KEY ("rendeles_id") REFERENCES "Rendelesek" ("rendeles_id");

ALTER TABLE "Itallap" ADD FOREIGN KEY ("ital_id") REFERENCES "RendelesTetelek" ("ital_id");

ALTER TABLE "Kiszerelesek" ADD FOREIGN KEY ("kiszereles_id") REFERENCES "Itallap" ("kiszereles_id");

ALTER TABLE "Statuszok" ADD FOREIGN KEY ("statusz_id") REFERENCES "Rendelesek" ("statusz_id");

ALTER TABLE "Kategoriak" ADD FOREIGN KEY ("kategoria_id") REFERENCES "Itallap" ("kategoria_id");