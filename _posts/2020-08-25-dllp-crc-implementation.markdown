---
layout: post
title:  "DLLP receiver and CRC implemented"
date:   2020-08-25 23:40:15 +0200
categories: GSoC
---
- A DLLP receiver was implemented, which takes DLLP data from a descrambled lane, parses it, validates the CRC and stores it in a FIFO.
- A generic CRC was implemented, which does bitwise CRC in the combinatorial domain and thus can process an arbitrary amount of bits in a single clock cycle.

[comments][comments]
[commit](https://github.com/ECP5-PCIe/ECP5-PCIe/commit/2665dbaf16db6922f1685f93fdf446fb7ab063b9)

[git]: https://github.com/ECP5-PCIe/ECP5-PCIe
[Comments]: https://github.com/ECP5-PCIe/ECP5-PCIe.github.io/issues/37