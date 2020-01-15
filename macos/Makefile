bundle: prepare
	pyinstaller --onefile --noconfirm --noconsole --clean --log-level=WARN --strip --osx-bundle-identifier=org.iverhun.BrowserDispatcher --icon=resources/AppIcon.icns --name="Browser Dispatcher" browser_dispatcher.py
	cp -rp resources/Info.plist dist/Browser\ Dispatcher.app/Contents/

prepare:
	pip install -r requirements.txt

clean:
	rm -rf build
	rm -rf dist