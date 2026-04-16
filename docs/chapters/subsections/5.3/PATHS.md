### PATHS -- Define Filename Directory Path Aliases

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[PATHS](#__RefHeading___Toc92959_4106839650) allows the user to define alias directory filenames to avoid long filenames with the [INCLUDE](#__RefHeading___Toc55749_2479612490), [IMPORT](#__RefHeading___Toc539691_2135714711), [RESTART](#__RefHeading___Toc135629_1317547213) or [GDFILE](#__RefHeading___Toc139346_951517595) keywords. To use the alias with the aforementioned keywords [PATHS](#__RefHeading___Toc92959_4106839650) should be prefixed with the \$ symbol.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | ALIAS | A character string enclosed in quotes defining the alias. | None |
| 2 | DIRC | A character string enclosed in quotes defining the directory filename. | None |
| Notes:<br>1)  Multiple entries must be on separate lines (see the example).<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 5.34: PATHS Keyword Description

#### Examples

\--

\-- PATH PATH

\-- ALIAS DIRECTORY FILENAME

PATHS

\'GRID\' \'/DISK1/NORNE/2017/GRID-INCLUDES\' /

\'SCHD\' \'/DISK1/NORNE/2017/SCHD-INCLUDES\' /

/

The above example defines "GRID" and "SCHD" aliases in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section than can be used in the [GRID](#__RefHeading___Toc38674_784232322) and [SCHEDULE](#__RefHeading___Toc43945_784232322) sections of the input deck. The next example shows how to use the "GRID" alias with the [INCLUDE](#__RefHeading___Toc55749_2479612490) keyword in the [GRID](#__RefHeading___Toc38674_784232322) section.

\--

\-- LOAD INCLUDE FILES

\--

INCLUDE

\'\$GRID/PORO.INC\' /

INCLUDE

\'\$GRID/PERMX.INC\' /

INCLUDE

\'\$GRID/NTG.INC\' /

Here the porosity, permeability and net-to-gross arrays are loaded in the [GRID](#__RefHeading___Toc38674_784232322) section using the directory filename aliases declared in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.
