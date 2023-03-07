# info de la materia: ST0263 Topicos especiales en telematica
#
## Estudiante: Stiven Yepes Vanegas, esyepesv@eafit.educo
## Profesor: Edwin Nelson Montoya Munera, emontoya@eafit.edu.co
#
#  Procesos comunicantes por API REST, RPC y MOM
#
# 1. breve descripción de la actividad

En esta actividad se requiere diseñar e implementar dos microservicios básicos que ofrecen servicios al API Gateway y se comunican mediante un middleware RPC y un middleware MOM. Los microservicios deben soportar la concurrencia y permitir que varios procesos remotos se comuniquen simultáneamente. A nivel de lógica de negocio, se implementarán dos servicios: uno para listar archivos y otro para buscar archivos. Cada proceso tendrá un archivo de configuración que contendrá información como la IP, el puerto y el directorio que listará o buscará archivos. Además, se implementará un API Gateway que expondrá una API REST para probar las funcionalidades de cada proceso. Se utilizará gRPC para la comunicación RPC y RabbitMQ o Apache Kafka para la comunicación MOM. Esta actividad tiene como objetivo practicar el diseño e implementación de microservicios y la comunicación entre ellos utilizando diferentes middleware.


## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
En cuanto a requisitos funcionales, se pudieron implementar los dos servicios (listar archivos y buscar si existe) mediante eL middleware gRPC, a los cuales se accede mediante un API Gateway. Al hacer la petición al API Gateway, esta se comunica en primera instancia con el servicio mediante gRPC, y en caso de que ocurra una falla, se comunicará asincronicamente dediante MOM. Sin embargo, este ultimo presentó un error al devolver la respuesta, por lo que no funciona correctamente.

## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
Como se mencionó en el apartado anterior, se trató de implementar la comunicacion mediente MOM, pero no se retornaba la respuesta. Este fallo hizo tambien que no se concentraran los esfuerzos en los otros requisitos funcionales, como que este sistema corriera en la instancia EC2 de AWS, por lo que la parte que si funciona lo hace en local y el archivo de configuración tanto de los procesos como en el Bootstrap.

# 2. información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.
se trató de implemtar la aquitectura planteada por el profesor, en la cual se tiene un API Gateway que se comunica con los dos servicios, uno mediante gRPC y el otro mediante MOM.


# 3. Descripción del ambiente de desarrollo y técnico:

lenguaje de programación: Python 3.8.10

librerias: os, Flask, jsonify, grpc, sys, pika, uuid, futures.

## como se compila y ejecuta.
Se deben ejecutar los 2 servicios, el API Gateway y el MOM, en este caso Rabbitmq, cada uno en sus correspondientes carpetas.

- API Gateway: python3 main.py
- gRPC: python3 file_service.py
- MOM: python3 mom.py

## descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)
Para configurar los paraametros del proyecto es necesario hacerlo desde el codigo funete de los diferentes componentes.

## resultados o pantallazos 

Programas corriendo:
![image](https://user-images.githubusercontent.com/60147085/223563426-f9c9c5e6-c607-4352-85e1-a3f28025b69e.png)

Servicio 1:
![image](https://user-images.githubusercontent.com/60147085/223563676-4bdefba7-1855-4b22-bf5f-fb9db0c59a13.png)

servicio 2:
![image](https://user-images.githubusercontent.com/60147085/223563774-a46cb6a3-dd1a-43f5-af98-0441aef69442.png)
![image](https://user-images.githubusercontent.com/60147085/223563846-d603a678-3d96-4724-a997-3d04e3642dfe.png)



