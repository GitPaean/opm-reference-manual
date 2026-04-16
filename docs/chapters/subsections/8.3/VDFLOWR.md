### VDFLOWR -- Velocity Dependent Flow Coefficient for Grid Block Flow (Region)

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

[VDFLOW](#__RefHeading___Toc530429_487874538) activates non-Darcy flow between grid blocks and defines a constant non-Darcy flow coefficient for individual regions allocated by the [SATNUM](#__RefHeading___Toc71136_2752266063) keyword in the [REGIONS](#__RefHeading___Toc40648_784232322) section. Note that the coefficient only applies to the gas phase. The coefficient is normally derived from well tests or calculated analytically based on the coefficient of inertial resistance, usually known as β, in Forchheimer's flow equation,[^1], [^2] and [^3]. Dake[^4], in chapter eight, reports a typical value of β to be 10.07 cm-1.

See also the [VDFLOW](#__RefHeading___Toc530429_487874538) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section that allows the non-Darcy coefficient to be entered for the whole grid, and the [WDFAC](#__RefHeading___Toc442057_2026549522) and [WDFACCOR](#__RefHeading___Toc48144_327352552) keywords in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section that assigns the non-Darcy coefficient to well connections.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

[^1]: Geertsma, J., 1974. Estimating the Coefficient of Inertial Resistance in Fluid Flow Through Porous Media. Soc.Pet.Eng.J., October: 445-450.

[^2]: Gewers, C.W.W. and Nichol, L.R., 1969. Gas Turbulence Factor in a Microvugular Carbonate. J.Can.Pet.Tech., April.

[^3]: Wong, S.W., 1970. Effects of Liquid Saturation on Turbulence Factors for Gas Liquid Systems. J.Can.Pet.Tech., October

[^4]: Dake, L.P. Fundamentals of Reservoir Engineering, Amsterdam, The Netherlands, Elsevier Science BV (1978) Chapter 8.6, pages 252-257.
