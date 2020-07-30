---
layout: post
title:  "SERDES testing finished"
date:   2020-07-30 23:40:15 +0200
categories: GSoC
---
- Testing was done on the SERDES, it was concluded that it mostly works fine
    - Word alignment needs to be enabled, otherwise it does not work properly
    - TX ampitude was measured with an oscilloscope and it was found that it is sufficient
- CDC was moved away from the ECP5 SERDES class itself since it is only responsible for SERDES functionality.

[comments][comments]

[git]: https://github.com/ECP5-PCIe/ECP5-PCIe
[Comments]: https://github.com/ECP5-PCIe/ECP5-PCIe.github.io/issues/30