#!/bin/bash

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
	incognito=$3
	url=$4

	if [[ "${incognito}" == "True" ]]; then
		open_incognito $browser $url
	else
		open_in_profile $browser $profile $url
	fi
}

result=`./browser_dispatcher.py $1 ../config/browser-config.yml`

echo $result

mapfile -t arr <<< "$result"

browser=${arr[0]}
profile=${arr[1]}
incognito=${arr[2]}

url=$1

echo "Browser: ${browser}"
echo "Profile: ${profile}"
echo "Incognoto: ${incognito}"
echo "Url: ${url}"

#open $browser $profile $incognito $url
