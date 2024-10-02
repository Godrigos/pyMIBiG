"""
class Args definition
"""

class Args:
    '''
    Create a prefix for resulting filenames.
    '''
    def __init__(self, args):
        self.organism = args.organism
        self.product = args.product
        self.biosynt = args.biosynt
        self.completeness = args.completeness
        self.minimal = args.minimal
        self.prefix: str = ''

    def create_prefix(self) -> str:
        '''
        Take user arguments and compose filenames prefix with them.
        '''

        org = f'{self.organism}_' if self.organism else ""
        prod = f'{self.product}_' if self.product else ""
        bio = f'{self.biosynt}_' if self.biosynt else ""
        comp = f'{self.completeness}'
        mini = '_minimal' if self.minimal else ""

        self.prefix = org + prod + bio + comp + mini

        return self.prefix
