from collections import OrderedDict

class Cost():

    def __init__(self, file_name):
        file = open(file_name)
        price = {}
        for line in file:
            k, v = line.strip().split(',')

            price[k.strip()] = v.strip()

            file.close
            self.price = price


if __name__== '__main__':
    main()
