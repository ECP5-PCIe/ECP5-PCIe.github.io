---
layout: post
title:  "TX and RX+TX test cases working"
date:   2020-06-24 23:40:15 +0200
categories: GSoC
---
- A TX test case has been written to verify that it works as intended
- A RX + TX test case has been written to verify that the RX outputs the same TS as has been sent by the TX.
- Comments were added to the ltssm test program
- The LTSSM timer is now for all states, this saves on gateware

[comments][comments]
[commit](https://github.com/ECP5-PCIe/ECP5-PCIe/commit/0d0a01998604d0b1381e8946a47b8717b6949c6c)

[git]: https://github.com/ECP5-PCIe/ECP5-PCIe
[Comments]: https://github.com/ECP5-PCIe/ECP5-PCIe.github.io/issues/18