
sequence = [1,3,5,7] 

double = [ double(x) for x in sequence]

double = map(double, sequence)
double = list(map(lambda x: x *2, sequence))

# what map does is it goes over each value in the sequence such as a list, 