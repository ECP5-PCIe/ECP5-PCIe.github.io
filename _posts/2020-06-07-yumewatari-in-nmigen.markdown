---
layout: post
title:  "Yumewatari commit f61133d working in nMigen!"
date:   2020-06-07 23:40:15 +0200
comment_issue_id: 1
categories: GSoC
---
- The working serdes class from Yumewatari was translated to nMigen
- It was found that the x16 slot works if the PRSNT signal is connected to ground, since apparently the mainboard is lacking ground at the PRSNT x1 pin (pin B17 on the PCIe connector).
	- That was required for the ispCLOCK IC to work properly.
- The x16 slot responds differently than the x1 slot and the returned data responds to different data being sent.
	- SKP ordered sets (COM, SKP, SKP, SKP) have been observed

[comments][comments]

[git]: https://github.com/ECP5-PCIe/ECP5-PCIe
[Comments]: https://github.com/ECP5-PCIe/ECP5-PCIe.github.io/issues/8