![alt python errors](https://github.com/Riade-bg/Pyerrors/blob/master/images/py-errors.png) <br />
![alt python errors](https://img.shields.io/pypi/pyversions/Django?style=flat-square)
![alt python errors](https://img.shields.io/pypi/l/Photon?style=flat-square)
![alt python errors](https://img.shields.io/badge/Version-v1.0-red?style=flat-square) <br />

## What is Pyerrors?
In simple words pyerrors scan your script for errors and return a simplified version of the error that is easy to read and to understand.

### Standart EOF Python Error:
![alt python errors](https://github.com/Riade-bg/Pyerrors/blob/master/images/normal-error.png) <br />

### Pyerrors Errors:
![alt python errors](https://github.com/Riade-bg/Pyerrors/blob/master/images/pyerrors-error-1.png) <br />
![alt python errors](https://github.com/Riade-bg/Pyerrors/blob/master/images/pyerrors-error-2.png) <br />

# Usage
```
## Go through requirements.txt an install dependencies if you find ImportError problem.
pip install -r requirements.txt
```
python pyerrors.py --errors|-e path_to_your_script
```
## Note: include this line on top of your code [ import warnings warnings.filterwarnings("error") ]
This will run the script and scan for errors in your script. Also you can scan for warnings:
python pyerrors.py --warnings|-w path_to_your_script
```

# Suported Errors in Pyerrors
```
  Exeptions:
  |
  |- • AssertionError
  |- • AttributeError
  |- • EOFError
  |- • FileNotFoundError
  |- • ImportError
  |- • IndexError
  |- • KeyError
  |- • KeyboardInterrupt
  |- • MemoryError
  |- • NameError
  |- • NotImplementedError
  |- • ModuleNotFoundError
  |- • OSError
  |- • OverflowError
  |- • ReferenceError
  |- • RuntimeError
  |- • StopIteration
  |- • SyntaxError
  |- • IndentationError
  |- • TabError
  |- • SystemError
  |- • TypeError
  |- • UnboundLocalError
  |- • ValueError
  |- • ZeroDivisionError
```   

**More features will be added to the script in later versions.**
