"""
    File: dates.py
    Author: Justin Kim
    Purpose: Read in file a lines and process them according to the OPcode
    if "I" create a date object and then add it to the DateSet object's dict
    if "R" print out all the events for that date
    Note: The "I" and "R" Opcode's are not case-sensitive
"""
    
class Date:
    """
    This class creates date objects
    Parameters: date is a date in yyyy-mm-dd format
                event is a string describing what occured on that date
    Returns: Nothing, but sets values to self._date and self._event
    """
    def __init__(self, date, event):
        self._date = date
        self._event = [event]

    """
    This method appends event to the list self._append and sorts the list
    Parameters: event is a string
    Returns: nothing
    """
    def add_event(self, event):
        self._event.append(event[0])
        self._event = sorted(self._event)
        
    def get_date(self):
        return self._date
    
    def get_event(self):
        return self._event
    
    def __str__(self):
        """
        This method just prints out a string with the date and all the events that took place on that date
        Parameters: none
        Returns: a string with the self._date and the list self._events
        """
        return print('{}: {}'.format(self._date, self._event))
    
class DateSet:
    """
    This class creates a dict of Date objects
    Parameters: none
    Returns: Nothing, but creates a dict with the Date_.date as a key and the Date object as the values
    Also it modifies Date obj in the dict if another Date object has the same date, but with another event
    """
    def __init__(self):
        self._dates_dict = {}
    def add_date(self, Date):
        if Date._date not in self._dates_dict:
            self._dates_dict[Date.get_date()] = Date
        else:
            self._dates_dict[Date.get_date()].add_event(Date._event)
            
    def __str__(self):
        """
        This method prints out a string in the format: date: event
        Parameters: none
        Returns: a string with the date and a list of all objects that have
        that date
        """
        return print('{}'.format(self._dates_dict))

def get_lines():
    """
    Prompts the user for a file name and opens the file,
    Creates a DateSet object and then processes the lines in the file
    creating date objects and adding them to the DateSet object or
    printing out all the events that happened on a date depending on
    the OPcode
    Parameters: None
    Returns: a DateSet object named date_dict
    """
    f = open(input())
    date_dict = DateSet()
    for line in f:
        date = process_line(line)
        if type(date) != str:
            date_dict.add_date(date)
        else:
            print_R(date, date_dict)
    return date_dict

def process_line(line):
    """
    This determines on how to process line, if 'I' then it'll break down the line and create a Date obj and return it
    if 'R' it'll break down the line differently and return a string instead
    Parameters: line is a string that has all the information from the Opcode, date and event
    Returns: a Date obj if Opcode is 'I' or a string if Opcode is 'R'
    """
    
    if line[0].upper() == 'I':
        line_split = line[1:].split(':', maxsplit = 1)
        date_str = canonicalize_date(line_split[0].strip())
        event = line_split[1].strip()
        
    elif line[0].upper() == 'R':
        line_split = line[1:]
        return canonicalize_date(line_split.strip())
    assert (line[0].upper() == 'I' or line[0].upper() == 'R'), "Error: Illegal Operation."
        
    return Date(date_str, event)

def print_R(date_str, DateSet):
    """
    Prints out a string in the format yyyy-mm-dd: event, does this for all
    events that correspond to the key date_str
    Parameters: date_str is a string and DateSet is a DateSet object
    Returns: Nothing, but prints out a string
    """
    for i in range(len(DateSet._dates_dict[date_str]._event)):
        print("{}: {}".format(date_str, DateSet._dates_dict[date_str]._event[i]))


def canonicalize_date(date_str):
    """
    Breaks down a string and turns it into a string into the format yyyy-mm-dd
    Parameters: date_str is a string in one of three formats
    Returns: a string in the format yyyy-mm-dd
    """
    months = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,\
                'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
    if '-' in date_str:
        date_list = date_str.split('-')
        yyyy = date_list[0]
        mm = date_list[1]
        dd = date_list [2]
    elif '/' in date_str:
        date_list = date_str.split('/')
        yyyy = date_list[2]
        mm = date_list[0]
        dd = date_list[1]
    else:
        date_list = date_str.split()
        yyyy = date_list[2]
        mm = months[date_list[0]]
        dd = date_list[1]
    
    assert 1 <= int(mm) <= 12, "Error: Illegal date."
    assert 1 <= int(dd) <= 31, "Error: Illegal date."

    return "{:d}-{:d}-{:d}".format( int(yyyy), int(mm), int(dd))

def main():
    date_dict = get_lines()

main()
