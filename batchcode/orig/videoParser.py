import yaml, settings, reformat

rawSettings, prettySettings = settings.getSettings(False)
fetchedSettings = []

with open('profiles/video.yml', 'r') as file1:
	video = yaml.safe_load(file1)


# Expected
# outputArgs = ['-e', '', '--encoder-preset', 'veryslow', '--encoder-tune', 'animation', '--encoder-profile', 'main', '--encoder-level', 'auto', '-q', '18', '-r', '23.976', '--cfr', ]



def getVideoCommand():
	outputArgs = ['-e', '', '--encoder-preset', '', '--encoder-tune', '', '--encoder-profile', '', '--encoder-level', '', '-q', '', '-r', '']

	fetchedSettings = []


	# Video Output Args
	fetchedSettings.append(video['Encoder'])
	fetchedSettings.append(video['Encoder Preset'])
	fetchedSettings.append(video['Encoder Tune'])
	fetchedSettings.append(video['Encoder Profile'])
	fetchedSettings.append(video['Encoder Level'])

	fetchedSettings.append(str(video['Constant Quality']))
	fetchedSettings.append(str(video['Framerate']))

	outputArgs = reformat.assemble(outputArgs, fetchedSettings)
	
	if bool(video['Constant Framerate']) == True:
		outputArgs.append('--cfr')

	return outputArgs


if __name__ == '__main__':
	print(getVideoCommand())
