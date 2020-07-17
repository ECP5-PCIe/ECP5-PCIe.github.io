---
layout: post
title:  "Weekly Jul-3"
date:   2020-07-01 23:40:15 +0200
categories: GSoC
---
- ROCKPro64 was set up
	- debian and uboot for testing
	- allows for PCIe reinitialization by running 'pci enum' in uboot
- Further testing on the SERDES was performed, the RX seemingly doesn't get what the TX sends
	- Whether the signal arrives can be seen by whether the CDR locks, since the phase relationship stays constant between the TX and RX domains when that happens
		- At 125 MHz for x2 and 250 MHz for x1 gearing at 2.5 Gbit/s, if PCIe is unconnected it is 90 / 180 MHz, since the refclk runs at a lower frequency
		

[comments][comments]

[git]: https://github.com/ECP5-PCIe/ECP5-PCIe
[Comments]: https://github.com/ECP5-PCIe/ECP5-PCIe.github.io/issues/25