#!/bin/sh
packageDirDarwin=~/Library/Application\ Support/Sublime\ Text\ 3/Packages/Jenkinsfile
packageDirLinux=~/.config/sublime-text/Packages/Jenkinsfile

if [ $(echo $OSTYPE | egrep "darwin") ]; then
    packageDir=$packageDirDarwin
else
    packageDir=$packageDirLinux
fi

if [ $(which chokidar) ]; then
    chokidar "**/*.py" -c "rm -fR \"$packageDir\" &&
        sleep 3 &&
        rsync -avu --exclude=".*" \"$PWD\" \"$packageDir\""
else
    while inotifywait -q --event modify --format '%w' ${PWD}/*.py; do
    rm -fR "$packageDir"
    echo Detected change.
    sleep 3;
    rsync -avu --exclude=".*" "${PWD}/" "$packageDir"
    done
fi