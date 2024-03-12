# wraparound

To build: 
- make sure conf.txt is deleted
- `cxfreeze -c -s main.py --target-dir dist --target-name wraparound` inside the root folder
- copy `resources/` into `dist/resources`

To upload:
- zip everything inside `dist/` and name it `wraparound.zip`
- `butler push wraparound.zip kyfex-uwu/wraparound:windows --userversion [version]`
