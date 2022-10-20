# mYelp

mYelp es en principio una herramienta para otorgar insignias a negocios referente a sus reseñas en la plataforma Yelp. Con el núcleo de la herramienta se espera implementar otros usos para el monitoreo estadístico de un negocio.


# Implementacion
![description](https://user-images.githubusercontent.com/54911620/197017798-fad06f0a-ef3b-4ad5-b1f6-5a7a4327dda9.png)

### Descripción
Por la flexibilidad que nos ofrece el framework. Django lo usaremos como base para nuestro proyecto, ya que tenemos la oportunidad de usar su sistemas MVC para Frontend y Backend, a si como tener la posibilidad de extenderlo con un sistema API REST o bien extender con cualquiera de las librerias de Python, Desde filtrados, particionados, uniones e incluso hasta funciones búsquedas avanzadas de PostgreSQL. 
Elegí PostgreSQL  ya que tiene un énfasis en la extensibilidad y el cumplimiento de los estándares. Es elegida porque cumple con la característica y protocolo ACID, lo que significa Atomicidad, Consistencia, Aislamiento y Durabilidad (siglas en inglés). Por ello, se garantiza la información de la base de datos y fiabilidad en el sistema. Django sera servida por medio de Gunicorn. 
Gunicorn es un servidor WSGI de Python puro para UNIX. No tiene dependencias y es fácil de instalar y usar, es el servidor de producción Python "clásico" y estándar de la industria. La ventaja final de usar Gunicorn es que, por naturaleza, es bastante rápido ademas junto con NGINX como proxy inverso y equilibrador de carga para administrar el tráfico entrante y distribuirlo a servidores ascendentes más lentos, desde servidores de bases de datos heredados hasta microservicios, por lo cual es ideal para usar delante de Gunicorn.
 Docker es una plataforma creada con el fin de desarrollar, implementar y ejecutar aplicaciones dentro de contenedores, lo cual nos permite encapsular nuestra aplicación y sus servicios, para ayudar tanto a replicar como a la alta disponibilidad.

### Instalación
La instalacion se realiza mediante docker-compose.
```sh
git clone https://github.com/raulespecialist/myelp.git
cd myelp
docker-compose up
```
   Para trabajar con los datos de inicio proporcionados por Yelp se nececita lo siguiente.
   Descargar el siguiente archivo [subset 2.zip](https://drive.google.com/file/d/1rPjOdKXggrs3QYcEk8MQ9yyAD_dPZPG9/view?usp=sharing)
   Descomprimirlo y copiar los 3 archivos json _users100k.json_ _business10k.json_ _review1M.json_ en la carpeta llamada _data/_ dentro de _myelp/_

Crear tablas iniciales por medio de Django
```sh
docker-compose run django_app python core/manage.py migrate
docker-compose run django_app python core/manage.py makemigrations award
docker-compose run django_app python core/manage.py migrate yelp
```
![postgres - public - award_review](https://user-images.githubusercontent.com/54911620/197017624-57fcd72c-6ffe-446e-aebd-b9959c8cbe04.png)

Recolectar los archivos estaticos para el frontend, Bootstrap5.
```sh
docker-compose run django_app python core/manage.py collectstatic
```
Importar los Datasets de Yelp a nuestras bases de datos, por medio de Python Pandas
```sh
docker-compose run django_app python data/import_business.py 
docker-compose run django_app python data/import_user.py
docker-compose run django_app python data/import_review.py
```
Si se desea crear un usuario administrador para el panel de administracion usar el siguiente comando.
```sh
docker-compose run django_app python core/manage.py createsuperuser
```
Para verificar la instalación ingresar en http://127.0.0.1/ para el área de administración http://127.0.0.1/admin


