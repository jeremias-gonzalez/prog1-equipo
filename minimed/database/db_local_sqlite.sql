-- 1. TABLA BASE: PERSONA
CREATE TABLE IF NOT EXISTS Persona (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    dni VARCHAR(20) UNIQUE NOT NULL,
    telefono VARCHAR(20),
    domicilio VARCHAR(255),
    fecha_nacimiento DATE
);

-- 2. TABLA DE LOGICA: MUTUALES
CREATE TABLE IF NOT EXISTS Mutuales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(100) UNIQUE NOT NULL
);

-- 3. TABLA DE ROLES: EMPLEADO
CREATE TABLE IF NOT EXISTS empleado (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_persona INTEGER UNIQUE NOT NULL,
    puesto VARCHAR(100),
    FOREIGN KEY (id_persona) REFERENCES Persona(id)
        ON DELETE CASCADE
);

-- 4. TABLA DE ROLES: ADMIN
CREATE TABLE IF NOT EXISTS admin (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    USER VARCHAR(50) UNIQUE NOT NULL,
    PASSWORD VARCHAR(255) NOT NULL,
    id_empleado INTEGER UNIQUE NOT NULL,
    FOREIGN KEY (id_empleado) REFERENCES empleado(id)
        ON DELETE CASCADE
);

-- 5. TABLA DE ROLES: MEDICO
CREATE TABLE IF NOT EXISTS Medico (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_persona INTEGER UNIQUE NOT NULL,
    especializacion VARCHAR(100) NOT NULL,
    matricula VARCHAR(50) UNIQUE,
    FOREIGN KEY (id_persona) REFERENCES Persona(id)
        ON DELETE CASCADE
);

-- 6. TABLA DE ROLES: PACIENTE
CREATE TABLE IF NOT EXISTS Paciente (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_persona INTEGER UNIQUE NOT NULL,
    id_mutual INTEGER,
    FOREIGN KEY (id_persona) REFERENCES Persona(id)
        ON DELETE CASCADE,
    FOREIGN KEY (id_mutual) REFERENCES Mutuales(id)
);

-- 7. TABLA DE LÓGICA: TURNOS
CREATE TABLE IF NOT EXISTS Turnos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_paciente INTEGER NOT NULL,
    id_medico INTEGER NOT NULL,
    fecha_turno DATE NOT NULL,
    hora TIME NOT NULL,
    detalle TEXT,
    metodo_de_pago VARCHAR(50),
    FOREIGN KEY (id_paciente) REFERENCES Paciente(id),
    FOREIGN KEY (id_medico) REFERENCES Medico(id)
);

-- Datos de prueba
-- 1. Insertar una Persona para el Admin
INSERT INTO Persona (nombre, apellido, dni, telefono)
VALUES ('Admin', 'Root', '10000000', '11223344');

-- 2. Insertar un Empleado (que será el Admin)
INSERT INTO empleado (id_persona, puesto)
VALUES ((SELECT id FROM Persona WHERE dni = '10000000'), 'Super Administrador');

-- 3. Insertar el usuario Admin
INSERT INTO admin (USER, PASSWORD, id_empleado)
VALUES ('admin', '1234', (SELECT id FROM empleado WHERE id_persona = (SELECT id FROM Persona WHERE dni = '10000000')));

-- 4. Insertar Mutual Básica
INSERT INTO Mutuales (nombre) VALUES ('Particular');

-- 5. Insertar Médico de prueba
INSERT INTO Persona (nombre, apellido, dni, telefono)
VALUES ('Roberto', 'García', '20000000', '4567890');
INSERT INTO Medico (id_persona, especializacion, matricula)
VALUES ((SELECT id FROM Persona WHERE dni = '20000000'), 'Clínica Médica', 'ABC12345');

-- 6. Insertar Paciente de prueba
INSERT INTO Persona (nombre, apellido, dni, telefono)
VALUES ('Juana', 'Pérez', '111', '1155556666');
INSERT INTO Paciente (id_persona, id_mutual)
VALUES (
    (SELECT id FROM Persona WHERE dni = '111'),
    (SELECT id FROM Mutuales WHERE nombre = 'Particular')
);

-- 7. Insertar un Turno para la prueba
INSERT INTO Turnos (id_paciente, id_medico, fecha_turno, hora)
VALUES (
    (SELECT id FROM Paciente WHERE id_persona = (SELECT id FROM Persona WHERE dni = '111')),
    (SELECT id FROM Medico WHERE matricula = 'ABC12345'),
    date('now'),
    time('10:30:00')
);