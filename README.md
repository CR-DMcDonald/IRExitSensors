# IRExitSensors

Welcome to the IRExitSensors repo, a hub where hardware hackers and red teamers collaborate on IR sensor technology. This project focuses on infrared sensors and their susceptibility to various signal patterns, with the goal of exploring methods to effectively bypass these security mechanisms. In addition, this repository aims to be a resource on constructing IR emitters (or torches), designed to execute these bypass door sensors. By providing detailed information on the necessary hardware components and assembly instructions, we hope enable professional red teamers and other security researchers to build their own devices tailored to specific security scenarios.

Please note that this repository is currently in the early stages of development. As we continue to gather more information and refine our techniques, expect regular updates and expansions to the content. We encourage contributions and feedback.

## Exit Sensors

### NT Series

Very common in the UK. The OEM doesn't ever seem to be specified on listing or the device itself, but suspected to be [YLI](https://www.yli.cn/en/product/Button/Infrared-Sensor/).

* [STP-NT100](nt100.md)
* [STP-NT200](nt200.md)

### Other

* [EBNT_TF_3](EBNT_TF_3.md)
* [DS-K7P03](ds-k7p03.md)
* [SP80NT](sp80nt.md) Videx NT Series Touch Free Entry & Exit
* [SMB-I016](smb-i016.md)
* [AMS-EBIR3-RG](ams-ebir3-rg.md)
* [DT_3L29](dt_3l29.md)
* [NT1](nt1.md)

### Capacitive Devices

These devices look a lot like IR touchless exit buttons, some are even advertised as such, but actually use capacitive sensors which are touch or have a range of about an inch.

* [unknown-00](unknown-00.md) no model number and unbrand fake IR sensor
* [HBK-E02](hbk-e02.md) 

## Torches and components

* [Flipper Zero](https://docs.flipper.net/infrared) - the flipper can be an easy to use device to show proof of concept, but doesnt have sufficent power for many use cases. This is espically true when there is no direct line of sight or across larger distances.
* [CHANZON](chanzon.md) - Chanzon produce a series of LED arrays, including some higher power components suitable for using at range.