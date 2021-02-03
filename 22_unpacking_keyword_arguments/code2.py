def named(name, age):
    print (name, age)

details ={"name" : "Bob", "age":25}

# named(details) #'details' dictionay will become a value for the name parameter but age parameter won't have a value

# named(details, 25) #we need to pass that in separately sth like this

named(**details) #unpacking the dictionay into two named arguments like that
                #when you do that, it treats the key as the name for the argument and age as the key for the argument
                #and assigns to them the value associated with those