rmdir /s /q "%userprofile%\AppData\Roaming\Sublime Text\Packages\Jenkinsfile"
timeout /t 3
mkdir "%userprofile%\AppData\Roaming\Sublime Text\Packages\Jenkinsfile"
copy . "%userprofile%\AppData\Roaming\Sublime Text\Packages\Jenkinsfile"