import csv, settings
from audioParser import getAudioTrackCommand as audio
from episodeParser import getEpisodeCommand as episode
from videoParser import getVideoCommand as video
from filterParser import getFilterCommand as filtr
from dimensionParser import getDimensionCommand as dim


class SettingError:
	Exception


def allEpisodes(numberOfEpisodes, episodeNumber):
	episodes = []
	episodeParameters = []
	audioParameters = []

	# set this for each series
	rawSettings, prettySettings = settings.getSettings(False)

	numberOfAudioTracks = int(rawSettings['Audio Track Quantity'])
	
	environment = rawSettings['Environment']


	# open csv of episodes to rip
	with open('/'.join([rawSettings['Episode Output Directory'], rawSettings['Episode List Name']]), 'r') as csvfile1:
		episodeList = csv.reader(csvfile1, delimiter=',')

		for row in episodeList:
			episodes.append(row)


	# assemble full command
	
	episodeParameters = episode(episodes[episodeNumber])
	if episodeParameters != False:
		if environment == 'Unix':			
			fullCommand = ['HandBrakeCLI'] + audio(numberOfAudioTracks) + episodeParameters + video() + filtr() + dim()
		elif environment == 'Windows':
			fullCommand = [rawSettings['HandBrakeCLI Executible Location']] + audio(numberOfAudioTracks) + episodeParameters + video() + filtr() + dim()
		else:
			raise SettingError(''.join['settings.yml [\'Environment\'] must be set to either Unix or Windows, not ', environment], '.\nHalting...')
	else:
		fullCommand = False

	return fullCommand


if __name__ == '__main__':
	#print('\nThis program is not meant to be run directly. Please instead call the functions within this program from another.\nExiting...\n')
	#exit(0)

	print('\n', allEpisodes(5, 3), '\n')
