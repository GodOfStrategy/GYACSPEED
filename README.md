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
Here is my BoM (which you can find in the root of my repository aswell):[bom.csv](https://github.com/user-attachments/files/29404539/bom.csv) [bom.txt](https://github.com/user-attachments/files/29404666/bom.txt)

