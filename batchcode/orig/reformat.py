

def combineArgs(lst: list, argument: int):
	"""
	Extracts the element at the specified index (argument) from each sublist in lst.
    
	Args:
		lst (list): A list of lists.
		argument (int): The index of the element to extract from each sublist.
    
	Returns:
		list: A list containing the elements at the specified index from each sublist.
	"""
	temp = []
	for i in range(len(lst)):
		temp.append(lst[i][argument])
	return temp


def lst2str(superlist: list):
	"""
	Converts a list of lists into a list of comma-separated strings, grouping elements by their index.
    
	Args:
		superlist (list): A list of lists, where each sublist contains related arguments.
    
	Returns:
		list: A list of strings, each string is a comma-separated group of related arguments.
	"""
	rawArgs = superlist
	groupedArgs = []
	zippedArgs = []
    
	rnge = len(superlist[0])

	# grab all related arguments `i` from each sublist of rawArgs, add to a new sublist in groupedArgs
	for i in range(len(rawArgs[0])):
		groupedArgs.append(combineArgs(rawArgs, i))
    
	# convert all list items to strings
	for i in range(len(groupedArgs)):
		for j in range(len(groupedArgs[0])):
			groupedArgs[i][j] = str(groupedArgs[i][j])

	# combine each sublist of related arguments into one string separated by a comma
	for i in range(len(groupedArgs)):
		zippedArgs.append(','.join(groupedArgs[i]))

	return zippedArgs


def dic2lstlst(dic: dict):
	"""
	Converts a dictionary into a list of [key, value] pairs.
    
	Args:
		dic (dict): The dictionary to convert.
    
	Returns:
		list: A list of [key, value] lists.
	"""
	keys = list(dic.keys())
	values = list(dic.values())
    
	return list(map(list, zip(keys, values)))


def prettyDic(dic: dict, new: bool):
	"""
	Formats a dictionary into a human-readable string, optionally labeling it as new or current settings.
    
	Args:
		dic (dict): The dictionary to format.
		new (bool): If True, label as 'New settings', else 'Current settings'.
    
	Returns:
		str: A formatted string representation of the dictionary.
	"""
	lstlst = dic2lstlst(dic)
	out = []
	for i in range(len(lstlst)):
		temp = []
		temp.append(str(lstlst[i][0]))
		temp.append("  =  ")
		temp.append(str(lstlst[i][1]))

		out.append(''.join(temp))
    
	out = '\n'.join(out)

	if new == True:
		return ''.join(['\nNew settings: \n', out])
	else:
		return ''.join(['\nCurrent settings: \n', out])


def allStr(lst):
	"""
	Converts all elements in a list to strings. Raises an error if input is a dictionary.
    
	Args:
		lst (list or any): The list to convert, or a single value.
    
	Returns:
		list: A list of strings.
    
	Raises:
		TypeError: If input is a dictionary.
	"""
	if type(lst) != list:
		if type(lst) == dict:
			raise TypeError('Function reformat.allStr does not accept dictionaries, but was given one.')
		lst = [lst]

	for i in range(len(lst)):
		lst[i] = str(lst[i])

	return lst

def assemble(options: list, settings: list):
	"""
	Inserts each setting from the settings list into the options list at every odd index (1, 3, 5, ...).
    
	Args:
		options (list): The list to insert settings into. Should be at least twice as long as settings.
		settings (list): The list of settings to insert.
    
	Returns:
		list: The modified options list with settings inserted.
	"""
	for i in range(len(settings)):
		options[i*2+1] = settings[i]

	return options
