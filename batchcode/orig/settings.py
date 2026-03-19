import yaml, reformat
from time import sleep


if __name__ == '__main__':
	print('\nThis program is not meant to be run directly. Please instead call the functions within this program from another.\nExiting...\n')
	exit(0)

def main():
	print('\n\n *** Settings Tool *** ')
	getChoice()


def getSettings(new): # if displaying "new" values, set arg to `True`
	with open('settings.yml', 'r') as setFile:
		readSettings = yaml.safe_load(setFile)

	return readSettings, reformat.prettyDic(readSettings, new)


def writeSettings():
	raw, pretty = getSettings(False)
	print(pretty)
	
	print('\nWhich setting would you like to choose? (line number)')
	lineNum = int(input(' : '))

	print('\nSelected:', list(raw.keys())[lineNum - 1], ' = ', list(raw.values())[lineNum - 1])

	change = input('Change to: ')
	rawTemp = raw
	tempKey = list(rawTemp.keys())[lineNum - 1]
	rawTemp[tempKey] = change
	print('Draft: ', list(rawTemp.keys())[lineNum - 1], ' = ', list(rawTemp.values())[lineNum - 1])
	
	looksGood = input('Ok? [Y/n]: ')
	if looksGood == 'y' or looksGood == 'Y' or looksGood == '':
		with open('settings.yml', 'w') as setFile:
			yaml.dump(rawTemp, setFile)
		
		raw, pretty = getSettings(True)
		print(pretty)
		sleep(2)


def getChoice():
	print('\n1. Print current settings')
	print('2. Change settings')
	print('3. Exit')
	choice = int(input(' : '))

	if choice == 1:
		raw, pretty = getSettings(False)
		print(pretty)
		getChoice()
	elif choice == 2:
		writeSettings()
		getChoice()
	elif choice == 3:
		return
	else:
		print('Unknown option "' + choice + '". Please try again.\n')
		getChoice()
