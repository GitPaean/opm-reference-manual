### BOGI -- Define Gi Oil Formation Volume Factor Pressure Tables

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [BOGI](#__RefHeading___Toc223321_1539708736) keyword defines Gi oil formation volume factor as a function of Gi and pressure for when the Gi option has been invoked via the [GIMODEL](#__RefHeading___Toc383678_1414963541) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

The accuracy of gas condensate and volatile oil modeling using a black-oil reservoir simulator is now firmly accepted in the industry; both depletion and gas cycling above the saturation point can be modeled and yield an acceptable match compared with compositional simulators. The main deficiency with the existing black-oil formulation is the treatment of gas injection below the saturation point, where the compositional effect of the stripping of liquid components is inversely proportional to their molecular weights, is not considered. This is because the black-oil model assumes that the saturated hydrocarbon fluid properties are only functions of pressure. Thus, when dry gas is injected into a condensate reservoir below the saturation pressure the injected gas continues to re-vaporize liquid at a rate governed only by the cell pressures. Compositional modeling indicate that this not the case.

The [GI](#__RefHeading___Toc372466_1414963541) option attempts to overcome the limitation of the standard black-oil approach by extending the black-oil model using the method of Cook et al.[^1] to take into account the fluid property changes occurring during gas injection. This is done by extending the fluid property treatment so that the saturated fluid properties depend on pressure (as per the standard black-oil formulation) and also on an additional parameter which characterizes the compositional changes in the reservoir liquid and vapor phases at constant pressure.

See also the [PVTG](#__RefHeading___Toc104060_57619843) and [GINODE](#__RefHeading___Toc389150_1414963541) keywords in the [PROPS](#__RefHeading___Toc39329_784232322) section.

[^1]: Cook, R. E., Jacoby, R. H., and Ramesh, A. B. "A Beta-type Reservoir Simulator for Approximating Compositional Effects During Gas Injection" paper SPE 4272, Society of Petroleum Engineers Journal (1974) 14, No. 5, 471-481.
