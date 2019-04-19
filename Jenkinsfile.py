import sys
import re
import os
import logging
import subprocess
from subprocess import Popen, PIPE

import sublime
import sublime_plugin

logger = None
settings = None

def plugin_loaded():
  global settings
  global setup_run

  settings = sublime.load_settings('Jenkinsfile.sublime-settings')
  setup_logging()

def setup_logging():
  global logger

  logdir = os.path.join(os.path.expanduser('~'), '.jenkinsfile')
  logfile = os.path.join(logdir, settings.get('logfile'))
  if not os.path.isdir(logdir):
    os.mkdir(logdir)

  logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
    datefmt='%m-%d %H:%M',
    filename=logfile,
    filemode='a'
  )
  logger = logging.getLogger('jenkinsfile')
  logger.debug('Logging started.')

def status_message(message):
  sublime.active_window().status_message(message)

if sublime.platform() == 'windows':
  startupinfo = subprocess.STARTUPINFO()
  startupinfo.dwFlags = subprocess.CREATE_NEW_CONSOLE | subprocess.STARTF_USESHOWWINDOW
  startupinfo.wShowWindow = subprocess.SW_HIDE  

class JenkinsfileCommand(sublime_plugin.TextCommand):
  global logger

  def run(self, edit):
    view = self.view
    if os.path.basename(view.file_name()) == 'Jenkinsfile':      
      view = self.view
      view.erase_phantoms('alerts')
      jenkinsfileRegion = sublime.Region(0, view.size())
      jenkinsfileString = view.substr(jenkinsfileRegion)
      logger.debug(jenkinsfileString)
      process = Popen(['plink', '-v', '-load', settings.get('pageant_session'), 'declarative-linter'], stdout=PIPE, stdin=PIPE, stderr=PIPE, startupinfo=startupinfo)
      process_output = process.communicate(input=bytes(jenkinsfileString, 'UTF-8'))
      stdout_data = (process_output[0]).decode('UTF-8')
      stderr_data = (process_output[1]).decode('UTF-8')
      
      if stderr_data:
        logger.debug('ERROR ' + stderr_data)
      logger.debug(stdout_data)

      errors = None
      output = stdout_data.splitlines()
      if output[0].lower().find('jenkinsfile successfully validated') != -1:
        sublime.set_timeout_async(lambda: status_message(output[0]), 1000)
        logger.debug(output[0])
        return
      else:
        errors = output

      phantom = None
      for e in errors:
        matches = re.finditer('line (([0-9]{1,}),)', e)
        for matchNum, match in enumerate(matches, start=1):
          #print('MATCH FOUND ' + match.group(2))
          region = view.line(view.text_point(int(match.group(2))-1, 0))
          view.add_phantom(region=region, content='''
            <html>
              <body id="jenkinsfile">
                  <style>
                    .dot {
                      height: 8px;
                      width: 8px;
                      background-color: red;
                      border-radius: 50%;
                      display: block;
                    }
                  </style>
                  <div class="error">
                    <code>''' +
                    stdout_data + '''</code>
                  </div>
              </body>
            </html>''',
          layout=sublime.LAYOUT_BELOW,
          key='alerts')
          sublime_plugin.on_hover(view.id(), 0, sublime.HOVER_GUTTER)
      
class EventListener(sublime_plugin.EventListener):
  def on_post_save(self, view):
    view.run_command('jenkinsfile')
