#function digui
def print_nest(nested_list):
    for first_heicracy in nested_list:
        if isinstance(first_heicracy,list):
            print_nest(first_heicracy)
        else:
            print first_heicracy

movies = ['forrestgump',1994,'tomhanks','oscar',['american','asian',['agan','china','japan']]]
print_nest(movies)
