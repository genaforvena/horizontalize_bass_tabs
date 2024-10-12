let enabled = false;

browser.browserAction.onClicked.addListener((tab) => {
  enabled = !enabled;
  browser.browserAction.setIcon({
    path: enabled ? "icon19_on.png" : "icon19.png"
  });
  browser.tabs.sendMessage(tab.id, { action: "toggle", enabled: enabled });
});

browser.tabs.onZoomChange.addListener((zoomChangeInfo) => {
  if (enabled) {
    browser.tabs.sendMessage(zoomChangeInfo.tabId, { action: "updateZoom", zoomFactor: zoomChangeInfo.newZoomFactor });
  }
});
