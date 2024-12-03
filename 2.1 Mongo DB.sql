// Conectar y agregar documentos a la colección 'Estudiantes'
db.Estudiantes.insertMany([
    { "nombre": "Carlos", "edad": 21, "ciudad": "Cartagena" },
    { "nombre": "María", "edad": 23, "ciudad": "Barranquilla" },
    { "nombre": "Pedro", "edad": 18, "ciudad": "Santa Marta" }
]);

// Obtener todos los documentos de la colección
db.Estudiantes.find();

// Obtener estudiantes que viven en Barranquilla
db.Estudiantes.find({ "ciudad": "Barranquilla" });

// Obtener estudiantes con edad mayor a 20 años
db.Estudiantes.find({ "edad": { $gt: 20 } });
