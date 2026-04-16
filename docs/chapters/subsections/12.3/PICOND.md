### PICOND -- Define the Generalized Pseudo Pressure Parameters

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [PICOND](#__RefHeading___Toc763537_2928331029) keyword defines the Generalized Pseudo Pressure ("GPP")[^1] and [^2] parameters used in a gas condensate well connection inflow equations. GPP accounts for both the impact of condensate drop out and compressibility in the mobility inflow term . If the keyword is absent from the input deck then the default values are applied.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

[^1]: Whitson, C. H. and Fevang, Ø. "Generalised Pseudopressure Well Treatment in Reservoir Simulation," Presented at the IBC Technical Services Conference on Optimisation of Gas Condensate Fields, Aberdeen, UK (June 26-27, 1997)

[^2]: Whitson, C. H. and Fevang, Ø. "Modeling Gas Condensate Well Deliverability," paper SPE 30714, SPE Reservoir Engineering (1996) 11, No. 4, 221-230; also presented at the SPE Annual Technical Conference and Exhibition, Dallas, Texas, USA (October 22-25, 1995).
