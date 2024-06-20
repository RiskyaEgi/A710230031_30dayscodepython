class India():
    def capital(self):
        print("New Delhi is the capital India")

    def languange(self):
        print("Hidia is the most widly spoke languange of india")

    def type(self):
        print("India is a Developing country.")

class USA():
    def capital(self):
        print("Washinton, D.C is the capital of USA")
    
    def languange(self):
        print("English is the primary languange of USA")

    def type(self):
        print("USA is a developed country")

obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.languange()
    country
