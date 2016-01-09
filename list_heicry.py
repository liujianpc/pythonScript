movies = ['forrestgump',1994,'tomhanks','oscar',['american','asian',['agan','china','japan']]]
for content in movies:
    if isinstance(content,list):
        for con in content:
            if isinstance(con,list):
                for co in con:
                    print co
            else:
                print con
    else:
        print content
                
