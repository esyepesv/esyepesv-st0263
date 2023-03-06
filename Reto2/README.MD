# info de la materia: ST0263 Topicos especiales en telematica
#
## Estudiante: Stiven Yepes Vanegas, esyepesv@eafit.educo
## Profesor: Edwin Nelson Montoya Munera, emontoya@eafit.edu.co
#
#  Procesos comunicantes por API REST, RPC y MOM
#
# 1. breve descripción de la actividad

En esta actividad se requiere diseñar e implementar dos microservicios básicos que ofrecen servicios al API Gateway y se comunican mediante un middleware RPC y un middleware MOM. Los microservicios deben soportar la concurrencia y permitir que varios procesos remotos se comuniquen simultáneamente. A nivel de lógica de negocio, se implementarán dos servicios: uno para listar archivos y otro para buscar uno o más archivos. Cada proceso tendrá un archivo de configuración que contendrá información como la IP, el puerto y el directorio que listará o buscará archivos. Además, se implementará un API Gateway que expondrá una API REST para probar las funcionalidades de cada proceso. Se utilizará gRPC para la comunicación RPC y RabbitMQ o Apache Kafka para la comunicación MOM. Esta actividad tiene como objetivo practicar el diseño e implementación de microservicios y la comunicación entre ellos utilizando diferentes middleware.


## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
se puedo implementar la parte de gRPC

## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
Se trató de implementar la comunicacion mediente MOM, pero o se retornaba la respuesta.

# 2. información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.
se trató de implemtar la aquitectura planteada por el profesor 


# 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

## como se compila y ejecuta.
## detalles del desarrollo.
## detalles técnicos
## descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)
## opcional - detalles de la organización del código por carpetas o descripción de algún archivo. (ESTRUCTURA DE DIRECTORIOS Y ARCHIVOS IMPORTANTE DEL PROYECTO, comando 'tree' de linux)
## 
## opcionalmente - si quiere mostrar resultados o pantallazos 

# 4. Descripción del ambiente de EJECUCIÓN (en producción) lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

# IP o nombres de dominio en nube o en la máquina servidor.

## descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)

## como se lanza el servidor.

## una mini guia de como un usuario utilizaría el software o la aplicación

## opcionalmente - si quiere mostrar resultados o pantallazos 

# 5. otra información que considere relevante para esta actividad.

# referencias:
<debemos siempre reconocer los créditos de partes del código que reutilizaremos, así como referencias a youtube, o referencias bibliográficas utilizadas para desarrollar el proyecto o la actividad>
## sitio1-url 
## sitio2-url
## url de donde tomo info para desarrollar este proyecto

#### versión README.md -> 1.0 (2022-agosto)
