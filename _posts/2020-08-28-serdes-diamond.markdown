---
layout: post
title:  "SERDES compiled with diamond and channel and DCU can now be configured via parameters."
date:   2020-08-28 23:40:15 +0200
categories: GSoC
---
- LTSSM test was compiled with diamond and x2 in-SERDES gearing
    - Did not make a difference for me, was still broken
    - Version compiled with trellis worked for another person
- SERDES class modified
    - DCU and channel now specificable in the constructor
        - Will make multilane development easier
        - Good for debugging, since there is a loopback cable on DCU0 CH1
            - No need to replace "CH0" with "CH1" in the SERDES class anymore for testing

[comments][comments]

[git]: https://github.com/ECP5-PCIe/ECP5-PCIe
[Comments]: https://github.com/ECP5-PCIe/ECP5-PCIe.github.io/issues/38