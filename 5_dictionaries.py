#INTRO TO DICTIONARIES **********************************************************************
names = {'madhu':23,'manoj':20,'kencha':29}
print(names)

""" o/p Example
{'madhu': 23, 'manoj': 20, 'kencha': 29}
************************************************************************************************
"""

names = {'madhu':23,'manoj':20,'kencha':29}
names['madhu']='25'
print(names['madhu'])

""" o/p
{'madhu': 25, 'manoj': 20, 'kencha': 29}
Dictionaries uses {}  and mutable 
"""

names = {'madhu':23,'manoj':20,'kencha':29}
print(names['manoj'])

""" o/p
20
"""

""" Allow Indexing By Keys"""

names = {'madhu':20,'manoj':51,'manoj':20, 'manoj':21,'kencha':29}
print(names)
print(names['manoj'])

""" Not Allow Duplicate Values and Keys Automatically Filter Consider Right to first"""
"""Un ordered access using keyword"""
"""Allow Different Datatypes"""