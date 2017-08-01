
#################name of file and other variables########################################################


name_file = 'data.txt'



################function related to data treatment#######################################################




def read_data(name_file):
    '''
    Loads the data contained in the file each line of the file corresponds to the subjects chosen by the student.

    @param name_file: file containing the saved data.
    

    @return: list of lists each list containing the subjects chosen by a single student.
    '''
    
    f=open(name_file,'r')

    data=[]
    for line in f:
        line=line[:len(line)-1]
        line=line.split(",")
        data.append(line)
        
        
    f.close()
    
    return data



########################function related to the construction of the graph##################################




def construct_graph(data):
    '''
    This method builds a graph in which the vertices are the different subjects and the edges exist between
    two vertices if the same student chose those two subjects. For example, if Joe chose to study graph theory(1),
    networks(2) and game theory(3), then an edge would exist between (1)&(2), (2)&(3) and (1)&(3).

    @param data: the data issued from the read_data method previously developed.

    @return g: a list of lists which is the graph built from our data. Each list is the list of neighbours of a vertice.

    @return visited: the list of the vertices following the same order as in the graph g. So, the neighbours of visited[i] are
    graph[i].
    '''
    g=[]
    visited=[]
    c=0
    for l in data:
        for k in l:
            if (not k in visited):
                visited.append(k)
                g.append([])
                c=visited.index(k)
            else:
                c=visited.index(k)
            for k1 in l:
                if (k1!=k) and (k1 not in g[c]):
                    g[c].append(k1)
                                        
    return (g,visited)





#################################functions manipulating the graph#########################################################




def max_degree(graph):
    '''
    This function calculates the maximum degree in the graph.

    @param graph: the graph that we want to determine its maximum degree.

    @return: the integer conveying the maximum degree of the graph.
    '''
    
    c=0    
    for i in graph:
        if len(i)>c:
            c=len(i)
            
    return c


    

def vertice_degree(graph,vertices):
    '''
    This function calculates the tuple corresponding to a vertice and its degree in the graph.

    @param graph: the graph of the subjects and the different links between them as explained in the function
    which constructs the graph.

    @param vertices: the list which gives the different vertices in the same order as the list of its neighbours
    listed in graph. So, the neighbours of vertices[i] are graph[i].

    @return: the list containing the tuple of a vertice and its degree sorted according to an ascending order based on the order.
    '''
    
    L=[] 
    for i in range(len(graph)):
        L.append((len(graph[i]),vertices[i]))

    L.sort()
    L.reverse()
            
    return L





def colour_graph(graph,vertices):
    '''
    This function determines the chromatic number of the graph given as an entry. It conveys the minimum number of days
    in which exams would take place without falling in the problem of having two exams programmed in the same day for the
    same student.

    @param graph: the graph of the subjects and the different links between them as explained in the function
    which constructs the graph.

    @param vertices: the list which gives the different vertices in the same order as the list of its neighbours
    listed in graph. So, the neighbours of vertices[i] are graph[i].

    @return M: the list of the numbers(colours) which range from 1 to the chromatic number of the graph. This list obeys to the same
    order of the vertices in the vertices list.So, the colour of vertices[i] is M[i]. Two differnet vertices having the same M[i]
    can as result take place on the same day.

    @return max(M): this is the chromatic number of the graph and the mainimum number of days on which all the exams
    can occur.
    '''

    M=[1 for j in range(len(graph))]
    
    if len(graph)==0:
        return 0

    L=vertice_degree(graph,vertices)
    for i in range(0,len(L)):
            for k in graph[vertices.index(L[i][1])]:            
                c=vertices.index(k)
                if M[vertices.index(L[i][1])]==M[c]:
                    M[c]=M[c]+1

                
    return (M,max(M))
                 

                 
    




                
                 












    

