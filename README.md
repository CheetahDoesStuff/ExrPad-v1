# ExrPad v1
The ExrPad v1 is a pretty small and neat macropad!

## Some words
Before i start, i just wanna thank @shadow and @rekirxs (both in the hackclub slack) for all the help through the process from the schematic to the case, couldnt have done it without you guys !

TODO: write smth here (i really wanna write this now but its 12 am and i need my 3 hours of netflix before i go to sleep)
## Details
### Specifications
The features include:
* A powerful microcontroller as the main piece in the device (Seed Studio XIAO rp2040)
* 6 Cherry MX switches that are fully programmable
* A rotary encoder and switch (pressable rotary encoder)
* A 128x32 OLED display

The entire thing is inside a neat package consiting a 3D printed case (top and bottom part)

## Repository
Folder structure:
```sh
ExrPad-v1 # Root
  /PCB # Folder containing all files for the PCB design
    ExrPad.kicad_pro # The main project file of the kiCAD project
    ExrPad.kicad_sch # KiCAD schematic
    ExrPad.kicad_pcb # KiCAD PCB Design
  /CAD # All files for the 3D design of the device
    ExrPad_v1_top_rev2.step # Top part of the case
    ExrPad_v1_bottom.step # Bottom part of the case
    ExrPad_v1_assembled.step # Full case with pcb and components, used for images
  /Firmware # All files related to the firmware/software side of the project
    TODO: This as well
```

## Images!
| Schematic       | PCB             | Case parts      | Full design (PCB and case) |
|-----------------|-----------------|-----------------|----------------------------|
| ![Schematic](https://github.com/CheetahDoesStuff/ExrPad-v1/blob/main/img/swappy-20260102_194253.png) | ![PCB](https://github.com/CheetahDoesStuff/ExrPad-v1/blob/main/img/swappy-20260102_194306.png) | ![Case](https://github.com/CheetahDoesStuff/ExrPad-v1/blob/main/img/swappy-20260102_194911.png) | ![Full](https://github.com/CheetahDoesStuff/ExrPad-v1/blob/main/img/swappy-20260102_194229.png) |


## BOM
- Seeed XIAO RP2040 — x1
- MX-style mechanical switches — x6
- EC11 rotary encoder (with switch) — x1
- Blank DSA keycaps — x6
- 0.91 inch OLED display — x1
- M3 x 16 mm screws & M3 heat-set inserts — x4
