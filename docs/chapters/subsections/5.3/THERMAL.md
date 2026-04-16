### THERMAL -- Activate the Thermal Modeling Option

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword activates the thermal modeling option.

In OPM Flow\'s thermal model ([THERMAL](#__RefHeading___Toc137276_650382403) keyword) enthalpy is conserved and the energy equations are solved fully implicitly with the black-oil equations. Whereas, in OPM Flow\'s temperature model ([TEMP](#__RefHeading___Toc146397_3544483072) keyword) internal energy is conserved (the work term is neglected and internal energy is equal to enthalpy) and the energy equations are solved sequentially after the black-oil equations. Note that the thermal model can be modified so that internal energy rather than enthalpy is conserved by setting the command line option \--conserve-inner-energy-thermal=true (the default is false). If properties like density or viscosity \"strongly\" depend on temperature, the thermal model is recommended.

There is no data required for this keyword and there is no terminating "/" for this keyword.

The temperature option ([TEMP](#__RefHeading___Toc146397_3544483072) keyword) and the thermal option ([THERMAL](#__RefHeading___Toc137276_650382403) keyword) are two separate modeling facilities in the commercial simulator, although some keywords can be used by both options, for example the [RTEMP](#__RefHeading___Toc111816_2939291539) keyword. OPM Flow's thermal model is not directly equivalent to either the commercial simulator's black-oil [TEMP](#__RefHeading___Toc146397_3544483072) or compositional [THERMAL](#__RefHeading___Toc137276_650382403) formulation.

The energy black-oil implementation in OPM Flow uses a mixture of the commercial simulators black-oil and the commercial simulators "compositional thermal" keywords, as well as some OPM Flow specific keywords. Keywords specifically associated with both OPM Flow's [THERMAL](#__RefHeading___Toc137276_650382403) and the commercial simulators [TEMP](#__RefHeading___Toc146397_3544483072) and [THERMAL](#__RefHeading___Toc137276_650382403) options are listed in for ease of reference.

| [RUNSPEC](#__RefHeading___Toc55591_1778172979) | ROCKDIMS | Thermal Rock Dimensions of Over and Underburden Rock Types |  |  |  |
| --- | --- | --- | --- | --- | --- |
| [TEMP](#__RefHeading___Toc146397_3544483072) | Activate the Temperature Modeling Option |  |  | Black-Oil |  |
| [THERMAL](#__RefHeading___Toc137276_650382403) | Activate the Thermal Modeling Option |  |  |  |  |
| [GRID](#__RefHeading___Toc38674_784232322) | ROCKCON | Thermal Rock Over and Underburden Connection Data |  |  |  |
| ROCKPROP | Thermal Rock Over and Underburden Property Data |  |  |  |  |
| [HEATCR](#__RefHeading___Toc128353_2509125675) | Rock Heat Capacity. |  |  |  |  |
| [HEATCRT](#__RefHeading___Toc138899_2509125675) | Rock Heat Capacity Temperature. |  |  |  |  |
| [THCGAS](#__RefHeading___Toc93091_718313858) | Gas Phase Thermal Conductivity. |  |  |  |  |
| [THCOIL](#__RefHeading___Toc119871_650382403) | Oil Phase Thermal Conductivity. |  |  |  |  |
| [THCONR](#__RefHeading___Toc132284_650382403) | Thermal Conductivity of liquids and reservoir rock. |  |  |  |  |
| [THCONSF](#__RefHeading___Toc132286_650382403) | Thermal Conductivity of liquids and reservoir rock scaling factor applied to [THCONR](#__RefHeading___Toc132284_650382403) to account for gas saturation. |  |  |  |  |
| [THCROCK](#__RefHeading___Toc124825_650382403) | Rock Thermal Conductivity. |  |  |  |  |
| THCSOLID | Solid Phase Thermal Conductivity. |  |  |  |  |
| [THCWATER](#__RefHeading___Toc323954_1728001293) | Water Thermal Conductivity. |  |  |  |  |
| [PROPS](#__RefHeading___Toc39329_784232322) | HEATVAP | Thermal Oil Component Heat of Vaporization |  |  |  |
| [GASDENT](#__RefHeading___Toc123086_2509125675) | Gas Density Temperature Coefficients (OPM Flow keyword). |  |  |  |  |
| [GASJT](#__RefHeading___Toc163486_2545341761) | Gas Joule-Thomson Coefficient (OPM Flow keyword). |  |  |  |  |
| [GASVISCT](#__RefHeading___Toc163486_254534176111) | Gas Viscosity versus Temperature Functions (OPM Flow black-oil keyword). |  |  |  |  |
| [OILDENT](#__RefHeading___Toc125713_2509125675) | Oil Density Temperature Coefficients (OPM Flow keyword). |  |  |  |  |
| [OILJT](#__RefHeading___Toc163486_25453417611) | Oil Joule-Thomson Coefficient (OPM Flow keyword). |  |  |  |  |
| [OILVISCT](#__RefHeading___Toc107282_57619843) | Oil Viscosity versus Temperature Functions (OPM Flow black-oil keyword). |  |  |  |  |
| [RTEMP](#__RefHeading___Toc111816_2939291539) | Constant Initial Reservoir Temperature. |  |  |  |  |
| [RTEMPA](#__RefHeading___Toc111818_2939291539) | Constant Initial Reservoir Temperature. |  |  |  |  |
| [RTEMPVD](#__RefHeading___Toc108628_29392915391) | Initial Reservoir Temperature versus Depth. |  |  |  |  |
| SPECHA | Thermal Specific Heat of Oil Component |  |  |  |  |
| [SPECHEAT](#__RefHeading___Toc121479_83452205) | Specific Heat of Oil, Water and Gas |  |  |  |  |
| [SPECROCK](#__RefHeading___Toc121481_83452205) | Specific Heat of the Reservoir Rock |  |  |  |  |
| [TEMPVD](#__RefHeading___Toc108626_29392915392) | Initial Reservoir Temperature versus Depth. |  |  |  |  |
| THANALB | Activate Thermal Analytic Water Density Option |  |  |  |  |
| THERMEX1 | Liquid Components Thermal Expansion Coefficient |  |  |  |  |
| [WATDENT](#__RefHeading___Toc173954_2545341761) | Oil Density Temperature Coefficients. |  |  |  |  |
| [WATJT](#__RefHeading___Toc163486_254534176112) | Water Joule-Thomson Coefficient (OPM Flow keyword). |  |  |  |  |
| [WATVISCT](#__RefHeading___Toc121489_83452205) | Oil Viscosity versus Temperature Function. |  |  |  |  |
| [REGIONS](#__RefHeading___Toc40648_784232322) | THERMNUM | Thermal Region Numbers. |  |  |  |
| [SOLUTION](#__RefHeading___Toc43947_784232322) | [RTEMP](#__RefHeading___Toc111816_2939291539) | Constant Initial Reservoir Temperature. |  |  |  |
| [RTEMPA](#__RefHeading___Toc111818_2939291539) | Constant Initial Reservoir Temperature. |  |  |  |  |
| [RTEMPVD](#__RefHeading___Toc108628_29392915391) | Initial Reservoir Temperature versus Depth. |  |  |  |  |
| [TEMPI](#__RefHeading___Toc117385_650382403) | Initial Reservoir Temperature for All Cells. |  |  |  |  |
| [TEMPVD](#__RefHeading___Toc108626_29392915392) | Initial Reservoir Temperature versus Depth. |  |  |  |  |
| [SCHEDULE](#__RefHeading___Toc43945_784232322) | [WTEMP](#__RefHeading___Toc192631_213178337) | Set An Injection Well's Fluid Temperature |  |  |  |
| [WINJTEMP](#__RefHeading___Toc152097_2509125675) | Define Injection Fluid Thermal Properties |  |  |  |  |
| Notes:<br>1)  Cells colored green implies the keyword can be used with this model formulation.<br>2)  Cells colored orange means the keyword is recognized by OPM Flow's parser but is ignored and not used by OPM Flow.<br>3)  Cells colored red should not be used with this model formulation.<br>4)  The list is focused on the OPM Flow implementation of the energy and black-oil formulation and therefore does not necessary include all the commercial simulator's compositional keywords. |  |  |  |  |  |

Table 5.46: OPM Flow's THERMAL Option Associated Keywords

In thermal runs a producing well's bottom-hole temperature is calculated based on a weighted average of the temperature in the grid cell connections open to flow in the producing well, that is the reported bottom-hole temperature, *TBHT*, is calculated as:

with

The term is the energy rate density (J/(K s)) of phase *p*,

where:

= number of phases,

= number of open connections in the well,

= the open connection index,

= the phase index, oil, water and gas.

= indicating that the parameter is evaluated at reservoir conditions,

= temperature (K),

= connection flow rate (m^3^/s),

= fluid density (kg/m^3^), and

= specific heat capacity (J/(K kg))

(see the [SPECHEAT](#__RefHeading___Toc121479_83452205) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section).

The current implementation makes use of the specific internal energy:

derived from the specific enthalpy, *h~*pi*~*

where is connection grid block pressure of phase *p*.

The phase rates at surface conditionsare converted to reservoir in situ ratesusing the phase formation volume factor, *B~*pi*~*, via:

And thus equation can be simplified to:

#### Example

\--

\-- ACTIVATE THE THERMAL MODELING OPTION (OPM FLOW THERMAL OPTION ONLY)

\--

THERMAL

The above example activates the thermal modeling option.
