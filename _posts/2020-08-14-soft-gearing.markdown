---
layout: post
title:  "Serdes gearing broken; Soft gearing as a fix"
date:   2020-08-14 23:40:15 +0200
categories: GSoC
---
- The gearing in the SERDES broken down in mysterious ways
    - It received a TS with half the symbols missing
        - They reappeared somewhere further below
- Gearing in Gateware was written
    - No more reliance on the SERDES primitive
        - I guess it is called "primitive" for a reason
    - Works properly
    - Meets timing requirements
    - Could possibly be expanded to x4 gearing for 5 Gbit/s data transfers
    - Now the LTSSM consistently gets to Configuration.Linkwidth.Start
        - Before that it sometimes got to Configuration.Idle, sometimes stuck somewhere inbetween and sometimes stuck somewhere at the beginning, which changed with every upload

[comments][comments]
[commit](https://github.com/ECP5-PCIe/ECP5-PCIe/commit/9fd7e9214ee0ef0f25d968e3017f3b75d2884421)

[git]: https://github.com/ECP5-PCIe/ECP5-PCIe
[Comments]: https://github.com/ECP5-PCIe/ECP5-PCIe.github.io/issues/35