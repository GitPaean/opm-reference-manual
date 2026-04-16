### SCDETAB -- Well Connection Karst Aquifer Properties for Scale Deposit

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

[SCDETAB](#__RefHeading___Toc624987_516898843) defines well connection karst[^1] aquifer properties for modeling scale deposited by dissolution of calcite from the aquifer water, for when the Scale Deposition option has been activated by declaring the dimensions of the scaling deposition tables using the [SCDPDIMS](#__RefHeading___Toc637730_516898843) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. The [SCDETAB](#__RefHeading___Toc624987_516898843) tables are allocated to individual wells using the [WSCTAB](#__RefHeading___Toc957314_4263943340) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

[^1]: Karst is a topography formed from the dissolution of soluble rocks such as limestone, dolomite, and gypsum. Karst aquifers are characterized by a network of conduits and caves, with the conduits and caves draining the pore space between the limestone grains (intergranular or primary porosity) and the fractures (secondary porosity) formed by joints, bedding planes, and faults.
