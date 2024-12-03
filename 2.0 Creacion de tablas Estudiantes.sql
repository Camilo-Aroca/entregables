CREATE TABLE Alumnos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50),
    edad INT,
    ciudad VARCHAR(50)
);

INSERT INTO Alumnos (nombre, edad, ciudad) VALUES ('Carlos', 21, 'Cartagena');
INSERT INTO Alumnos (nombre, edad, ciudad) VALUES ('María', 23, 'Barranquilla');
INSERT INTO Alumnos (nombre, edad, ciudad) VALUES ('Pedro', 18, 'Santa Marta');

SELECT * FROM Alumnos;

SELECT * FROM Alumnos WHERE ciudad = 'Barranquilla';

SELECT * FROM Alumnos WHERE edad > 20;
