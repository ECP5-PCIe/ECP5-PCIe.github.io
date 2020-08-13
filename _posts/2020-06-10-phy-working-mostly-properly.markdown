---
layout: post
title:  "Fixed PHY cdc, now working fine a significant portion of the time"
date:   2020-06-10 23:40:15 +0200
categories: GSoC
---
- Changed gearing FIFO drive clock to FF_EBRD_CLK
    - which is being driven by tx_clk_i
- CDC changed to AsyncFIFOBuffered
    - Increased depth to 10
- PHY works often and gets repeatedly to Configuration.Idle
    - Doesn't receive IDLE symbols and jumps back to detect
    - ROCKPro64 seems to send DLLPs when in that state
    - Sometimes it gets stuck and doesn't progress far, re-upload fixes that
        - Maybe reset ECP5 when that happens?
            - Would be a hack

[comments][comments]
[commit][https://github.com/ECP5-PCIe/ECP5-PCIe/commit/f499fec3af2645410d2d423f39c31d5500bdad35]

[git]: https://github.com/ECP5-PCIe/ECP5-PCIe
[Comments]: https://github.com/ECP5-PCIe/ECP5-PCIe.github.io/issues/TODO