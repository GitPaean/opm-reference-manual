### WSEGLABY -- Define Multi-Segment Well Labyrinth ICD Connections

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [WSEGSICD](#__RefHeading___Toc124296_23127940) keyword defines a multi-segment well segment to be a labyrinth Inflow Control Device. ("ICD") as part of a completion for a multi-segment well. Note that the well must have been previously define by the [WELSPECS](#__RefHeading___Toc268463_1366622701) and [WELSEGS](#__RefHeading___Toc97661_3261743917) keywords in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section and that the data for the keyword should be repeated for each multi-segment completion that contains a labyrinth ICD.

An ICD is a well completion component usually installed along the producing section of a well to minimize the unwanted water and gas breakthrough in an oil well, or early water production in a gas well, due to an uneven flow profile over the completed interval. Permeability variations over the producing interval cause the high permeability zones to produce higher quantities of fluids than the lower permeability zones and this uneven producing fluid profile may result in bypassed hydrocarbons. Secondly, for horizontal wells, the pressure loss from the "toe" to the "heel" of the well again results in an uneven fluid profile over the producing interval. In order to rectify this ICDs can be installed so that the well fluids have to flow through an ICD before entering the tubing; thus, creating an additional "designed" pressure loss.

A labyrinth ICD is a type of frictional ICD that adds an additional pressure loss by directing the fluid along a series of channels before entering the tubing. The channel flow path is designed in such a manner as to create the desired pressure loss for a given ICD. By placing various ICD's over the production interval one can design a completion that results in a more uniform producing fluid profile throughout the length of the producing interval. Although this type of ICD is not implemented in OPM Flow, it works in a similar fashion to how a spiral ICD works. Spiral ICDs are implemented in OPM Flow and the data is entered via the [WSEGSICD](#__RefHeading___Toc124296_23127940) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
