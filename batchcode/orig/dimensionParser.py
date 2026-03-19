import yaml

# pictureOutputArgs = ['-w', '', '-h', '', '--crop-mode', 'none', '--auto-anamorphic']

class SettingError:
	Exception



def getDimensionCommand():
	with open('profiles/dimensions.yml', 'r') as file1:
		dimensions = yaml.safe_load(file1)

	fetchedSettings = []



	# Orientation and Cropping
	# ['--rotate=angle=0:hflip=0', '--crop-mode=none']

	fetchedSettings.append(''.join(['--rotate=', 'angle=', str(dimensions['Rotation Angle']), ':hflip=', str(int(dimensions['Horizontal Flipping']))]))
	fetchedSettings.append('--crop-mode')
	fetchedSettings.append(dimensions['Crop Mode'])

	if dimensions['Crop Mode'] == 'custom':
		crop = dimensions['Crop']
		fetchedSettings.append('--crop')
		fetchedSettings.append(''.join([str(crop[0]), ':', str(crop[1]), ':', str(crop[2]), ':', str(crop[3])]))



	# Resolution and Scaling
	# ['-X', '720', '-Y', '480', '--auto-anamorphic']

	maxRes = dimensions['Resolution Limit']
	fetchedSettings.append('-X') 
	fetchedSettings.append(str(maxRes[0]))
	fetchedSettings.append('-Y')
	fetchedSettings.append(str(maxRes[1]))

	if dimensions['Anamorphic'] == 'auto':
		fetchedSettings.append('--auto-anamorphic')
	elif bool(dimensions['Anamorphic']) == False:
		fetchedSettings.append('--non-anamorphic')
	else:
		raise SettingError('profiles/dimensions.yml - Anamorphic is set to ' + fetchedSettings['Anamorphic'] + '. Only "off" and "auto" are currently supported.')



	return fetchedSettings


if __name__ == "__main__":
	print(getDimensionCommand())
