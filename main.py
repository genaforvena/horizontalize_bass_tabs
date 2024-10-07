import requests
import re
import sys

def download_tab(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"An error occurred while downloading the tab: {e}")
        return None

def clear_line(line):
    return re.sub(r'[^0-9|-]', '', line)

def extract_and_combine_tabs(text, max_length=400):
    # Extract tab sections
    tab_pattern = r'\[tab\](.*?)\[/tab\]'
    tab_sections = re.findall(tab_pattern, text, re.DOTALL)
    
    g_strings = []
    d_strings = []
    a_strings = []
    e_strings = []
    
    for tab in tab_sections:
        lines = tab.strip().split('\\n')

        for line in lines:
            clean_line = clear_line(line)
            if 'G|' in line:
                if not g_strings or len(g_strings[-1]) + len(line) + 1 > max_length:
                    g_strings.append(clean_line)
                else:
                    g_strings[-1] += (clean_line) + " "
            if 'D|' in line:
                if not d_strings or len(d_strings[-1]) + len(line) + 1 > max_length:
                    d_strings.append(clean_line)
                else:
                    d_strings[-1] += clean_line + " "
            if 'A|' in line:
                if not a_strings or len(a_strings[-1]) + len(line) + 1 > max_length:
                    a_strings.append(clean_line)
                else:
                    a_strings[-1] += clean_line + " "
            if 'E|' in line:
                if not e_strings or len(e_strings[-1]) + len(line) + 1 > max_length:
                    e_strings.append(clean_line)
                else:
                    e_strings[-1] += clean_line + " "

    combined_tabs = ""
    for g, d, a, e in zip(g_strings, d_strings, a_strings, e_strings):
        combined_tabs += 'G|' + g + '\n' + 'D|' + d + '\n' + 'A|' + a + '\n' + 'E|' + e + '\n' + '\n\n'

    return combined_tabs.strip()

def main():
    print("Ultimate Guitar Bass Tab Downloader and String Combiner")
    print("------------------------------------------------------")
    
    url = input("Enter the Ultimate Guitar URL for the bass tab: ")
    
    if len(sys.argv) > 1:
        max_length = int(sys.argv[1])
    else:
        max_length = 400
    
    html_content = download_tab(url)
    
    if html_content:
        combined_tabs = extract_and_combine_tabs(html_content, max_length)
        
        if combined_tabs:
            output_file = "combined_tab.txt"
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(combined_tabs)
            print(f"\nCombined tab has been saved to {output_file}")
            print("\nCombined Tab:")
            print(combined_tabs)
        else:
            print("No tab sections found in the downloaded content.")
    else:
        print("Failed to download the tab.")

if __name__ == "__main__":
    main()