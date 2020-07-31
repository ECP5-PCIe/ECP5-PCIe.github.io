---
layout: post
title:  "Some changes to the SERDES and a new SKP sequence transmitter"
date:   2020-07-31 23:40:15 +0200
categories: GSoC
---
- It was found out that sometimes TS sets were broken
    - The TX clock on the SERDES was changed to be taken from the TX instead of the RX side which fixed that issue
- SKP ordered sets were added to the transmitter

[comments][comments]

[git]: https://github.com/ECP5-PCIe/ECP5-PCIe
[Comments]: https://github.com/ECP5-PCIe/ECP5-PCIe.github.io/issues/31