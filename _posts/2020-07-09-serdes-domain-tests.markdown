---
layout: post
title:  "Serdes and Domain Crossing tests"
date:   2020-07-09 23:40:15 +0200
categories: GSoC
---
- Testing pertaining to domain crossing
    - A loopback only works at some phase relations between RX and TX clock
        - Likely due to FFSynchronizer issues
    - LTSSM got to L0 by itself when the PC was off
        - Likely due to parasitic coupling of TX and RX
    - Skipping SERDES clock cycles to change the phase between RX and TX clock has been added

[comments][comments]
[commit](https://github.com/ECP5-PCIe/ECP5-PCIe/commit/f0001f07c48741254834a279448cb41841e9653e)

[git]: https://github.com/ECP5-PCIe/ECP5-PCIe
[Comments]: https://github.com/ECP5-PCIe/ECP5-PCIe.github.io/issues/22