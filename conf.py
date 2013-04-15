# -*- coding: utf-8 -*-
import sys, os

source_suffix = '.rst'
master_doc = 'index'
project = u'Pythonな会社でchefしてる例の紹介'
copyright = u'2013, Takayuki SHIMIZUKAWA'
version = release = '1.0'
exclude_patterns = ['_build']
templates_path = ['_templates']
pygments_style = 'sphinx'
extensions = ['sphinxjp.themecore']
html_logo = 'sphinx-logo.png'
html_static_path = ['_static']
html_use_index = False

html_theme = 's6'
language = 'ja'


def setup(app):
    app.add_stylesheet('custom.css')

