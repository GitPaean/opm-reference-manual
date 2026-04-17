### WTMULT -- Multiply a Well Target or Constraint by a Constant

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword, WTMULT, multiplies a defined well's target or constraint by a constant, for the target and constraints previously stipulated on the WCONPROD, WCONINJE, or WELTARG keywords, but not for the history matching wells using the WCONHIST or WCONINJH keywords. All the aforementioned keywords are in the SCHEDULE section. The constant should be positive value.

| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the well target or constraint (CONTROL) is being adjusted by the multipler (FACTOR).<br>Note that the well name (WELNAME) must have been declared previously using the WELSPECS keyword in the SCHEDULE section, otherwise an error may occur. | None |
| --- | --- | --- | --- |
| 2 | CONTROL | A defined character string that declares the well target or constraint that will be adjusted by multiplying its current value by the FACTOR defined in (3). CONTROL should be set to one of the following character strings:<br>1)  ORAT: the well's surface oil production rate will be adjusted.<br>2)  WRAT: the well's surface water production rate will be adjusted.<br>3)  GRAT: the well's surface gas production rate will be adjusted.<br>4)  LRAT: the well's surface liquid (oil plus water) production rate will be adjusted.<br>5)  CRAT: the well's linearly combined maximum surface rate, as per the LINCOM keyword in the SCHEDULE section, will be adjusted.<br>6)  RESV: the well's in situ reservoir volume rate will be adjusted.<br>7)  BHP: the well's bottom-hole pressure will be adjusted.<br>8)  THP: the well's tubing head pressure will be adjusted. In this case a vertical performance table must have been previously assigned to the well via the WCONPROD or WCONINJE keywords. The tables are entered via the VFPINJ or the VFPPROD keywords. All the keywords are in the SCHEDULE section.<br>9)  LIFT: the well's artificial lift quantity will be adjusted. Again, as for the THP, a vertical performance table must have been assigned to the well.<br>10) GUID: the well's guide rate will be adjusted. Only wells under group control and have a guide rate stipulated by the WGRUPCON keyword in the SCHEDULE section, may use this option.<br>11) CVAL: the well's calorific rate will be adjusted.<br>12) NGL: the well's natural gas liquid rate will be adjusted.<br>Note that the CRAT, CVAL and the NGL options are not available in OPM Flow and should not be used. | None |
| 3 | FACTOR | A postive real value that defines the FACTOR that is used to multiply the CONTROL specified in (2).<br>This value may be specified using a User Defined Argument (UDA). | None |
| dimensionless | dimensionless | dimensionless |  |
| 4 | NTIME | A positive integer greater than or equal to one that defines the number of report time steps for which the well target or constraint (CONTROL) is multiplied by the FACTOR. This is only applied when the FACTOR is specified by a User Defined Argument (UDA).<br>The default value of one means that the multiplication is applied only at the current time step for the UDA variable.<br>This option is not supported by OPM Flow. | 1 |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  User Defined Quantities (\"UDQ\") can be used as User Defined Arguments (\"UDA\") for various group, well, and connection keywords in the SCHEDULE section. User Defined Arguments are activated using the UDADIMS keyword in the RUNSPEC section, and defined by the UDQ keyword in the SCHEDULE section.<br>2)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.128: WTMULT Keyword Description

See also the WELTARG and WELCNTL keywords in the SCHEDULE section, that can be used to reset the well's target and constraints of both rates and pressures, as well as the well's control mode.

#### Example

The example shows three oil wells having the flow streams adjusted.

\--

\-- WELL TARGET/LIMIT MULTIPLIER

\--

\-- WELL WELL MULT REPORT

\-- NAME CNTL FACTOR TIMES

WTMULT

OP01 ORAT 0.90 /

OP02 BHP 0.95 /

OP03 LIFT 1.25 /

/

Well OP01 has its current oil rate target multiplied by 0.90, well OP02 has its bottom-hole pressure constraint multiplied by 0.95, and well OP03 has its artificial lift quantity increased by 1.25 times.
