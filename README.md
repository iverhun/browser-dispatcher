# browser-dispatcher

## Prerequisites
1. Pyton 3
2. PIP
3. `pip install PyYAML`
4. `pip install pyinstaller`
1. `PYTHON_CONFIGURE_OPTS="--enable-framework" pyenv install 3.7.3`
`


## Configuration
TODO

## Build from sources
### MacOS
1. Download the [platypus](https://sveinbjorn.org/platypus) tool
2. In the "App Name" field type `Browser Dispatcher`
3. In the script path, specify the `<path to this repo>/macos/browser-dispatcher.sh`
4. Select the "Accept dropped items" checkbox and click "Settings" button.
5. Select the "Register as URI scheme handler" checbox and add `http` and `https` to the list if URI schemes
6. Hit "Create App" button.
7. Move the generated `BrowserDispatcher.app` to your Applications folder.
8. Go to `Mac -> System Preferences -> General` and select the "Browser Dispatcher" as your default web browser.	

# Developer notes
* installing Python 3 on MacOS: https://opensource.com/article/19/5/python-3-default-mac
* Converting a plist File to XML from Binary
`plutil -convert xml1 Info.plist`
* Converting a plist File from XML to Binary
`plutil -convert binary1 Info.plist`

