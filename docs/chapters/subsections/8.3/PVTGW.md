### PVTGW -- Gas PVT Properties for Dry Gas with Vaporized Water

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[PVTGW](#__RefHeading___Toc355649_3149455253) defines the gas PVT properties for dry gas[^1] with vaporized water. This keyword should be used when the [VAPWAT](#__RefHeading___Toc317543_3149455253) keyword has be declared in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section indicating that that vaporized water is present in the dry gas phase. The keyword may be used for gas-water and oil-water-gas input decks that contain the dry gas and vaporized water phases.

| 1 | PRESS | A real monotonically increasing down the column vector that defines the gas phase pressure, associated with the corresponding saturated water-gas ratio ("WGR") or Rw, the gas formation volume factor, and the gas viscosity for the stated saturated RWS.<br>For a given PRESS the variability of the gas formation volume factor and the gas viscosity with respect to the under-saturated Rw is optionally included as a sub table under RWU, FVFU and VISU columns, that is it is not necessary to repeat PRESS for each sub table entry. However, each sub table must be terminated by a "/".<br>The under saturated Rw entries are optional, except for perhaps the last PRESS entry to define the PVT properties above the initial saturation pressure. | None |  |
| --- | --- | --- | --- | --- |
| psia | barsa | atma |  |  |
| 2 | RWS | RWU | A columnar vector of real positive numbers for both the saturated (RWS) and under saturated (RWU) Rw sub table entries.<br>The RWS entry on the main table is the saturated WGR at the pressure indicated by PRESS and may be increasing or decreasing in value as PRESS varies.<br>Subsequent under-saturated Rw for a sub table at the given PRESS, as defined by RWU, are monotonically decreasing for entries in a given sub table. | None |
| stb/Mscf | sm^3^/sm^3^ | scc/scc |  |  |
| 3 | FVFS | FVFU | A columnar vector of real decreasing down the column values that defines the corresponding gas phase formation volume factor for a given pressure (PRESS) and for a given Rw (either RWS or RWU). | None |
| rb/Mscf | rm^3^/sm^3^ | rcc/scc |  |  |
| 4 | VISS | VISU | VISS a columnar vector of real increasing down the column values that defines the corresponding gas phase viscosity for a given pressure (PRESS) and for a given RWS.<br>VISU a columnar vector of real decreasing from VISS down the column values that defines the corresponding gas phase viscosity for a given pressure (PRESS) and for a given RWU. | None |
| cP | cP | cP |  |  |
| Notes:<br>1)  The keyword is followed by NTPVT tables as declared on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>2)  Each table must contain a minimum of two rows and a maximum of NPPVT rows and NRPVT Rw entries as declared on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>3)  Apart from the PRES data there must be same number of entries for each column.<br>4)  Each sub table defining the under saturated gas properties must be terminated by "/".<br>5)  Each main table is terminated by a single "/" on a separate line and there is no "/" terminator for the keyword. |  |  |  |  |

Table 8.118: PVTGW Keyword Description

Note that provided the first table has been entered, subsequent tables may be defaulted, in this case the prior table is copied to the current table.

See also the [PVTG](#__RefHeading___Toc104060_57619843) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section that defines the wet gas PVT for when vaporized oil is present in the gas phase. Alternatively, the [PVTGWO](#__RefHeading___Toc356776_4176551521) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section may be utilized instead of [PVTG](#__RefHeading___Toc104060_57619843) and [PVTGW](#__RefHeading___Toc355649_3149455253) to fully define the wet gas PVT properties, for when both vaporized oil and water are present in the gas phase.

#### Example

\--

\-- GAS PVT TABLE FOR DRY GAS WITH VAPORIZED WATER (OPM FLOW KEYWORD)

\--

PVTGW

\-- PRES RW BG VISC

\-- PSIA SM\^3/SM\^3 RM\^3/SM\^3 CPOISE

\-- \-\-\-\-\-- \-\-\-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\--

300 0.000479 0.042340 0.01344

0 0.042310 0.01389 /

600 0.000469 0.020460 0.01420

0 0.020430 0.01450 /

900 0.000403 0.013280 0.01526

0 0.013250 0.01532 /

1200 0.000354 0.009770 0.01660

0 0.009730 0.01634 /

1500 0.000272 0.007730 0.01818

0 0.007690 0.01752 /

1800 0.000225 0.006426 0.01994

0 0.006405 0.01883 /

2100 0.000191 0.005541 0.02181

0 0.005553 0.02021 /

2400 0.000163 0.004919 0.02370

0 0.004952 0.02163 /

/ TABLE NO. 1

\-- PRES RW BG VISC

\-- PSIA SM\^3/SM\^3 RM\^3/SM\^3 CPOISE

\-- \-\-\-\-\-- \-\-\-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\--

300 0.000479 0.042340 0.01344 /

600 0.000469 0.020460 0.01420 /

900 0.000403 0.013280 0.01526 /

1200 0.000354 0.009770 0.01660 /

1500 0.000272 0.007730 0.01818 /

1800 0.000225 0.006426 0.01994 /

2100 0.000191 0.005541 0.02181 /

2400 0.000163 0.004919 0.02370 /

/ TABLE NO. 2

The above example defines two dry gas PVT tables assuming NTPVT equals two and NPPVT is greater than or equal to eight on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

Notice that there is no terminating "/" for this keyword only for a table and a sub table.

[^1]: Natural gas that occurs in the absence of condensate or liquid hydrocarbons, or gas that had condensable hydrocarbons removed, is called dry gas. It is primarily methane with some intermediates. The hydrocarbon mixture is solely gas in the reservoir and there is no liquid (condensate surface liquid) formed either in the reservoir or at surface. The term dry indicates that the gas does not contain heavier hydrocarbons to form liquids at the surface conditions. Dry gas typically has GOR\'s greater than 100,000 scf/stb or 18,000 Sm3/m3.
