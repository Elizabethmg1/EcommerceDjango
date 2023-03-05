# EcommerceDjango

## Esta es una API rest utilizando Django rest framework

Contiene 3 endpoints:

* "orders": "http://127.0.0.1:8000/api/v1/orders/"

Con en cual podemos visualizar los datos y agregar nuevos

* "orderlist": "http://127.0.0.1:8000/api/v1/orderlist/"

Con el cual podemos visualizar los datos de la siguiente manera:

![image](https://user-images.githubusercontent.com/68891729/222981406-a9149ac7-210b-4129-9548-9316511d9b27.png)

* "orderdetail": "http://127.0.0.1:8000/api/v1/orderdetail/"

Con el cual podemos agregar productos seleccionando el id de producto y el id del cliente al cual lo queremos agregar:

![image](https://user-images.githubusercontent.com/68891729/222981517-0a3c731d-dd76-4496-9a51-8dc2451de0a3.png)

Ademas al ir al siguiente endpoint: http://127.0.0.1:8000/api/v1/orders/1/ 

podremos visualizar la orden con id 1 y borrarlo en caso de querer hacerlo.

El proyecto tambien cuenta con un directorio "QuerySQL" el cual contiene capturas de pantalla de los datos y de la query SQL a ejecutar para saber cual fue el producto mas ordenado.
