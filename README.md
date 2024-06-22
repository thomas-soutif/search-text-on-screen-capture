A tool that allow you to looking for a list of words in real-time, by capturing the screen and making analysis with Tesseract.
It's quite fast on specific region (around 0.3seconds), and on the entire screen it takes around 1 second.

## Requirement

You need to have Tesseract install on your system to use this script. 

Here the github link to install it on Windows : https://github.com/UB-Mannheim/tesseract/wiki

For Linux, you can install the package ```tesseract-ocr``` depend on your distribution.

## Installation on Windows

```bash
python -m venv venv
.\venv\Script\activate.bat
pip install -r requirements.txt
```

## Installation on linux

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python find.py [your list of words separate by space]
#For example
python find.py Search Youtube 
```

In the example, it will so looking for the word Search, and Youtube , then the program will exit when finding.

### Choose the part of the screen

By default, it will look only on the top left of the screen, but if you want to choose that, you can modify the line

```python
screen_image = capture_top_left_screen_region()
```

in the ```main()``` function.
