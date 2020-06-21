---
layout: post
title:  "LTSSM now fully in RX clock domain"
date:   2020-06-21 23:40:15 +0200
categories: GSoC
---
- The LTSSM timer was fixed
	- Now the time is reset when leaving the state
- Clock Domain Crossing from RX to TX domain in the PHY class
	- Since the frequency between them is the same in normal operation, but the phase is not, it was required
	- LTSSM now hangs at Polling.Configuration.TS or Recovery.RcvrLock instead of Polling.Active.TS

[commit](https://github.com/ECP5-PCIe/ECP5-PCIe/commit/ddf48dd68e3fcb8a4dcff36ad7701b9a421a037a)

[comments][comments]

[git]: https://github.com/ECP5-PCIe/ECP5-PCIe
[Comments]: https://github.com/ECP5-PCIe/ECP5-PCIe.github.io/issues/16