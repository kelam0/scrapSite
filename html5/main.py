# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 20:20:10 2017

@author: Malek
"""

import htmlPy
from back_end import BackEnd

app = htmlPy.AppGUI(
    title=u"Sample application")
app.maximized = True
app.template_path = "."
app.bind(BackEnd(app))

app.template = ("index.html", {})

if __name__ == "__main__":
    app.start()