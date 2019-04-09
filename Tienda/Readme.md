Martinez Garcia Mariana Yasmin \\ \\ \\


Aqui estan los archivos "Producto.py" que contiene una clase llamada "Producto" que recibe el nombre, marca, categoria y precio de un producto. Ademas, contiene un metodo que permite mostrar estos detalles. \\  \\ \\



"Cliente.py" que contiene una clase llamada "Cliente" que tiene como atributos nombre del cliente y el saldo que tiene ese cliente. Y como metodo tiene uno que permite mostrar sus detalles con la ayuda de "str" que nos permite facilitar la forma de "llamar" al objeto. \\ \\ \\



"Tienda.py" contiene otra clase llamada "Tienda". Como atributos tiene un nombre,un cliente de la clase "Cliente" y contiene un atributo que llama a un metodode esta misma clase que contiene una lista con objetos de la clase Producto. Y al igual que las anteriores, el metodo que contiene permite mostrar detalles (tambien fue modifiado y sustituido por "str"). 
Como se modifico la parte del atributo "producto", tambien se agrego el metodo que permite crear esta lista, y otro metodo que muestra los productos de la lista. \\ \\ \\


"MenuCliente.py", esta clase permite registrar a un nuevo cliente, se le pide al usuario que coloque su Nombre y su saldo y regresa el objeto de la clase Cliente.py \\ \\ \\


"Carrito.py" Esta clase recibe un objeto de la clase Cliente.py y tiene como metodos, agregarProducto, eliminarProduto, imprimirProdutos y mostrarTotal. El primero agrega un producto de los que ya estan definidos en la clase Tienda.py, el segundo elimina un producto de su carrito, el tercero muestra los productos que el cliente tiene en su carrito y el ultimo suma los precios de cada producto y te muestra el total. \\ \\ \\


Y el otro archivo se llama "Pruebas.py", esta contiene una clase llamada "Pruebas"y en esta clase se hizo pruebas de cada una de las clases anteriores. \\



