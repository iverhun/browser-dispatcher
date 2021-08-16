build: clean test bundle archive

archive:
	tar -zcvf "dist/Browser Dispatcher.app.tar.gz" "dist/Browser Dispatcher.app"

bundle: prepare iconset
	python -m PyInstaller --onefile --noconfirm --noconsole --clean --log-level=WARN --strip --osx-bundle-identifier=org.iverhun.BrowserDispatcher --icon=build/AppIcon.icns --name="Browser Dispatcher" browser_dispatcher.py
	cp -rp resources/Info.plist dist/Browser\ Dispatcher.app/Contents/

iconset:
	mkdir -p build/AppIcon.iconset
	sips -z 16 16     resources/BD.png --out build/AppIcon.iconset/icon_16x16.png
	sips -z 32 32     resources/BD.png --out build/AppIcon.iconset/icon_16x16@2x.png
	sips -z 32 32     resources/BD.png --out build/AppIcon.iconset/icon_32x32.png
	sips -z 64 64     resources/BD.png --out build/AppIcon.iconset/icon_32x32@2x.png
	sips -z 128 128   resources/BD.png --out build/AppIcon.iconset/icon_128x128.png
	sips -z 256 256   resources/BD.png --out build/AppIcon.iconset/icon_128x128@2x.png
	sips -z 256 256   resources/BD.png --out build/AppIcon.iconset/icon_256x256.png
	sips -z 512 512   resources/BD.png --out build/AppIcon.iconset/icon_256x256@2x.png
	sips -z 512 512   resources/BD.png --out build/AppIcon.iconset/icon_512x512.png
	cp resources/BD.png build/AppIcon.iconset/icon_512x512@2x.png
	iconutil -c icns build/AppIcon.iconset

prepare:
	pip install -r requirements.txt

test: prepare
	python -m unittest discover

clean:
	rm -rf build
	rm -rf dist
