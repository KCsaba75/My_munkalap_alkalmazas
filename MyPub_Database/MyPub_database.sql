CREATE TABLE "Itallap" (
  "ital_id" INT PRIMARY KEY,
  "nev" VARCHAR(255) NOT NULL,
  "kiszereles_id" INT,
  "ar" "DECIMAL(5, 2)" NOT NULL
);

CREATE TABLE "Felhasznalo" (
  "user_id" INT PRIMARY KEY,
  "nev" VARCHAR(255) NOT NULL,
  "email" VARCHAR(255) NOT NULL
);

CREATE TABLE "Asztal" (
  "asztal_id" INT PRIMARY KEY,
  "szam" VARCHAR(50) NOT NULL
);

CREATE TABLE "Rendeles" (
  "rendeles_id" INT PRIMARY KEY,
  "user_id" INT,
  "asztal_id" INT,
  "datum" DATETIME,
  "statusz_id" INT
);

CREATE TABLE "KedvencItalok" (
  "kedvenc_id" INT PRIMARY KEY,
  "user_id" INT, 
  "ital_id" INT
);

CREATE TABLE "RendelesTetel" (
  "tetel_id" INT PRIMARY KEY,
  "rendeles_id" INT,
  "ital_id" INT,
  "mennyiseg" INT
);

CREATE TABLE "Kiszereles" (
  "kszereles_id" INT PRIMARY KEY,
  "Kiszereles_nev" VARCHAR(50) NOT NULL
);

CREATE TABLE "Statusz" (
  "statusz_id" INT PRIMARY KEY,
  "nev" VARCHAR(50)
);

ALTER TABLE "Rendeles" ADD FOREIGN KEY ("asztal_id") REFERENCES "Asztal" ("asztal_id");

ALTER TABLE "KedvencItalok" ADD FOREIGN KEY ("user_id") REFERENCES "Felhasznalo" ("user_id");

ALTER TABLE "KedvencItalok" ADD FOREIGN KEY ("ital_id") REFERENCES "Itallap" ("ital_id");

ALTER TABLE "Felhasznalo" ADD FOREIGN KEY ("user_id") REFERENCES "Rendeles" ("user_id");

ALTER TABLE "RendelesTetel" ADD FOREIGN KEY ("rendeles_id") REFERENCES "Rendeles" ("rendeles_id");

ALTER TABLE "Itallap" ADD FOREIGN KEY ("ital_id") REFERENCES "RendelesTetel" ("ital_id");

ALTER TABLE "Kiszereles" ADD FOREIGN KEY ("Kiszereles_nev") REFERENCES "Itallap" ("kiszereles_id");

ALTER TABLE "Statusz" ADD FOREIGN KEY ("statusz_id") REFERENCES "Rendeles" ("statusz_id");
