# Treap 🌳

El treap que también es conocido como random binary tree, es un binary tree que tiene una "key" o "value" este es el que asigna el usuario y un valor aleatorio "priority". Este mantiene el balance con probabilidades altas.

<img src="https://i.imgur.com/ZLqklAd.jpg" width="350" height="300"/> 

En este caso, el número celeste es el "priority" que es el número que se da de manera aleatoria y el verde el "value" que es cualquier número que ingresa el usuario. 

Este árbol tiene la característica de que no solo tiene que balancear el "value" del usuario sino también el "priority" ya que este debe ser max-heap.

## 📌 El max-heap significa que los padres deben tener un mayor valor que sus hijos.

<img src="https://i.imgur.com/SdWqoUN.jpg" width="350" height="300"/> 

### ⚠️ Este caso requiere de rotaciones de izquierda o derecha para poder rebalancear no solo los priority sino que también los value ⚠️

Uno de los usos que se le puede dar a un treap y es uno de los más comunes es el de cuestiones de seguridad. Ya que el treap no se basa en historial sino en aleatoridad.

## Implementación en el código

