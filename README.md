# mYelp

mYelp es en principio una herramienta para otorgar insignias a negocios referente a sus reseñas en la plataforma Yelp. Con el núcleo de la herramienta se espera implementar otros usos para el monitoreo estadístico de un negocio.


# Implementacion
![Descripcion grafica](https://github.com/raulespecialist/myelp/blob/a956e72cf3277722820098d4fb8f0a4289556c4b/description.png)
## Descripción
Por la flexibilidad que nos ofrece el framework **Django** lo usaremos como base para nuestro proyecto, ya que tenemos la oportunidad de usar su sistemas MVC para Frontend y Backend, a si como tener la posibilidad de extenderlo con un sistema API REST o bien extender con cualquiera de las librerias de Python, Desde filtrados, particionados, uniones e incluso hasta funciones búsquedas avanzadas de PostgreSQL. 
Elegí **PostgreSQL**  ya que tiene un énfasis en la extensibilidad y el cumplimiento de los estándares. Es elegida porque cumple con la característica y protocolo ACID, lo que significa Atomicidad, Consistencia, Aislamiento y Durabilidad (siglas en inglés). Por ello, se garantiza la información de la base de datos y fiabilidad en el sistema. Django sera servida por medio de Gunicorn. 
**Gunicorn** es un servidor WSGI de Python puro para UNIX. No tiene dependencias y es fácil de instalar y usar, es el servidor de producción Python "clásico" y estándar de la industria. La ventaja final de usar Gunicorn es que, por naturaleza, es bastante rápido ademas junto con **NGINX** como proxy inverso y equilibrador de carga para administrar el tráfico entrante y distribuirlo a servidores ascendentes más lentos, desde servidores de bases de datos heredados hasta microservicios, por lo cual es ideal para usar delante de **Gunicorn**.
 **Docker** es una plataforma creada con el fin de desarrollar, implementar y ejecutar aplicaciones dentro de contenedores, lo cual nos permite encapsular nuestra aplicacion y sus servicios, para ayudar tanto a replicar como a la alta disponibilidad.
 
