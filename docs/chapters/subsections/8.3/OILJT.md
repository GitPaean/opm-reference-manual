### OILJT -- Define Oil Joule-Thomson Coefficient

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

[OILJT](#__RefHeading___Toc163486_25453417611) activates the oil Joule-Thomson effect[^1] in temperature calculations, and defines the oil Joule-Thomson Coefficient ("JTC") at a given reference pressure, for when OPM Flow's thermal option has been activated by the [THERMAL](#__RefHeading___Toc137276_650382403) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979).

This keyword can only be used if OPM Flow's thermal option has been activated by the [THERMAL](#__RefHeading___Toc137276_650382403) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. Note this is different to the commercial simulator that uses the [TEMP](#__RefHeading___Toc146397_3544483072) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section to activate the black-oil thermal model, and does not include the Joule-Thomson effect in temperature calculations.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > No.                                                                                                                                                                                  | > Name       | > Description                                                                                                                                                                                                                                     | > Default |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > Field                                                                                                                                                                                | > Metric     | > Laboratory                                                                                                                                                                                                                                      |           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > 1                                                                                                                                                                                    | > PRESS      | > A real positive value that defines the reference pressure for the corresponding Joule-Thomson Coefficient, OILJTC.                                                                                                                              | > None    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > psia                                                                                                                                                                                 | > barsa      | > atma                                                                                                                                                                                                                                            |           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > 2                                                                                                                                                                                    | > OILJTC     | > OILJTC is a real positive or negative value that defines the oil phase Joule-Thomson Coefficient.                                                                                                                                               | > 0       |
|                                                                                                                                                                                        |              |                                                                                                                                                                                                                                                   |           |
|                                                                                                                                                                                        |              | > If the value is defaulted (1\*) or set to 0, then OILJTC is internally calculated using the thermal oil density data on the [OIL](#__RefHeading___Toc97439_1778172979)DENT keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section.  |           |
|                                                                                                                                                                                        |              |                                                                                                                                                                                                                                                   |           |
|                                                                                                                                                                                        |              | > If a non-zero value is specified, then the OILJTC is assumed to be constant and equal to that value.                                                                                                                                            |           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > oF/psia                                                                                                                                                                              | > ^o^C/barsa | > ^o^C/atma                                                                                                                                                                                                                                       |           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| > Notes:                                                                                                                                                                               |              |                                                                                                                                                                                                                                                   |           |
|                                                                                                                                                                                        |              |                                                                                                                                                                                                                                                   |           |
| 1)  The keyword is followed by NTPVT records as declared on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.   |              |                                                                                                                                                                                                                                                   |           |
|                                                                                                                                                                                        |              |                                                                                                                                                                                                                                                   |           |
| 2)  Each data set is terminated by a "/" and there is no "/" terminator for the keyword.                                                                                               |              |                                                                                                                                                                                                                                                   |           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+

Table 8.92: OILJT Keyword Description

The Joule--Thomson effect is when a real gas, as oppose to an ideal gas, expands, resulting in the temperature of the gas dropping[^2]. For liquids the effect is the opposite, that is the internal energy is transferred to kinetic energy with a corresponding increase in temperature as velocity increases.

Thermodynamically, the Joule--Thomson coefficient is defined as the isenthalpic[^3] change in temperature in a fluid caused by a unitary pressure drop, as shown in the following equation:

Which can also express as[^4]:

Setting the gravity term, , to zero we have:

Where:

= Joule--Thomson coefficient (oC/Pa),

= thermal expansivity at constant pressure (1/oC),

= specific heat at constant pressure (J/kg oC),

= gravitational acceleration (m/s2)

= pressure (Pa),

= temperature (oC), and

= height (m).

#### Example

The following example shows the [OILJT](#__RefHeading___Toc163486_25453417611) keyword for when the thermal option has been activated by the [THERMAL](#__RefHeading___Toc137276_650382403) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, and for when NTPVT on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section is set equal to two.

\--

\-- OIL JOULE-THOMSON COEFFICIENT (OPM FLOW EXTENSION KEYWORD)

\--

\-- REF OIL

\-- PRESS JTC

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\--

OILJT

20.0 1\* / TABLE NO. 01

20.0 -0.20 / TABLE NO. 02

Here the first entry is defaulted, and the simulator will therefore calculate the oil JTC internally using the data on the [OILDENT](#__RefHeading___Toc125713_2509125675) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section.

There is no terminating "/" for this keyword.

[^1]: The Joule--Thomson coefficient is defined as the change in temperature with respect to an increase in pressure at constant enthalpy.

[^2]: Natural Gas Engineering (McGraw-Hill chemical engineering series), Donald L. Katz, Robert l Lee, McGraw-Hill Education, 1990 (ISBN 0071007776, 9780071007771).

[^3]: An isenthalpic process or isoenthalpic process, is a process that proceeds without any change in enthalpy, H; or specific enthalpy, h.

[^4]: Pippard, A.B.: Elements of Classical Thermodynamics: For Advanced Students of Physics. Cambridge University Press, Cambridge, UK (1957)
