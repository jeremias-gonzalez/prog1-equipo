-- SQLite
CREATE TABLE provincia (
    idProvincia INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL
);

-- Tabla de localidades
CREATE TABLE localidad (
    idLocalidad INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    idProvincia INTEGER NOT NULL,
    FOREIGN KEY (idProvincia) REFERENCES provincia(idProvincia)
);
