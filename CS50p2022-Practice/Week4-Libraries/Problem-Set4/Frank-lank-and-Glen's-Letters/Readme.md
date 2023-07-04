# Frank, Ian and Glen’s Letters

FIGlet, named after Frank, Ian, and Glen’s letters, is a program from the early 1990s for making large letters out of ordinary text, a form of ASCII art:

```bash
 _ _ _          _   _     _
| (_) | _____  | |_| |__ (_)___
| | | |/ / _ \ | __| '_ \| / __|
| | |   <  __/ | |_| | | | \__ \
|_|_|_|\_\___|  \__|_| |_|_|___/
```

Among the fonts supported by FIGlet are those at figlet.org/examples.html.

FIGlet has since been ported to Python as a module called pyfiglet.

In a file called `figlet.py`, implement a program that:

- Expects zero or two command-line arguments:
  - Zero if the user would like to output text in a random font.
  - Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.
- Prompts the user for a str of text.
- Outputs that text in the desired font.
If the user provides two command-line arguments and the first is not `-f` or `--font` or the second is not the name of a font, the program should exit via sys.exit with an error message.

## Hints

- You can install `pyfiglet` with:

```bash
pip install pyfiglet
```

- The documentation for pyfiglet isn’t very clear, but you can use the module as follows:

```python
from pyfiglet import Figlet

figlet = Figlet()
```

You can then get a `list` of available fonts with code like this:

```python
figlet.getFonts()
```

You can set the font with code like this, wherein `f` is the font’s name as a `str`:

```python
figlet.setFont(font=f)
```

And you can output text in that font with code like this, wherein `s` is that text as a `str`:

```python
print(figlet.renderText(s))
```

Note that the random module comes with quite a few functions, per docs.python.org/3/library/random.html. 

## Demo

```bash
$ python figlet.py                                                  
Input: hello, world                                                        
Output:                                                                         
 _          _ _                             _     _                             
| |__   ___| | | ___    __      _____  _ __| | __| |                            
| '_ \ / _ \ | |/ _ \   \ \ /\ / / _ \| '__| |/ _` |                            
| | | |  __/ | | (_) |   \ V  V / (_) | |  | | (_| |                            
|_| |_|\___|_|_|\___( )   \_/\_/ \___/|_|  |_|\__,_|                            
                    |/                                                        

$ python figlet.py -f slant                                                     
Input: hello, world                                                             
Output:                                                                         
    __         ____                               __    __                      
   / /_  ___  / / /___       _      ______  _____/ /___/ /                      
  / __ \/ _ \/ / / __ \     | | /| / / __ \/ ___/ / __  /                       
 / / / /  __/ / / /_/ /     | |/ |/ / /_/ / /  / / /_/ /                        
/_/ /_/\___/_/_/\____( )    |__/|__/\____/_/  /_/\__,_/                         
                     |/

$ python figlet.py --font rectangles                                            
Input: hello, world                                                             
Output:                                                                         
                                                                                
 _       _ _                        _   _                                       
| |_ ___| | |___      _ _ _ ___ ___| |_| |                                      
|   | -_| | | . |_   | | | | . |  _| | . |                                      
|_|_|___|_|_|___| |  |_____|___|_| |_|___|                                      
                |_| 

```

## How to Test

Here’s how to test your code manually:

- Run your program with `python figlet.py test`. Your program should exit via `sys.exit` and print an error message:

```bash
Invalid usage
```

- Run your program with `python figlet.py -a slant`. Your program should exit via `sys.exit` and print an error message:

```bash
Invalid usage
```

- Run your program with `python figlet.py -f invalid_font`. Your program should exit via `sys.exit` and print an error message:

```bash
Invalid usage
```

- Run your program with `python figlet.py -f slant`. Type `CS50`. Your program should print the following:

```bash
   ___________ __________ 
  / ____/ ___// ____/ __ \
 / /    \__ \/___ \/ / / /
/ /___ ___/ /___/ / /_/ / 
\____//____/_____/\____/  
```

- Run your program with `python figlet.py -f rectangles`. Type `Hello, world`. Your program should print the following:

```bash
 _____     _ _                        _   _ 
|  |  |___| | |___      _ _ _ ___ ___| |_| |
|     | -_| | | . |_   | | | | . |  _| | . |
|__|__|___|_|_|___| |  |_____|___|_| |_|___|
                  |_|                       
```

- Run your program with `python figlet.py -f alphabet`. Type Moo. Your program should print the following:

```bash
M   M         
MM MM         
M M M ooo ooo 
M   M o o o o 
M   M ooo ooo         
```