#!/usr/bin/env bash

ALL_LINES=$(find $HOME/Library/Application\ Support/Google/Chrome/* -name Preferences -print0 | xargs -I % -0 jq -r  "[{name: .profile.name, file:\"%\"}] | map_values({name: .name, profile: .file | split(\"/\")[-2] })" % )
echo $ALL_LINES | sed 's/\] \[/,/g' | jq '.' > $HOME/.browser-dispatcher/profiles.json

