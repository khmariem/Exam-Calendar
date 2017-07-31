
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
    l=f.readline()
    while (not l==""):
        l=l[:len(l)-1]
        l.split(",")
        data.append(l)
        l=f.readline()
        
        
    f.close()
    
    return data



########################function related to the construction of the graph##################################

def construct_graph(data):
    '''
    This method builds a graph in which the vertices are the different subjects and the edges exist between
    two vertices if the same student chose those two subjects. For example, if Joe chose to study graph theory(1),
    networks(2) and game theory(3), then an edge would exist between (1)&(2), (2)&(3) and (1)&(3).

    @param data: the data issued from the read_data method previously developed.

    @return: a dictionary which is the graph built from our data.
    '''
    g=dict()
    for l in data:
        for k in l:
            print(k)
            if (not g.__contains__(k)):
                g[k]={}
            for k1 in l:
                if k1!=k:
                    g[k]={g[k],k1}
                    
    return g


def max_degree(graph):
    '''
    This function calculates the maximum degree in the graph.

    @param graph: the graph that we want to determine its maximum degree.

    @return: the integer conveying the maximum degree of the graph.
    '''
    
    c=0    
    for i in graph:
        if len(g[i])>c:
            c=len(g[i])
            
    return c


def colour_graph(graph):

    M=[1 for j in range(len(graph))]
    
    if len(graph)==0:
        return 0
    else:
        j=1

    L=vertice_degree(graph)
    for i in range(1,len(M)):
        for k in graph[L[i][1]]:            
            c=0
            for j in range(len(L)):
                if L[j][1]==k:
                    c=j
                    break
                
            if M[c]==M[i]:
                M[c]=M[i]+1

    return max(M)
    

def vertice_degree(graph):
    '''
    This function calculates the tuple corresponding to a vertice and its degree in the graph.

    @param graph: the graph we work on.

    @return: the list containing the tuple of a vertice and its degree sorted according to an ascending order.
    '''
    
    L=[] 
    for i in graph:
        L.append(len(graph[i]),i)

    L.sort()
    L.reverse()
            
    return L

                 

                 
    




                
                 












    

