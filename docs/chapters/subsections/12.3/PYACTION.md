### PYACTION -- Define Python Based Action Conditions and Command Processing

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [PYACTION](#__RefHeading___Toc393199_4211536922) keyword is part of OPM Flow's Python scripting facility that loads a standard Python script file that can be used to define a series of conditions and actions as the simulation proceeds through time. The "included" Python script file is executed by the standard Python interpreter. Thus, OPM Flow's Python scripting facility offers greater flexibility compared to the commercial simulator's [ACTION](#__RefHeading___Toc148342_63720426) series of keywords ([ACTION](#__RefHeading___Toc148342_63720426), [ACTIONG](#__RefHeading___Toc152219_2992482751), [ACTIONR](#__RefHeading___Toc152221_2992482751), [ACTIONS](#__RefHeading___Toc152223_2992482751), [ACTIONW](#__RefHeading___Toc152225_2992482751) and [ACTIONX](#__RefHeading___Toc152227_2992482751)) that can apply Boolean conditional tests to variables at the field, group, region, well segment and well levels. Note that OPM Flow has also implemented the commercial simulator's [ACTIONX](#__RefHeading___Toc152227_2992482751) keyword, but not the [ACTION](#__RefHeading___Toc148342_63720426), [ACTIONG](#__RefHeading___Toc152219_2992482751), [ACTIONR](#__RefHeading___Toc152221_2992482751), [ACTIONS](#__RefHeading___Toc152223_2992482751) and [ACTIONW](#__RefHeading___Toc152225_2992482751) keywords, as the [ACTIONX](#__RefHeading___Toc152227_2992482751) keyword implements their functionality with greater flexibility. For a python class documentation and for further documentation and examples, also refer to the [OPM Online Python Documentation](https://opm.github.io/opm-python-documentation/index.html).

This keyword starts the definition of a [PYACTION](#__RefHeading___Toc393199_4211536922) section that specifies the name of the action and a string indicating the number of times the action should be run; this is then followed by the name of the file containing the Python script. Note that unlike an [ACTIONX](#__RefHeading___Toc152227_2992482751) block that is terminated by the [ENDACTIO](#__RefHeading___Toc109407_332691817) keyword the [PYACTION](#__RefHeading___Toc393199_4211536922) section has no terminating keyword.

Although this keyword is read by OPM Flow and the script processing has been implemented, one should use caution when using this facility as it may result in OPM Flow aborting. This is because the [PYACTION](#__RefHeading___Toc393199_4211536922) facility allows the user to implement complex functionality and the implementation was new for the 2020-04 release. Users should therefore use caution when using this facility.

| [PYACTION](#__RefHeading___Toc393199_4211536922) | [PYACTION](#__RefHeading___Toc393199_4211536922) declares the start of a [PYACTION](#__RefHeading___Toc393199_4211536922) Definition Section. This is then followed by one record that defines the name of the action and a string indicating the number of times the action should be run; this is then followed by a second record indicating the file containing the Python script. | Not Applicable |  |
| --- | --- | --- | --- |
| 1-1 | ACTNAME | ACTNAME is a character sting of any length enclose in quotes that defines the name of this action definition. | None |
| 1-2 | ACTNSTEP | ACTNSTEP is a defined character string that indicates the number of times the action should be performed, and should be set to one of the following:<br>1)  SINGLE: Here the action script is run only once.<br>2)  UNLIMITED: If this option is selected then the action is run at the end of every time step.<br>3)  FIRST_TRUE: This option forces the action to be run at the end of every time step until the script returns a value of True.<br>Note that the FIRST_TRUE option is only supported for back compatibility when using the deprecated run() function style Python scripts. | SINGLE |
| 1-4 | / | Record terminated by a "/" | Not Applicable |
| 2-1 | FILENAME | A character string enclosed in quotes that defines the Python module/script file to read in and to be processed by OPM Flow. | None |
| 2-2 | / | Record terminated by a "/" | Not Applicable |
| Notes:<br>1)  There is no terminating "/" for this keyword. |  |  |  |

Table 12.60: PYACTION Keyword Description

The [PYACTION](#__RefHeading___Toc393199_4211536922) keyword is a result of combining two programming languages, the interactive Python interpreter and OPM Flow's source code language C++. When combing two languages one extends and embeds one into the other. When extending Python with C++ the functionality implemented in C++ is made available to Python applications, when embedding Python in C++ one can call Python functions from within C++. The [PYACTION](#__RefHeading___Toc393199_4211536922) keyword is based on embedding a Python interpreter in the C++ OPM Flow simulator, such that Python code is run from within the simulator.

Note that to use the [PYACTION](#__RefHeading___Toc393199_4211536922) keyword OPM Flow must be built with embedded python enabled in opm-common/CMakeLists.txt.

option(OPM_ENABLE_EMBEDDED_PYTHON \"Enable embedded python?\" ON)

In order to fully benefit from the power of the [PYACTION](#__RefHeading___Toc393199_4211536922) keyword one should familiarize oneself with the Python wrapper classes for the various OPM Flow C++ classes. These classes are essential to share the simulator state with the [PYACTION](#__RefHeading___Toc393199_4211536922) script. That is, the function provides the interface between the two programming languages.

To learn more about these classes you can use the pydoc utility, for example, to learn more about the SummaryState class, in a Linux terminal one would issue the following bash command:

bash% pydoc opm.io.sim.SummaryState

The Python script file (FILENAME in the [PYACTION](#__RefHeading___Toc393199_4211536922) keyword) should be a standard Python module[^1] that defines the [PYACTION](#__RefHeading___Toc393199_4211536922) script and should consist of 100% pure Python. The [PYACTION](#__RefHeading___Toc393199_4211536922) Python module (FILENAME) is imported during processing of the input deck and as such this implies:

3)  1)  1)  Basic Python syntax checking is performed when the Python module (FILENAME) is read in.

        2)  It is verified that the module has the correct format.

The syntax of the Python module (FILENAME) is given in together with a description of the Python module opm_embedded.

| 1 | ecl_state | The ecl_state variable is an instance of the opm.io.ecl_state.EclipseState class which is initialized with all the static information in the simulation, for example the 3D grid properties and the PVT and saturation tables.<br>This object can be read by the Python script but the available data should not be modified as any updates will not be passed back to the simulator. |
| --- | --- | --- |
| 2 | schedule | The schedule variable is an instance of the opm.io.sched.Schedule class which has all the [SCHEDULE](#__RefHeading___Toc43945_784232322) information internalized (Schedule object). For a complete documentation of the available call points of opm.io.schedule.Schedule, we refer to <https://opm.github.io/opm-python-documentation/master/common.html#opm.io.schedule.Schedule>. The most notable ones are:<br>schedule.open_well(well_name, report_step)<br>schedule.shut_well(well_name, report_step)<br>schedule.stop_well(well_name, report_step)<br>Which can be used to open, shut or stop a well at a particular report step (or at the current report step if the report_step argument is not specified), and:<br>schedule.insert_keywords(kw)<br>Which can be used to insert various keywords where kw is a string defining the keyword and associated records. For the 2024.10 release this has been tested with the following keywords:<br>[BOX](#__RefHeading___Toc42110_3671211675),<br>[COMPSEGS](#__RefHeading___Toc316604_3519154785),<br>[ENDBOX](#__RefHeading___Toc88719_1778172979), [EXIT](#__RefHeading___Toc627737_1466963378),<br>[FIELD](#__RefHeading___Toc71850_2267116897),<br>[INCLUDE](#__RefHeading___Toc55749_2479612490),<br>[GCONINJE](#__RefHeading___Toc134874_2055188184), [GCONPROD](#__RefHeading___Toc146746_4203985108), [GCONSUMP](#__RefHeading___Toc188037_2026549522), [GEFAC](#__RefHeading___Toc268455_1366622701), [GRUPTREE](#__RefHeading___Toc118321_1596574740),<br>[METRIC](#__RefHeading___Toc70639_2267116897), [MULTX](#__RefHeading___Toc80283_1778172979), [MULTX-](#__RefHeading___Toc80285_1778172979), [MULTY](#__RefHeading___Toc80287_1778172979), [MULTY-](#__RefHeading___Toc80289_1778172979), [MULTZ](#__RefHeading___Toc80291_1778172979), [MULTZ-](#__RefHeading___Toc80293_1778172979),<br>[NEXT](#__RefHeading___Toc117629_2179381650), [NEXTSTEP](#__RefHeading___Toc323446_1841740821),<br>[WCONINJE](#__RefHeading___Toc146750_4203985108), [WCONPROD](#__RefHeading___Toc146754_4203985108), [WECON](#__RefHeading___Toc134884_2055188184), [WEFAC](#__RefHeading___Toc48856_327352552), [WELOPEN](#__RefHeading___Toc268461_1366622701), [WELPI](#__RefHeading___Toc121389_332691817), [WELTARG](#__RefHeading___Toc134888_2055188184), [WGRUPCON](#__RefHeading___Toc121641_2412586160), [WELSEGS](#__RefHeading___Toc97661_3261743917), [WELSPECS](#__RefHeading___Toc268463_1366622701), [WSEGVALV](#__RefHeading___Toc1091865_4263943340), [WLIST](#__RefHeading___Toc179534_3325167686), [WPIMULT](#__RefHeading___Toc121645_2412586160), [WTEST](#__RefHeading___Toc121925_2556401936), [WTMULT](#__RefHeading___Toc1141674_4263943340)<br>This list is subject to change for future releases.<br>The parsing strictness for the [ACTIONX](#__RefHeading___Toc152227_2992482751) and [PYACTION](#__RefHeading___Toc393199_4211536922) keywords can be set using the \--action-parsing-strictness command line option. If the default option \--action-parsing-strictness=\"normal\" has been set then OPM Flow will only apply keywords that have been tested, whereas if the option \--action-parsing-strictness=\"low\" has been set then OPM Flow will attempt to apply all keywords (however the simulation results may be incorrect).<br>Adding additional call points to the opm.io.schedule.Schedule instance in order to update the Schedule object in more ways is an obvious candidate for improving the [PYACTION](#__RefHeading___Toc393199_4211536922) functionality. |
| 3 | report_step | The current report step. |
| 4 | summary_state | The summary_state variable is an instance of the opm.io.sim.SummaryState class, the purpose of this class is to serve as a container for [SUMMARY](#__RefHeading___Toc43949_784232322) variables that contain the simulation results; for example, the Field Oil Rate (FOPR) or a Well's Water CuT (WWCT). See the [[SUMMARY SECTION](#anchor-2)](#11.SUMMARY SECTION|outline) for a detailed description of the variables available.<br>The summary_state variable will typically be the variable one will use to access the state of the simulation. For example, to check if the water cut in well OP01 exceeds 0.5 one would use the following statement:<br>if summary_state.well_var(\"OP01\", \"WWCT\") \> 0.50:<br>\...<br>The summary_state variable can also be use to update variables including [UDQ](#__RefHeading___Toc161095_2932703077) variables, i.e:<br>summary_state.update_well_var(\"OP01\", \"WUXX\", 0.25)<br>The above assigns a value of 0.25 to the well [UDQ](#__RefHeading___Toc161095_2932703077) variable WUXX for well OP01. |

Table 12.61: [PYACTION](#__RefHeading___Toc393199_4211536922) Module Script Definition

See also the [PYINPUT](#__RefHeading___Toc356358_1898124664) and [PYEND](#__RefHeading___Toc356356_1898124664) keywords in the [GRID](#__RefHeading___Toc38674_784232322)[^2] section which are also part of OPM Flow's Python scripting facility, that process standard Python commands that can be used to manipulate and define the simulators input parameters during processing of the input deck. The main purpose of the facility is to script the construction of the various keywords.

#### Examples

The first example checks if well OP01 has a water cut greater than 0.8 and if so then the well is shut in. In the input deck we would have:

\--

\-- START OF PYACTION SECTION

\--

\-- ACTNAME ACTNSTEP

PYACTION

\'MAXWCUT\' \'UNLIMITED\' /

\'pthon/script/MAXWCUT.py\' /

\--

\-- END OF PYACTION SECTION

\--

And then in the Python module file \'pthon/script/MAXWCUT.py\' one would have:

\#

\# OPM Flow PYACTION Module Script

\#

import opm_embedded

schedule = opm_embedded.current_schedule

summary_state = opm_embedded.current_summary_state

if (not \'setup_done\' in locals()):

executed = False

setup_done = True

if (not executed and summary_state.well_var(\"OP1\", \"WWCT\") \> 0.80):

message = \"Well OP01 has been shut-in due to WWCT \> 0.80\\n\"

opm_embedded.OpmLog.info(message)

schedule.shut_well(\"OP1\")

executed = True

Note how the \'executed\' variable is used to ensure that the action is only executed once the first time the water cut is greater than 0.8.

The next example is based on the first example from the [ACTIONX](#__RefHeading___Toc152227_2992482751) keyword ([[ACTIONX -- Define Action Conditions and Command Processing](#anchor-4)](#12.3.6.ACTIONX – Define ACTION Conditions and Command Processing|outline)). The Python script first checks if the field's water production is greater than 30,000 stb/d, and if not returns control back to the simulator. If the field water production is greater than 30,000 stb/d then the script uses a Python variable count to keep track of the number of times the script has been executed, and then sorts the wells from high water cut to low, via the wct_list variable, and then shuts in the worst offending well. If a well is shut-in the count variable is increased by one and control is passed back to the simulator. The script is executed as maximum of ten times.

\--

\-- START OF PYACTION SECTION

\--

\-- ACTNAME ACTNSTEP

PYACTION

\'WSHUTIN\' \'UNLIMITED\' /

\'pthon/script/WSHUTIN.py\' /

\--

\-- END OF PYACTION SECTION

\--

And then in the Python module file \'pthon/script/WSHUTIN.py\' one would have:

\#

\# OPM Flow PYACTION Module Script

\#

import opm_embedded

schedule = opm_embedded.current_schedule

summary_state = opm_embedded.current_summary_state

if (not \'setup_done\' in locals()):

execution_counter = 0

setup_done = True

if (execution_counter \< 10 and summary_state\[\"FWPR\"\] \>= 30000):

\#

\# Get Sorted Well List

\#

wct_list = sorted( \[ (well, summary_state.well_var(well, \"WWCT\"))

for well in summary_state.wells\], reverse=True )

\#

\# Shut-in Well with Highest Water Cut

\#

well, wwct = wct_list\[0\]

if wwct \> 0:

schedule.shut_well(well)

execution_counter += 1

Note that by using [PYACTION](#__RefHeading___Toc393199_4211536922) it makes sense to combine the [UDQ](#__RefHeading___Toc161095_2932703077) variable into the [PYACTION](#__RefHeading___Toc393199_4211536922) statement, like shown in the example above, although this is not necessary, as one could in principle use a normal [UDQ](#__RefHeading___Toc161095_2932703077) statement and then access the variables in the [PYACTION](#__RefHeading___Toc393199_4211536922) script using the summary_state variable.

The final example checks to see if the field's gas rate is below 600 MMscf/d and if the simulation time is greater that January 1, 2030. If it is, then compression is installed by re-setting all the gas producing well's THP and BHP pressures to 450 psia and 300 psia respectively. In addition all gas wells currently shut-in are tested to see if they can be opened up under the new THP and BHP constraints.

\--

\-- START OF PYACTION SECTION

\--

\-- ACTNAME ACTNSTEP

PYACTION

\'WSHUTIN\' \'UNLIMITED\' /

\'pthon/script/PHASE3.py\' /

\--

\-- END OF PYACTION SECTION

\--

And then in the Python module file \'pthon/script/PHASE3.py\' one would have:

\#

\# OPM Flow PYACTION Module Script

\#

import datetime

import opm_embedded

schedule = opm_embedded.current_schedule

summary_state = opm_embedded.current_summary_state

if (not \'setup_done\' in locals()):

executed = False

setup_done = True

if not executed:

sim_time = schedule.start +

datetime.timedelta( seconds = summary_state.elapsed() )

if (summary_state\[\"FGPR\"\] \< 600000 and

sim_time \> datetime.datetime(2030, 1, 1)):

\#

\# Do WELTARG and WTEST action

\#

\...

executed = True

Note how the current simulation time (sim_time) is evaluated from the simulation start time (schedule.start) and elapsed time (summary_state.elapsed); and how it is compared with 00:00 on 1 January 2030 using the Python datetime module.

[^1]: A Python module is a file containing Python definitions and statements. The file name is the module name with the suffix .py appended. Within a module, the module's name (as a string) is available as the value of the global variable \_\_name\_\_.

[^2]: Note the [PYINPUT](#__RefHeading___Toc356358_1898124664) and [PYEND](#__RefHeading___Toc356356_1898124664) keywords can be used in the [GRID](#__RefHeading___Toc38674_784232322), [EDIT](#__RefHeading___Toc40641_784232322), [PROPS](#__RefHeading___Toc39329_784232322), [SOLUTION](#__RefHeading___Toc43947_784232322), [SUMMARY](#__RefHeading___Toc43949_784232322) and [SCHEDULE](#__RefHeading___Toc43945_784232322) sections, but are described in the [GRID](#__RefHeading___Toc38674_784232322) section.
