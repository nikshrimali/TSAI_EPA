# OneWithSequenceTypes

Below stuff has been implemented

## Polygon Class:
Initializer takes in:
- number of edges/vertices
- circumradius

Provides below properties:
- edges
- vertices
- interior angle
- edge length
- apothem
- area
- perimeter
that has these functionalities:
- a proper __repr__ function
- implements equality (==) based on # vertices and circumradius (__eq__)
- implements > based on number of vertices only (__gt__)


## Custom Polygon sequence type:
where initializer takes in:
- number of vertices for largest polygon in the sequence
- common circumradius for all polygons
that can provide these properties:
- max efficiency polygon: returns the Polygon with the highest area: perimeter ratio
that has these functionalities:
- functions as a sequence type (__getitem__)
- supports the len() function (__len__)
- has a proper representation (__repr__)

