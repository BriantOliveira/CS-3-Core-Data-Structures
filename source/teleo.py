from collections import OrderedDict

class Teleo():

    def __init__(self, file_name):
        file = open(file_name)
        #Turn the dataset into a dictionary
        route_info = {}
        for line in file:
            """
            n = phone Number
            p = price
            """
            n, p = line.strip().split(',')

            route_info[n.strip()] = p.strip()

        file.close()
        self.route_info = route_info

    def cost(self, number):
        """
        You have a carrier route list with 100,000(100K) entries (in arbitrary order)
        and a single phone number. How quickly can you find the cost of calling
        this number?
        """
        cost = None
        size = -1

        # If the number starts at the prefix and the cost is not defined the
        # current prefix < the last cost so we set the current cost to the prefix
        for prefix in self.route_info:
            if number.startswith(prefix) and (cost is None or len(prefix) > size):
                cost = prefix
                size = len(prefix)
        #In case if we don't get teh cost
        if cost is None:
            return None
        #Return the best cost
        return self.route_info[cost]
        print(cost)

    def route_cost(self, number):
        """
        List of route cost to check:
        You have a carrier route list with 100,000(100K) entries (in arbitrary order)
        and a list of 1000 phone numbers. How can you operationalize the route cost
        look up problem?
        """
        route_prices = {}

        #Go through our list of numbers and add to our list the best result
        for number in number:
            #Add the best result of number and the best price
            route_prices[number] = self.route_cost(number)

        return route_prices

if __name__== '__main__':
    inst = Teleo('../routes/route-costs-1000000.txt')
    inst.cost('..routes/route-costs-1000000')
