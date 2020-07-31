# YouTube-Video-Grabber
#### Using Invidio.us RSS feed - Grabs all the latest videos uploaded by various YouTube channels provided

### Disclaimer:
- _This code doesn't use any official YouTube api_ 
- _Only uses public RSS feed from invidio.us_
- _Videos are not downloaded, just offering the links to the videos_

## Requirements
* `Python 3.8`

## Installation

```bash
# clone the repo
$ git clone https://github.com/Maneesh3/YouTube-Video-Grabber.git

# install the requirements
$ pip3 install -r requirements.txt
```

## Usage
```
usage: 
$ cd YT-Video-Grabber
$ python video-grabber.py

usage: video-grabber.py [-h] [-a] [-u CHURL] [-f FPATH]

[#] YouTube Video Grabber [#]

optional arguments:
  -h, --help                show this help message and exit
  -a, --add                 add channel flag; -a
  -u CHURL, --url CHURL     channel url; -u <URL>
  -f FPATH, --lfile FPATH   channel urls file; -f <file path>
  
Channel json file is created and backedup after every update made
```
  
## TODO:
- [x] adding list of channels, single channel  
- [ ] Main list function must be completed
- [ ] Make a flask app for GUI 
- [ ] Reconstruct the source code using classes and with proper documentation


Copyright (c) 2020 Maneesh
