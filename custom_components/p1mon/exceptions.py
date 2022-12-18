"""Exceptions for the module"""

class P1MonError(Exception):
    """Generic P1mon error"""

class P1MonConnectionError(Exception):
    """Default connection error for p1 mon"""

class P1MonConnectionTimeOutError(Exception):
    """Connection timeout error for p1 mon"""

class P1MonConnectionBrokenError(Exception):
    """Connection has been broken while processing data"""
    
class P1MonEmptyResponseError(Exception):
    """Connection gave no output"""

class P1MonIndexError(Exception):
    """Data processing gave an index error (Incomplete Data)"""
    
class P1MonValueError(Exception):
    """Data processing gave a value error (Incomplete Data)"""
    