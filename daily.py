import sys

dat = """---
layout: post
title:  "%TITLE"
date:   """ + sys.argv[1] + """ 23:40:15 +0200
categories: GSoC
---
- TODO

[comments][comments]

[git]: https://github.com/ECP5-PCIe/ECP5-PCIe
[Comments]: https://github.com/ECP5-PCIe/ECP5-PCIe.github.io/issues/TODO"""

with open("_posts/" + sys.argv[1] + "-" + sys.argv[2] + ".markdown", 'w') as file:
    file.write(dat.replace("%TITLE", sys.argv[3]))