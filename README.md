<!-- # HandBrake Auto-Transcode

Designed for automated HandBrake batch ripping of TV shows

This program grabs information from various YAML files and one CSV file and sends a command to HandBrakeCLI based on that information to rip specified titles off of disk images. It is designed specifically to speed up the ripping of TV show collector's editions on DVDs or Blu-Rays, using the syntax of c#d#t#.iso:
- c# = case number
- d# = disk number
- t# = title number
This is also the syntax used in the CSV file that contains a list of all titles on the disk, regardless if they will be ripped. Selecting of titles to rip is done via the case#/disk#.yml file, where metadata about the title is also stored.

Default rip profiles for audio, video, filters, dimensions, and subtitles *(wip)* are stored in profiles/(profileName).yml. 

Currently, the only releases available are for Windows, because that's what I use for transcoding (go NVENC!), but I will be publishing releases for other platforms once I have more time — and once this is more complete. However, because it's just Python 3 source, it will run on whatever platform can run HandBrakeCLI and Python. I believe I programmed it to look for system-wide installs of HandBrakeCLI in non-Windows OSs *as long as the `Executable Path:` key in ['settings.yml'] is set to `Unix`.* Also, if excecuting from source, `pyyaml` must be installed. It can be easily installed via `pip install pyyaml`.



# Note for Windows users:

The HandBrakeCLI executable should be placed in `/HandBrake/HandBrakeCLI.exe`, where `/` is the root of the release folder. If you would like to use a different location, you must change the `Executable Path:` key in [`settings.yml`]. -->

# Batch\[-en]Code

HandBrake sucks for batch transcoding, even via the CLI. And I (a Blu-ray collector who doesn't re-encode his Bly-rays&mdash;until now) *hate* HandBrake's default settings. Even the "Super HQ" presets are not high quality enough for me. Transcoding HDR10 4K Blu-ray rips down to 32 Mbps, though still much higher than any streaming service will serve you, feels incredibly wrong to me.

I could create my own presets (which is a giant pain on its own), but those presets don't really save audio settings. They do sometimes have some settings, but they are unacceptable for my desires. I want all tracks to be carried over, unmodified, un-downmixed, and un-reencoded. Usually, I want HandBrake to just touch the video and completely ignore the audio&mdash;a setting or CLI flag ***that does not exist.***

These are my opinions, and some may consider them rediculous. This hobby is full of very opinionated people. That's why this program is configurable.

This is the spiritual continuation of a previous project (that's still in this repo, but the code is horrible and I wrote literally no comments... I was still learning to program at the time).

So, for the tl;dr, I made this out of frustration, bafflement, and strong opinions.

## Project Status

Not ready for production.

## Documentation

I'm working on it as I go along, but at this stage in the development where things may change significantly in a short amount of time, it's not worth creating dedicated documentation just yet. At this point, all documentation can be found within my code, which I aim to comment well.