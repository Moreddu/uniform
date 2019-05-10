class Point2D(object):
    def __init__(self, slot1=None, slot2= None):
        self.x= slot1
        self.y= slot2

    def stampa_x(self):
        print(self.x)


class Point4D(Point2D):

    def __init__(self, slot2, slot3, newslot4, **newslot5):
        super(Point4D, self).__init__(slot1=slot2, slot2=slot3)
        self.z= newslot4
        self.t=newslot5

    def stampa_tempo(self):
        print(self.t)

if __name__ == "__main__":
    punto2D = Point2D(10,20)
    punto4D = Point4D(20,30,40,secondi=50)
    print("Object a", punto2D.__dict__)         #__dict__ stampa il dizionario, è un metodo di object
    print("Object b", punto4D.__dict__)
    punto2D.stampa_x()
    punto4D.stampa_tempo()