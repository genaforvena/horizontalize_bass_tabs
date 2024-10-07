import requests
import re

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

def extract_and_combine_tabs(text):
    # Extract tab sections
    tab_pattern = r'\[tab\](.*?)\[/tab\]'
    tab_sections = re.findall(tab_pattern, text, re.DOTALL)
    
    g_string = ""
    d_string = ""
    a_string = ""
    e_string = ""
    
    for tab in tab_sections:
        lines = tab.strip().split('\\n')

        for line in lines:
            if 'G|' in line:
                g_string += line + " "
            if 'D|' in line:
                d_string += line + " "
            if 'A|' in line:
                a_string += line + " "
            if 'E|' in line:
                e_string += line + " "

    
    tabs = f"G{g_string}\nD{d_string}\nA{a_string}\nE{e_string}"
    g_string = re.sub(r'[^0-9|-]', '', g_string)  
    d_string = re.sub(r'[^0-9|-]', '', d_string)  
    a_string = re.sub(r'[^0-9|-]', '', a_string)  
    e_string = re.sub(r'[^0-9|-]', '', e_string)  
    
    combined_tabs = f"G{g_string}\nD{d_string}\nA{a_string}\nE{e_string}"
    return combined_tabs

def main():
    print("Ultimate Guitar Bass Tab Downloader and String Combiner")
    print("------------------------------------------------------")
    
    url = input("Enter the Ultimate Guitar URL for the bass tab: ")
    
    html_content = download_tab(url)
    
    if html_content:
        combined_tabs = extract_and_combine_tabs(html_content)
        
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