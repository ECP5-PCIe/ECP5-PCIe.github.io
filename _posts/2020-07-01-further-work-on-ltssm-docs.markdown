---
layout: post
title:  "Further work on the LTSSM and further reading of documentations"
date:   2020-07-01 23:40:15 +0200
categories: GSoC
---
- Further reading on PCIe LTSSM was done
- Some bugs in the LTSSM, like the timer not resetting when the state changes for a different reason than a timeout, were fixed
- LTSSM seems to work fine to Configuration.Idle where no IDL symbols are received
	- Instead the computer seems to be sending data, which looks garbled?

[comments][comments]
[commit](https://github.com/ECP5-PCIe/ECP5-PCIe/commit/a07449e689317dea8440c57b11dce78f00a2aa47)

[git]: https://github.com/ECP5-PCIe/ECP5-PCIe
[Comments]: https://github.com/ECP5-PCIe/ECP5-PCIe.github.io/issues/20