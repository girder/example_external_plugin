#!/usr/bin/env python
# -*- coding: utf-8 -*-

###############################################################################
#  Copyright Kitware Inc.
#
#  Licensed under the Apache License, Version 2.0 ( the "License" );
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
###############################################################################

import os

from girder.constants import SettingKey, PACKAGE_DIR, STATIC_ROOT_DIR
from girder.utility.model_importer import ModelImporter
from girder.utility.webroot import WebrootBase

from .hello_rest import Hello


class Webroot(WebrootBase):
    """
    The webroot endpoint simply serves the main index HTML file.
    """
    def __init__(self, templatePath=None):
        plugin_name = __name__.split('.')[-1]
        if not templatePath:
            templatePath = os.path.join(PACKAGE_DIR, os.pardir, 'plugins',
                                        plugin_name, 'server', 'webroot.mako')
        super(Webroot, self).__init__(templatePath)

        self.vars = {
            'apiRoot': '/api/v1',
            'staticRoot': '/static',
            'title': 'Hello World',
            'main_plugin': plugin_name
            }

    def _renderHTML(self):
        self.vars['pluginCss'] = []
        self.vars['pluginJs'] = []
        builtDir = os.path.join(
            STATIC_ROOT_DIR, 'clients', 'web', 'static', 'built', 'plugins')
        self.vars['plugins'] = ModelImporter.model('setting').get(
            SettingKey.PLUGINS_ENABLED, ())
        for plugin in self.vars['plugins']:
            if os.path.exists(os.path.join(builtDir, plugin, 'plugin.min.css')):
                self.vars['pluginCss'].append(plugin)
            if os.path.exists(os.path.join(builtDir, plugin, 'plugin.min.js')):
                self.vars['pluginJs'].append(plugin)

        return super(Webroot, self)._renderHTML()


def load(info):
    # set the title of the HTML pages
    info['serverRoot'].updateHtmlVars({'title': 'Hello World'})

    # Move girder app to /girder, serve isic_archive app from /
    info['serverRoot'], info['serverRoot'].girder = (
        Webroot(), info['serverRoot'])

    info['serverRoot'].api = info['serverRoot'].girder.api

    # Bind our hello REST resource
    info['apiRoot'].hello = Hello()
