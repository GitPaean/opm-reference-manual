### SOMGAS -- STONE1 Model Minimum Oil Saturation versus Gas Saturation

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

This keyword defines the minimum oil saturation as a function of gas saturation for Stone's[^1] first three phase oil relative permeability model as modified by Aziz and Settari[^2]. If the [STONE1](#__RefHeading___Toc210162_2884651453) and [STONE2](#__RefHeading___Toc210166_2884651453) keywords are not present in the input deck then the default three phase oil relative permeability model is employed. The [SOMGAS](#__RefHeading___Toc798236_4250154414) and [STONE1](#__RefHeading___Toc210162_2884651453) keywords should only be used in three phase runs containing the oil, gas and water phases. The keyword is optional.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

[^1]: Stone, H. L. "Probability Model for Estimating Three-Phase Relative Permeability," paper SPE 2116, Journal of Canadian Petroleum Technology (1973) 22, No. 2, 214-218.

[^2]: Aziz, K. and Settari, A. Petroleum Reservoir Simulation, London, UK, Applied Science Publishers (1979), page 398.
