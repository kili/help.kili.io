Kili Help Documentation
============

## INTRO
This repository contains the sources used to build Kili's help documentation.<br>
We use [pelican](http://docs.getpelican.com/en/3.3.0/) to build the contents of this repository into the site you see at http://help.kili.io.

## PREREQUIESITES
To contribute, we reccomend you install:-

- [Python >= 2.7](https://www.python.org/download/releases/2.7), 
- [PIP](http://www.pip-installer.org/en/latest/installing.html) and 
- [virtualenv](http://www.virtualenv.org/en/latest/virtualenv.html)


## INSTALLATION

1. Fork the source - https://github.com/kili/help.kili.io/fork.
2. Clone your fork and cd into it.
3. Create a virtualenv for your repo:- `mkvirtualenv -a . help.kili.io`.
4. Install the remaining dependencies:-  `pip install -r requirements.txt`.
5. Initialize & update the submodule with our pelican theme: `git submodule init && git submodule update`.

## CONTRIBUTE

1. Start the development server:- `./develop_server.sh start`.
2. Add or edit markdown articles in the content folder.
3. Add, commit and push your changes.
4. Send us a pull request.
5. ????
6. Profit!!!11 .....Seriously! We will pay you 50 USD for each UNIQUE, [HIGH QUALITY](https://wiki.openstack.org/wiki/Documentation/Conventions) article.)

We look forward to including your content.
Cheers and enjoy contributing!


Kili Team
