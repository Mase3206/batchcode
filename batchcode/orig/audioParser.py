import yaml, reformat, settings

rawSettings, prettySettings = settings.getSettings(False)




with open('profiles/audio.yml', 'r') as file1:
	defaultAudio = yaml.safe_load(file1)



def getAudioTrackParams(trackNumber):
	trackList = ['Track', str(trackNumber)]
	track = ' '.join(trackList)
	out = []
	out.append(defaultAudio[track]['Track'])
	out.append(defaultAudio[track]['Codec'])
	out.append(defaultAudio[track]['Bitrate'])
	out.append(defaultAudio[track]['Mixdown'])
	out.append(defaultAudio[track]['Name'])

	return out


def getAudioTrackCommand(totalTracks):
	outputArgs = ['-a','','-E','','-B','','-6','','-A','']
	rawArgs = []
	
	# add track params sublist to rawArgs list
	for i in range(totalTracks):
		rawArgs.append(getAudioTrackParams(i+1))

	# combine each sublist of related arguments into one string separated by a comma
	zippedArgs = reformat.lst2str(rawArgs)
	
	# put groupedArgs items into the correct place in outputArgs
	outputArgs = reformat.assemble(outputArgs, zippedArgs)

	return reformat.assemble(outputArgs, zippedArgs)


if __name__ == "__main__":
	print(getAudioTrackCommand(3))