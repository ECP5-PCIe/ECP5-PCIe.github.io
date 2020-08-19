---
layout: post
title:  "LTSSM working to L0, scrambling implemented"
date:   2020-08-19 23:40:15 +0200
categories: GSoC
---
- LTSSM works to L0
    - Further L states not yet implemented
    - Apparently idle symbol means scrambled D0.0 and not the IDL symbol...
        - This was confirmed by disabling scrambling with TS, after which scrambling was implemented.
- Scrambling works
    - Kind of hacky due to processing 2 symbols per clock cycle


[comments][comments]
[commit](https://github.com/ECP5-PCIe/ECP5-PCIe/commit/629611990eb5ade1a902dbfaccf942e0da8ccf46)

[git]: https://github.com/ECP5-PCIe/ECP5-PCIe
[Comments]: https://github.com/ECP5-PCIe/ECP5-PCIe.github.io/issues/TODO