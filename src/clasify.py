class Clasify():

    def __init__(self):
        '''
            Make your own clasifier with help
            of this class:

                Properties:

                    Clasify.data values to clasify in different categories

                    Clasify.classes categories for clasify the values

                    Clasify.rel pair vallue to category
        '''
        self.data : list = []

        self.classes : list[str] = []

        self.rel : dict = dict()

    def newType(self, cla : str):
        '''
            Add a new category  to the list
        '''
        if (not self.classes.__contains__(cla)):
            self.classes.append(cla.__str__())

    def newValue(self, val):
        '''
            Add new values to the data list.
        '''
        if (not self.data.__contains__(val)):
            self.data.append(val)

    def getValues(self, name : str) -> list:
        '''
            Get values from a file to clasify later
        '''
        values = open(name.__str__(), 'r')
        
        for line in values.readlines():
            self.newValue(line.replace('\n', ''))

        values.close()

        return self.data

    def getTypes(self, name : str) -> list:
        '''
            Get categories from a file to clasify values later
        '''
        types = open(name.__str__(), 'r')

        for line in types.readlines():
            self.newType(line.replace('\n', ''))

        types.close()

        return self.classes

    def relation(self, cond):
        '''
            Make relations in Clasify.rel dict with
            a conditional function as parameter.
        '''
        for value in self.data:
            for category in self.classes:
                # Make code for override with right condition
                if (cond(value)):
                    self.rel.__setitem__(value.__str__(), category)
                    break
                else:
                    self.rel.__setitem__(value.__str__(), category)        

    def getRelation(self, name : str):
        '''
            Note: Run Clasify.relation method before run this

                    Add data to or create a new CSV file with all 
                    values and categories of the Clasify instance object.
        '''                
        try:
            # Create file if doesn't exist
            data = open(name, 'x')
            # Add first row with tags for identify values
            data.write('Value,Category')
        except:
            # Open in append mode when the file exist    
            data = open(name, 'a')
        # Add the data from self.rel
        for value in self.rel.keys():
            data.write(f'\n{value},{self.rel[value]}')
        # Free out file from memory of safe mode
        data.close()
        del data    