#!/bin/sh
packageDir=~/Library/Application\ Support/Sublime\ Text\ 3/Packages/Jenkinsfile
devDir=~/code/sublime-Jenkinsfile/

if [ $(which chokidar) ]; then
    chokidar "**/*.py" -c "rm -fR \"$packageDir\" &&
        sleep 3 &&
        rsync -avu --exclude=".*" \"$devDir\" \"$packageDir\""
else
    while inotifywait -q --event modify --format '%w' ~/sublime-Jenkinsfile/*.py; do
    cd ~/.config/sublime-text/Packages
    rm -fR Jenkinsfile
    echo Detected change.
    sleep 3;
    rsync -avu ~/sublime-Jenkinsfile/ Jenkinsfile
    ls -la ~/.config/sublime-text/Packages
    done
fi