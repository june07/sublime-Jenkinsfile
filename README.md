# sublime-Jenkinsfile

Jenkinsfile is a plugin for Sublime Text.

[https://packagecontrol.io/packages/Jenkinsfile](https://packagecontrol.io/packages/Jenkinsfile)

  - Securely (ssh) lint your Jenkinsfile ([What is a Jenkinsfile?](https://jenkins.io/doc/book/pipeline/jenkinsfile/)) inside of Sublime Text
  - Lint against Jenkins cloud instance if ssh access is unavailble on your primary environment
  - Magic

Jenkins includes Pipeline Development Tools as shown on [Jenkins.io][jenkins.io linter]...
> Jenkins can validate, or "lint", a Declarative Pipeline from the command line before actually running it.
> This can be done using a Jenkins CLI command or by making an HTTP POST request with appropriate parameters.
> We **recommended using the SSH interface** to run the linter.
> See the Jenkins CLI documentation for details on how to properly configure Jenkins for secure command-line access.


## Technology

* [Sublime Text] - obviously

Jenkinsfile uses a number of open source projects to work properly:
* [Python] - a programming language changes the world
* [SSH] - a cryptographic network protocol for operating network services securely over an unsecured network

And of course Jenkinsfile itself is open source with a [public Git repository][jenkinsfilegh] on GitHub.

## How to install

With Package Control:
1. First step is done with Package Control or manually
    - **With Package Control**
    Run “Package Control: Install Package” command, find and install Jenkinsfile plugin.

    - **Manually** *(without Package Control)*:
    Clone or download from [git][jenkinsfilegh] into your packages folder (in ST, find Browse Packages (in ST4 it's under Preferences)… menu item to open this folder).
    note: You must clone or download into a directory named "Jenkinsfile" and not sublime-Jenkinsfile.
    
    ![image](https://user-images.githubusercontent.com/11353590/219444106-d6207f7e-e872-48d2-80b0-b715c65acd25.png)

2.  Restart Sublime Text (if required)

## Setup

~~Currently you must use Pageant (Windows) to create a session that can authenticate via ssh to your Jenkins host.~~<br>
You can now use this plugin via two methods either via Pageant on Windows or via plain SSH.

1. Using via SSH (Linux, OSX, or Windows):
   * Set the `jenkins_ssh_user` (default admin), `jenkins_ssh_host` (default localhost), and `jenkins_ssh_port` (default 22) configuration values to match that of your Jenkins server.<br><br>
   * Note: On Windows you must clear the pageant_session configuration variable to use SSH.
2. Or for a Pageant setup on Windows:
   * The name of the session must match the configured value of `pageant_session` (default is "jenkins") as shown:
      ![](http://june07.github.io/image/JenkinsfilePageantConfig500.jpg)

## Usage

Now whenever you have are editing a Jenkinsfile (must be named as such) and save the file, the plugin will invoke the remote instance of the Jenkins declarative-linter.
The file can also be linted without saving by using the keyboard shortcut (cntl-alt-j by default)

![](http://june07.github.io/image/JenkinsfileScreenshot1.jpg)
![](http://june07.github.io/image/JenkinsfileScreenshot2.jpg)

## Todos

 - Add support for ~~Linux~~(done 2/16/23!), All OSs are not supported via SSH.
 - Add hosted Jenkins validation

License
----

MIT

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [jenkins.io linter]: <https://jenkins.io/doc/book/pipeline/development/#linter>
   [python]: <https://www.python.org/>
   [jenkinsfilegh]: <https://github.com/june07/sublime-Jenkinsfile>
   [Sublime Text]: <https://www.sublimetext.com/>
   [SSH]: <https://en.wikipedia.org/wiki/Secure_Shell>
   [putty/pageant]: <https://www.putty.org/>
   
.
