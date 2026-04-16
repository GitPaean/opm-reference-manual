### WSEGVALV -- Define Multi-Segment Well Sub-Critical Valve

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [WSEGVALV](#__RefHeading___Toc1091865_4263943340) keyword defines a multi-segment well segment to be a sub-critical valve Inflow Control Device ("ICD") as part of a completion for a multi-segment well. Note that the well must have been previously defined by the [WELSPECS](#__RefHeading___Toc268463_1366622701) and [WELSEGS](#__RefHeading___Toc97661_3261743917) keywords in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section and that the data for the keyword should be repeated for each multi-segment completion that contains a sub-critical valve ICD.

An ICD is a well completion component usually installed along the producing section of a well to minimize the unwanted water and gas breakthrough in an oil well, or early water production in a gas well, due to an uneven flow profile over the completed interval. Permeability variations over the producing interval cause the high permeability zones to produce higher quantities of fluids than the lower permeability zones and this uneven producing fluid profile may result in bypassed hydrocarbons. Secondly, for horizontal wells, the pressure loss from the "toe" to the "heel" of the well again results in an uneven fluid profile over the producing interval. In order to rectify this ICDs can be installed so that the well fluids have to flow through an ICD before entering the tubing; thus, creating an additional "designed" pressure loss.

A sub-critical valve ICD is a type of frictional ICD that adds an additional pressure loss by directing the fluid through a constriction before entering the tubing. The pressure drop is a function of the fluid density, the volumetric flow rate, and the diameter of the constriction. By placing various ICD's over the production interval one can design a completion that results in a more uniform producing fluid profile throughout the length of the producing interval.

| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which a multi-segment well is being defined.<br>Note that the well name (WELNAME) must have been declared previously using both the [WELSPECS](#__RefHeading___Toc268463_1366622701) and [WELSEGS](#__RefHeading___Toc97661_3261743917) keywords in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, otherwise an error may occur. | None |
| --- | --- | --- | --- |
| 2 | ISEG1 | A positive integer greater than or equal to two and less than or equal to MXSEGS on the [WSEGDIMS](#__RefHeading___Toc104259_3115110868) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section that defines the segment containing the sub-critical valve. | None |
| 3 | ICDCV | A real positive value greater than zero that defines the dimensionless flow coefficient for the valve (C~v~). This a vendor specific value for a given vendor's ICD. | None |
| dimensionless | dimensionless | dimensionless |  |
| 4 | AREAREST | A real positive value that defines the cross-sectional area of flow in the restricted section of the valve (A~r~) and should have a minimum value of 1.0 x 10^-10^.<br>This value may be specified using a User Defined Argument (UDA).<br>AREAREST is used to convert the segment volumetric flow rate into the flow velocity at the constriction (υ~r~). | None |
| ft^2^ | m^2^ | cm^2^ |  |
| 5 | SEGLEN | A real positive value greater than or equal to zero that defines the additional pipe length for the frictional pressure drop (L).<br>If set to zero then there is no additional pressure loss due to friction, whereas, if set to the default (1\*), then the segment pipe length is calculated from the corresponding [WELSEGS](#__RefHeading___Toc97661_3261743917) keyword. | Defined |
| ft | m | cm |  |
| 6 | ID | A real positive value that defines the pipe internal diameter of the segment used to calculate the pressure drop due to friction (D).<br>The value is used to replace the segment pipe internal diameter defined on the [WELSEGS](#__RefHeading___Toc97661_3261743917) keyword in record 2-7, also named ID. If ID is defaulted on this keyword then the equivalent value on the [WELSEGS](#__RefHeading___Toc97661_3261743917) keyword will be used instead.<br>Note for non-circular pipe segments use the equivalent diameter instead, that is: | Defined |
| feet | m | cm |  |
| 7 | EPSILON | A real positive value that defines the pipe absolute roughness for this segment.<br>The value is used to replace the segment pipe absolute roughness defined on the [WELSEGS](#__RefHeading___Toc97661_3261743917) keyword in record 2-8, also named EPSILON. If EPSILON is defaulted on this keyword then the equivalent value on the [WELSEGS](#__RefHeading___Toc97661_3261743917) keyword will be used instead. | Defined |
| feet | m | cm |  |
| 8 | AREAPIPE | A real positive value that defines the cross-sectional area of flow in the pipe (A~p~), as opposed to the restricted section of the valve (A~r~).<br>AREAPIPE is used to convert the segment volumetric flow rate into the flow velocity through the pipe (υ~p~).<br>The value is used to replace the segment pipe cross-sectional area of flow defined on the [WELSEGS](#__RefHeading___Toc97661_3261743917) keyword in record 2-9, named XAREA. If AREAPIPE is defaulted on this keyword then the equivalent value on the [WELSEGS](#__RefHeading___Toc97661_3261743917) keyword will be used instead. | Defined |
| ft^2^ | m^2^ | cm^2^ |  |
| 9 | STATUS | A character string of length four that defines the ICD's operational status, STATUS should be set to one of the following character strings:<br>1)  OPEN: the ICD connections are are open to flow.<br>2)  SHUT: the ICD connections are closed to flow (shut-in). | OPEN |
| 10 | AREAMAX | A real positive value that defines the maximum cross-sectional area of flow in the restricted section of the valve (A~max~).<br>AREAMAX is used to convert the segment volumetric flow rate into the maximum flow velocity at the constriction (υ~r~).<br>If defaulted then AREAPIPE will be used if defined, otherwise XAREA (item 2-9) on the [WELSEGS](#__RefHeading___Toc97661_3261743917) keyword will be used. | Defined |
| ft^2^ | m^2^ | cm^2^ |  |
| Notes:<br>1)  User Defined Quantities (\"UDQ\") can be used as User Defined Arguments (\"UDA\") for various group, well, and connection keywords in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. User Defined Arguments are activated using the [UDADIMS](#__RefHeading___Toc65914_1778172979) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, and defined by the [UDQ](#__RefHeading___Toc161095_2932703077) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.<br>2)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.121: WSEGVALV Keyword Description

The total number of wells should be defined via the [WELLDIMS](#__RefHeading___Toc82886_327352552) keyword and the number of multi-segment wells should be declared on the [WSEGDIMS](#__RefHeading___Toc104259_3115110868) keyword, both keywords are in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. In addition, the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword should be used to define wells, the [COMPDAT](#__RefHeading___Toc97651_3261743917) keyword to define the well completions for both ordinary wells and multi-segment wells, and the [COMPSEGS](#__RefHeading___Toc316604_3519154785) keyword to define a multi-segment segment completions. Finally, the [WSEGVALV](#__RefHeading___Toc1091865_4263943340) keyword can then be use to define ICD connections for the well. All the aforementioned keywords are described in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.

OPM flow calculates the pressure drop across the ICD using a homogeneous sub-critical flow through a constriction model. The model consists of two variables, the pressure drop due to the constriction,, and the pressure drop due to friction,, as shown in equation .

Where:

C~1~ and C~2~ = Unit conversion constants as listed in .

C~v~ = Vendor supplied dimensionless flow coefficient for the valve.

D = Diameter of the pipe.

f = Fanning friction factor.

L = Segment pipe length.

ρ = Fluid mixture density.

υ~r~ = The flow velocity of the mixture through the constriction.

υ~p~ = The flow velocity of the mixture through the segment pipe.

| Conversion Factor Constants and Variable Units |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| No. | Name | Field | Metric | Laboratory | Property |
| 1 | C~1~ | 2.159 x 10^-4^ | 1.0 x 10^-5^ | 9.869 x 10^-7^ | Constant |
| 2 | C~2~ | 2.892 x 10^-14^ | 1.340 x 10^-15^ | 7.615 x 10^-14^ |  |
| 3 | Density | lb/ft^3^ | kg/m^3^ | gm/cc | Units |
| 4 | Pressure | psia | bars | atm |  |
| 5 | Velocity | ft/s | m/s | cm/s |  |
| 6 | Volumetric Flow | ft^3^/day | m^3^/day | cc/hour |  |

Table 12.122: WELVALV Conversion Factor Constants and Units

In addition as both υ~r~ and υ~p~ are dependent on their respective cross-section areas then the volumetric flow (q) through the device requires that:

Substituting equation forin equation one obtains:

Where:

A~r~ = Cross-sectional area of the constriction.

C~2~ = Unit conversion constants as listed in .

C~v~ = Vendor supplied dimensionless flow coefficient for the valve.

ρ = Fluid mixture density.

q = Volumetric flow rate.

The base strength of the device, K is defined using equation as follows:

Note if K is greater than 0.1 then the device will be shut.

The setting of the device, that is how open the device is, is related to the restricted area and the maximum restricted area of the device as follows:

Where:

A~r~ = Cross-sectional area of the constriction.

A~max~ = Maximum cross-sectional area of the constriction.

#### Example

The following example is based on one producing well segment oil well (OP01) using the [WELSPECS](#__RefHeading___Toc268463_1366622701), [WELSEGS](#__RefHeading___Toc97661_3261743917) [COMPDAT](#__RefHeading___Toc97651_3261743917) and [COMPSEGS](#__RefHeading___Toc316604_3519154785) keywords, as per the [WSEGSICD](#__RefHeading___Toc124296_23127940) keyword example ([[Example](#anchor-3)](#12.3.310.1.Example|outline)), and is therefore not repeated here.

\--

\-- MULTI-SEGMENT WELL ICD SEGMENT SPECIFICATION DATA

\--

\-- WELL SEG DEVICE AREA PIPE PIPE PIPE PIPE OPEN MAX

\-- NAME NO CV REST LENG ID EPSI AREA SHUT AREA

WSEGVALV OP01 7 0.960 0.012 1\* 1\* 1\* 1\* OPEN 1\* / DEFAULT VALUES

OP01 12 0.960 0.012 1\* 1\* 1\* 1\* OPEN 1\* / TAKEN FROM

OP01 17 0.960 0.012 1\* 1\* 1\* 1\* OPEN 1\* / WELSEGS KEYWORD

OP01 22 0.850 0.100 1\* 1\* 1\* 1\* OPEN 1\* /

OP01 23 0.850 0.100 1\* 1\* 1\* 1\* OPEN 1\* /

OP01 24 0.850 0.100 1\* 1\* 1\* 1\* OPEN 1\* /

OP01 25 0.850 0.100 1\* 1\* 1\* 1\* OPEN 1\* /

/

Here segments 7, 12 and 17 have the same type of sub-critical valves with their pipe properties taken from the [WELSEGS](#__RefHeading___Toc97661_3261743917) keyword used to define well OP01 as a multi-segment well. Similarly, segments 22 to 25 have the same ICD properties, and again the pipe properties are taken from the [WELSEGS](#__RefHeading___Toc97661_3261743917) keyword.
