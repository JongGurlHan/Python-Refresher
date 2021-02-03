def print_param2(**kwargs): 
    print (kwargs) 
    print (kwargs.keys()) 
    print (kwargs.values()) 
    

print_param2(first = 'a', second = 'b', third = 'c', fourth = 'd')

   
        #{'second': 'b', 'fourth': 'd', 'third': 'c', 'first': 'a'} 
        # #['second', 'fourth', 'third', 'first'] 
        #['b', 'd', 'c', 'a'] 
        # #second : b #fourth : d #third : c #first : a

