---
layout: post
title:  "More comments and LTSSM bugfixes and more debug options

"
date:   2020-06-26 23:40:15 +0200
categories: GSoC
---
- Further commenting was done to improve code readability
- A few bugs were found in the LTSSM polling states
	- Further comparison with PCIe specification pending in the next few days
- LTSSM state machine debugging was fancified
	- Real time from the 100 MHz oscillator was added, to see if the RX clock domain gitches
	- Link and Lane numbers from the PHY were added
- Another debugging option for recording symbols received in a specific state was added

[comments][comments]
[commit](https://github.com/ECP5-PCIe/ECP5-PCIe/commit/83a33310bb7e068ae1e35e9fb0b6a6068d5684b0)

[git]: https://github.com/ECP5-PCIe/ECP5-PCIe
[Comments]: https://github.com/ECP5-PCIe/ECP5-PCIe.github.io/issues/19