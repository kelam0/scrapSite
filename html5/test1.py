# -*- coding: utf-8 -*-
"""
Created on Fri Nov 03 22:33:17 2017

@author: Malek
"""

import htmlPy
import os

app = htmlPy.AppGUI(title=u"htmlPy Quickstart", maximized=True)

app.template_path = os.path.abspath(".")
app.static_path = os.path.abspath(".")

app.template = ("index.html", {"username": "htmlPy_user"})

app.start()