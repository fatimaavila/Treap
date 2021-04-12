# Treap 🌳

El treap que también es conocido como random binary tree, es un binary tree tiene una "key" o "value" este es el que asigna el usuario y un valor aleatorio "priority". Este mantiene el balance con probabilidades altas.

<img src="https://i.imgur.com/ZLqklAd.jpg" width="350" height="300"/> 

En este caso, el número celeste es el "priority"  es el número que se da de manera aleatoria y el verde el "value"  es cualquier número que ingresa el usuario. 

Este árbol tiene la característica de que no solo tiene que balancear el "value" del usuario sino también el "priority" ya que este debe ser max-heap.

## 📌 El max-heap significa que los padres deben tener un mayor valor que sus hijos.

<img src="https://i.imgur.com/SdWqoUN.jpg" width="350" height="300"/> 

### ⚠️ Este caso requiere de rotaciones de izquierda o derecha para poder rebalancear no solo los priority sino que también los value ⚠️

Uno de los usos que se le puede dar a un treap y uno de los más comunes es el de cuestiones de seguridad. Ya que el treap no se basa en historial sino en aleatoridad.

## Implementación en el código

<img src="https://i.imgur.com/kS8dNwl.jpg" width="250" height="360"/> 

El número que está señalado en celeste es el priority, este se utiliza con decimales para que sea muy difícil que haya un repetido.
Y el que está en verde es el value ingresado por el usuario que se hace con comandos. '+' para agregar y '-' para eliminar. 
