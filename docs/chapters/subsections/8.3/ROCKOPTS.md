### ROCKOPTS -- Define Rock Compaction and Compressibility Options

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [ROCKOPTS](#__RefHeading___Toc111814_2939291539) keyword defines various options with respect to rock compaction and rock compressibility.

| 1 | ROCKOPT1 | A defined character string that specifies how the overburden pressures supplied by the [OVERBURD](#__RefHeading___Toc162159_4194303431) keyword are applied to the tabulated pressures in the [ROCKTAB](#__RefHeading___Toc107256_3812137098) keywords:<br>1)  STRESS: Use this option if the overburden pressures on the [OVERBURD](#__RefHeading___Toc162159_4194303431) keyword are greater than the fluid pressure which results in the effective fluid pressure being negative. To avoid the rock compaction tables being entered with negative pressure values use this option. In this case the pore volume and transmissibility multipliers will be tabulated against the effective overburden pressure.<br>2)  PRESSURE: In this case the pore volume and transmissibility multipliers should be tabulated against the effective fluid pressure. This the default value.<br>ROCKOPT1 should be set to PRESSURE if the [OVERBURD](#__RefHeading___Toc162159_4194303431) is not used in the input deck.<br>Only the default value of PRESSURE is supported. | PRESSURE |
| --- | --- | --- | --- |
| 2 | ROCKOPT2 | A defined character string that sets the reference pressure option:<br>1)  STORE: Copies the initial calculated grid block pressures into the overburden pressure array, resulting in the pore volumes being referenced at the initial pressures instead of the reference pressures as per the [ROCKTAB](#__RefHeading___Toc107256_3812137098) keyword.<br>2)  NOSTORE: This option results in the pore volumes being referenced as per the [ROCKTAB](#__RefHeading___Toc107256_3812137098) keyword. This is the default value.<br>Note that STORE option should not be used with the [OVERBURD](#__RefHeading___Toc162159_4194303431) keywords as the [OVERBURD](#__RefHeading___Toc162159_4194303431) data will be overwritten. | NOSTORE |
| 3 | ROCKOPT3 | A defined character string that specifies which region array should be used to allocate the various [ROCK](#__RefHeading___Toc45809_719036256) and [ROCKTAB](#__RefHeading___Toc107256_3812137098) property tables in the model:<br>1)  ROCKOPT3, should be set to [ROCKNUM](#__RefHeading___Toc118210_2939291539), [SATNUM](#__RefHeading___Toc71136_2752266063) or [PVTNUM](#__RefHeading___Toc68366_2752266063).<br>2)  If the parameter is defaulted or the ROCKOPT keyword is not present in the deck, then the [PVTNUM](#__RefHeading___Toc68366_2752266063) array is used.<br>3)  Secondly, if ROCKOPT3 is set to [ROCKNUM](#__RefHeading___Toc118210_2939291539) but the NTROCC parameter on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section is defaulted, then again the [PVTNUM](#__RefHeading___Toc68366_2752266063) array will be utilized.<br>Only the [PVTNUM](#__RefHeading___Toc68366_2752266063) and [ROCKNUM](#__RefHeading___Toc118210_2939291539) options are currently supported. | [PVTNUM](#__RefHeading___Toc68366_2752266063) |
| 4 | ROCKOPT4 | A defined character string that sets the initial conditions for the HYSTER and BOBERG options:<br>1)  DEFLATION: This option defines the reservoir rock to be fully compacted and the deflation curve is used to calculated the initial pore volume and transmissibility multipliers. This is the default value.<br>2)  ELASTIC: This option sets the pore volume and transmissibility multipliers to one, as the reservoir rock is set to lie on the elastic curve.<br>This parameter is ignored by OPM Flow as the [ROCKCOMP](#__RefHeading___Toc55593_1778172979)(ROCKOPT) options of HYSTER and BOBERG are not supported by the simulator. | DEFLATION |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 8.128: ROCKOPTS Keyword Description

#### Example

\--

\-- ROCKOPT1 ROCKOPT2 ROCKOPT3 ROCKOPT4

\-- PRS/STRE NO/STORE ARRAY

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\--

ROCKOPTS

PRESSURE NOSTORE PVTNUM / ROCK COMP OPTIONS

The above example defines the default values for the [ROCKOPTS](#__RefHeading___Toc111814_2939291539) keyword.
