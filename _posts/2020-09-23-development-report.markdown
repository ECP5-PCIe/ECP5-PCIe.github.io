---
layout: post
title:  "Development Report"
date:   2020-09-23 23:40:15 +0200
categories: GSoC
---

This project is about implementing PCIe on the ECP5 FPGA.
For now the focus is on PCIe Gen1 x1.

The PCIe protocol is composed of three layers.
First comes the physical layer, composed of the SERDES (the electrical sub-block) and the LTSSM (the logical sub-block)
Communication happens over a link which is composed of a number of lanes.
Each lane has a transmit and a receive differential pair and a SERDES responsible for encoding data with 8b10b.
Then comes the LTSSM, which is responsible for configuring a link and lanes within it and recovering from faults.
The most basic functions of the LTSSM, required to reach the operational state called L0, were implemented.
That works reliably on a ECP5-5G Versa board connected to a ROCKPro64 SBC.
Getting to that point had a number of obstacles concerning the SERDES and clock domain crossing.
For example SERDES gearing worked fine until sometime it didn't anymore and it started shuffling the data around (despite the same gateware running).
Gearing is done in gateware for now, though that limits the maximum speed.
Now the physical layer works reliably, though maybe the data path should be changed to 4 symbols width to allow for PCIe Gen2.

After that comes the Data Link Layer, which is responsible for transmitting and receiving Transaction Layer packets (which originate from the topmost layer, the Transaction Layer).
It checks them for integrity with a CRC, retransmits them in case of errors and manages credits.
Credits exist to ensure that the receiver has enough space for TLPs, such that TLPs don't get lost due to the buffer being full.
Work on it was started on the last week of August.
For managing credits and reporting TLP errors it uses Data Link Layer Packets.
A DLLP transmitter and receiver were made, which can send and receive DLLP packets.
TLPs were not implemented yet.

[git]: https://github.com/ECP5-PCIe/ECP5-PCIe
