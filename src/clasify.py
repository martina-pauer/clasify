class Clasify():

    def __init__(self):
        '''
            Make your own clasifier with help
            of this class:

                Properties:

                    Clasify.data values to clasify in different categories

                    Clasify.classes categories for clasify the values

                    Clasify.rel pair value to category
        '''
        self.data: list = []

        self.classes: list[str] = []

        self.rel: dict = {}

    def new_type(self, cla : str):
        '''
            Add a new category  to the list
        '''
        if (not self.classes.__contains__(cla)):
            self.classes.append(cla.__str__())

    def new_value(self, val):
        '''
            Add new values to the data list.
        '''
        if (not self.data.__contains__(val)):
            self.data.append(val)

    def get_values(self, name : str) -> list:
        '''
            Get values from a file to clasify later
        '''
        values = open(name.__str__(), 'r')
        
        for line in values.readlines():
            self.new_value(line.replace('\n', ''))

        values.close()

        return self.data

    def get_types(self, name : str) -> list:
        '''
            Get categories from a file to clasify values later
        '''
        types = open(name.__str__(), 'r')

        for line in types.readlines():
            self.new_type(line.replace('\n', ''))

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

    def get_relation(self, name : str):
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
        # Auxiliar function for check if value is on file
        def is_value_in_file(path: str, val: str):
            obj = open(path, 'r')
            result = False
            
            for line in obj.readlines():
                if line.__contains__(val):
                    result = True
                    break

            obj.close()

            return result
        # Add the data from self.rel
        for value in self.rel.keys():
            # Normalization: no add a duplicate value for save data integrity
            if not is_value_in_file(name, value):
                data.write(f'\n{value},{self.rel[value]}')
        # Free out file from memory of safe mode
        data.close()
        del data 

    def merge(self, source_object, conditional_functions: list):
        '''
            Join data and category relations from
            one object and conditional functions
            list to be more acurate and huge the
            Clasify.rel dictionary
        '''
        # Make relation with conditional functions by separate and later join all
        source_object.relation(conditional_functions[0])
        self.relation(conditional_functions[conditional_functions.__len__() - 1])
        # join data, classes and rel list from both objects into this object
        self.data = self.data.__add__(source_object.data)
        self.classes = self.classes.__add__(source_object.classes)
        self.rel.update(source_object.rel)
        # make fixing to the relation with all the conditions between
        for condition_number in range(1, conditional_functions.__len__() - 1):
            # All central conditions are to fix clasification
            self.relation(conditional_functions[condition_number])