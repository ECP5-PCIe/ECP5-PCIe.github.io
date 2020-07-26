---
layout: post
title:  "ROCKPro64 automatic PCIe init"
date:   2020-07-25 23:40:15 +0200
categories: GSoC
---
- Gateware was written to reliably send 'pci init' to the ROCKPro64
    - This is useful for starting with the same beginning state and it doesn't require a restart of the ROCKPro64 to reinitialize PCIe
    - It can also be used to start recording a trace up from some point
    - Booting problems were solved by turning on the ROCKPro64 before uploading any gateware and modifying the uboot such that it goes directly to uboot.

[comments][comments]
[commit](https://github.com/ECP5-PCIe/ECP5-PCIe/commit/ee819177252857058d35409abb9bf9455f60017b)

[git]: https://github.com/ECP5-PCIe/ECP5-PCIe
[Comments]: https://github.com/ECP5-PCIe/ECP5-PCIe.github.io/issues/28