#!/usr/bin/python3
def color_compare(color_blocks: list[int], color: int) -> bool:
    '''
        Compare the first two colors searching match
        with color decimal code
    '''
    return  (
                color_blocks[0] == color
                or color_blocks[1] == color
            )

class Color():
    def __init__(self, hex_string: str):
        '''
            Define color logic with a hexadecimal
            string code of 6 characters
        '''
        self.code: str = hex_string
        self.warming_points: int = 0

    def predominant(self) -> str:
        '''
            Say predominant color contains one or more 
            'red', 'green' or 'blue'
        '''
        # Divide colors block
        red = int(self.code[0].__add__(self.code[1]), 16)
        green = int(self.code[2].__add__(self.code[3]), 16)
        blue = int(self.code[4].__add__(self.code[5]), 16)
        # Sort from greater to minor in a list
        blocks = [red, green, blue]
        current_block = blocks[0]

        for block_number in range(0, 2):
            current_block = blocks[block_number]
            # The loop only run for the first five when this has meaning
            if current_block < blocks[block_number + 1]:
                # Interchanges values when the current is less than next
                blocks[block_number] = blocks[block_number + 1]
                blocks[block_number + 1] = current_block
        # When the list has first the greater numbers says the first two
        result = ''
        # Add color name when the first two are equal to color block
        if  color_compare(blocks, red):
            result += 'red'
            self.warming_points += (5 * red)
        if  color_compare(blocks, green):
            result += 'green'
            self.warming_points += (red // 2)    
        if color_compare(blocks, blue):
            result += 'blue'
            self.warming_points += (red // 5)

        return result

    def warm(self, min_points: int) -> bool:
        '''
            Says by predominant color(red or green) and warming points 
            if a color is warm
        '''
        return  (
                    self.warming_points >= min_points        
                    or self.predominant().__contains__('red')
                    or self.predominant().__contains__('green')
                )

import sys

def warmar(points: str):
    '''
        When the warming points are
        greater or equal to minimum is
        dangerously warm
    '''
    points = int(points.split(' ')[2])
    return points >= int(sys.argv[2])
# Run only in this script when import the name is module name
if __name__ == '__main__':
    # Execute in this main script only
    import random
    import os
    import sys
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    from clasify import Clasify

    test = Clasify()
    
    minimum = 700

    test.new_type('Danger')
    test.new_type('Calm')

    for color in range(0, 10):
        # Generate 10 random colors
        obj =  Color    (
                            # Generate blocks of two hexadecimals digits
                            hex(random.randint(16, 255)).replace('0x', '')
                            + hex(random.randint(16, 255)).replace('0x', '')
                            + hex(random.randint(16, 255)).replace('0x', '')
                        )
        # Add the warming of color
        obj.warm(minimum)
        output = (f'#{obj.code} has {obj.warming_points} warming points')
        print(output)
        test.new_value(output)
    # Make comparations for see if a color is so warm (potentialy dangerous)
    test.relation(warmar)
    # Save results and clean
    prefix = '/workspaces/clasify'
    test.get_relation(f'{prefix}/data/colors/color_warming.csv')
    os.system(f'rm -R {prefix}/src/__pycache__')