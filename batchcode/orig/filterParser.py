import yaml, reformat

def combDetect(settings):
	# mode=m:spatial-metric=s:motion-thresh=m:spatial-thresh=s:filter-mode=f:block-thresh=b:block-width=b:block-height=b:disable=d

	if bool(settings['Status']) != False:
		if settings['Preset'] == 'custom':
			values = ['--comb-detect=mode=', '', ':spatial-metric=', '', ':motion-thresh=', '', ':spatial-thresh=', '', ':filter-mode=', '', ':block-thresh=', '', ':block-width=', '', ':block-height=', '']
			keys = ['Mode', 'Spacial Metric', 'Motion Threshold', 'Spacial Threshold', 'Filter Mode', 'Block Threshold', 'Block Width', 'Block Height']

			for i in range(len(keys)):
				values[i*2+1] = settings['Custom'][keys[i]]
			
			return values
		
		elif settings['Preset'] == 'default':
			return '--comb-detect'
		
		else:
			return ['--comb-detect=', settings['Preset']]
		
	else:
		return '--no-comb-detect'



def decomb(settings):
	# mode=m:magnitude-thresh=m:variance-thresh=v:laplacian-thresh=l:dilation-thresh=d:erosion-thresh=e:noise-thresh=n:search-distance=s:postproc=p:parity=p

	if bool(settings['Status']) != False:
		if settings['Preset'] == 'custom':
			values = ['--decomb=mode=', '', ':magnitude-thresh=', '', ':variance-thresh=', '', ':laplacian-thresh=', '', ':dilation-thresh=', '', ':erosion-thresh=', '', ':noise-thresh=', '', ':search-distance=', '', ':postproc=', ':parity=', '']
			keys = ['Magnitude Threshold', 'Variance Threshold', 'Laplacian Threshold', 'Dilation Threshold', 'Erosion Threshold', 'Noise Threshold', 'Search Distance', 'Post-Processing', 'Parity']

			for i in range(len(keys)):
				values[i*2+1] = settings['Custom'][keys[i]]
			
			return values
		
		elif settings['Preset'] == 'default':
			return '--decomb'
		
		else:
			return ['--decomb=', settings['Preset']]
		
	else:
		return '--no-decomb'



def denoise(settings):
	def hqdn3d(settings, subsettings):
		if settings['Preset'] == 'custom':
			values = ['--hqdn3d=y-spatial=', '', ':cb-spatial=', '', ':cr-spatial=', '', ':y-temporal=', '', ':cb-temporal=', '', ':cr-temporal=', '']
			keys = ['Y', 'Cb', 'Cr']

			for i in range(len(keys)):
				values[i*2+1] = subsettings['Spacial'][keys[i]]
				values[i*2+7] = subsettings['Temporal'][keys[i]]
			
			#values.append('"')
			return values
		
		elif subsettings['Preset'] == 'default':
			return '--hqdn3d'
		
		else:
			return ['--hqdn3d=', subsettings['Preset']]
		

	def nlmeans(settings, subsettings):
		if settings['Preset'] == 'custom':
			values = ['--nlmeans=y-strength=', '', ':y-origin-tune=', '', ':y-patch-size=', '', ':y-range=', '', ':y-frame-count=', '', ':y-prefilter=', '', ':cb-strength=', '', ':cb-origin-tune=', '', ':cb-patch-size=', '', ':cb-range=', '', ':cb-frame-count=', '', ':cb-prefilter=', '', ':cr-strength=', '', ':cr-origin-tune=', '', ':cr-patch-size=', '', ':cr-range=', '', ':cr-frame-count=', '', ':cr-prefilter=', '', ':threads=', '']
			keys = ['Strength', 'Origin Tune', 'Patch Size', 'Range', 'Frame Count', 'Pre-filter']

			for i in range(len(keys)):
				values[i*2+1] = subsettings['Y'][keys[i]]
				values[i*2+14] = subsettings['Cb'][keys[i]]
				values[i*2+26] = subsettings['Cr'][keys[i]]

			values[37] = subsettings['Threads']
			
			return values
		
		elif settings['Preset'] == 'default':
			return '--nlmeans'
		
		else:
			return ['--nlmeans=', settings['Preset']]


	if bool(settings['Status']) != False:
		if settings['Algorithm'] == 'hqdn3d':
			# y-spatial=y:cb-spatial=c:cr-spatial=c:y-temporal=y:cb-temporal=c:cr-temporal=c
			return hqdn3d(settings, settings['HQDN3D'])
			
		elif settings['Algorithm'] == 'nlmeans':
			# y-strength=y:y-origin-tune=y:y-patch-size=y:y-range=y:y-frame-count=y:y-prefilter=y:cb-strength=c:cb-origin-tune=c:cb-patch-size=c:cb-range=c:cb-frame-count=c:cb-prefilter=c:cr-strength=c:cr-origin-tune=c:cr-patch-size=c:cr-range=c:cr-frame-count=c:cr-prefilter=c:threads=t
			return nlmeans(settings, settings['NLmeans'])
		
	else:
		return ['--no-hqdn3d', '--no-nlmeans']



def getFilterCommand():
	with open('profiles/filters.yml', 'r') as file1:
		filters = yaml.safe_load(file1)

	return [''.join(reformat.allStr(combDetect(filters['Comb Detect']))), ''.join(reformat.allStr(decomb(filters['Decomb']))), ''.join(reformat.allStr(denoise(filters['Denoise'])))]


if __name__ == '__main__':
	print(getFilterCommand())
