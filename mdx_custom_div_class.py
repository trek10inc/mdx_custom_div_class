"""
Markdown Custom class extension for Python-Markdown
=========================================

Markdown extension that allows defining div element
with custom class for a given text. Usage:

    >>> import markdown
    >>> md = markdown.Markdown(extensions=['custom_div_class'])

    >>> md.convert(```!!!alert
                    spam
                    !!!```)
    u'<div class="alert">spam</div>'

copyright @2014 Konrad Wasowicz <exaroth@gmail.com> (Modified by Jared Short 2015)

"""


from __future__ import absolute_import
from __future__ import unicode_literals
import markdown
from markdown import Extension
from markdown.preprocessors import Preprocessor
from markdown.inlinepatterns import Pattern
import re


CUSTOM_CLS_RE = r'[!]{3}(?P<class>[A-Za-z\t\-0-9 .]+)(?P<text>.+)[!]{3}'


class CustomDivClassExtension(Extension):
    """ Extension class for markdown """

    def extendMarkdown(self, md, md_globals):
        md.inlinePatterns["custom_div_class"] = CustomDivClassPattern(CUSTOM_CLS_RE, md)

class CustomDivClassPattern(Pattern):
    def handleMatch(self, matched):

        """
        If string matched
        regexp expression create
        new div elem with given class
        """

        cls = matched.group("class").lower()
        text = matched.group("text")

        elem = markdown.util.etree.Element("div")
        elem.set("class", cls)
        elem.text = text
        return elem

def makeExtension(*args, **kwargs):
    return CustomDivClassExtension(*args, **kwargs)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
