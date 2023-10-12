from fastapi import FastAPI, HTTPException
from models.ModelPsycologist import Psicologo, read_psicologos, read_psicologo, create_psicologo, update_psicologo, delete_psicologo

app = FastAPI()

# Ruta para listar todos los psicólogos
@app.get("/psicologos")
def listar_psicologos():
    psicologos = read_psicologos()
    return psicologos

# Ruta para obtener un psicólogo por ID
@app.get("/psicologo/{id}")
def obtener_psicologo(id: int):
    psicologo = read_psicologo(id)
    if psicologo:
        return psicologo
    else:
        raise HTTPException(status_code=404, detail="Psicólogo no encontrado")

# Ruta para insertar un nuevo psicólogo
@app.post("/psicologo")
def insertar_psicologo(psicologo: Psicologo):
    contador_filas_afectadas = create_psicologo(psicologo)
    return {"message": f"Filas afectadas: [{contador_filas_afectadas}] - | Profesional {psicologo.nombre} ingresado satisfactoriamente"}

# Ruta para actualizar un psicólogo por ID
@app.put("/psicologo/{id}")
def actualizar_psicologo(id: int, psicologo: Psicologo):
    actualizado_psicologo = update_psicologo(id, psicologo)
    if actualizado_psicologo:
        return {"message": f"Profesional {psicologo.nombre} actualizado satisfactoriamente"}
    else:
        raise HTTPException(status_code=404, detail="Psicólogo no encontrado")

# Ruta para eliminar un psicólogo por ID
@app.delete("/psicologo/{id}")
def eliminar_psicologo(id: int):
    contador_filas_afectadas = delete_psicologo(id)
    if contador_filas_afectadas:
        return {"message": f"Filas afectadas: [{contador_filas_afectadas}] - | Profesional eliminado satisfactoriamente"}
    else:
        raise HTTPException(status_code=404, detail="Psicólogo no encontrado")