# Exam-Calendar
This is a project that was inspired by the application of the graph theory to find the most suitable exam calendar using less days.

It uses a file that already has the data we need which consist of the choice subjects for all the students, "data.txt" is a small file that I created to test my work. You can enrich it, if you want, with other lines. Yet, it must end with "/" as shown in the initial text to prevent bugs.


*How to use this project:

1)execute the projet.py file,
2)Use the "construct_graph" function for the construction of the graph and the vertices,
3)Use the "colour_graph" function, it will restitute the chromatic number of the graph( and as a result the optimal number of examination days) and the list of the days in which each vertice should occur. The days are represented under the form of numbers varying from 1 to the chromatic number.
