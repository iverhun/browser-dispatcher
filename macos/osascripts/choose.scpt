on run theBrowserProfileChoices
  tell application "System Events"
    activate
    set theFavoriteFruit to choose from list theBrowserProfileChoices with prompt "Select browser profile:" default items {item 1 of theBrowserProfileChoices}
  end tell
end run