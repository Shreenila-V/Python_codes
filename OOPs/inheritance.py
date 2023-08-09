class fruits:
    def about(self):
        print("about fruit mango")
class mango(fruits):
    def taste(self):
        print("mango taste is sweet ")
class mangocolour(mango):
    def colour(self):
        print("mango colour is yellow")
class mango_colour_nature(mangocolour):
    def nature(self):
        print("mango nature is not citric")
f=mango_colour_nature()
f.about()
f.taste()
f.colour()
f.nature()

