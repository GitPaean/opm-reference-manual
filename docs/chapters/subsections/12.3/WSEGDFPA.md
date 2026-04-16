### WSEGDFPA -- Define Multi-Segment Well Drift Flux Slip Model Parameters

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

This keyword, [WSEGDFPA](#__RefHeading___Toc978485_4263943340), enables modification of a multi-segment well's drift flux slip model default parameters used by the WSEGDFMA keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section to define the model. A slip model[^1] and [^2] enables the different phases in the wellbore to flow at different velocities, for example gas will flow up the tubing at a higher velocity than oil and water. The option is activated by the FLOWOPT parameter on the [WELSEGS](#__RefHeading___Toc97661_3261743917) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section; however, the slip model flow calculation is not available in OPM Flow.

See also the [WSEGDFIN](#__RefHeading___Toc978481_4263943340) keyword that sets the slip model's input parameters and the [WSEGDFMD](#__RefHeading___Toc978483_4263943340) keyword that sets which drift flux slip model should be used. Note if the [WSEGDFPA](#__RefHeading___Toc978485_4263943340) keyword is used than it must be placed after the [WSEGDFMD](#__RefHeading___Toc978483_4263943340) keyword, but before the [WELSEGS](#__RefHeading___Toc97661_3261743917) keyword that defines a multi-segment well. All the aforementioned keywords are in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

[^1]: Shi, H., Holmes, J.A., Durlofsky, L. J., Aziz, K., Diaz, L. R., Alkaya, B., and Oddie, G. "Drift-Flux Modeling of Two-Phase Flow in Wellbores," paper SPE 84228, Society of Petroleum Engineers Journal (2005) 10, No. 1, 24-33; also presented as "Drift-Flux Modeling of Multiphase Flow in Wellbores," at the SPE Annual Technical Conference and Exhibition, Denver, Colorado, USA(October 5-8, 2003).

[^2]: Shi, H., Holmes, J.A., Diaz, L. R., Durlofsky, L. J., and Aziz, K. "Drift-Flux Parameters for Three-Phase Steady-State Flow in Wellbores," paper SPE 89836, Society of Petroleum Engineers Journal(2005) 10, No. 2, 130-137; also presented at the SPE Annual Technical Conference and Exhibition, Houston, Texas, USA (September 26-29, 2004).
