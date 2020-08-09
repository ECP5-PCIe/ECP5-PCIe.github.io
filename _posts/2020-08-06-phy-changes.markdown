---
layout: post
title:  "Some fixes for the PHY"
date:   2020-08-06 23:40:15 +0200
categories: GSoC
---
- Added back timing constraints, otherwise it does not work.
- Fixed RX inversion detection
    - It didn't work at all before
    - Now it inverts the RX and waits a few hundred cycles, since it takes a while to take effect
- Added TX CDC variants for testing
    - FFSynchronizer
    - AsyncFIFOBuffered
    - combinatorial connection
        - Seems to work best? At least in loopback.

[comments][comments]

[git]: https://github.com/ECP5-PCIe/ECP5-PCIe
[Comments]: https://github.com/ECP5-PCIe/ECP5-PCIe.github.io/issues/33