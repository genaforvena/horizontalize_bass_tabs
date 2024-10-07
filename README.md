# Ultimate Guitar Bass Tab Downloader and String Combiner

This Python script downloads bass tabs from Ultimate Guitar, extracts the tab content, and reformats it into a more compact and readable format. It combines the tab lines for each string (G, D, A, E) while preserving the original tab structure.

## Features

- Downloads bass tabs from Ultimate Guitar URLs
- Extracts tab sections from the downloaded HTML content
- Combines tab lines for each string (G, D, A, E)
- Cleans the tab content, removing non-essential characters
- Limits the length of each combined string to improve readability
- Saves the reformatted tab to a text file

## Requirements

- Python 3.6 or higher
- `requests` library

## Installation

1. Ensure you have Python 3.6 or higher installed on your system.
2. Install the required `requests` library:

   ```
   pip install requests
   ```

3. Download the script file (`main.py`) to your local machine.

## Usage

1. Run the script from the command line:

   ```
   python main.py [max_length]
   ```

   Where `[max_length]` is an optional argument to set the maximum length of each combined string (default is 400 characters).

2. When prompted, enter the Ultimate Guitar URL for the bass tab you want to download and reformat.

3. The script will download the tab, reformat it, and save the result to a file named `combined_tab.txt` in the same directory as the script.

4. The reformatted tab will also be displayed in the console.

## Example

```
python main.py 500
Enter the Ultimate Guitar URL for the bass tab: https://tabs.ultimate-guitar.com/tab/john-coltrane/giant-steps-bass-2586318


Combined tab has been saved to combined_tab.txt

Combined Tab:
G||-4----2----|-0-----------|---------------|--------------||-0---------|-------------|---------4-----|----0--1--3--| |----3--0-----|-2-----------|-0--2--4--0--|-------------|
D||-----------|------3----1-|-1--0--------|--------------||------3----|-1-----------|------4-----4--|-3-----------| |-1--------1--|----0--2--4--|-------------|-2-----4-----|
A||-----------|-------------|---------3--1--|-0--------0---||-----------|------4----2-|-2-----------|-------------| |-------------|-------------|-------------|----4-----3--|
E||-----------|-------------|---------------|----3--2------||-----------|-------------|---------------|-------------| |-------------|-------------|-------------|-------------|
```

## Note

This script is intended for personal use only. Please respect Ultimate Guitar's terms of service and copyright laws when using this tool.

## Troubleshooting

If you encounter any issues:

1. Ensure you have a stable internet connection.
2. Check that the provided URL is valid and accessible.
3. Make sure you have the latest version of the `requests` library installed.

If problems persist, please open an issue on the GitHub repository.