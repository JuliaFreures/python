CURRENCY_NAMES ={
    "USD": "Dólares dos EUA",
    "BRL": "Real"
}

class Currency:
    def __init__(self, v, code):
        self.value = v
        self.code = code

    def __str__(self):
        return f"{self.value}{self.code}"
    
    def __eq__(self, rhs ):
        if self.code == rhs.code and self.value == rhs.value:
            return True
        return False
    def __gt__(self, rhs):
        
        if self.code == rhs.code:
            return self.value > rhs.value 
        raise ValueError("Moedas devem ser do mesmo país")
    def __ne__(self, rhs):
        return not (self == rhs)
if __name__ == '__main__':    
    moeda1 = Currency(50, "BRL")
    # moeda3 = moeda1
    moeda2 = Currency(51, "USD")
    print(moeda1 > moeda2)
    #print(moeda2)
    #print(moeda3 == moeda1)
    #print(moeda2 == moeda1)
#print(moeda.value)
#print(moeda.code)

#print("Nome da moeda", CURRENCY_NAMES[moeda.code])