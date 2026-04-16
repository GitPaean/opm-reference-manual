### IMBNUMMF -- Define the Imbibition Saturation Table Region Numbers (Matrix-Fracture)

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [IMBNUMMF](#__RefHeading___Toc523278_2135714711) keyword defines the imbibition saturation tables (relative permeability and capillary pressure tables) region numbers for flow between the matrix and fracture blocks, for when the HYSTER option on the [SATOPTS](#__RefHeading___Toc37029_327352552) keyword has been invoked to activate the Hysteresis option, and the Dual Porosity or Dual Permeability models have been activated via the [DUALPORO](#__RefHeading___Toc241173_1772380413) or [DUALPERM](#__RefHeading___Toc241171_1772380413) keywords. All keywords are in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

The region number specifies which set of relative permeability tables ([SGFN](#__RefHeading___Toc106868_335817223), [SWFN](#__RefHeading___Toc106882_335817223), [SOF2](#__RefHeading___Toc106876_335817223), [SOF3](#__RefHeading___Toc106878_335817223), [SOF32D](#__RefHeading___Toc765497_4250154414), [SGOF](#__RefHeading___Toc106870_335817223), [SLGOF](#__RefHeading___Toc106874_335817223) and [SWOF](#__RefHeading___Toc45811_7190362561)) are used to calculate the relative permeability and capillary pressure between the matrix and fracture blocks. The keyword is optional and any cell not assigned a value will use the assignment from the [IMBNUM](#__RefHeading___Toc129665_83452205) array.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
