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

A SERDES class able to utilize one of the four SERDES in the ECP5 was implemented, allowing to select a channel / DCU and gearing (though there currently are problems with x2 gearing).

Link configuration happens with Training Sequences, of which there are two, TS1 and TS2.
For the physical layer, a transmitter and receiver was implemented which are mostly responsible for training sequences.
Currently they work on a 2 symbol per cycle basis, though in the future that may be changed to be adjustable or fixed to 4 symbols per cycle.

Then comes the LTSSM, which is responsible for configuring a link and lanes within it and recovering from faults.
The most basic functions of the LTSSM, required to reach the operational state called L0, were implemented.
A scrambling pattern generator was implemented, to encode and decode scrambled symbols.
Data on a link is scrambled to reduce EMI, since it essentially broadens the peaks of the spectrum.

It gets reliably to the L0 state and stays there indefinitely on a ECP5-5G Versa board connected to a ROCKPro64 SBC.
It can be observed that the ROCKPro64 sends out Data Link Layer credit packets for all three credit types.

Getting to that point had a number of obstacles concerning the SERDES and clock domain crossing.
For example SERDES gearing worked fine until sometime it didn't anymore and it started shuffling the data around (despite the same gateware running).
There was also an issue with the SERDES only working sometimes after uploading gateware.
Gearing is done in gateware for now, though that limits the maximum speed, since 5 GT/s would require the gearing to run at 500 MHz.
Now the physical layer works reliably, though maybe the data path should be changed to 4 symbols width to allow for PCIe Gen2.

After that comes the Data Link Layer, which is responsible for transmitting and receiving Transaction Layer packets (which originate from the topmost layer, the Transaction Layer).
It checks them for integrity with a CRC, retransmits them in case of errors and manages credits.

Credits are a unit of data measurement, separately managed for three different packet types (and their headers, for a total of 6 credit types).
They exist to ensure that the receiver has enough space for TLPs, such that TLPs don't flood the link due to the receive buffer being full, which would cause them to be resent.
For managing credits and reporting TLP errors it uses Data Link Layer Packets.

Work on it was started on the last week of August.
A DLLP transmitter and receiver were made, which can send and receive DLLP packets.
The CRC for it is generated with a universally configurable CRC generator which will also be used for the CRC of the Transaction Layer Packets (it can be configured to process any number of bits for a CRC with any number of bits).
Currently the Data Link Layer state machine is being worked on.

[git]: https://github.com/ECP5-PCIe/ECP5-PCIe
