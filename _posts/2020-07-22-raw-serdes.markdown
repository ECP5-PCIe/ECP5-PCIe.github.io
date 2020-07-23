---
layout: post
title:  "Testing the serdes - Undecoded"
date:   2020-07-22 23:40:15 +0200
categories: GSoC
---
- Gateware was written for testing the SERDES without en/decoding and it was found that on a second Versa it behaved as expected. On my Versa sometimes the decoding broke.
    - Phase between TX and RX is constant but random with every startup, sometimes it is fine, sometimes there are errors on my Versa.

[comments][comments]

[git]: https://github.com/ECP5-PCIe/ECP5-PCIe
[Comments]: https://github.com/ECP5-PCIe/ECP5-PCIe.github.io/issues/27