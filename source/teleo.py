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

class MultiCarrier:

    def __init__(self, file_name):
        self.routers = []

                for name in file_name:
                    self.routers.append(Router(name))

    def route_princes(self, number):
        """
        Senario 4: High-throughput pricing API
        You have 5 carrier route list, each with 10,000,000 entries (in arbitrary order)
        and you want to create a web-service API to allow clients to price a call before
        it is initiated. How can you create an efficient route cost lookup solution that
        can handle high spikes of traffic (up to 10,000 request per min) without overloading
        your API servers?
        """

        route_cost = None

        #Loop through every routes
        for route in self.routers:
            price = route.cost(number)

            if route_cost is None or price < route_cost:
                route_cost = price
        return route_cost




if __name__== '__main__':
    inst = Teleo('../routing/data/route-costs-1000000.txt')
    #inst.cost('../routing/data/route-costs-1000000')
