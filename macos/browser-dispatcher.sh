#/bin/bash

# TODO: remove this debug line
echo "Hello $1" >> ~/tmp/script.log

function list_profiles() {
	find $HOME/Library/Application\ Support/Google/Chrome/* -name Preferences -print0 | xargs -I % -0 jq -r  "[{name: .profile.name, file:\"%\"}] | map_values({name: .name, profile: .file | split(\"/\")[-2] })" %
}

function open_in_profile () {
	browser=$1
	profile=$2
	url=$3
	/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --profile-directory="${profile}" "${url}" >> /dev/null &
}

function open_incognito () {
	browser=$1
	url=$2

	/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --incognito "${url}" >> /dev/null &
}

function open() {
  browser=$1
	profile=$2
	url=$3
}

result=`./browser_resolver.py $1 ../config/browser-config.yml`

mapfile -t arr <<< "$result"

browser=${arr[0]}
profile=${arr[1]}
incognito=${arr[2]}

echo "Browser: ${browser}"
echo "Profile: ${profile}"
echo "Incognoto: ${incognito}"

open_in_profile "${profile}" "$1"
