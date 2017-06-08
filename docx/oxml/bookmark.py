# encoding: utf-8

"""
Custom element classes related to paragraphs (CT_P).
"""

from . import OxmlElement
from .simpletypes import ST_DecimalNumber, ST_String
from .xmlchemy import BaseOxmlElement, RequiredAttribute, OptionalAttribute, ZeroOrMore


class CT_Markup(BaseOxmlElement):
    """
    It may represent several elements, such as ``<w:bookmarkEnd>``,
    It is extendable.
    """

    id = RequiredAttribute('w:id', ST_DecimalNumber)


class CT_BookmarkRange(CT_Markup):

    colFirst = OptionalAttribute('w:colFirst', ST_DecimalNumber)
    colLast = OptionalAttribute('w:colLast', ST_DecimalNumber)


class CT_BookmarkStart(CT_BookmarkRange):
    """
    ``<w:bookmarkStart>`` element, setting the start of the bookmark
    """

    r = ZeroOrMore('w:r')
    name = RequiredAttribute('w:name', ST_String)
