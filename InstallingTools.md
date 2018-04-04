# Installing tools

## Preparation

Last login: Wed Apr  4 09:38:02 on ttys000
petr@pc49$ cd /Users/petr/Desktop/git/tn-VariableRecipe 
petr@pc49$ sh install.sh
Password:
The directory '/Users/petr/Library/Caches/pip/http' or its parent directory is not owned by the current user and the cache has been disabled. Please check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
The directory '/Users/petr/Library/Caches/pip' or its parent directory is not owned by the current user and caching wheels has been disabled. check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
Collecting fonttools
  Downloading fonttools-3.25.0-py2.py3-none-any.whl (603kB)
    100% |████████████████████████████████| 686kB 217kB/s 
Installing collected packages: fonttools
Successfully installed fonttools-3.25.0
The directory '/Users/petr/Library/Caches/pip/http' or its parent directory is not owned by the current user and the cache has been disabled. Please check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
The directory '/Users/petr/Library/Caches/pip' or its parent directory is not owned by the current user and caching wheels has been disabled. check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
Collecting fontmake
  Downloading fontmake-1.4.0-py2.py3-none-any.whl
Collecting booleanOperations>=0.8.0 (from fontmake)
  Downloading booleanOperations-0.8.0-py2.py3-none-any.whl
Collecting defcon>=0.3.5 (from fontmake)
  Downloading defcon-0.5.0-py2.py3-none-any.whl (212kB)
    100% |████████████████████████████████| 296kB 304kB/s 
Collecting ufo2ft>=1.1.0 (from fontmake)
  Downloading ufo2ft-1.1.0-py2.py3-none-any.whl (47kB)
    100% |████████████████████████████████| 51kB 1.2MB/s 
Requirement already satisfied: fonttools>=3.21.2 in /Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages (from fontmake)
Collecting glyphsLib>=2.2.1 (from fontmake)
  Downloading glyphsLib-2.2.1-py2.py3-none-any.whl (272kB)
    100% |████████████████████████████████| 276kB 374kB/s 
Collecting MutatorMath>=2.1.0 (from fontmake)
  Downloading MutatorMath-2.1.0-py2.py3-none-any.whl
Collecting cu2qu>=1.3.0 (from fontmake)
  Downloading cu2qu-1.4.0-py2.py3-none-any.whl
Collecting pyclipper>=1.0.5 (from booleanOperations>=0.8.0->fontmake)
  Downloading pyclipper-1.1.0-cp35-cp35m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl (279kB)
    100% |████████████████████████████████| 368kB 913kB/s 
Collecting ufoLib>=2.0.0 (from booleanOperations>=0.8.0->fontmake)
  Downloading ufoLib-2.1.1-py2.py3-none-any.whl (93kB)
    100% |████████████████████████████████| 184kB 1.1MB/s 
Collecting compreffor>=0.4.5 (from ufo2ft>=1.1.0->fontmake)
  Downloading compreffor-0.4.6-cp35-cp35m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl (118kB)
    100% |████████████████████████████████| 122kB 152kB/s 
Collecting fontMath>=0.4.4 (from MutatorMath>=2.1.0->fontmake)
  Downloading fontMath-0.4.4-py2.py3-none-any.whl
Installing collected packages: pyclipper, ufoLib, booleanOperations, defcon, compreffor, cu2qu, ufo2ft, fontMath, MutatorMath, glyphsLib, fontmake
Successfully installed MutatorMath-2.1.0 booleanOperations-0.8.0 compreffor-0.4.6 cu2qu-1.4.0 defcon-0.5.0 fontMath-0.4.4 fontmake-1.4.0 glyphsLib-2.2.1 pyclipper-1.1.0 ufo2ft-1.1.0 ufoLib-2.1.1
petr@pc49$ 
