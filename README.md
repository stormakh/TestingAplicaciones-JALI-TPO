# Testing de Aplicaciones: Trabajo Práctico Obligatorio

## Nombre del equipo 

-'JALI'

## Integrantes

-'Perez Ezequiel Agustin Integrante 1'

-'Tormakh Santiago Integrante 2'

-'Yang Harry Alan Integrante 3'

-'Viñas Santiago Integrante 4'

---------------------------------------------------------------------------------Entrega 2------------------------------------------------------------------

"Análisis de los casos de prueba creados para las historias de Usuario de la Entrega 1"

1. Para las Historias de Usuario de la Entrega 1:
a. ¿Consideran que los Casos de Prueba creados, cuando los ejecuten, les darán la suficiente confianza de que la aplicación cumple con los Criterios de Aceptación?

Afirmativamente, hasta ahora creemos que la cantidad de casos de prueba darían suficiente confianza para que se puedan cumplir con los criterios de aceptación, entre ellos poder crear una cuenta exitosamente, poder ingresar con ella exitosamente, poder acceder al menú exitosamente, poder agregar cosas al carrito y hacer el checkout de forma aceptable y por último, poder editar los datos de la cuenta del cliente, lo que cumpliría con el funcionamiento básico de la plataforma, aunque se debe tener en cuenta que estos casos de prueba pueden estar sujetos a cambios durante el desarrollo del proyecto para adaptarla a variables inesperadas o cambios en la misma, Por ende no son definitivas. 

Se toma como sabido también que es imposible probar todas las variables posibles así que tratamos de cubrir la mayor cantidad de casos posibles.

b. ¿Han tenido que asumir cómo se iba a comportar la aplicación para crear los Casos de Prueba?

No tuvimos que hacer suposiciones acerca de lo que iba a hacer la aplicación, la verdad que en ese sentido opinamos que la explicación provista por el cliente al principio presentaba ciertos detalles faltantes, pero mediante las preguntas respondidas durante el QA en clase, se aclararon estas incertitudes.

c. ¿Pueden identificar algo que no les haya permitido crear Casos de Prueba (por ejemplo, requerimientos poco claros, falta de visibilidad de cómo se va a realizar el proyecto, no conocer cómo se lleva adelante el desarrollo, etc) y por qué?

En un principio, como mencionado previamente, si sentimos que el cliente nos había dado requerimientos poco claros, o faltaba información acerca de la aplicación, pero cuando le hicimos las preguntas pertinentes a este mismo, como por ejemplo (que características debía tener la contraseña durante la creación de cuentas o que caracteres se podían utilizar) pudimos resolver todas nuestras dudas acerca de cómo teníamos que llevar adelante el proyecto y pudimos hacerlo de forma pertinente. 

Básicamente, era conocer un poco mas acerca del proyecto y saber bien que quería el cliente y de esta forma no hacer suposiciones en los casos de uso.

2. Algunas de las Historias de Usuario eran más claras que otras. ¿Cuál es la Historia de Usuario con la que más problema han tenido para crear Casos de Prueba y por qué? ¿Cuál ha sido la más clara de entender y por qué?

Creemos que la Historia de Usuario menos clara fue la primera (ID: PE-16), La de creación de cuenta, ya que de no ser por las consultas que hicimos, no hubiéramos podido hacerla debido a la cantidad de suposiciones que había que hacer. Faltaban muchos criterios de aceptación en cuanto a los campos a completar en esta Historia de Usuario como: Si se empleaba una verificación del código postal, Desde qué fecha es válida durante el ingreso de la fecha de nacimiento, además de los previamente mencionados, etc. 

En cuanto a la mas fácil, esta fue la ultima que esta relacionada con poder acceder al home de la página, ya que no se necesitaba de mucha información/criterios/requerimientos, era simplemente que haya un botón que nos lleve al home en las subsecciones, menos en el menú.

"Ejecución de los Casos de Prueba creados"

Casos de prueba ejecutados:

TC-01 (Modificado): debido a que el sitio web presenta un campo obligatorio al crear una cuenta la cual es "Address Alias", sin este no se puede proceder, por ende se agregó un paso extra en el cúal se ingresa este campo.

TS-1A: Es indispensable para el usuario poder crear su cuenta por ende se eligio este caso de prueba.

TS-1B: El sistema debe ser capaz de reconocer cuando una contraseña es incorrecta sino existirían contraseñas inseguras que pueden poner en riesgo los datos e información personal de los usuarios

TC-02 (Modificado): En el Sitio web, los botones no presentan los mismos nombres que en el caso de uso, por ejemplo, en la versión anterior en un paso estaba escrito, apretar el botón "Submit" y en el sitio web aparece el botón como "Sign in"

TS-2A: Es importante que el usuario sea capaz de iniciar sesión a la cuenta que creó.

TS-2B: Se debe verificar que cuando se ingresen datos inválidos o inexistentes que el sistema no permita que el usuario acceda, sino podría acceder a información o cuentas la cual no está autorizado.

TC-03 (Modificado): Igualmente que el anterior muchos de los nombres de los botones y lugares donde debe hacer click el usuario tienen nombres distintos, esto se arregló en las versiones más nuevas de los Casos de Uso.

TS-3A: Es crucial que el usuario tenga la capacidad de editar sus datos personales e contraseña debido a que el usuario puede equivocarse o querer cambiarlo. Por ende es algo de imporatancia

TS-4B: Es medio redundante que el usuario introduzca devuelta la misma contraseña al querer cambiar la misma, el sistema debe poder detectar eso para informar al usuario, además se ahorra el tiempo de edición de la base datos, ya que no debe sobreescribir una entrada por lo mismo que antes, ahorrando recursos de los servidores.

TS-04 (Modificado): Se cambió los productos a buscar y a seleccionar debido a que ahora tenemos productos en concreto, previamente no se sabía que productos eran y se utilizaban placeholders.

TS-4A: Es de suma importancia que el usuario sea capaz de añadir productos que desea adquirir sin presenciar errores, ya que sino impediría la compra de los productos.

TS-4B: Es muy normal que un usuario quiera comprar más que solo uno por producto por ende se debe ver que esto funcione si problemas.

TS-05 (No fue modificado)

TS-05A: En este caso, es mejor para que el usuario se oriente y tenga en frente suyo acceso a todo lo que el desee al ser redirigido el segundo en el que este inicie sesión.

TS-05B: El usuario debe ser capaz de poder volver a la página principal desde cualquier lado de la página web, sino sería muy tedioso tener que volver manualmente.

Modificación Global de Casos de Uso: Se actualizó el primer paso de todos los casos de uso, al tener disponible el link actual del sitio web, se reemplazo el placeholder previo.
