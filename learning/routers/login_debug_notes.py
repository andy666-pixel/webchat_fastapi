"""
📘 GUÍA RÁPIDA - FastAPI: Error <UnboundLocalError: cannot access local variable 'x' where it is not associated with a value> en dependencias

🚫 Error común:
UnboundLocalError: cannot access local variable 'form_data' where it is not associated with a value

❓ ¿Por qué ocurre:
Este error ocurre cuando declaras una variable dentro de una función (como `form_data`), pero nunca le asignas un valor antes de usarla.

🔍 Diagnóstico:

Código original con error:
------------------------------------
def login(data: OAuth2PasswordRequestForm = Depends()):
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
    db: Annotated[Session, Depends(SessionDep)]
    
    user = authenticate_user(form_data.username, form_data.password, db)
------------------------------------

🚫 Problemas:
1. `form_data` y `db` solo están anotados (Annotated[...]): **no se les asigna ningún valor**.
2. FastAPI no los inyecta si no están en los **parámetros de la función**.
3. Se usan como si tuvieran valor → causa el error UnboundLocalError.

✅ Versión corregida:
------------------------------------
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

@app.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(), 
    db: Session = Depends(SessionDep)
):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise InvalidCredentialsException
    return {"status": "Success"}
------------------------------------

✔️ ¿Por qué funciona?
- `form_data` y `db` se declaran directamente como **parámetros de la función**.
- FastAPI se encarga de:
    - Leer los datos del formulario.
    - Crear instancias de las dependencias.
    - Pasarlas a la función automáticamente.

🎓 ¿Qué es Depends() en FastAPI?

- `Depends()` es el sistema de **inyección de dependencias** de FastAPI.
- Cuando defines:
  
    def login(form_data: OAuth2PasswordRequestForm = Depends())

  FastAPI entiende que debe crear una instancia de `OAuth2PasswordRequestForm` a partir del request y asignarla a `form_data`.

- Lo mismo con:
  
    db: Session = Depends(SessionDep)

  FastAPI llama a `SessionDep()` y pasa el resultado como `db`.

🧠 Tabla resumen:

| Código original                             | ¿Por qué falla?                      |
|--------------------------------------------|--------------------------------------|
| `form_data: Annotated[...]`                | Solo anota tipo, no da valor         |
| `db: Annotated[...]`                       | Igual, sin valor asignado            |
| `form_data.username` antes de asignar      | Variable usada sin valor → error     |

✅ Consejos prácticos para evitar este error:

1. ✅ **Siempre usa `Depends()` directamente en los parámetros** de la función.
2. 🚫 **No uses `Annotated[...]` dentro del cuerpo** de la función si esperas que FastAPI lo resuelva.
3. ✅ **No dupliques dependencias con diferentes nombres** (usa solo `form_data`, no también `data`).
4. ✅ **Deja que FastAPI maneje las dependencias**, no intentes inyectarlas manualmente dentro del cuerpo de la función.
5. ✅ **Prueba todo con Swagger (/docs)** para confirmar que las dependencias se están resolviendo correctamente.

"""
