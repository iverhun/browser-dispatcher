# browser-dispatcher

## Prerequisites
1. Pyton 3
2. PIP
3. `pip install PyYAML`
4. `pip install pyinstaller`
1. `PYTHON_CONFIGURE_OPTS="--enable-framework" pyenv install 3.7.3`


## Configuration

### Targets
TODO

### Rules
The rules are defined in the `$HOME/.browser-dispatcher/config.yml` file as elements of the `rules` array.

By default, the URL schema is ignored. 
If you need to apply the rule to the URL schema, set the `ignore_url_schema` property to `False`   

The domain names starting with `www.` are handled the same way it wouldn't contain the `www` prefix, i.e. the
`www.example.com` is exactly the same as `example.com`
   
There are several types of rules. 

#### Pattern-based rules
##### Ant-like rules
TODO

##### Regular expression rules 
TODO

#### Host rules
You should use this type of rule if you need **exact match** of the host name, IP address and optionally port. 
The rule object has 2 properties:
1. collection of `hosts`
1. reference to the desired `target` 


Example:

```yaml
- hosts:
  - host1.com
  - host2.com
  - host3.com:3000
  target: *host
- hosts:
  - 192.168.0.100
  - 192.168.0.101:4000
  target: *ip
```


## Build from sources
### MacOS
1. `cd macos`
1. `make clean bundle`
7. Move the generated `dist/BrowserDispatcher.app` to your Applications folder.
8. Go to `Mac -> System Preferences -> General` and select the "Browser Dispatcher" as your default web browser.	

# Developer notes
* installing Python 3 on MacOS: https://opensource.com/article/19/5/python-3-default-mac
* Converting a plist File to XML from Binary
`plutil -convert xml1 Info.plist`
* Converting a plist File from XML to Binary
`plutil -convert binary1 Info.plist`

