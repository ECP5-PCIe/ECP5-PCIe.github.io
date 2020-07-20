---
layout: post
title:  "ROCKPro64 UART control"
date:   2020-07-20 23:40:15 +0200
categories: GSoC
---
- Implementation of a UART controller for the ROCKPro64 has begun
    - A problem is that the TX might not be connected until it starts, otherwise it doesn't boot at all.
    - Solution: FPGA Tristate IO
    - This allows for data acquisition to be triggered after 'pci init' has been sent to uboot
    - ROCKPro64 doesn't need an UART adapter
    - Another problem could be that the ROCKPro64 boots before the gateware is uploaded and needs to be rebooted

[comments][comments]

[git]: https://github.com/ECP5-PCIe/ECP5-PCIe
[Comments]: https://github.com/ECP5-PCIe/ECP5-PCIe.github.io/issues/26