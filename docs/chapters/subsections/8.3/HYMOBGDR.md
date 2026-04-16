### HYMOBGDR -- Activate Carlson and Killough Alternative Drainage Hysteresis Option

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

This keyword, [HYMOBGDR](#__RefHeading___Toc211572_2135714711), activates the Carlson and Killough alternative secondary drainage hysteresis option for when the hysteresis option has been activated by the HYSTER variable on the [SATOPTS](#__RefHeading___Toc37029_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, and either the Carlson[^1] or Killough[^2] models have been selected via the [EHYSTR](#__RefHeading___Toc67396_621662414) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section. Due to numerical accuracy, the gas saturation may fall below the critical gas saturation ([SGCR](#__RefHeading___Toc20428_784232322)), that is the largest gas saturation for which the gas relative permeability is zero, and gas would therefore be immobile until the gas saturation increases above [SGCR](#__RefHeading___Toc20428_784232322). This option overcomes this situation by letting the gas become mobile once it starts increasing, effectively setting the [SGCR](#__RefHeading___Toc20428_784232322) to the current gas saturation.

There is no data required for this keyword and there is no terminating "/" for this keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

#### Example

\--

\-- ACTIVATE CARLSON AND KILLOUGH ALTERNATIVE DRAINAGE HYSTERESIS OPTION

\--

HYMOBGDR

[^1]: Carlson, F. M. "Simulation of Relative Permeability Hysteresis to the Non-Wetting Phase," paper SPE 10157, presented at the SPE Annual Technical Conference & Exhibition, San Antonio, Texas, USA (October 5-7, 1981).

[^2]: Killough, J. E. "Reservoir Simulation with History-dependent Saturation Functions," paper SPE 5106, Society of Petroleum Engineers Journal (1976) 16, No. 1, 37-48.
