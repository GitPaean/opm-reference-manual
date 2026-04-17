### GDCQ -- Define Group Multiple Daily Contract Quantities

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The GDCQ keyword defines the Daily Contract Quantities ("DCQ") for when multiple group contracts are required when the Gas Field Operations model has been activated by the GASFIELD keyword in the RUNSPEC section, or the GWSINGF has been invoked to define multiple group contracts in the SCHEDULE section. The group contracts must first be defined by the GSWINGF keyword, followed by the GCDQ keyword, and then the GASYEAR or GASPERIO keywords. GCDQ may be repeated in the SCHEDULE section to reset group DCQs.

See also the SWINGFAC keyword that set a single group DCQ at the field level, as opposed to having multiple DCQ group contracts using the GDCQ keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
