import os
from pygments.formatters import HtmlFormatter

htmlFormatter = HtmlFormatter().get_style_defs('.codehilite')

file_css = open(os.path.join(".","jvcms","static","css","pygments.css"), 'a')
file_css.write(htmlFormatter)
file_css.write("\n")
file_css.close()