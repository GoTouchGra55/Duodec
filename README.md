# Duodec

A 12-key + 1 rotary encoder macropad built on
the RP2040-Zero, designed for developers and
students who live in their terminal.

![Duodec 3d model](Assets/3dModel.png)

---

## Overview

**Duodec** (Latin: _twelve_) is a compact, open-source macropad featuring 12 mechanical switches, a clickable rotary encoder, and an 128x32 OLED display. Built around the RP2040-Zero, it's fully programmable in Python.

![PCB traces of Duodec](Assets/Routes.png)

Designed as a productivity tool for VS Code, terminal workflows, and what not!

![Duodec PCB schematic](Assets/Schematic.png)

---

## Features

- 12x mechanical key switches in a 4×3 matrix
- 1x EC11 rotary encoder with push-button click
- 128×32 OLED display
- RP2040-Zero (RP2040 chip, USB-C)
- Fully programmable in Python
- Multiple layers for different workflows
- SMD diodes (SOD-123) for key matrix
- Custom 3D printed case
- Open source hardware and software

## Bill of Materials

 Component | Purpose | Unit Price | Qty | Total | Distributor |
|-----------|---------|-----------|-----|-------|-------------|
| [LEOBOG Graywood V4 Linear Switch (Pack of 10)](https://www.daraz.com.np//products/i170535424-s1189144506.html?spm=a2o42.cart.0.0.51756af7WGkkNn&urlFlag=true) | Key input | $3.39 | 2 | $6.78 | Daraz Nepal |
| [PCB and 3D Parts](https://jlcpcb.com) | PCB backbone + protective 3D printed parts | $17.59 | 1 | $17.59 | JLCPCB |
| [Solder Wire](https://www.daraz.com.np//products/i123779146-s1033610157.html?spm=a2o42.cart.0.0.62f26af7Sxc2ig&urlFlag=true) | Soldering components onto PCB | $1.22 | 1 | $1.22 | Daraz Nepal |
| [Soldering Iron](https://www.daraz.com.np/products/60w-combo-kit-soldering-iron-rod-iron-wire-flux-i130121110-s1038004751.html?c=&channelLpJumpArgs=&clickTrackInfo=query%253Asoldering%252Biron%253Bnid%253A130121110%253Bsrc%253ALazadaMainSrp%253Brn%253A62207e213f0fc10a5988c7c53425f72f%253Bregion%253Anp%253Bsku%253A130121110_NP%253Bprice%253A395%253Bclient%253Adesktop%253Bsupplier_id%253A900151539064%253Bsession_id%253A%253Bbiz_source%253Ahttps%253A%252F%252Fwww.daraz.com.np%252F%253Bslot%253A2%253Butlog_bucket_id%253A470687%253Basc_category_id%253A10000505%253Bitem_id%253A130121110%253Bsku_id%253A1038004751%253Bshop_id%253A28907%253BtemplateInfo%253A&freeshipping=0&fs_ab=1&fuse_fs=&lang=en&location=Bagmati%20Province&price=395&priceCompare=skuId%3A1038004751%3Bsource%3Alazada-search-voucher%3Bsn%3A62207e213f0fc10a5988c7c53425f72f%3BoriginPrice%3A39500%3BdisplayPrice%3A39500%3BsinglePromotionId%3A-1%3BsingleToolCode%3AmockedSalePrice%3BvoucherPricePlugin%3A0%3Btimestamp%3A1773164808027&ratingscore=4.3431372549019605&request_id=62207e213f0fc10a5988c7c53425f72f&review=102&sale=598&search=1&source=search&spm=a2a0e.searchlist.list.2&stock=1) | Soldering tool | $2.69 | 1 | $2.69 | Daraz Nepal |
| [SOD-123 SMD Switching Diode](https://www.daraz.com.np//products/i416542528-s1792465060.html?spm=a2o42.cart.0.0.d5e26af7ClJinq&urlFlag=true&tradePath=%2CcartPriceDrop%2Ccart) | Prevents ghosting in key matrix | $4.39 | 1 | $4.39 | Daraz Nepal |
| [Rotary Encoder (EC11)](https://www.daraz.com.np//products/i140566281-s1074190810.html?spm=a2o42.cart.0.0.43eb6af7Kj2eoO&urlFlag=true&tradePath=%2CcartPriceDrop%2Ccart) | Rotary and click input | $0.67 | 1 | $0.67 | Daraz Nepal |
| [128x32 OLED Display](https://www.daraz.com.np//products/i129083637-s1037084826.html?spm=a2o42.cart.0.0.6da46af71wwJuc&urlFlag=true&tradePath=%2CcartPriceDrop%2Ccart) | Displays layer and status info | $4.76 | 1 | $4.76 | Daraz Nepal |
| [RP2040-Zero](https://www.daraz.com.np/products/rp2040-zero-rp2040-for-raspberry-pi-microcontroller-i149575151-s1104086822.html?c=&channelLpJumpArgs=&clickTrackInfo=query%253Araspberry%252Bpi%253Bnid%253A149575151%253Bsrc%253ALazadaMainSrp%253Brn%253A78867d50594033c86c348e0653d82b42%253Bregion%253Anp%253Bsku%253A149575151_NP%253Bprice%253A700%253Bclient%253Adesktop%253Bsupplier_id%253A900153636107%253Bsession_id%253A%253Bbiz_source%253Ah5_external%253Bslot%253A39%253Butlog_bucket_id%253A470687%253Basc_category_id%253A10000489%253Bitem_id%253A149575151%253Bsku_id%253A1104086822%253Bshop_id%253A64405%253BtemplateInfo%253A&freeshipping=0&fs_ab=1&fuse_fs=&lang=en&location=Bagmati%20Province&price=7E%202&priceCompare=skuId%3A1104086822%3Bsource%3Alazada-search-voucher%3Bsn%3A78867d50594033c86c348e0653d82b42%3BoriginPrice%3A70000%3BdisplayPrice%3A70000%3BsinglePromotionId%3A-1%3BsingleToolCode%3A-1%3BvoucherPricePlugin%3A0%3Btimestamp%3A1773147507692&ratingscore=&request_id=78867d50594033c86c348e0653d82b42&review=&sale=0&search=1&source=search&spm=a2a0e.searchlist.list.39&stock=1) | Microcontroller | $4.76 | 1 | $4.76 | Daraz Nepal |
| **Total** | | | | **$56.03** | |
