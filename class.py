class Bird(object):
        def __init__(self):
                pass
        def say(self):
                print 'Bird'

class BBird(object):
        def __init__(self):
                pass
        def say(self):
                print 'BBird'
                      
class SongBird(BBird,Bird):
        def __init__(self):
                super(SongBird,self).__init__()
        BBsay = BBird.say
        Bsay = Bird.say
                
sb=SongBird()
sb.BBsay()
sb.Bsay()
