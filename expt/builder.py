# builder pattern

from collections import OrderedDict
from string import Template

class RedshiftTable():
    def __init__(self, name):
        self.name = name
        self.columns = OrderedDict()
        self.distkey = None
        self.sortkey = []
        
    def add_column(self, column_name, definition):
        if column_name in self.columns:
            raise Exception("Column %s already exists. If you want to change the column, use the method change_column." % column_name)
        self.columns[column_name] = definition

    def change_column(self, column_name, definition):
        if not column_name in self.columns:
            raise Exception("Column %s doesn't exists. If you want to add the column, use method add_column instead." % column_name)
        # change column_name definition
        self.columns[column_name] = definition

    def add_sort_key(self, key):
        """Add key into sortkey"""
        if not key in self.columns:
            raise Exception("Column %s doesn't exists. Please create column first." % key)
        if key in sortkey:
            raise Exception("Key %s already in sort keys.")
        # add sort key
        self.sortkey.append(key)

    def change_sortkey(self, sortkey):
        """Change sortkey for a table.
        Args:
            sortkey -- a string list
        """
        # validate each key in sortkey
        for key in sortkey:
            if key not in self.columns:
                raise Exception("Column %s doesn't exists. Please create column first." % key)
        # change sortkey
        self.sortkey = sortkey

    def change_distkey(self, key):
        """Change distkey. """
        if not key in self.columns:
            raise Exception("Column %s doesn't exists. Please create column first." % key)
        # change distkey
        self.distkey = key
        
    def generate_query():
        """CREATE TABLE $table_name"""
        # TODO(jiwei): implement this
        query = ""
        return query

