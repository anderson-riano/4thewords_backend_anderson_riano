CREATE DATABASE IF NOT EXISTS 4thewords_prueba_anderson_riano;
USE 4thewords_prueba_anderson_riano;

-- Tabla de provincias
CREATE TABLE IF NOT EXISTS provincias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE
);

-- Tabla de cantones
CREATE TABLE IF NOT EXISTS cantones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    provincia_id INT NOT NULL,
    FOREIGN KEY (provincia_id) REFERENCES provincias(id) ON DELETE CASCADE
);

-- Tabla de distritos
CREATE TABLE IF NOT EXISTS distritos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    canton_id INT NOT NULL,
    FOREIGN KEY (canton_id) REFERENCES cantones(id) ON DELETE CASCADE
);

-- Tabla de leyendas
CREATE TABLE IF NOT EXISTS leyendas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    categoria VARCHAR(100) NOT NULL,
    descripcion TEXT NOT NULL,
    fecha DATE NOT NULL,
    imagen_url VARCHAR(255) NOT NULL,
    distrito_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (distrito_id) REFERENCES distritos(id) ON DELETE CASCADE
);

-- Insertar datos de prueba en provincias
INSERT INTO provincias (nombre) VALUES 
('San José'), ('Alajuela'), ('Cartago'), ('Heredia'), 
('Guanacaste'), ('Puntarenas'), ('Limón');

-- Insertar datos de prueba en cantones
INSERT INTO cantones (nombre, provincia_id) VALUES
('San José', 1), ('Escazú', 1), ('Alajuela', 2), 
('Cartago', 3), ('Heredia', 4), ('Liberia', 5),
('Puntarenas', 6), ('Limón', 7);

-- Insertar datos de prueba en distritos
INSERT INTO distritos (nombre, canton_id) VALUES
('Carmen', 1), ('San Sebastián', 1), ('San Rafael', 2), 
('Alajuela Centro', 3), ('Oreamuno', 4), ('San Francisco', 5), 
('Liberia Centro', 6), ('Puntarenas Centro', 7), ('Limón Centro', 8);

-- Insertar 10 leyendas de prueba
INSERT INTO leyendas (nombre, categoria, descripcion, fecha, imagen_url, distrito_id)
VALUES 
('La Tulevieja', 'Mito', 'Leyenda de una madre que busca a su hijo', '1850-06-15', 'https://example.com/tulevieja.jpg', 1),
('El Cadejos', 'Mito', 'Perro fantasmagórico que protege a los borrachos', '1900-08-20', 'https://example.com/cadejos.jpg', 4),
('La Llorona', 'Terror', 'Espíritu de una mujer que llora por sus hijos', '1700-09-10', 'https://example.com/llorona.jpg', 5),
('El Padre sin Cabeza', 'Terror', 'Sacerdote decapitado que aparece en las noches', '1890-07-12', 'https://example.com/padre.jpg', 6),
('La Cegua', 'Misterio', 'Mujer con cabeza de caballo que asusta a los infieles', '1750-11-22', 'https://example.com/cegua.jpg', 7),
('El Duende', 'Folclore', 'Criatura traviesa que esconde cosas', '1800-03-05', 'https://example.com/duende.jpg', 8),
('El Tesoro de los Dantas', 'Misterio', 'Oro enterrado por los indígenas', '1600-12-01', 'https://example.com/dantas.jpg', 9),
('La Mona', 'Terror', 'Bruja transformada en mono', '1950-04-18', 'https://example.com/mona.jpg', 3),
('El Sombrerón', 'Folclore', 'Hombre pequeño con sombrero que enamora mujeres', '1805-02-14', 'https://example.com/sombreron.jpg', 4),
('La Carreta sin Bueyes', 'Misterio', 'Carreta espectral que anuncia la muerte', '1780-10-30', 'https://example.com/carreta.jpg', 5);
