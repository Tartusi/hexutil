# hexutil

## Description

Transform text to hex and hex to to text

## Usage

### htt (hextotext)
```
python hexutil.py htt -h   
usage: hexutil.py htt [-h] hex

positional arguments:
  hex         hex to textify

optional arguments:
  -h, --help  show this help message and exit
```
```
$ python hexutil.py htt 61626364
abcd
```

### tth (texttohex)

```
python hexutil.py tth -h
usage: hexutil.py tth [-h] [-rotate ROTATE] [-reverse] text

positional arguments:
  text            text to hexify

optional arguments:
  -h, --help      show this help message and exit
  -rotate ROTATE  Print a new line each [rotate] char
  -reverse        reverse the hex printed on the line
```

```
$ python hexutil.py tth  bonjour
626f6e6a
6f7572
$ python hexutil.py tth  -reverse bonjour
72756f6a
6e6f62
$ python hexutil.py tth  -reverse -rotate 2 bonjour
7275
6f6a
6e6f
62
```

