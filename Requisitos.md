#### Leyenda
- [ ] No testeado
- [x] Test exitoso
- :x: Test fallido
- A -> B (R n) A diseña los test para los requisitos n y B los ejecuta

# 2019-1-Electronic-Operations-T5
# Requisitos a testear:

## Requisitos generales:
### Joaco -> Nico (R 1 - 9, 11) 
 1. [ ] El sistema debe permitir que el administrador del sistema cree cuentas de
evaluador en el sistema, solicitando el nombre, apellido, correo electrónico y
generando al azar la contraseña del usuario.
 2. [ ] Todo usuario debe autentificarse para acceder al sistema, usando su correo
electrónico y su contraseña.
 3. [ ] No se puede crear más de una cuenta en el sistema con el mismo correo
electrónico.
 4. [ ] El sistema debe considerar 2 tipos de usuarios: administrador, y evaluador.
 5. [ ] El administrador también puede evaluar presentaciones.
 6. [ ] Cada curso debe tener un nombre, código, número de sección, y año y semestre
de realización.
 7. [ ] Cada combinación de código, número de sección, y año y semestre de
realización de curso debe ser única en el sistema.
 8. [ ] Un curso puede tener más de un evaluador.
 9. [ ] Dentro de un curso, cada estudiante debe pertenecer a un equipo de trabajo.
 Clave: mzbVtuMXzz

 11. [ ] Cada curso puede tener cero o más evaluaciones.

### Claudio -> Clemente (R 15)
 15. [ ]  El sistema debe mostrar un listado de las últimas 10 evaluaciones asociadas al
usuario, ordenados por fecha (más nuevos al inicio de la lista), indicando el
curso asociado, cuales están pendientes y cuales ya fueron contestadas.

### Clemente -> Joaco (R 16)
 16. [ ]  El usuario puede acceder a la ficha de una evaluación desde el resumen de las
evaluaciones.

## Ficha de una evaluación:

### Nico -> Claudio (R 28 - 37)
28. [ ] El sistema debe indicar el curso asociado a la evaluación, el estado de la
evaluación (abierta, cerrada), las fechas de inicio y fin, duración esperada de las
presentaciones y la rúbrica asociada.
29. [ ] En el caso del administrador, el sistema debe permitir actualizar los plazos de
una evaluación, sin perder las evaluaciones que ya fueron realizadas por los
evaluadores.
30. [ ] En el caso del administrador, el sistema debe mostrar una lista de los
evaluadores asociados a la evaluación.
31. [ ] El administrador puede agregar o quitar evaluadores antes de abrir la evaluación
a los evaluadores.
32. [ ] Una vez iniciada una evaluación, el administrador solo puede quitar evaluadores
asociado que no han ingresado notas.
33. [ ] Una vez iniciada una evaluación, el administrador puede agregar nuevos
evaluadores.
34. [ ] El sistema debe mostrar la rúbrica asociada a la evaluación.
35. [ ] El administrador puede editar la rúbrica asociada a una evaluación antes de abrir
la evaluación a los evaluadores.
36. [ ] No se podrá modificar la rúbrica de una evaluación después de que se haya
registrado la evaluación de un equipo.
37. [ ] Si la evaluación aún está abierta, en el caso del administrador se debe mostrar
un listado de los equipos cuya evaluación aún está pendiente.

### Clemente -> Joaco (R 38 - 45)
38. [ ] Si la evaluación aún está abierta, el administrador puede elegir uno de los
equipos cuya evaluación está pendiente, para comenzar su evaluación.
39. [ ] Al comenzar la evaluación de un equipo, en el caso del administrador, el sistema
debe mostrar quiénes del equipo han presentado y quienes no. El administrador
debe indicar los nombres de los estudiantes que presentaran.
40. [ ] Una vez iniciada una evaluación, los evaluadores asociados solo podrán
ingresar puntajes al equipo seleccionado por el administrador.
41. [ ] En cada evaluación de equipo, los evaluadores deben indicar puntajes para
todos los aspectos de la rúbrica.
42. [ ] Para finalizar una evaluación, el usuario debe confirmar los puntajes ingresados.
43. [ ] Si un usuario no está de acuerdo con los puntajes ingresados, debe poder
actualizar los puntajes ingresados.
44. [ ] Solo el administrador puede indicar el tiempo que demoró una presentación.
45. [ ] El sistema debe indicar si corresponde aplicar un descuento a un equipo, en
base a la duración mínima y máxima asociada a la rúbrica aplicada.

## Ficha de una rubrica:

### Claudio -> Clemente (R 47 - 51)
47. [ ] El sistema debe mostrar los aspectos a evaluar, como también los niveles de
cumplimiento y los puntajes asociados.
48. [ ] En el caso del administrador, el sistema debe permitir agregar, quitar o modificar
aspectos a evaluar.
49. [ ] En el caso del administrador, el sistema debe permitir agregar, quitar o modificar
niveles de cumplimiento para un aspecto a evaluar.
50. [ ] En el caso del administrador, el sistema debe permitir indicar las duraciones
mínimas y máximas de las presentaciones que serán evaluadas.
51. [ ] El sistema debe validar que la suma de los niveles máximos de los todos los
aspectos de cualquier rúbrica siempre sea 6.

## Landing page admin:

### Claudio -> Clemente (R 61, 64, 65)
61. [ ] El sistema debe permitir la gestión (creación, modificación y eliminación) de evaluadores.
64. [ ] El sistema debe permitir la gestión (creación, modificación y eliminación) de
evaluaciones.
65. [ ] El sistema debe permitir la gestión (creación, modificación y eliminación) de
rubricas.
