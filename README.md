# sugaroid
The Intelligent Sugar Artificial Intelligence

## Installation
If sugaroid gets published to PYPI, the command to install it should be relatively simple
```bash
python3 -m pip install sugaroid --user
```
Until then
```bash
git clone https://github.com/srevinsaju/sugaroid
cd sugaroid
pip3 install .
```

## Getting Started
Sugaroid is an newly developing AI, aiming to serve as companion to kids as well as a reader of documentation. 
Initially designed for the @sugarlabs organization, sugaroid intends to read text files, ReST and Markdown documents,
parse it and provide meaninful insights for questions regarding the same
Sugaroid uses Natural Language Processing (NLP) using `nltk` and `spacy` to comprehend answers

To get `sugaroid` running
execute
```bash
$ sugaroid
```

## Language
The language system of Sugar API is cloudy. The current system uses `googletrans` to translate its commands and use trained 
data. Basic corpus's of recognized languages are supported and will be implemented before the release of v1

## API
Sugaroid API is modular, which benfits its implementation in other sugar activitiesm if necessary

Documentation will be upddated later

# License
Sugaroid is based on `MIT` License, anyone is free to modify this open source code. Contributions are accepted as PRs only 
and not patches. 

# Disclaimer
Sugaroid is only a developing AI, the information provided by it may / may not be correct. The author does not take any
resoponsibility on the information provided by it, if it holds wrong. Users wishing to see a better sugaroid may raise an
Issue to the code base to help corrections and enable future developers to contribute
