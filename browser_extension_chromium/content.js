let enabled = false;
let zoomFactor = 1;

function clearLine(line) {
  return line.replace(/[^0-9|-]/g, '');
}

function extractAndCombineTabs(text, maxLength = 400) {
  const tabPattern = /\[tab\](.*?)\[\/tab\]/gs;
  const tabSections = text.match(tabPattern);
  
  const strings = { 'G': [], 'D': [], 'A': [], 'E': [] };
  
  if (tabSections) {
    tabSections.forEach(tab => {
      const lines = tab.trim().split('\n');
      lines.forEach(line => {
        const cleanLine = clearLine(line);
        ['G', 'D', 'A', 'E'].forEach(string => {
          if (line.includes(`${string}|`)) {
            if (!strings[string].length || strings[string][strings[string].length - 1].length + cleanLine.length + 1 > maxLength) {
              strings[string].push(cleanLine);
            } else {
              strings[string][strings[string].length - 1] += cleanLine + " ";
            }
          }
        });
      });
    });
  }
  
  let combinedTabs = "";
  const maxLines = Math.max(...Object.values(strings).map(s => s.length));
  for (let i = 0; i < maxLines; i++) {
    combinedTabs += `G|${strings['G'][i] || ''}\n`;
    combinedTabs += `D|${strings['D'][i] || ''}\n`;
    combinedTabs += `A|${strings['A'][i] || ''}\n`;
    combinedTabs += `E|${strings['E'][i] || ''}\n\n`;
  }
  
  return combinedTabs.trim();
}

function convertTab() {
  const tabContent = document.querySelector('.js-tab-content');
  if (tabContent) {
    const combinedTabs = extractAndCombineTabs(tabContent.innerHTML);
    const formattedTab = document.createElement('pre');
    formattedTab.textContent = combinedTabs;
    formattedTab.style.fontFamily = 'monospace';
    formattedTab.style.whiteSpace = 'pre';
    formattedTab.style.fontSize = `${14 * zoomFactor}px`;
    formattedTab.style.lineHeight = '1.2';
    formattedTab.style.backgroundColor = '#f5f5f5';
    formattedTab.style.padding = '10px';
    formattedTab.style.border = '1px solid #ddd';
    formattedTab.style.borderRadius = '4px';
    formattedTab.style.overflow = 'auto';
    
    if (tabContent.nextElementSibling && tabContent.nextElementSibling.classList.contains('formatted-tab')) {
      tabContent.nextElementSibling.remove();
    }
    tabContent.insertAdjacentElement('afterend', formattedTab);
    formattedTab.classList.add('formatted-tab');
  }
}

browser.runtime.onMessage.addListener((message) => {
  if (message.action === "toggle") {
    enabled = message.enabled;
    if (enabled) {
      convertTab();
    } else {
      const formattedTab = document.querySelector('.formatted-tab');
      if (formattedTab) {
        formattedTab.remove();
      }
    }
  } else if (message.action === "updateZoom") {
    zoomFactor = message.zoomFactor;
    if (enabled) {
      convertTab();
    }
  }
});
