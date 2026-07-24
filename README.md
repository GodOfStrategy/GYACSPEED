# GYACSPEED
Speedometer, accelerometer and a gyroscope for my bicycle, with the XIAO RP2040 as the MCU, with a 1.3" OLED display for the information.
I saw the Hermes starter project and though, "Why only stop at a gyroscope?" and then answered my own question by adding a speedometer powered by the Ublox NEO-M9N GNSS module, and a gyroscope and an accelerometer powered by the LSM6DSLTR!! So that I can see my speed, acceleration, and how I take turn using the gryoscope and such, with the XIAO RP2040 serving as my MCU.
So, I drew the Schematics:<img width="1391" height="751" alt="{8956B950-8E5F-49AF-B97F-7C96270D963C}" src="https://github.com/user-attachments/assets/7e88a04e-40c4-4668-8409-4212c6a5d7c5" />
Then I routed the PCB:<img width="673" height="504" alt="{BFD462F4-F5AD-4BB6-BA28-4471AD29F06E}" src="https://github.com/user-attachments/assets/d28e0b98-8791-46cc-9660-d0f1f2e81bbd" />
How my assembled PCB is supposed to look like:<img width="897" height="557" alt="{270DA254-DB51-4898-A8E7-48D921C7D5DD}" src="https://github.com/user-attachments/assets/1ecd5e6c-22e6-45b9-b9fe-0c509a08746a" />

Then I designed a case in Fusion 360 for my project, and found solutions so as to how will I mount it on my bicycle and then came up with this monstrosity:<img width="1375" height="670" alt="Screenshot 2026-06-25 144437" src="https://github.com/user-attachments/assets/9607199a-67d4-4d0d-a152-9fe11bc8bcbb" />
<img width="669" height="593" alt="Screenshot 2026-06-25 144455" src="https://github.com/user-attachments/assets/96535f8e-32a2-409a-b336-e39b6fc55e91" />
<img width="544" height="655" alt="Screenshot 2026-06-26 144135" src="https://github.com/user-attachments/assets/531ab09e-ec2e-4cc9-9e48-e4345823149a" />
<img width="635" height="529" alt="Screenshot 2026-06-26 144124" src="https://github.com/user-attachments/assets/9c8ce95d-c4bc-4c91-83f6-3ee8b4c3b20f" />
Here is my BoM (which you can find in the root of my repository aswell):
﻿| Designator | Footprint | Quantity | Value | LCSC Part # | Price (US $) | Links | Distributor | Generic Name |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | 805 | 5 | 100uF |  | 3.54 | GRM21BR60E107ME15K Murata Electronics \\ | Mouser India | Mouser India | Capacitors |
| C10, C3, C4, C5 | 402 | 10 | 10uF |  | 0.46 | Link [(mouser.in in Bing)](https://www.bing.com/search?q="https%3A%2F%2Fwww.mouser.in%2FProductDetail%2FTAIYO-YUDEN%2FMSASJ105CB5106MFNC12%3Fqs%3DPBDs2xEllI8xKzMj03Wyvw%253D%253D") | Mouser India |  |
| C11, C12, C7, C8, C9 | 402 | 5 | 0.1uF |  | 0.24 | Link [(mouser.in in Bing)](https://www.bing.com/search?q="https%3A%2F%2Fwww.mouser.in%2FProductDetail%2F80-C0402C104K4P") | Mouser India |  |
| C2 | 402 | 1 | 1pF |  | 0.25 | 04023A1R0DAT2A KYOCERA AVX \\ | Mouser India |  |  |
| C6 | 402 | 10 | 1uF |  | 0.17 | Link [(mouser.in in Bing)](https://www.bing.com/search?q="https%3A%2F%2Fwww.mouser.in%2FProductDetail%2FKYOCERA-AVX%2F0402X5R105KTAAT%3Fqs%3DXAiT9M5g4x9uZyL2wCxs9w%253D%253D") | Mouser India |  |
| D1 | D_SMA | 3 | SS14 |  | 1.3 | Link [(mouser.in in Bing)](https://www.bing.com/search?q="https%3A%2F%2Fwww.mouser.in%2FProductDetail%2Fonsemi%2FSS14%3Fqs%3DmVVXn4M53U%25252BvrBaFv5vr4w%253D%253D") | Mouser India | Reverse Polarity Protection diode |
| DS1 | LCD_OLED_128X64_1.3_I2C | 2 | OLED_128X64_1.3_I2C |  | 5.66 | Link [(amazon.in in Bing)](https://www.bing.com/search?q="https%3A%2F%2Fwww.amazon.in%2FTishvi-Interface-Contrast-Microcontroller-Projects%2Fdp%2FB0GZQBH8TX") | Amazon India | OLED |
| E1 | XCVR_ANT-GNCP-TH25AL12 | 2 | ANT-GNCP-TH25AL12 |  | 22.2 | Link [(mouser.in in Bing)](https://www.bing.com/search?q="https%3A%2F%2Fwww.mouser.in%2FProductDetail%2FTE-Connectivity%2FANT-GNCP-TH25AL12%3Fqs%3DA6eO%25252BMLsxmRfsTs3t3ApUw%253D%253D") | Mouser India | Passive antenna |
| J1, J2 | PinHeader_1x05_P2.54mm_Vertical | 0 | Conn_01x05_Pin |  | 0 |  | Self-Sourced |  |
| J3 | PinHeader_1x02_P2.54mm_Vertical |  | Conn_01x02_Socket |  |  |  |  |  |
| L1 | 603 | 1 | 1 uH |  | 0.52 | Link [(mouser.in in Bing)](https://www.bing.com/search?q="https%3A%2F%2Fwww.mouser.in%2FProductDetail%2FABRACON%2FAIML-0603-1R0K-T%3Fqs%3D1vO2EIVe%25252BY7DV5QHOd2BCw%253D%253D") | Mouser India | Inductor |
| Q1, Q2 | SOT-23-3_L3.0-W1.7-P0.95-LS2.9-BR | 4 | SI2301CDS-T1-GE3 | C10487 | 3.47 | SI2301CDS-T1-BE3 Vishay / Siliconix \\ | Mouser India | Mouser India | MOSFETs |
| R1 | 402 | 1 | 453K |  | 0.088 | RC0402FR-07453KL YAGEO \\ | Mouser India | Mouser India | Resistors |
| R2 | 402 | 1 | 100K |  | 0.37 | Link [(mouser.in in Bing)](https://www.bing.com/search?q="https%3A%2F%2Fwww.mouser.in%2FProductDetail%2FYAGEO%2FAC0805JR-7W100KL%3Fqs%3Dr5DSvlrkXmI4dHdBm%252FLHKQ%253D%253D") | Mouser India |  |
| R3 | 402 | 1 | 2.2K |  | 0.078 | RC0402JR-7D2K2L YAGEO \\ | Mouser India | Mouser India |  |
| R4 | 402 | 1 | 330 |  | 0.078 | CR0402-JW-331GLF Bourns \\ | Mouser India | Mouser India |  |
| U1 | XIAO-RP2040-DIP | 2 | XIAO-RP2040-DIP |  | 10.57 | Link [(mouser.in in Bing)](https://www.bing.com/search?q="https%3A%2F%2Fwww.mouser.in%2FProductDetail%2FSeeed-Studio%2F102010428%3Fqs%3DZnm5pLBrcAJ75FCbdxzDHQ%253D%253D") | Mouser India | MCU |
| U2 | XCVR_NEO-M9N-00B | 2 | NEO-M9N-00B |  | 23.69 | Link [(mouser.in in Bing)](https://www.bing.com/search?q="https%3A%2F%2Fwww.mouser.in%2FProductDetail%2Fu-blox%2FNEO-M9N-00B%3Fqs%3DDPoM0jnrROVeJ6BHpcwcjw%253D%253D") | Mouser India | GNSS Module |
| U3 | LGA-14_3x2.5mm_P0.5mm_LayoutBorder3x4y | 2 | LSM6DS3 |  | 13.42 | Link [(mouser.in in Bing)](https://www.bing.com/search?q="https%3A%2F%2Fwww.mouser.in%2FProductDetail%2FSTMicroelectronics%2FLSM6DSV32XTR%3Fqs%3DHoCaDK9Nz5d%25252BGVBpjxkjlg%253D%253D") | Mouser India | 3D Gyroscope + Accelerometer |
| U4 | VQFN-7_L2.0-W2.0-P0.55-TL_RWU | 2 | TPS61022RWUR | C915088 | 6.31 | TPS61022RWUR Texas Instruments \\ | Mouser India | Mouser India | Switching Buck Regulator |
| U5 | WSON-6_L1.5-W1.5-P0.50-TL | 2 | BQ29703DSER | C2876295 | 1.12 | BQ29703DSER Texas Instruments \\ | Mouser India | Mouser India | Battery overdischarge protection |
| — | — | 1 | Hot air gun |  | 37.02 | Link [(amazon.in in Bing)](https://www.bing.com/search?q="https%3A%2F%2Fwww.amazon.in%2FSoldering-600W-Adjustable-Temperature-Electronics%2Fdp%2FB0DT693N47") | Amazon India | Hot air gun [2 in 1] |
| — | — | 1 | Soldering Paste |  | 6.34 | Link [(amazon.in in Bing)](https://www.bing.com/search?q="https%3A%2F%2Fwww.amazon.in%2FSR-Syringe-Circuit-Assembly-Mechanic-Soldering%2Fdp%2FB0H511T6TD") | Amazon India | Soldering Paste |
| — | — | 1 | Flux Paste |  | 4.75 | Link [(amazon.in in Bing)](https://www.bing.com/search?q="https%3A%2F%2Fwww.amazon.in%2FDesoldering-Microprocessor-Smartphones-Motherboards-Electronic%2Fdp%2FB0C7N66JFQ") | Amazon India | Flux Paste |
| — | — | 10 | M3 bolts 15mm |  | 2.91 | Link [(amazon.in in Bing)](https://www.bing.com/search?q="https%3A%2F%2Fwww.amazon.in%2FRpi-shop-Phillips-Countersunk-Quantity%2Fdp%2FB08HNBTZ3D") | Amazon India | M3 bolts 15mm |
| — | — | 30 | M3 bolts 30mm |  | 3.7 | [ |[bom(final).csv](https://github.com/user-attachments/files/29474485/bom.final.csv)


