Kili Help Documentation
============

## INTRO
This repository contains the sources used to build [Kili's](http://kili.io)  help documentation.<br>
We use <a href="http://docs.getpelican.com" target="_blank">pelican</a> to build the contents of this repository into the site you see at <a href="http://help.kili.io">help.kili.io</a>

## PREREQUIESITES
To contribute, we recommend you install:-

- <a href="https://www.python.org/download/releases/2.7" target="_blank">Python >= 2.7</a>
- <a href="http://www.pip-installer.org/en/latest/installing.html" target="_blank">PIP</a>
- <a href="http://www.virtualenv.org/en/latest/virtualenv.html" target="_blank">virtualenv</a>


## INSTALLATION

1. <a href="https://github.com/kili/help.kili.io/fork" target="_blank">Click here to fork this Repo</a>.
2. Clone your fork and cd into it.
3. Create a virtualenv for your repo:- `mkvirtualenv -a . help.kili.io`.
4. Install the remaining dependencies:-  `pip install -r requirements.txt`.
5. Initialize & update the submodule with our pelican theme: `git submodule init && git submodule update`.

## CONTRIBUTE

1. Start the development server:- `./develop_server.sh start`.
2. Add or edit markdown articles in the content folder.
3. Add, commit and push your changes.
4. Send us a pull request.
5. We'll work with you to make it better.  The most important thing is the article, don't worry if you can't get Pelican to work - just submit the pull request with the article in Markdown format and we an go from there.
6. Profit!!!! .....(We will pay you 50 USD for each UNIQUE, <a href="https://wiki.openstack.org/wiki/Documentation/Conventions" target="_blank" >HIGH QUALITY</a> article.)

We look forward to including your content.

Cheers and enjoy contributing!
