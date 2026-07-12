class India():
    def capital(self):
        print("Capital of India is New Delhi")
    
    def language(self):
        print("Most widely spoken language is Hindi")
    
    def type(self):
        print("India is a developing country")

class USA():
    def capital(self):
        print("Capital of USA is Washington, D.C.")
    
    def language(self):
        print("Most widely spoken language is English")
    
    def type(self):
        print("USA is a developed country")

obj_india = India()
obj_usa = USA()

for country in (obj_india, obj_usa):
    country.capital()
    country.language()
    country.type()