#### this is a simulation assuming that the spread of the virus itself is not controlled, and assuming that the virus runs rampant



"""



the modelling formula used here is:
    Nd = no of cases on a day
    E = Average no of people someone infected is exposed to
        this is higher for people who are very socially active, and low for people who are not
    p = probability of each exposure becoming an infection



    the formula is eventually:
        N(d+1) = (1+E.p)Nd

    

    we should be using a logarithmic scale here

"""

import matplotlib.pyplot as plt

class Coronavirus:
    def __init__(self, init_day, E, p):
        self.nd = init_day
        self.e = E
        self.p = p
    


    def ddaytime(self, total_population):
        ls = []
        days = 0
        while(self.nd < total_population):
            ls.append(self.nd)
            self.nd = self.nd*(1+self.e*self.p)
            days += 1
        return ls



c = Coronavirus(1, 25, 0.6)
y = c.ddaytime(1_000_000_000)
x = [a for a in range(1, len(y)+1)]
print(x, y)
plt.plot(x, y)
plt.show()





