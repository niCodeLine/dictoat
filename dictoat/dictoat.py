class Dictoat:
    def __init__(self, dictt: dict = None, *, safety: bool = True, symbol: str = '_'):
        '''
        convert your dicts to objects for easier access
        
        :param dictt: dictionary
        :param safety: adds a symbols (default "_") to the name to avoid matching reserved keywords
        :param symbol: symbol to be added as safety procedure

        :type dictt: dict
        :type safety: bool
        :type symbol: str
        
        '''
        if dictt is None:
            dictt = {}
        for key, val in dictt.items():
            attr_name = f"{key}{symbol}" if safety else str(key) # the undersquare avoids coinciding with reserved keywords
            if isinstance(val, dict):
                setattr(self, attr_name, Dictoat(val, safety=safety))
            else:
                setattr(self, attr_name, val)