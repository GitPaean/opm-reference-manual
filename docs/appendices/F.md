---
title: 'Example: EGRID Header Keywords'
source: parts/appendices/F.fodt
generated_by: scripts/python/src/fodt/fodt2md
---

- OPM FLOW OUTPUT FILE FORMATS

Appendix Table of Contents
[APPENDIX F: OPM FLOW OUTPUT FILE FORMATS	2525](#-refheading-toc173255-3199336838)
[F.1 Overview	2529](#-refheading-toc156996-536838053)
[F.1.1 File Types	2529](#-refheading-toc207867-2189581950)
[F.1.2 File Naming Conventions	2534](#-refheading-toc156998-536838053)
[F.1.3 Unformatted File Format Considerations	2536](#-refheading-toc157000-536838053)
[F.1.4 File Output Format	2537](#-refheading-toc325986-3670698802)
[F.2 EGRID \- Model Structural Data for Irregular Corner\-Point Grids File	2540](#-refheading-toc157002-536838053)
[F.2.1 EGRID Header Keywords	2542](#-refheading-toc157004-536838053)
[F.2.2 EGRID Global Irregular Corner Point Grid Keywords	2546](#-refheading-toc157006-536838053)
[F.2.3 EGRID LGR Irregular Corner Point Grid Keywords	2550](#-refheading-toc157008-536838053)
[F.2.4 EGRID Non\-Neighbor Connections for Irregular Corner Point Grid Keywords	2553](#-refheading-toc157010-536838053)
[F.3 EGRID \- Model Structural Data for Unstructured Grids File	2556](#-refheading-toc157012-536838053)
[F.4 EGRID \- Model Structural Data for Mixed Grids File	2556](#-refheading-toc157014-536838053)
[F.5 GRID \- Model Structural Data File	2556](#-refheading-toc157016-536838053)
[F.5.1 RESTART Data \- LGR Grid Header Keywords	2556](#-refheading-toc183105-23177801971)
[F.6 INIT – Model Initialization and Static Data File	2559](#-refheading-toc157018-536838053)
[F.6.1 INIT Index File	2559](#-refheading-toc157020-536838053)
[F.6.2 INIT Data File Specification	2560](#-refheading-toc157022-536838053)
[F.6.3 INIT Data – Static Data Header Keywords	2563](#-refheading-toc183093-2317780197)
[F.6.4 INIT Data – Static Grid Array Data Keywords	2568](#-refheading-toc183097-2317780197)
[F.6.5 INIT Data \- LGR Static Data Header Keywords	2571](#-refheading-toc183105-2317780197)
[F.6.6 INIT Data \- LGR Grid Array Data Keywords	2574](#-refheading-toc157008-5368380531)
[F.6.7 INIT Data – Static Tabular Data Header Keyword	2576](#-refheading-toc183113-2317780197)
[F.6.8 INIT Data – Static Tabular and Constant Data Array Keywords	2579](#-refheading-toc1917801-204878952)
[F.7 RESTART Files – Dynamic Data \(Solution, Groups, Wells, Connections, Aquifers, etc.\)	2581](#-refheading-toc157024-536838053)
[F.7.1 RESTART Index Files	2582](#-refheading-toc157026-536838053)
[F.7.2 RESTART Data File Specification	2583](#-refheading-toc192633-213178337)
[F.7.3 RESTART Data \- Header Keywords	2585](#-refheading-toc183093-23177801971)
[F.7.4 RESTART Data – Group, Well, and Connection Data Keywords	2597](#-refheading-toc204774-4221434794)
[F.7.5 RESTART Data – UDQ and ACTIONX Keywords	2617](#-refheading-toc1543754-3510395024)
[F.7.6 RESTART Data – Aquifer Data Keywords	2624](#-refheading-toc195712-2189581950)
[F.7.7 RESTART Data – Hidden Keyword	2629](#-refheading-toc180532-2189581950)
[F.7.8 RESTART Data \- Solution Data keyword	2630](#-refheading-toc183097-23177801971)
[F.7.9 RESTART Data \- LGR Solution Data Keywords	2638](#-refheading-toc157008-53683805311)
[F.8 RFT Files – Pressure, Saturation and Production Log Data	2641](#-refheading-toc157030-536838053)
[F.8.1 RFT Data File Specification	2641](#-refheading-toc1917803-204878952)
[F.8.2 RFT Data File – Time and Date keywords	2642](#-refheading-toc323052-3560815606)
[F.8.3 RFT Data File – Well and Connection Data Keyword	2643](#-refheading-toc323054-3560815606)
[F.8.4 RFT Data File – RFT Solution Data Keyword	2645](#-refheading-toc330979-3560815606)
[F.8.5 RFT Data File – Solution PLT Data Keywords	2647](#-refheading-toc330981-3560815606)
[F.8.6 RFT Data File – Solution Multi\-Segment Well Keywords	2647](#-refheading-toc330983-3560815606)
[F.8.7 RFT Data File – Solution River Keywords	2647](#-refheading-toc338898-3560815606)
[F.9 SUMMARY Files – Time Based Vector Data	2648](#-refheading-toc157038-536838053)
[F.9.1 Enhanced SUMMARY Data File Keywords	2648](#-refheading-toc1917805-204878952)
[F.9.2 SUMMARY Index File keywords	2651](#-refheading-toc516418-3038542954)
[F.9.3 SUMMARY Data File Keywords	2656](#-refheading-toc1917807-204878952)
[F.10 SAVE Files \- Initialization and Solution Data	2658](#-refheading-toc157040-536838053)

Appendix Index of Tables
[Table F.1: OPM Flow Output File Types Summary	2532](#table7007csequence)
[Table F.2: RUNSPEC Input and Output File Format Keywords	2533](#table7017csequence)
[Table F.3: OPM Flow File Naming Conventions	2535](#table7027csequence)
[Table F.4: Big\-Endian and Little\-Endian Representation	2536](#table7037csequence)
[Table F.5: Output File Keyword Format	2537](#table7047csequence)
[Table F.6: INTEHEAD Keyword \- IWEL Example	2539](#table7057csequence)
[Table F.7: EGRID \- Model Structural Data for Irregular Corner\-Point Grids	2542](#table7067csequence)
[Table F.8: EGRID Header Keywords	2544](#table7077csequence)
[Table F.9: EGRID Global Irregular Corner Point Grid Keywords	2548](#table7087csequence)
[Table F.10: EGRID LGR Irregular Corner Point Grid Keywords	2551](#table7097csequence)
[Table F.11: EGRID NNC Keywords for Irregular Corner Point Grids	2554](#table7107csequence)
[Table F.12: RESTART Data \- LGR Grid Header Keywords	2557](#table7117csequence)
[Table F.13: INIT Data File Structure	2562](#table7127csequence)
[Table F.14: INIT Data – Static Data Header Keywords	2566](#table7137csequence)
[Table F.15: INIT Data – Static Grid Array Data Keywords	2570](#table7147csequence)
[Table F.16: INIT Data \- LGR Static Data Header Keywords	2572](#table7157csequence)
[Table F.17: INIT Data \- LGR Grid Array Data Keywords	2574](#table7167csequence)
[Table F.18: INIT Data – Static Tabular Data Header Keyword	2578](#table7177csequence)
[Table F.19: INIT Data – Static Tabular and Constant Data Array Keywords	2579](#table7187csequence)
[Table F.20: RESTART Data File Structure	2584](#table7197csequence)
[Table F.21: RESTART Data \- Header Keywords	2595](#table7207csequence)
[Table F.22: RESTART Data – Group, Well, and Connection Keywords \(Groups\)	2602](#table7217csequence)
[Table F.23: RESTART Data – Group, Well, and Connection Keywords \(Multi\-Segment Wells\)	2605](#table7227csequence)
[Table F.24: RESTART Data – Group, Well, and Connection Keywords \(Wells\)	2611](#table7237csequence)
[Table F.25: RESTART Data – Group, Well, and Connection Keywords \(Connections\)	2613](#table7247csequence)
[Table F.26: RESTART Data – Group, Well, and Connection Keywords \(Tracers\)	2614](#table7257csequence)
[Table F.27: RESTART Data – Group, Well, and Connection Keywords \(Network\)	2615](#table7267csequence)
[Table F.28: RESTART Data – UDQ Keywords	2619](#table7277csequence)
[Table F.29: RESTART Data – ACTIONX Keywords	2622](#table7287csequence)
[Table F.30: RESTART Data – Analytical Aquifer Data Keywords	2626](#table7297csequence)
[Table F.31: RESTART Data – Numerical Aquifer Data Keywords	2627](#table7307csequence)
[Table F.32: RESTART Data – Hidden Keyword	2629](#table7317csequence)
[Table F.33: RESTART Data \- Solution Data keyword	2630](#table7327csequence)
[Table F.34: RESTART Data – Solution Data Keyword for Tracer Concentration Name	2631](#table7337csequence)
[Table F.35: RESTART Data \- Solution Data Keywords	2636](#table7347csequence)
[Table F.36: RESTART Data – LGR Solution Data Keywords	2638](#table7357csequence)
[Table F.37: RFT Data File Format	2642](#table7367csequence)
[Table F.38: RFT Data File – Time and Date Keywords	2642](#table7377csequence)
[Table F.39: RFT Data File – Well and Connection Data Keyword	2644](#table7387csequence)
[Table F.40: RFT Data File – RFT Solution Data Keywords	2645](#table7397csequence)
[Table F.41: Enhanced SUMMARY File Keywords	2650](#table7407csequence)
[Table F.42: SUMMARY Index File Keywords \(Global\)	2653](#table7417csequence)
[Table F.43: SUMMARY Index File Keywords \(LGR\)	2654](#table7427csequence)
[Table F.44: SUMMARY Index File Keywords \(Commercial Simulator\)	2654](#table7437csequence)
[Table F.45: SUMMARY Data File Keywords	2656](#table7447csequence)
[Table F.46: SUMMARY Data File Keywords \(LGR\)	2657](#table7457csequence)

    - Overview
-

This section of the manual describes the various output files generated by OPM Flow and attempts to outline the format of the various files, in order for third party software to read and write these type of files. From the 2019\-04 release a substantial effort has been undertaken to make OPM Flow’s output files compatible with the commercial simulator’s output files. This compatibility enables OMP Flow to “restart” from the commercial simulator’s generated [RESTART](#-refheading-toc135629-1317547213) files as well as the commercial simulator to “restart” from the OPM Flow’s [RESTART](#-refheading-toc135629-1317547213) files.  Although, this might not be the case for all models, as restarting a simulation model from another simulators restart file is complicated and may not be possible in all cases. 
Where applicable, files written by OPM Flow can be loaded into OPM ResInsight post processing software for further analysis and for displaying the results. Please see section [Error: Reference source not found Error: Reference source not found](#22running-opm-flow-2019-04-from-the-command-line) for the various command line options for setting the output format type.
        - File Types
    -
-

OPM Flow, similar to the commercial simulator, writes out various files, some of which are used by post processing software \(OPM ResInsight\) and some that are directly used by the user, for example the \*.PRT file that contains various reports. Table A.1 summaries the various file formats and the status of the file formats currently supported by OPM Flow.
| File Type | Data Type | Description | OPM Flow Status |
| --- | --- | --- | --- |
| DATA | Input Data | DATA files contain the input data in ASCII format used to run OPM Flow. | Fully Supported, as outlined in the manual |
| DBG | Debug Data | This file contains ASCII developer debug output specific to OPM Flow, that is there no compatibility with the commercial simulator’s DBG file. | OPM Flow Specific |
| EGRID | Structure Data | EGRID files contain the structural information for the model via the [COORD](#-refheading-toc45757-719036256), [ZCORN](#-refheading-toc45757-7190362561), etc. keywords,  and employs the extensible [GRID](#-refheading-toc38674-784232322) format, which is more compact than the [GRID](#-refheading-toc38674-784232322) formatted files and is the only format supported by OPM Flow. The output for this file type must be requested via the [Error: Reference source not found](#6339gridfile-set-the-grid-file-output-options) in the [GRID](#-refheading-toc38674-784232322) section. The data is used in post\-processing software to view the grid and is not in itself used by OPM Flow. | Fully Supported |
| [GRID](#-refheading-toc38674-784232322) | Structure Data | This file type contains the structural information for the model via the [COORD](#-refheading-toc45757-719036256), [ZCORN](#-refheading-toc45757-7190362561), etc. keywords, and consists of two data formats: - The standard [GRID](#-refheading-toc38674-784232322) file format that contains only the active global cells. - The extended [GRID](#-refheading-toc38674-784232322) file format that contains \(1\) plus local grid refinements and local coarsening grid specifications. Neither of these two formats are currently supported by OPM Flow. | Not Supported |
| [INIT](#-refheading-toc45789-719036256) Index | Static Property Index | The [INIT](#-refheading-toc45789-719036256) index file type specifies and defines the format and data type written to the [INIT](#-refheading-toc45789-719036256) Data file. This file is not required by OPM Flow or OPM ResInsight to be able to read and write the [INIT](#-refheading-toc45789-719036256) data file. | Not Supported and Not Required |
| [INIT](#-refheading-toc45789-719036256) Data | Static Property Data | This file type contains static model properties, that is, - Grid property data: porosity \([PORO](#-refheading-toc45797-719036256) array\), permeability \([PERMX](#-refheading-toc45791-719036256), [PERMY](#-refheading-toc45793-719036256), and [PERMZ](#-refheading-toc45795-719036256)\), net\-to\-gross \([NTG](#-refheading-toc33334-784232322)\), etc. - Region allocation array data: [EQLNUM](#-refheading-toc73734-2752266063), [FIPNUM](#-refheading-toc77229-2752266063), [PVTNUM](#-refheading-toc68366-2752266063), [SATNUM](#-refheading-toc71136-2752266063), etc. - Fluid and rock property static data, including end\-point scaling arrays: [SGCR](#-refheading-toc20428-784232322), [SGL](#-refheading-toc22881-784232322), [SOWCR](#-refheading-toc30436-784232322), [PCW](#-refheading-toc84164-621662414), etc. - Fluid and rock property tables: [PVDG](#-refheading-toc104056-57619843), [PVTO](#-refheading-toc104062-57619843), [PCW](#-refheading-toc84164-621662414),  [SGFN](#-refheading-toc106868-335817223), [SWFN](#-refheading-toc106882-335817223), etc. In order to request this type of output see the [Error: Reference source not found](#6343init-activates-the-init-file-option) in the [GRID](#-refheading-toc38674-784232322) section. Activating this keyword results in both the [INIT](#-refheading-toc45789-719036256) static property index and data files being written out by the commercial simulator. OPM Flow only writes out this file as the index file is not required by OPM ResInsight. The data is used in post\-processing software to view the grid property data and is not in itself used by OPM Flow. | Fully Supported |
| LOG | Output File | The LOG file for the commercial simulator contains an ASCII copy of the output from the terminal. The file itself is not generated by the commercial simulator but by an auxiliary program, ECLRUN, that is used to call and execute all the commercial simulators. OPM Flow does not generate a LOG file; however, the file can be generated by using the Linux tee command, for example: flow CASENAME \\| tee CASENAME.LOG Which will copy the terminal output to the CASENAME.LOG file. Alternatively, one can use the OPMRUN, the Graphical User Interface \(“GUI”\) program for OPM Flow, that provides similar functionality to the commercial simulator’s auxiliary program. | OPM Flow Specific |
| PRT | Output File | This file contains ASCII user output reports specific to OPM Flow, although there is a strong desire to make the OPM Flow reports similar to those that are produced by the commercial simulator. | OPM Flow Specific |
| [RESTART](#-refheading-toc135629-1317547213) Index | Dynamic Solution Index | The [RESTART](#-refheading-toc135629-1317547213) index file type specifies and defines the format and data type written to the [RESTART](#-refheading-toc135629-1317547213) Data file. This file is not required by OPM Flow or OPM ResInsight to be able to read and write the [RESTART](#-refheading-toc135629-1317547213) data file. | Not Supported and Not Required |
| [RESTART](#-refheading-toc135629-1317547213) Data | Dynamic Solution Data | This file type contains dynamic solution data for each active cell in the model at the user requested time steps, that is, - Grid solution pressure and saturation data \([PRESSURE](#-refheading-toc135627-1317547213), [SGAS](#-refheading-toc137369-1317547213), [SOIL](#-refheading-toc137371-1317547213), and [SWAT](#-refheading-toc137373-1317547213)\). Note that Ternary saturations are normally computed by the post\-processing software. - Grid solution fluid property data \(GAS\_DEN, GAS\_VISC, OIL\-DENS, etc.\). The [RPTRST](#-refheading-toc210154-2884651453) and the [RPTSCHED](#-refheading-toc268459-1366622701) keywords in the [SCHEDULE](#-refheading-toc43945-784232322) defines the data and frequency of the data to be written to the [RESTART](#-refheading-toc135629-1317547213) file at each requested restart point. Activating this keyword results in both the [RESTART](#-refheading-toc135629-1317547213) index and data files being written out by the commercial simulator; OPM Flow only writes this file. In addition to the solution data, this file type also includes group and well configuration data \(number of connections, connections open and closed, etc.\) This information is required to ensure that the correct group and well configuration is available at a given time in order to be able to restart the simulation at a restart point. The data is used to visualize the simulation results of the model in two and three dimensional space using post\-processing software. The file is also used by OPM Flow to “restart” from a previous simulation case. | Fully Supported |
| RFT | Dynamic Wellbore Vector Data | Data written to the RFT file consists of wellbore vector data, for example, pressure and saturation versus wellbore depth at various time steps. The data written out is not restricted to just Repeat Formation Tester \(“RFT”\) data, but can contain any Production Logging Tool \(“PLT”\) data made available in the simulator.  Note that only the RFT data set is currently supported by OPM Flow. The keywords [WRFT](#-refheading-toc268467-1366622701) and [WRFTPLT](#-refheading-toc268469-1366622701) in the [SCHEDULE](#-refheading-toc43945-784232322) section are used to define the wells, data, and time step at which the data should be written to the RFT file. The data is used in post\-processing software to compare the actual wire line logging data with the simulation derived results. The file is not in itself used by OPM Flow. | Fully Supported \(RFT\) |
| RSM | Output File | The RSM file contains the variables requested to be written to the [SUMMARY](#-refheading-toc43949-784232322) file via the keywords described in the [Error: Reference source not found](#11summary-section), in a tabulated ASCII output format. The format of the file enables the data to be easily loaded into the LibreOffice Calc program for further processing, as each vector represents one column. The report is written at the end of the simulation run by parsing the [SUMMARY](#-refheading-toc43949-784232322) Index and [SUMMARY](#-refheading-toc43949-784232322) Data files. | Fully Supported |
| [SAVE](#-refheading-toc100040-3115110868) | Staic and Dynamic Data | [SAVE](#-refheading-toc100040-3115110868) files are basically a combination of both the [INIT](#-refheading-toc45789-719036256) and [RESTART](#-refheading-toc135629-1317547213) files, except for the static initialization data that also includes the processed data, e.g., [PORV](#-refheading-toc96547-718313858), [TRANX](#-refheading-toc93085-718313858), [TRANY](#-refheading-toc93087-718313858), [TRANZ](#-refheading-toc93089-718313858), etc. This enables “fast restarts” as the pore volumes and transmissibility arrays do not have to be re\-calculated in a “restart” run. This file type is currently not supported by OPM Flow. | Not Supported |
| [SUMMARY](#-refheading-toc43949-784232322) ESMRY | Dynamic Vector Data | This is an OPM FLOW specific Enhanced [SUMMARY](#-refheading-toc43949-784232322)  \(\*.ESMRY\) output file format that is optimized for fast loading of selected vectors by post\-processing applications. The \*.ESMRY file is re\-written for every time step and does not have a performance impact on the simulation. Load times are in the order of 30 times faster compared with fetching selected vectors using the \*.UNSMRY file format in post processing software. | Fully Supported |
| [SUMMARY](#-refheading-toc43949-784232322) Index | Dynamic Vector Index | The [SUMMARY](#-refheading-toc43949-784232322) index file type specifies and defines the format and data type written to the [SUMMARY](#-refheading-toc43949-784232322) Data file. | Fully Supported |
| [SUMMARY](#-refheading-toc43949-784232322) Data | Dynamic Vector Data | The [SUMMARY](#-refheading-toc43949-784232322) data file contains the variables requested to be written to the file via the keywords described in the [Error: Reference source not found](#11summary-section). The data consists of vectors that are used to generate line graphs of properties such as oil flow rate versus time, grid plot pressure versus time, etc. The properties to be stored on the [SUMMARY](#-refheading-toc43949-784232322) file are written to the summary file at the end of each successful time step. The data can be used to compare actual production data with the simulation derived results in post processing software. Note that although the file format is fully supported, not all of the [SUMMARY](#-refheading-toc43949-784232322) variables are are available. | Fully Supported |
| Notes: - All files can be written out in either ASCII or binary formats, except for DBG, LOG, PRT, and RSM files that are always written in ASCII format. - In addition, [SUMMARY](#-refheading-toc43949-784232322) and [RESTART](#-refheading-toc135629-1317547213) files can be loaded or written out in either unified or non\-unified formats. - File Type cells colored in gray indicate the output may be different to the commercial simulators equivalent file type.  File Type cells colored in orange represent file types that are not currently supported by OPM Flow. |  |  |  |

Table A.1: OPM Flow Output File Types Summary

As mentioned in Table A.1 all files can be written out in either ASCII or binary formats. In addition, the [SUMMARY](#-refheading-toc43949-784232322) and [RESTART](#-refheading-toc135629-1317547213) files can be loaded or written out in either unified or non\-unified formats.  The file type \(ASCII or binary\) and file structure format \(unified or non\-unified formats\) are set via various keywords in the [RUNSPEC](#-refheading-toc55591-1778172979) section, as outlined in Table A.2.

| Process | [RUNSPEC](#-refheading-toc55591-1778172979) Keyword | Description | Files |
| --- | --- | --- | --- |
| Input | [FMTIN](#-refheading-toc46649-1640804870) | The keyword defines the input files to be formatted as ASCII, i.e., text files, as oppose to binary files.  The input deck file is always of this type. The option relates to the OPM Flow derived files that are used as input, for example when restarting from another case. If the keyword is omitted then the default is for binary file input. | \*.FEGRID \*.FINSPEC \*.FINIT \*.FRSSPEC \*.FUNRST \*.FSMSPEC \*.FUNSMRY |
| [MULTIN](#-refheading-toc195177-1371377330) | A character string that defines the input files to be non\-unified multiple files, as opposed to unified files. In this case, one file is read in per  reporting time step, as opposed to all time steps reports being read from one file. If the keyword is omitted then the default is for one file per reporting time step. | \*.RSSPEC \*.X0001 \*.SMSPEC \*.S0001 |  |
| [UNIFIN](#-refheading-toc46653-1640804870) | [UNIFIN](#-refheading-toc46653-1640804870) defines the input files to be unified files, as opposed to non\-unified multiple files. A unified file is a single file containing output for each reporting time step.  For this option a single summary file and a single restart file will be read. If the keyword is omitted then the default is for one file per report time step. | \*.RSSPEC \*.UNRST \*.SMSPEC \*.UNSMRY |  |
| Output | [FMTOUT](#-refheading-toc46651-1640804870) | The keyword sets all output files to be formatted as ASCII i.e. text files, as opposed to binary files. The \*.DBG, \*.LOG, \*.PRT, and \*.RSM files are always of this type. The option relates to the OPM Flow output files only. In this case the files will be portable across operating systems, but will also be very large in terms of hard disk space. For this reason it is recommend that the default option is used so that only binary files are written out. If the keyword is omitted then the default is for binary file input. | \*.FEGRID \*.FINSPEC \*.FINIT \*.FRSSPEC \*.FUNRST \*.FSMSPEC \*.FUNSMRY |
| [MULTOUT](#-refheading-toc195175-1371377330) | A character string that defines the output files to be non\-unified multiple files, as opposed to unified files. In this case, one file is written for each reporting time step, as opposed to all time steps reports being written in one file. If the keyword is omitted then the default is for one file per reporting time step. | \*.RSSPEC \*.X0001 \*.SMSPEC \*.S0001 |  |
| [UNIFOUT](#-refheading-toc65809-1640804870) | [UNIFOUT](#-refheading-toc65809-1640804870) defines the output files to be unified files, as opposed to non\-unified multiple files. A unified file is a single file containing output for each reporting time step. Here a single summary file and a single restart file will be generated, as opposed to one file per report time step. If the keyword is omitted then the default is for one file per report time step . | \*.RSSPEC \*.UNRST \*.SMSPEC \*.UNSMRY |  |
| Notes: - A binary file is computer\-readable but not human\-readable. All executable programs are stored in binary files, as are most numeric data files. In contrast, text files are stored in a form \(usually ASCII\) that is human\-readable. - For unified files if the run terminates unexpectedly, or there is sufficient disk space, then the last report output is not stored.  The main advantage of unified files is that if a number of simulation cases reside in one directory, the number of output files per case is minimum compared to using non\-unified multiple files. There is no limit on the number of reporting steps that a unified file can store. |  |  |  |

Table A.2: RUNSPEC Input and Output File Format Keywords

        - File Naming Conventions
    -
-

OPM Flow automatically generates the file names based on the input file name and the output options selected via the keywords in the [RUNSPEC](#-refheading-toc55591-1778172979) summarized in Table A.2.  For example, the command line syntax for running OPM Flow is:
```eclipse

						flow [OPTIONS] CASENAME
```

and typing the following command from the terminal:
```eclipse
							flow CASENAME
```

will start the simulator and run the case specified by CASENAME.DATA. Here CASENAME is the “root” of the filename and DATA is the extension of the filename.  OPM Flow will generate the output files based on the CASENAME with the extension based on the type \(ASCII or binary\) and file structure format \(unified or non\-unified formats\), as outlined in Table A.3. Note that if CASENAME includes a relative or absolute path to the data file,  the run directory will be set so that all output files are generated in the directory holding the data file.

| File Type | Unformatted Extension | Description | Formatted Extension |
| --- | --- | --- | --- |
| DATA |  | Input data file. | \*.DATA |
| DBG |  | Output debug file. | \*.DBG |
| EGRID | \*.EGRID | EGRID files containing the structural grid data and is the only format supported by OPM Flow. This output for this file type must be requested via the [Error: Reference source not found](#6339gridfile-set-the-grid-file-output-options) in the [GRID](#-refheading-toc38674-784232322) section. | \*.FEGRID |
| [GRID](#-refheading-toc38674-784232322) | \*.GRID | Grid file in either the standard [GRID](#-refheading-toc38674-784232322) file format or the extended [GRID](#-refheading-toc38674-784232322) file format Neither of these two formats are currently supported by OPM Flow. | \*.FGRID |
| [INIT](#-refheading-toc45789-719036256) Index | \*.INSPEC | The [INIT](#-refheading-toc45789-719036256) index file for both unified and non\-unified formats | \*.FINSPEC |
| [INIT](#-refheading-toc45789-719036256) | \*.INIT | This file type contains static model properties. | \*.FINIT |
| LOG |  | Output log file that contains a copy of the output from the terminal.  The file itself is not generated by the commercial simulator but by an auxiliary program, ECLRUN, that is used to call and execute all the commercial simulators. | \*.LOG |
| PRT |  | Output print file. | \*.PRT |
| [RESTART](#-refheading-toc135629-1317547213) Index | \*.RSSPEC | The [RESTART](#-refheading-toc135629-1317547213) index file for both unified and non\-unified formats.  This file is not required by OPM Flow or OPM ResInsight to be able to read and write the [RESTART](#-refheading-toc135629-1317547213) data file. | \*.FRSSPEC |
| [RESTART](#-refheading-toc135629-1317547213) Data Non\-Unified | \*.Xnnnn | The [RESTART](#-refheading-toc135629-1317547213) data files containing the solution arrays requested to be written to the [RESTART](#-refheading-toc135629-1317547213) files. For example: CASENAME.X0001 CASENAME.X0002 CASENAME.X0003 etc. CASENAME.RSSPEC | \*.Fnnnn |
| [RESTART](#-refheading-toc135629-1317547213) Data Unified | \*.UNRST | The [RESTART](#-refheading-toc135629-1317547213) data file containing the solution arrays requested to be written to the [RESTART](#-refheading-toc135629-1317547213) file. For example: CASENAME.UNRST CASENAME.RSSPEC | \*.FUNRST |
| RFT | \*.RFT | The RFT data file containing wellbore vector data requested to be written to the RFT file. For example: CASENAME.RFT | \*.FRFT |
| RSM |  | Output RSM file. | \*.RSM |
| [SAVE](#-refheading-toc100040-3115110868) | \*.SAVE | The [SAVE](#-refheading-toc100040-3115110868) file type is currently not supported by OPM Flow. | \*.FSAVE |
| [SUMMARY](#-refheading-toc43949-784232322) ESMRY | \*.ESMRY | OPM Flow Enhanced [SUMMARY](#-refheading-toc43949-784232322)  \(\*.ESMRY\) output file format that is optimized for fast loading of selected vectors by post\-processing applications. Note that the [FMTOUT](#-refheading-toc46651-1640804870),  [MULTOUT](#-refheading-toc195175-1371377330), and [UNIFOUT](#-refheading-toc65809-1640804870) keywords have no impact on this file type. |  |
| [SUMMARY](#-refheading-toc43949-784232322) Index | \*.SMSPEC | The [SUMMARY](#-refheading-toc43949-784232322) index file for both unified and non\-unified formats. | \*.FSMSPEC |
| [SUMMARY](#-refheading-toc43949-784232322) Data Non\-Unified | \*.Snnnn | The [SUMMARY](#-refheading-toc43949-784232322) data files containing the variables requested to be written to the [SUMMARY](#-refheading-toc43949-784232322) files. For example: CASENAME.S0001 CASENAME.S0002 CASENAME.S0003 etc. CASENAME.SMSPEC | \*.Annnn |
| [SUMMARY](#-refheading-toc43949-784232322) Data Unified | \*.UNSMRY | The [SUMMARY](#-refheading-toc43949-784232322) data file containing the variables requested to be written to the [SUMMARY](#-refheading-toc43949-784232322) file. For example: CASENAME.UNSMRY CASENAME.SMSPEC | \*.FUNSMRY |
| Notes: - The above file naming convention is for Linux type operating systems, as OPM Flow is currently only officially supported for Linux distributions. - File Type cells colored in gray indicate the output may be different to the commercial simulators equivalent file type.  File Type cells colored in orange represent file types that are not supported by OPM Flow. - Formatted and Unformatted Extension cells colored in gray indicate the format is not available or not applicable. |  |  |  |

Table A.3: OPM Flow File Naming Conventions

        - Unformatted File Format Considerations
    -
-

Originally the commercial simulator was written in FORTRAN 77 and the current version is still written in a version of FORTRAN.   FORTRAN unformatted file output is dependent on the FORTRAN compiler used to generated the executable program. Typically an unformatted record consists of a four byte prefix outlining the length of the record in bytes, then the actual data record, followed by suffix containing the length of the record in bytes. Most but not all compilers use four bytes. This aids in reading records, for example, the four byte record size at the end of the record assists with a backspace operation.  If the record size is greater than two Gigabytes \(2^30 bytes\), the record is divide into sub\-records. In this case the sign bit of the prefix inform that the record is continued by a sub\-record or not and the sign bit of the suffix indicate whether or not there is a preceding sub record. 
OPM Flow unformatted files are written using the big\-endian mode, that is the most significant value in the sequence is stored at the lowest storage address, that is first.  This is opposite to the little\-endian mode, where the least significant value in the sequence is stored first. For example, consider the number 1025 \(2 to the tenth power plus one\) stored in a four byte integer:
```eclipse
00000000 00000000 00000100 00000001
```

| Address | **Big\-Endian repres****entation** **of 1025** | **Little****\-Endian repres****entation** **of 1025** |
| --- | --- | --- |
| 00 | 00000000 | 00000001 |
| 01 | 00000000 | 00000100 |
| 02 | 00000100 | 00000000 |
| 03 | 00000001 | 00000000 |

Table A.4: Big\-Endian and Little\-Endian Representation

OPM Flow is written in C\+\+ using the open source GNU C\+\+ compiler and therefore developers using C\+\+ need to ensure that unformatted files are read or written using the correct big\-endian mode. 

        - File Output Format
    -
-

All the files consist of a series of “header” keywords that defined various parameters based on their format type: integer, real, Boolean, double precision, and character. For example for the [INIT](#-refheading-toc45789-719036256) and [RESTART](#-refheading-toc135629-1317547213) files the header keywords are:
        - SEQNUM: Report time step keyword \([RESTART](#-refheading-toc135629-1317547213) file only\).
        - INTEHEAD: Integer \(four byte\) keyword that contains constant values for example, the dimensions of the model, as well as the location and length of data contained in the subsequent property keywords.
        - LOGIHEAD: Boolean or logical \(four byte\) keyword that consists of a set of either T \(true\) or F \(false\) character strings, for example, if dissolved gas is present in the model then set to T for true or F for false.
        - DOUBHEAD: Real double precision keyword \(eight byte\) that contains real values, for example, the current time step and [TUNING](#-refheading-toc146744-4203985108) keyword parameters. Note that the integer parameters on the [TUNING](#-refheading-toc146744-4203985108) keyword are stored in the INTEHEAD keyword data array.
    -
-

These are then followed by a series of “property” keywords that outline the various additional data. For the [RESTART](#-refheading-toc135629-1317547213) files the header keywords are repeated for each time step a [RESTART](#-refheading-toc135629-1317547213) record is written. There are also additional header keywords for Local Grid Refinements \(“LGR”\) that are repeated for each [LGR](#-refheading-toc55049-4106839650) and for time step. 
All the keywords follow the same format, including the property keywords, as outlined in Table A.5, which shows a portion of the INTEHEAD header keyword definition for the [RESTART](#-refheading-toc135629-1317547213) file.

| No. | Description | Output File Keyword Format |  |  | Status or Value |
| --- | --- | --- | --- | --- | --- |
|  | INTEHEAD | Global grid header keyword for the [RESTART](#-refheading-toc135629-1317547213) Data file that defines the  integer variables for this time step. NIHEAD is the number of entries associated with this keyword, and is dependent on the features being used in the model. Undefined values should be set to zero. |  |  | Required |
| 1\-1 | Format | INTEHEAD | NIHEAD | INTE |  |
| 2\-1 | Data | An encoded integer corresponding to the time the file was created. For files not originating from the commercial simulator, this value may be set to zero. |  |  | ISNUM |
| 2\-2 | Data | Simulator version, should be set to zero. |  |  | VERSION |
| 2\-3 | Data | Unit system used in the simulation, set to 1 for metric, 2 for field, and 3 for laboratory |  |  |  |
| 2\-4 | Data | Undefined. |  |  | 0 |
| Notes: - Rows shaded in gray indicate the start of a keyword. - Cells colored red in the No. column indicate that this item is either “Not Used” or “Undefined”. |  |  |  |  |  |

Table A.5: Output File Keyword Format

The row colored gray in the table specifies the start of a keyword definition and shows the format for the keyword \(INTEHEAD\) together with a description of the keyword. The next row, item 1\-1 in the No. column, outlines the format of the keyword, that is the keyword name \(INITHEAD\), the number of data entries for the keyword \(NIHEAD\), and the type of entries \(INTE for integers\). The next set of rows specify the individual data entries, for example, item 2\-3 in the No. column is the third integer value that declares the unit system for the file.  Note that Cells colored red in the No. column indicate that this item is either “Not Used” or “Undefined”. 
| Note Under the No. column in Table A.5 the count base is one \(offset one\), as per FORTRAN; however, in C\+\+ the base is zero \(offset zero\) and therefore C\+\+ programmers must subtract one from this column to obtain the correct reference. This reference adjustment should be applied to all references in this Appendix. OPM Flow is written in C\+\+, then developers should use offset zero in reviewing or modifying the code. |
| --- |

The Data Type variable in row 1\-1 in Table A.5 should have one of the following values:
        - CHAR for eight character words enclosed in single quotes \(ASCII character decimal 39\) for formatted output.
        - DOUB for double precision eight byte real values.
        - INTE for standard four byte integers.
        - LOGI for standard four byte Boolean \(logical\) values.
        - MESS keyword that has no associated data.
        - REAL for single precision four byte reals values.
    -
-

All keywords follow the same format including the property array like [PORO](#-refheading-toc45797-719036256) and [PRESSURE](#-refheading-toc135627-1317547213). So for example,  the INTEHEAD keyword would be like this in a typical formatted [RESTART](#-refheading-toc135629-1317547213) file:

```eclipse
 'INTEHEAD'         249 'INTE'
  -955283513      200400           2       -2345       -2345       -2345
       -2345       -2345          10          10           1         100
          10       -2345           7       -2345           0           1
           0           2           2           0           0           0
         110         108         109           3          97          93
       -2345       -2345          19          38          53       -2345
          97          93         146           5           0           1
          15          24           8           5           2           4
  ………………………….……………..
```

And the pressure and water saturation arrays would be of the same form in a typical formatted [RESTART](#-refheading-toc135629-1317547213) file:
```eclipse

 'PRESSURE'       44431 'REAL'
   0.26889725E+03   0.26838983E+03   0.26826810E+03   0.26820352E+03
   0.26814493E+03   0.26809378E+03   0.26807767E+03   0.26806363E+03
   0.26802625E+03   0.26798474E+03   0.26795001E+03   0.26791434E+03
   0.26787915E+03   0.26783920E+03   0.26777118E+03   0.26769208E+03         ………………………….……………..
 'SWAT    '       44431 'REAL'
   0.10500000E+00   0.10500000E+00   0.10500000E+00   0.10500000E+00
   0.10500000E+00   0.10500000E+00   0.10500000E+00   0.14000000E+00
   0.14000000E+00   0.14500000E+00   0.14500000E+00   0.14500000E+00
   0.14500000E+00   0.14500000E+00   0.16000000E+00   0.16000000E+00
………………………….……………..
```

Secondly, the No. Entries is the number of values following the keyword and as such cannot be used to determine the size of an array that is not associated with the grid, say for example the number of active connections in a well. Instead, the array size is given in another property keyword. In this case, the number of elements for each well in the IWEL property array is given in the INTEHEAD keyword as shown in Table A.6 \(see Table A.21 for a full description of the [RESTART](#-refheading-toc135629-1317547213) INTEHEAD keyword\).
| No. | keyword Name | [RESTART](#-refheading-toc135629-1317547213) Data \- Header keywords |  |  | Status or Value |
| --- | --- | --- | --- | --- | --- |
|  | INTEHEAD | Global grid header keyword for the [RESTART](#-refheading-toc135629-1317547213) Data file. |  |  | Required |
| 1\-1 | Format | INTEHEAD | NIHEAD | INTE |  |
| 2\-17 | Data | Number of wells in the model. |  |  | NWELLS |
| 2\-25 | Data | Number of values per well in the IWEL array \(default value is 97\). |  |  | NIWELZ |

Table A.6: INTEHEAD Keyword \- IWEL Example

Now if INTEHEAD\(17\) was equal to three and INTEHEAD\(5\) was equal to five then the IWEL property array for the three wells would have the data arranged as shown in Figure A.1.

Here the Items are the values affiliated with a specific well, and Pos\(ition\) is the actual position in the IWEL property array,  shown as gray boxes in Figure A.1.

Similarly for well connections and completions. In this case the maximum number of connections for all the wells is given in INTEHEAD\(18\) element and a well’s current number of connections is given via the IWEL\(5\) element in the IWEL property array \(see Table A.27 for a detailed description of the IWEL keyword\). 

Now if the number of wells equal two \(INTEHEAD\(17\)\) and INTEHEAD\(18\) is equal to four, that is the maximum number of connections is set to four, together with IWEL\(5\) equal to three for the first well and four for the second well,  the ICON property array for the two wells would have the data arranged as shown in Figure A.2.

Here the connection co\-ordinates are given by \(I, J, K\) and the actual position in the ICON array is shown in the gray colored boxes. Note that Well\-1 has the required maximum number of connections but the fourth connection has the default values of zero, as the IWEL\(5\) value for this well only has three active connections.
Note also that the number of data elements per connection in the ICON vector is given by NICONZ which is given by INTEHEAD\(33\) and that the size of the ICON vector is NICONZ x NCWMAX x NWELLS, where NCWMAX is set by INTEHEAD \(18\) and NWELLS by INTEHEAD\(17\). In the example, NICONZ was assumed to be three for illustrative purposes, while the actual value is a constant 25 in the most recent versions of the commercial simulator.  These arbitrary constants, like NICONZ, use to determine vector lengths, appear to be constant for various versions of the commercial simulator.
The following sections outline the format of the various individual files supported by OPM Flow, except for the DBG, LOG, PRT, and RSM ASCII format files.

    - EGRID - Model Structural Data for Irregular Corner-Point Grids File
-

EGRID files contain the structural information for the model via the [COORD](#-refheading-toc45757-719036256), [ZCORN](#-refheading-toc45757-7190362561), etc. keywords,  and employs the extensible [GRID](#-refheading-toc38674-784232322) format, which is more compact than the [GRID](#-refheading-toc38674-784232322) formatted files and is the only format supported by OPM Flow. 
The output for this file type must be requested via the [Error: Reference source not found](#6339gridfile-set-the-grid-file-output-options) in the [GRID](#-refheading-toc38674-784232322) section, as shown below:
```eclipse
--
--       GRID FILE OUTPUT OPTIONS
--       GRID    EGRID
--       OPTN    OPTN
GRIDFILE
         0       1                                                             /
```

The above example defines that no [GRID](#-refheading-toc38674-784232322) file will be written out and that the extensible [GRID](#-refheading-toc38674-784232322) \(that is the EGRID geometry format\) file will be produced.  This is the only configuration that OPM Flow supports.
The [FMTIN](#-refheading-toc46649-1640804870) and [FMTOUT](#-refheading-toc46651-1640804870) keywords in the [RUNSPEC](#-refheading-toc55591-1778172979) section defines the input and output files to be formatted as ASCII i.e. text files, \(\*.FEGRID\), as oppose to unformatted binary files \(\*.EGRID\).  If these keywords are omitted then the default is for unformatted binary file input.
The EGRID file structure consists of a series header keywords that define the header keyword data type, the number of data entries, and then the associated header keyword data.  There are a total of four major keyword header types for this file type: \(1\) File Header, \(2\) Global Grid Header, \(3\) Local Grid Refinement Header1
       Several keywords are used for both global and [LGR](#-refheading-toc55049-4106839650) grids, for example the GRIDHEAD,  [COORD](#-refheading-toc45757-719036256), [*ZCORN*](#-refheading-toc45757-7190362561) keywords. \(repeated for each local grid refinement in the model\), and \(4\) Non\-Neighbor Connection Header. 
In addition to the structural data, this file type also contains information describing the geometry relationship between the global grid and any Local Grid Refinements \(“LGR”\) that are present in the model, together with the Non\-Neighbor Connections \(“NNC”\) that may be present due to structural discontinuities. The overall structure of this file is is outlined in Table A.7

| Reference | Section | Global Section keywords | Global Data keywords | [LGR](#-refheading-toc55049-4106839650) Section keywords | [LGR](#-refheading-toc55049-4106839650) Data keywords | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| A.2.1 |  | FILEHEAD [MAPUNITS](#-refheading-toc39962-2479612490) [MAPAXES](#-refheading-toc39960-2479612490) [GRIDUNIT](#-refheading-toc41568-2479612490) [GDORIENT](#-refheading-toc45783-719036256) |  |  |  | EGRID header keyword that defines various Global Grid properties. |
| A.2.2 |  | GRIDHEAD | [COORD](#-refheading-toc45757-719036256) |  |  | EGRID global irregular corner point grid keyword that defines the grid geometry. |
| [ZCORN](#-refheading-toc45757-7190362561) |  |  |  |  |  |  |
| etc. |  |  |  |  |  |  |
| A.2.2 |  | ENDGRID |  |  |  | Marks the end of the EGRID global irregular corner point grid keyword. |
| A.2.3 |  |  |  | [LGR](#-refheading-toc55049-4106839650) LGRPARNT LGRSGRID |  | EGRID [LGR](#-refheading-toc55049-4106839650) irregular corner point grid keyword that defines the [LGR](#-refheading-toc55049-4106839650) name and optionally the nested or parent LGRs associated with this [LGR](#-refheading-toc55049-4106839650). |
| A.2.3 |  |  |  | GRIDHEAD | [COORD](#-refheading-toc45757-719036256) | EGRID [LGR](#-refheading-toc55049-4106839650) irregular corner point grid keyword that defines the grid geometry. |
| [ZCORN](#-refheading-toc45757-7190362561) |  |  |  |  |  |  |
| etc. |  |  |  |  |  |  |
| A.2.3 |  |  |  | ENDGRID |  | Marks the end of the EGRID [LGR](#-refheading-toc55049-4106839650) irregular corner point grid keyword. |
| A.2.3 |  |  |  | ENDLGR |  | Sets the end of current [LGR](#-refheading-toc55049-4106839650) section. |
| A.2.3 |  |  |  | [LGR](#-refheading-toc55049-4106839650) LGRPARNT LGRSGRID |  | EGRID [LGR](#-refheading-toc55049-4106839650) irregular corner point grid keyword that defines the [LGR](#-refheading-toc55049-4106839650) name and optionally the nested or parent LGRs associated with this [LGR](#-refheading-toc55049-4106839650) |
| A.2.3 |  |  |  | GRIDHEAD | [COORD](#-refheading-toc45757-719036256) | EGRID [LGR](#-refheading-toc55049-4106839650) irregular corner point grid keyword that defines the grid geometry. |
| [ZCORN](#-refheading-toc45757-7190362561) |  |  |  |  |  |  |
| etc. |  |  |  |  |  |  |
| A.2.3 |  |  |  | ENDGRID |  | End of the EGRID [LGR](#-refheading-toc55049-4106839650) grid section. |
| A.2.3 |  |  |  | ENDLGR |  | Sets the end of current [LGR](#-refheading-toc55049-4106839650) section. |
| A.2.4 |  | NNCHEAD | NNC1 |  |  | EGRID Global Non\-Neighbor Connections for Irregular Corner Point Grid keywords. |
| NNC2 |  |  |  |  |  |  |
| A.2.4 |  |  |  | NNCHEAD | NNC1 | First [LGR](#-refheading-toc55049-4106839650) EGRID global and local non\-neighbor connections for irregular corner point grid keywords. |
| NNC2 |  |  |  |  |  |  |
| NNCL |  |  |  |  |  |  |
| NNCG |  |  |  |  |  |  |
| A.2.4 |  |  |  | NNCHEAD | NNC1 | Second [LGR](#-refheading-toc55049-4106839650) EGRID global and local non\-neighbor connections for irregular corner point grid keywords. |
| NNC2 |  |  |  |  |  |  |
| NNCL |  |  |  |  |  |  |
| NNCG |  |  |  |  |  |  |
| A.2.4 |  |  |  | NNCHEADA | NNA1 | EGRID amalgamated and local non\-neighbor connections for irregular corner point grid keywords. |
| NNA2 |  |  |  |  |  |  |
| Notes: - Cells shaded in gray indicate the combination is not applicable and cells colored orange indicate that this item is not currently supported by OPM Flow. |  |  |  |  |  |  |

Table A.7: EGRID \- Model Structural Data for Irregular Corner\-Point Grids

Each major header keyword is subdivided into a series of sub\-header keywords that define a particular data set. The general format for a header keyword is the keyword \(enclosed in single quotes\), followed by the number of data entries \(an integer value\), followed by the data type which is set to CHAR, INTE, or REAL \(enclosed in quotes\).  This will then be followed by the data for the keyword.
The following sections describe the format of the various keywords and the associated data sets.

        - EGRID Header Keywords
    -
-

The FILEHEAD keyword defines the key attributes of the file via a series of integer constants, this is then followed by the [MAPUNITS](#-refheading-toc39962-2479612490), [MAPAXES](#-refheading-toc39960-2479612490), [GRIDUNIT](#-refheading-toc41568-2479612490), and [GDORIENT](#-refheading-toc45783-719036256) keywords and their data sets. Note that some keywords are optional and are not used by OPM Flow per se, but are used by pre\- and post processing software. Secondly, some features are not supported by OPM Flow, for example local grid refinements, and thus OPM will not write out the data associated with these features.
Table A.8 outlines the structure of the EGRID Header Keywords and their affiliated data. 
| No. | Keyword Name | EGRID Header Keyword Table A.8 |  |  | Status or Value |
| --- | --- | --- | --- | --- | --- |
|  | FILEHEAD | This keyword marks the start of the EGRID file and defines various parameters associated with this file type. |  |  | Required |
| 1\-1 | Format | FILEHEAD | 100 | INTE |  |
| 2\-1 | Data | Version number for this file type, for example 3. |  |  | 3 |
| 2\-2 | Data | The year this version of the file format was released, for example 2004. |  |  | 2004 |
| 2\-3 | Data | Not used. |  |  |  |
| 2\-4 | Data | Version number of earliest this file format is supported, normally set to 0. |  |  | 0 |
| 2\-5 | Data | Type of grid, set to 0 for Irregular Corner\-Point Grids, 1 for Unstructured Grids, or 2 for a mixture of Irregular Corner\-Point and Unstructured Grids \(Mixed Grids\). |  |  | 0 |
| 2\-6 | Data | Type of rock model, set to 0 for a single porosity/permeability rock model, 1 for dual porosity rock model, or 3 for a dual permeability rock model. |  |  | 0 |
| 2\-7 | Data | Original grid format, set to 0 for unknown, 1 for Irregular Corner\-Point Grids, or 2 for Cartesian Regular Grids. |  |  |  |
| 2\-8 to 2\-100 | Data | Not used |  |  | 0 |
|  | [MAPUNITS](#-refheading-toc39962-2479612490) | This keyword defines the [MAPUNITS](#-refheading-toc39962-2479612490). |  |  | Optional |
| 1\-1 | Format | [MAPUNITS](#-refheading-toc39962-2479612490) | 1 | CHAR |  |
| 2\-1 | Data | The units of the map data, normally set to FEET or METRES. |  |  |  |
|  | [MAPAXES](#-refheading-toc39960-2479612490) | The [MAPAXES](#-refheading-toc39960-2479612490) keyword defines the grid position relative to the map coordinates. The six values in the data fields define the relative map \(x, y\) coordinates for three locations to enable conversion from grid to map coordinate in pre\- and post processing software. |  |  | Optional |
| 1\-1 | Format | [MAPAXES](#-refheading-toc39960-2479612490) | 6 | REAL |  |
| 2\-1 | Data | X\-coordinate on the y\-axis located at the end of the y\-axis. |  |  |  |
| 2\-2 | Data | Y\-coordinate on the y\-axis located at the end of the y\-axis. |  |  |  |
| 2\-3 | Data | X\-coordinate at the origin. |  |  |  |
| 2\-4 | Data | Y\-coordinate at the origin. |  |  |  |
| 2\-5 | Data | X\-coordinate on the x\-axis located at the end of the x\-axis. |  |  |  |
| 2\-6 | Data | Y\-coordinate on the x\-axis located at the end of the x\-axis. |  |  |  |
|  | [GRIDUNIT](#-refheading-toc41568-2479612490) | The [GRIDUNIT](#-refheading-toc41568-2479612490) keyword defines units of the [COORD](#-refheading-toc45757-719036256) and [ZCORN](#-refheading-toc45757-7190362561) arrays and the grid coordinate space |  |  | Required |
| 1\-2 | Format | [GRIDUNIT](#-refheading-toc41568-2479612490) | 2 | CHAR |  |
| 2\-1 | Data | The first entry defines units of the [COORD](#-refheading-toc45757-719036256) and [ZCORN](#-refheading-toc45757-7190362561) arrays and should be normally set to FEET or METRES \(enclosed in single quotes\). |  |  |  |
| 2\-2 | Data | The second entry defines the grid coordinate space \(MAP or MAPFT if [COORD](#-refheading-toc45757-719036256) and [ZCORN](#-refheading-toc45757-7190362561) are defined in map coordinates, or blank if in grid coordinates \(‘         ’\). |  |  |  |
|  | [GDORIENT](#-refheading-toc45783-719036256) | Grid orientation keyword defines the property ordering in the I, J, and K dimensions, the direction of the Z\-direction, and the “handedness of the grid. |  |  | Optional |
| 1\-1 | Format | [GDORIENT](#-refheading-toc45783-719036256) | 5 | CHAR |  |
| 2\-1 | Data | Define the property ordering in the I dimension \(set to either INC for increasing or DEC for decreasing\). |  |  |  |
| 2\-2 | Data | Define the property ordering in the J dimension \(set to either INC for increasing or DEC for decreasing\). |  |  |  |
| 2\-3 | Data | Define the property ordering in the K dimension \(set to either INC for increasing or DEC for decreasing\). |  |  |  |
| 2\-4 | Data | Declare the direction of the Z\-direction, should be set to either UP or DOWN. |  |  |  |
| 2\-5 | Data | Set the “handedness of the grid., should be set to either LEFT or RIGHT. |  |  |  |
| Notes: - Rows shaded in gray indicate the start of a keyword. - Cells colored orange in the No. column indicate that this item is not supported by OPM Flow and those colored red are either “Not Used” or “Undefined”. - For formatted output all character variables, including the keywords should be enclosed in single quotes, for example the FILEHEAD keyword should be written out as ‘FILEHEAD’. - [GDORIENT](#-refheading-toc45783-719036256) keyword in the [GRID](#-refheading-toc38674-784232322) section is not supported by OPM Flow. |  |  |  |  |  |

Table A.8: EGRID Header Keywords

#### <a id="-refheading-toc716937-3964674244"></a>Example: EGRID Header Keywords

The following example shows a typical formatted file EGRID header keyword data set taken from the Norne model.
```eclipse
 'FILEHEAD'         100 'INTE'
           3        2004           0           0           0           0
           0           0           0           0           0           0
           0           0           0           0           0           0
           0           0           0           0           0           0
           0           0           0           0           0           0
           0           0           0           0           0           0
           0           0           0           0           0           0
           0           0           0           0           0           0
           0           0           0           0           0           0
           0           0           0           0           0           0
           0           0           0           0           0           0
           0           0           0           0           0           0
           0           0           0           0           0           0
           0           0           0           0           0           0
           0           0           0           0           0           0
           0           0           0           0           0           0
           0           0           0           0
 'MAPAXES '           6 'REAL'
   0.00000000E+00   0.10000000E+03   0.00000000E+00   0.00000000E+00
   0.10000000E+03   0.00000000E+00
 'GRIDUNIT'           2 'CHAR'
 'METRES  ' '        '
```

Note that the [GDORIENT](#-refheading-toc45783-719036256) keyword is not written out.

        - EGRID Global Irregular Corner Point Grid Keywords
    -
-

Following the EGRID Header Keyword data set, the EGRID Global Irregular Corner Point Grid Keywords should be read or written to the EGRID file. This data set includes the actual structural data for the model, that is the [COORD](#-refheading-toc45757-719036256) and [ZCORN](#-refheading-toc45757-7190362561) keyword data, as well as the [ACTNUM](#-refheading-toc4410-421927891) keyword data that defines if a given cell is active \(set to 1\), or inactive \(set to zero\).  The structure for this type data is defined in Table A.9.
| No. | keyword Name | EGRID Global Irregular Corner Point Grid Keywords Table A.9 |  |  |  | Status or Value |
| --- | --- | --- | --- | --- | --- | --- |
|  | GRIDHEAD | Global grid keyword that defines the start of this keyword type. |  |  |  | Required |
| 1\-1 | Format | GRIDHEAD | 100 |  | INTE |  |
| 2\-1 | Data | Type of grid, set to 0 for a mixture of Irregular Corner\-Point and Unstructured Grids, 1 for Irregular Corner\-Point Grids, and 2 for Unstructured Grids. Only the default value of one is supported by OPM Flow. |  |  |  | 1 |
| 2\-2 | Data | The number of grid blocks in the x\-direction \(NX\). |  |  |  |  |
| 2\-3 | Data | The number of grid blocks in the y\-direction \(NY\). |  |  |  |  |
| 2\-4 | Data | The number of grid blocks in the z\-direction \(NZ\). |  |  |  |  |
| 2\-5 | Data | The grid reference number set to zero for the global grid or a value greater than zero to represent a [LGR](#-refheading-toc55049-4106839650). For example if there are five [LGR](#-refheading-toc55049-4106839650)’s, then this complete data set is repeated six times, once for the global grid, and five times for the five LGRs., with the first [LGR](#-refheading-toc55049-4106839650) having a reference number of 1 and the last [LGR](#-refheading-toc55049-4106839650) having a reference number of 5. |  |  |  |  |
| 2\-6 to 2\-24 | Data | Not used. |  |  |  | 0 |
| 2\-25 | Data | [NUMRES](#-refheading-toc81021-4106839650) the number of reservoirs, that is the number of [COORD](#-refheading-toc45757-719036256) data sets to be processed by OPM Flow. This should be set to one as the only value supported by OPM Flow |  |  |  | 1 |
| 2\-26 | Data | NSEG the number of coordinate line segments, should be set to 1. |  |  |  | 1 |
| 2\-27 | Data | Cartesian/Radial grid indicator set to 0 for Cartesian grids and greater than zero for radial grids. Currently OPM Flow does not support radial geometries so this value should always be set to zero. |  |  |  | 0 |
| 2\-28 | Data | The [LGR](#-refheading-toc55049-4106839650) location of the lower I\-index [LGR](#-refheading-toc55049-4106839650) in the global grid.  This value should be set to zero if there is no [LGR](#-refheading-toc55049-4106839650) grids. |  |  |  | 0 |
| 2\-29 | Data | The [LGR](#-refheading-toc55049-4106839650) location of the lower J\-index [LGR](#-refheading-toc55049-4106839650) in the global grid.  This value should be set to zero if there is no [LGR](#-refheading-toc55049-4106839650) grids. |  |  |  | 0 |
| 2\-30 | Data | The [LGR](#-refheading-toc55049-4106839650) location of the lower K\-index [LGR](#-refheading-toc55049-4106839650) in the global grid.  This value should be set to zero if there is no [LGR](#-refheading-toc55049-4106839650) grids. |  |  |  | 0 |
| 2\-31 | Data | The [LGR](#-refheading-toc55049-4106839650) location of the upperI \-index [LGR](#-refheading-toc55049-4106839650) in the global grid.  This value should be set to zero if there is no [LGR](#-refheading-toc55049-4106839650) grids. |  |  |  | 0 |
| 2\-32 | Data | The [LGR](#-refheading-toc55049-4106839650) location of the upper J\-index [LGR](#-refheading-toc55049-4106839650) in the global grid.  This value should be set to zero if there is no [LGR](#-refheading-toc55049-4106839650) grids. |  |  |  | 0 |
| 2\-33 | Data | The [LGR](#-refheading-toc55049-4106839650) location of the uper K\-index [LGR](#-refheading-toc55049-4106839650) in the global grid.  This value should be set to zero if there is no [LGR](#-refheading-toc55049-4106839650) grids. |  |  |  | 0 |
| 2\-34 to 2\-100 | Data | Not used by OPM Flow. |  |  |  | 0 |
|  | BOXORIG | Not supported. |  |  |  | Optional |
| 1\-1 | Format | BOXORIG | 3 |  | INTE |  |
| 2\-1 to 2\-3 | Data | Ignored by OPM Flow. |  |  |  |  |
|  | [COORD](#-refheading-toc45757-719036256) | Property keyword that defines the start of the [COORD](#-refheading-toc45757-719036256) data set. The [COORD](#-refheading-toc45757-719036256) data defines a set of coordinate lines or pillars for a reservoir grid via an array.  The number of data values for this keyword should be 6 x \(NX\+1\) x \(NY\+1\) x [NUMRES](#-refheading-toc81021-4106839650). Where [NUMRES](#-refheading-toc81021-4106839650) represents the number of separate coordinate lines \(or reservoirs\). In OPM Flow [NUMRES](#-refheading-toc81021-4106839650) can only be set to one. |  |  |  | Required |
| 1\-1 | Format | [COORD](#-refheading-toc45757-719036256) | 6 x \(NX\+1\) x \(NY\+1\) |  | REAL |  |
| 2\-1 | Data | [COORD](#-refheading-toc45757-719036256) data in the same format as the [COORD](#-refheading-toc45757-719036256) keyword described in the [GRID](#-refheading-toc38674-784232322) section of the manual. |  |  |  |  |
|  | [COORDSYS](#-refheading-toc45759-719036256) | Coordinate definitions for each [NUMRES](#-refheading-toc81021-4106839650) reservoir. The number of data values for this keyword should be 6 x [NUMRES](#-refheading-toc81021-4106839650). Where [NUMRES](#-refheading-toc81021-4106839650) represents the number of separate coordinate lines \(or reservoirs\). In OPM Flow [NUMRES](#-refheading-toc81021-4106839650) can only be set to one. |  |  |  | Optional |
| 1\-1 | Format | [COORDSYS](#-refheading-toc45759-719036256) |  | 6 | INTE |  |
| 2\-1 to 2\-6 | Data | Ignored by OPM Flow. |  |  |  |  |
|  | [ZCORN](#-refheading-toc45757-7190362561) | Property keyword that defines the start of the [ZCORN](#-refheading-toc45757-7190362561) data set. [ZCORN](#-refheading-toc45757-7190362561) defines the depth of each corner point of a grid block on the pillars defining the reservoir grid. The number of data values for this keyword should be 8 x NX x NY x NZ. |  |  |  | Required |
| 1\-2 | Format | [ZCORN](#-refheading-toc45757-7190362561) |  | 8 x NX x NY x NZ | REAL |  |
| 1\-3 | Type | Type of data in the Data fields. |  |  |  |  |
| 2\-1 | Data | [ZCORN](#-refheading-toc45757-7190362561) data in the same format as the [ZCORN](#-refheading-toc45757-7190362561) keyword described in the [GRID](#-refheading-toc38674-784232322) section of the manual. |  |  |  |  |
|  | [ACTNUM](#-refheading-toc4410-421927891) | Property keyword that defines the start of the [ACTNUM](#-refheading-toc4410-421927891) data set. [ACTNUM](#-refheading-toc4410-421927891) specifies which grid blocks are active or inactive. A value of 1 indicates the block is active and a value of 0 indicates the block is inactive. Although this data set status is set to Optional, it is normally always written out by pre\-processing software. The number of data values for this keyword should be NX x NY x NZ integer values. |  |  |  | Optional |
| 1\-1 | Format | [ACTNUM](#-refheading-toc4410-421927891) |  | NX x NY x NZ | INTE |  |
| 2\-1 | Data | [ACTNUM](#-refheading-toc4410-421927891) data in the same format as the [ACTNUM](#-refheading-toc4410-421927891) keyword described in the [GRID](#-refheading-toc38674-784232322) section of the manual. |  |  |  |  |
|  | CORSNUM | Property keyword that defines the start of the CORSNUM data set for when the grid has been coarsened. The number of data values for this keyword should be NX x NY x NZ integer values. Grid coarsening is currently not supported in OPM Flow. |  |  |  | Optional |
| 1\-1 | Format | CORSNUM |  | NX x NY x NZ | INTE |  |
| 2\-1 | Data | CORSNUM data set. |  |  |  |  |
| 1\-1 | ENDGRID | The ENDGRID keyword marks the end of the these set of keywords. Always set to 0 to indicate that there is no data section following this keyword. |  |  |  | Required |
| 1\-2 | Format | ENDGRID |  | 0 | INTE | 0 |
| Notes: - Rows shaded in gray indicate the start of a keyword. - Cells colored orange in the No. column indicate that this item is not supported by OPM Flow and those colored red are either “Not Used” or “Undefined”. - For formatted output all character variables, including the keywords, should be enclosed in single quotes, for example the GRIDHEAD keyword should be written out as ‘GRIDHEAD’. |  |  |  |  |  |  |

Table A.9: EGRID Global Irregular Corner Point Grid Keywords

#### <a id="-refheading-toc716939-3964674244"></a>Example: EGRID Global Irregular Corner Point Grid Keywords

The following example shows a typical formatted EGRID Global Irregular Corner Point Grid Keywords data set, taken from the Norne model.
```eclipse
'GRIDHEAD'         100 'INTE'
           1          46         112          22           0           0
           0           0           0           0           0           0
           0           0           0           0           0           0
           0           0           0           0           0           0
           1           1           0           0           0           0
           0           0           0           0           0           0
           0           0           0           0           0           0
           0           0           0           0           0           0
           0           0           0           0           0           0
           0           0           0           0           0           0
           0           0           0           0           0           0
           0           0           0           0           0           0
           0           0           0           0           0           0
           0           0           0           0           0           0
           0           0           0           0           0           0
           0           0           0           0           0           0
           0           0           0           0
 'COORD   '       31866 'REAL'
   0.45311400E+06   0.73199210E+07   0.30374729E+04   0.45311400E+06
   0.73199210E+07   0.31328311E+04   0.45315503E+06   0.73198400E+07
   0.29839331E+04   0.45314275E+06   0.73198640E+07   0.31735720E+04
   0.45319609E+06   0.73197590E+07   0.30059690E+04   0.45317150E+06
   0.73198075E+07   0.32158359E+04   0.45323716E+06   0.73196780E+07
   0.30002649E+04   0.45320025E+06   0.73197510E+07   0.32172500E+04
   0.45327819E+06   0.73195970E+07   0.29893479E+04   0.45322903E+06
   0.73196940E+07   0.32139509E+04   0.45331925E+06   0.73195165E+07
………………………….……………..
 'ZCORN   '      906752 'REAL'
   0.30374729E+04   0.29839331E+04   0.29839331E+04   0.30059690E+04
   0.30059690E+04   0.30002649E+04   0.30002649E+04   0.29893479E+04
   0.29893479E+04   0.29956799E+04   0.29956799E+04   0.30008550E+04
   0.30008550E+04   0.30052520E+04   0.30052520E+04   0.30308621E+04
   0.30308621E+04   0.30368701E+04   0.30368701E+04   0.30380171E+04
   0.30380171E+04   0.30450271E+04   0.30450271E+04   0.30554099E+04
   0.30554099E+04   0.30665410E+04   0.30665410E+04   0.30766240E+04
   0.30766240E+04   0.30869380E+04   0.30869380E+04   0.30961531E+04
………………………….……………..
 'ACTNUM  '      113344 'INTE'
           0           0           0           0           0           0
           0           0           0           0           0           0
           0           0           0           0           0           0
           0           0           0           0           0           0
           0           0           0           0           0           0
           0           0           0           0           0           0
           0           0           0           0           0           0
           0           0           0           0           0           0
           0           0           0           0           0           0
           0           0           0           0           0           0
………………………….……………..
 'ENDGRID '           0 'INTE'
```

End of Example
        - EGRID LGR Irregular Corner Point Grid Keywords
    -
-

The data structure for Local Grid Refinement \(“LGR”\) Irregular Corner Point Grids is similar to the global grid format described in the previous section. Additional data that defines the [LGR](#-refheading-toc55049-4106839650) properties \([LGR](#-refheading-toc55049-4106839650) Name for example\) are included in this definition and the [LGR](#-refheading-toc55049-4106839650) keywords are repeated for each [LGR](#-refheading-toc55049-4106839650) in the model. The keyword description is outlined in Table A.10. 
Note that currently OPM Flow does not support [LGR](#-refheading-toc55049-4106839650) grids and therefore this series of keywords cannot be used by OPM Flow.
| No. | Keyword Name | EGRID [LGR](#-refheading-toc55049-4106839650) Irregular Corner Point Grid Keywords Table A.10 \(Repeated for Each [LGR](#-refheading-toc55049-4106839650) in the Model\) |  |  | Status or Value |
| --- | --- | --- | --- | --- | --- |
|  | [LGR](#-refheading-toc55049-4106839650) | [LGR](#-refheading-toc55049-4106839650) keyword defines the start of the [LGR](#-refheading-toc55049-4106839650) section of keywords and is required when LGRs are in the model. |  |  | Required |
| 1\-1 | Format | [LGR](#-refheading-toc55049-4106839650) | 1 | CHAR |  |
| 2\-1 | Data | Name of the [LGR](#-refheading-toc55049-4106839650) |  |  |  |
|  | LGRPARNT | Start of LGRPARNT keyword that defines the parent [LGR](#-refheading-toc55049-4106839650) for when nested [LGR](#-refheading-toc55049-4106839650) have been used. |  |  | Optional |
| 1\-1 | Format | LGRPARNT | 1 | CHAR |  |
| 2\-1 | Data | Name of parent [LGR](#-refheading-toc55049-4106839650) |  |  |  |
|  | LGRSGRID | Start of the LGRSGRID keyword for LGRs parented from a sub\-grid. |  |  | Optional |
| 1\-1 | Format | LGRSGRID | 1 | CHAR |  |
| 2\-1 | Data | Name of parent [LGR](#-refheading-toc55049-4106839650) |  |  |  |
|  | GRIDHEAD | [LGR](#-refheading-toc55049-4106839650) grid keyword that defines the start of this keyword type for the [LGR](#-refheading-toc55049-4106839650). The format is the same as the Global grid keyword \- see Table A.9. |  |  | Required |
|  | BOXORIG | Not supported. The format is the same as the Global grid keyword \- see Table A.9. |  |  | Optional |
|  | [COORD](#-refheading-toc45757-719036256) | Property keyword that defines the start of the [LGR](#-refheading-toc55049-4106839650) [COORD](#-refheading-toc45757-719036256) data set. The [COORD](#-refheading-toc45757-719036256) data defines a set of coordinate lines or pillars for [LGR](#-refheading-toc55049-4106839650) grid via an array. The format is the same as the Global grid keyword \- see Table A.9. |  |  | Required |
|  | [COORDSYS](#-refheading-toc45759-719036256) | Coordinate definitions for the [LGR](#-refheading-toc55049-4106839650). The format is the same as the Global grid keyword \- see Table A.9. |  |  | Optional |
|  | [ZCORN](#-refheading-toc45757-7190362561) | Property keyword that defines the start of the [LGR](#-refheading-toc55049-4106839650) [ZCORN](#-refheading-toc45757-7190362561) data set. The format is the same as the Global grid keyword \- see Table A.9. |  |  | Required |
|  | [ACTNUM](#-refheading-toc4410-421927891) | Property keyword that defines the start of the [LGR](#-refheading-toc55049-4106839650) [ACTNUM](#-refheading-toc4410-421927891) data set. The format is the same as the Global grid keyword \- see Table A.9. |  |  | Optional |
|  | HOSTNUM | Property keyword that defines the start of the HOSTNUM data set. which is only applicable to [LGR](#-refheading-toc55049-4106839650) grids. Number of data values for this keyword should be NX x NY x NZ integer values. |  |  | Required |
| 1\-1 | Format | HOSTNUM | NX x NY x NZ | INTE |  |
| 2\-1 | Data | HOSTNUM data set. |  |  |  |
|  | ENDGRID | The ENDGRID keyword marks the end of the [LGR](#-refheading-toc55049-4106839650) Grid Header section. Always set to 0 to indicate that there is no Data section for this keyword. |  |  | Required |
| 1\-1 | Format | ENDGRID | 0 | INTE | 0 |
|  | ENDLGR | ENDLGR keyword marks the end of the [LGR](#-refheading-toc55049-4106839650) Header section. Always set to 0 to indicate that there is no Data section for this keyword. |  |  | Required |
| 1\-1 | Format | ENDLGR | 0 | INTE | 0 |
| Notes: - Rows shaded in gray indicate the start of a keyword. - Cells colored orange in the No. column indicate that this item is not supported by OPM Flow. - For formatted output all character variables, including the keywords, should be enclosed in single quotes, for example the [LGR](#-refheading-toc55049-4106839650) keyword should be written out as ‘LGR     ’. |  |  |  |  |  |

Table A.10: EGRID LGR Irregular Corner Point Grid Keywords

Note that this data set is repeated for each [LGR](#-refheading-toc55049-4106839650) in the model as demonstrated in the following example.

#### <a id="-refheading-toc716941-3964674244"></a>Example: EGRID LGR Irregular Corner Point Grid Keywords

The following example shows a typical formatted data set for this series of keywords with two Cartesian [LGR](#-refheading-toc55049-4106839650) grids, named LGR\-1 and LGR\-2 define via the following [CARFIN](#-refheading-toc150726-63720426) keyword statements:
```eclipse
--
--       CARFIN LGR GRID COMMANDS
--
--       LGR        ----- FINE GRID ------   -- CARFIN GRID --  MAX     HOST
--       NAME       I1  I2  J1  J2  K1  K2     NX    NY    NZ   WELLS   NAME
CARFIN
        'LGR-1'      2   2   2   2   1   1      2     2      2     1    GLOBAL / CARFIN LGR GRID PARAMETERS

--
--       CARFIN LGR GRID COMMANDS
--
--       LGR        ----- FINE GRID ------   -- CARFIN GRID --  MAX     HOST
--       NAME       I1  I2  J1  J2  K1  K2     NX    NY    NZ   WELLS   NAME
CARFIN
        'LGR-2'      9   9   9   9   1   1      2     2      2     1    GLOBAL / CARFIN LGR GRID PARAMETERS

ENDFIN
```

The resulting keywords are as follows:
```eclipse
 'LGR     '           1 'CHAR'
 'LGR-1   '
 'LGRPARNT'           1 'CHAR'
 '        '
 'GRIDHEAD'         100 'INTE'
           1           2           2           2           1           0
           0           0           0           0           0           0
           0           0           0           0           0           0
           0           0           0           0           0           0
           1           1           0           2           2           1
  ………………………….……………..
            0           0           0           0
 'COORD   '          54 'REAL'
   0.10000000E+04   0.10000000E+04   0.00000000E+00   0.10000000E+04
   0.10000000E+04   0.10000000E+04   0.15000000E+04   0.10000000E+04
   0.00000000E+00   0.15000000E+04   0.10000000E+04   0.10000000E+04
   0.20000000E+04   0.10000000E+04   0.00000000E+00   0.20000000E+04
   0.10000000E+04   0.10000000E+04   0.10000000E+04   0.15000000E+04
  ………………………….……………..
    0.20000000E+04   0.10000000E+04
 'ZCORN   '          64 'REAL'
   0.83250000E+04   0.83250000E+04   0.83250000E+04   0.83250000E+04
   0.83250000E+04   0.83250000E+04   0.83250000E+04   0.83250000E+04
   0.83250000E+04   0.83250000E+04   0.83250000E+04   0.83250000E+04
   0.83250000E+04   0.83250000E+04   0.83250000E+04   0.83250000E+04
   0.83350000E+04   0.83350000E+04   0.83350000E+04   0.83350000E+04
  ………………………….……………..
    0.83450000E+04   0.83450000E+04   0.83450000E+04   0.83450000E+04
 'ACTNUM  '           8 'INTE'
           1           1           1           1           1           1
           1           1
 'HOSTNUM '           8 'INTE'
          12          12          12          12          12          12
          12          12
 'ENDGRID '           0 'INTE'
 'ENDLGR  '           0 'INTE'
 'LGR     '           1 'CHAR'
 'LGR-2   '
 'LGRPARNT'           1 'CHAR'
 '        '
 'GRIDHEAD'         100 'INTE'
           1           2           2           2           2           0
   ………………………….……………..
           0           0           0           0
 'COORD   '          54 'REAL'
   0.80000000E+04   0.80000000E+04   0.00000000E+00   0.80000000E+04
   0.80000000E+04   0.10000000E+04   0.85000000E+04   0.80000000E+04
   ………………………….……………..
   0.90000000E+04   0.10000000E+04
 'ZCORN   '          64 'REAL'
   0.83250000E+04   0.83250000E+04   0.83250000E+04   0.83250000E+04
   ………………………….……………..
   0.83450000E+04   0.83450000E+04   0.83450000E+04   0.83450000E+04
 'ACTNUM  '           8 'INTE'
           1           1           1           1           1           1
           1           1
 'HOSTNUM '           8 'INTE'
          89          89          89          89          89          89
          89          89
 'ENDGRID '           0 'INTE'
 'ENDLGR  '           0 'INTE'
```

End of Example
        - EGRID Non-Neighbor Connections for Irregular Corner Point Grid Keywords
    -
-

The keywords in this section are used to define Non\-Neighbor Connections \(“NNC”\) for both the global grid and any [LGR](#-refheading-toc55049-4106839650)’s included in the model.  This data set is only written out if there are NNCs in the model and can be skipped if this is the case; however, apart from very simple models, nearly all full field models will have NNCs as a result of modeling the structural faults in the model.  Likewise, the keywords affiliate with LGRs are also skipped if the there are no LGRs in the model.
Note that actual [NNC](#-refheading-toc63285-718313858) transmissibility data for the NNCs \([TRANX](#-refheading-toc93085-718313858), [TRANY](#-refheading-toc93087-718313858), and [TRANZ](#-refheading-toc93089-718313858)\) are stored in the [INIT](#-refheading-toc45789-719036256) Data File and not in the EGRID File.
The keyword definitions are tabulated in Table A.11.
| No. | Keyword Name | EGRID Non\-Neighbor Connections Keywords for Irregular Corner Point Grids Table A.11 |  |  | Status or Value |
| --- | --- | --- | --- | --- | --- |
|  | NNCHEAD | This keyword marks the start of the non\-neighbor keywords and defines the number of non\-neighbor connections. |  |  | Required |
| 1\-1 | Format | NNCHEAD | 10 | INTE |  |
| 2\-1 | Data | The number of non\-neighbor connections \(NUMNNC\). |  |  |  |
| 2\-2 | Data | Grid identifier set to zero for the global grid, or a value greater than zero to represent a [LGR](#-refheading-toc55049-4106839650). |  |  |  |
| 2\-3 to 2\-10 | Data | Not used. |  |  |  |
|  | NNC1 | NNC1 defines the cell numbers for the UPSTREAM non\-neighbor connections, where NUMNNC is the number of non\-neighbor connections. |  |  | Required |
| 1\-1 | Format | NNC1 | NUMNNC | INTE |  |
| 2\-1 | Data | NUMNNC integer values defining the cell numbers for the UPSTREAM non\-neighbor connections. |  |  |  |
|  | NNC2 | NNC2 defines the cell numbers for the DOWNSTREAM non\-neighbor connections, where NUMNNC is the number of non\-neighbor connections. |  |  | Required |
| 1\-1 | Format | NNC2 | NUMNNC | INTE |  |
| 2\-1 | Data | NUMNNC integer values defining the cell numbers for the DOWNSTREAM non\-neighbor connections. |  |  |  |
|  | NNCL | This keyword defines the local cells connected to the global grid, where NCONGL is the number of entries. |  |  | Optional |
| 1\-1 | Format | NNCL | NCONCL | INTE |  |
| 2\-1 | Data | NCONCL integer values defining the local cells connected to the global grid. |  |  |  |
|  | NNCG | This keyword defines the global cells connected to the current local grid being defined by this section of keywords, where NCONGL is the number of entries. |  |  | Optional |
| 1\-1 | Format | NNCG | NCONGL | INTE |  |
| 2\-1 | Data | NCONGL integer values defining the global cells connected to the current local grid. |  |  |  |
|  | NNCHEADA | This keyword defines the connection between two LGRs that have been amalgamated. |  |  | Optional |
| 1\-1 | Format | NNCHEADA | 10 | INTE |  |
| 2\-1 | Data | LGR index of the first [LGR](#-refheading-toc55049-4106839650) in the amalgamation \(ILOC1\). |  |  |  |
| 2\-2 | Data | LGR index of the second [LGR](#-refheading-toc55049-4106839650) in the amalgamation \(ILOC2\). |  |  |  |
| 2\-3 to 2\-10 |  | Not used. |  |  |  |
|  | NNA1 | This keyword defines the ILOC1 cells connected in the amalgamation, where NUMNCA is the number of entries. |  |  | Optional |
| 1\-1 | Format | NNA1 | NUMNCA | INTE |  |
| 2\-1 | Data | NUMNCA integer values defining the ILOC1 cells connected in the amalgamation. |  |  |  |
|  | NNA2 | This keyword defines the ILOC2 cells connected in the amalgamation, where NUMNCA is the number of entries. |  |  |  |
| 1\-1 | Format | NNA2 | NUMNCA | INTE |  |
| 2\-1 | Data | NUMNCA integer values defining the ILOC2 cells connected in the amalgamation. |  |  |  |
| Notes: - Rows shaded in gray indicate the start of a keyword. - Cells colored orange in the No. column indicate that this item is not supported by OPM Flow and those colored red are either “Not Used” or “Undefined”. - For formatted output all character variables, including the keywords, should be enclosed in single quotes, for example the NNCHEAD keyword should be written out as ‘NNCHEAD’. - Local Grid Refinements are currently not supported by OPM Flow and neither therefore is [LGR](#-refheading-toc55049-4106839650) amalgamation of LGRs. |  |  |  |  |  |

Table A.11: EGRID NNC Keywords for Irregular Corner Point Grids

Note that if [LGR](#-refheading-toc55049-4106839650)’s are present in the model then the keywords relating to LGRs are repeated for each [LGR](#-refheading-toc55049-4106839650) in the model.

#### <a id="-refheading-toc716943-3964674244"></a>Example: EGRID Grid Keywords for Non\-Neighbor Connections for Irregular Corner Point Grids

The example shows the NNCs for the global grid and two LGRs.
```eclipse
 'NNCHEAD '          10 'INTE'
       11363           0           0           0           0           0
           0           0           0           0
 'NNC1    '       11363 'INTE'
        5717        5717       21173       26325       31477       36629
       41781       46933       52085       57237       62389       67541
       72693       77845       82997       88149       93301      103605
………………………….……………..
 'NNC2    '       11363 'INTE'
         566       10870       26326       31478       36630       41782
       46934       52086       57238       62390       67542       72694
       77846       82998       88150       93302       98454       98454
      103606         612        5764       26372       21220       31524
………………………….……………..

 'NNCHEAD '          10 'INTE'
           0           1           0           0           0           0
           0           0           0           0
 'NNC1    '           0 'INTE'
 'NNC2    '           0 'INTE'
 'NNCL    '          16 'INTE'
           1           5           3           7           1           5
           2           6           2           6           4           8
           3           7           4           8
 'NNCG    '          16 'INTE'
          11          11          11          11           2           2
           2           2          13          13          13          13
          22          22          22          22
 'NNCHEAD '          10 'INTE'
           0           2           0           0           0           0
           0           0           0           0
 'NNC1    '           0 'INTE'
 'NNC2    '           0 'INTE'
 'NNCL    '          16 'INTE'
           1           5           3           7           1           5
           2           6           2           6           4           8
           3           7           4           8
 'NNCG    '          16 'INTE'
          88          88          88          88          79          79
          79          79          90          90          90          90
          99          99          99          99
```

End of Example
    - EGRID - Model Structural Data for Unstructured Grids File
-

This file format is currently not supported by OPM Flow.
    - EGRID - Model Structural Data for Mixed Grids File
-

This file format is currently not supported by OPM Flow.
    - GRID - Model Structural Data File
-

This file format is currently not supported by OPM Flow.

        - RESTART Data - LGR Grid Header Keywords
    -
-

This set of keywords define an [LGR](#-refheading-toc55049-4106839650)’s properties, [LGR](#-refheading-toc55049-4106839650) Name for example, and always proceeds an [LGR](#-refheading-toc55049-4106839650) data set for a given [LGR](#-refheading-toc55049-4106839650); that is the keywords are repeated for each [LGR](#-refheading-toc55049-4106839650) data set in the model and each time step.  Note that a given [LGR](#-refheading-toc55049-4106839650) data set is terminated by the ENDLGR keyword and the SEQNUM keyword terminates the input for a time step, which switches the input back to the global grid properties. The keyword description is outlined in Table A.12. 
Note that currently OPM Flow does not support [LGR](#-refheading-toc55049-4106839650) grids and therefore this set of keywords cannot be used by OPM Flow.
| No. | keyword Name | [RESTART](#-refheading-toc135629-1317547213) Data \- [LGR](#-refheading-toc55049-4106839650) Grid Header Keywords Table A.12 \(Repeated for Each [LGR](#-refheading-toc55049-4106839650) in the Model\) |  |  | Status or Value |
| --- | --- | --- | --- | --- | --- |
|  | [LGR](#-refheading-toc55049-4106839650) | [LGR](#-refheading-toc55049-4106839650) grid header keyword that defines the name of the [LGR](#-refheading-toc55049-4106839650). |  |  | Always Required |
| 1\-1 | Keyword | [LGR](#-refheading-toc55049-4106839650) | 1 | CHAR |  |
| 2\-1 | Data | Name of the [LGR](#-refheading-toc55049-4106839650). |  |  |  |
|  | LGRHEADI | [LGR](#-refheading-toc55049-4106839650) that defines the integer variables for this time step. |  |  | Always Required |
| 1\-1 | Format | LGRHEADI | 45 | INTE |  |
| 2\-1 to 2\-45 | Data | Undefined. |  |  |  |
|  | LGRHEADQ | [LGR](#-refheading-toc55049-4106839650) grid keyword that defines the logical variables \(T for true and F for false\) for this time step. |  |  | Always Required |
| 1\-1 | Format | LGRHEADQ | 5 | LOGI |  |
| 2\-1 to 2\-5 | Data | Undefined. |  |  |  |
|  | LGRHEADD | [LGR](#-refheading-toc55049-4106839650) grid keyword that defines the double precision REAL variables for this time step. |  |  | Always Required |
| 1\-1 | Format | LGRHEADD | 5 | DOUB | 5 |
| 2\-1 to 2\-5 | Data | Undefined. |  |  |  |
|  | ENDLGR | The ENDLGR keyword marks the end of an [LGR](#-refheading-toc55049-4106839650) section for a given [LGR](#-refheading-toc55049-4106839650). |  |  | Always Required |
| 1\-1 | Format | ENDLGR | 1 | MESG |  |
|  | Data | [LGR](#-refheading-toc55049-4106839650) number. |  |  |  |
| Notes: - Rows shaded in gray indicate the start of a keyword. - Cells colored orange in the No. column indicate that this item is not supported by OPM Flow and those colored red are either “Not Used” or “Undefined”. - For formatted output all character variables, including the keyword, should be enclosed in single quotes, for example the [LGR](#-refheading-toc55049-4106839650) keyword should be written out as ‘LGR     ’. |  |  |  |  |  |

Table A.12: RESTART Data \- LGR Grid Header Keywords

This keyword type is repeated for each [LGR](#-refheading-toc55049-4106839650) in the model with the last [LGR](#-refheading-toc55049-4106839650) data set terminated by the LGRSGONE keyword to mark the end of the [LGR](#-refheading-toc55049-4106839650) input.
| Note The [LGR](#-refheading-toc55049-4106839650), LGRHEADI, LGRHEADQ, and LGRHEADD always proceed [LGR](#-refheading-toc55049-4106839650) data sets and the ENDLGR keyword terminates the end of a data section of [LGR](#-refheading-toc55049-4106839650) data. |
| --- |

#### <a id="-refheading-toc716961-3964674244"></a>Example: RESTART Data \- LGR Grid Header Keywords

The following example shows a typical formatted [LGR](#-refheading-toc55049-4106839650) grid header data set for a single [LGR](#-refheading-toc55049-4106839650) grid named LGR\-1.

```eclipse
 'LGR     '           1 'CHAR'
 'LGR-1   '
 'LGRHEADI'          45 'INTE'
           1         100       -2345       -2345       -2345       -2345
       -2345       -2345       -2345       -2345       -2345       -2345
       -2345       -2345       -2345       -2345       -2345       -2345
       -2345       -2345       -2345       -2345       -2345       -2345
       -2345       -2345       -2345       -2345       -2345       -2345
       -2345       -2345       -2345       -2345       -2345       -2345
       -2345       -2345       -2345       -2345       -2345       -2345
       -2345       -2345       -2345
 'LGRHEADQ'           5 'LOGI'
  F  F  F  F  F
 'LGRHEADD'           5 'DOUB'
   0.00000000000000D+00  -0.10000000200409D+21  -0.10000000200409D+21
  -0.10000000200409D+21  -0.10000000200409D+21
```

End of Example

    - INIT – Model Initialization and Static Data File
-

The [INIT](#-refheading-toc45789-719036256) files contain the static data specified in the [GRID](#-refheading-toc38674-784232322), [PROPS](#-refheading-toc39329-784232322), and [REGIONS](#-refheading-toc40648-784232322) sections. For example, the [PORO](#-refheading-toc45797-719036256), [PERMX](#-refheading-toc45791-719036256), and [NTG](#-refheading-toc33334-784232322) arrays from the [GRID](#-refheading-toc38674-784232322) section and the resulting [PORV](#-refheading-toc96547-718313858), [TRANX](#-refheading-toc93085-718313858), [TRANY](#-refheading-toc93087-718313858), and [TRANZ](#-refheading-toc93089-718313858) arrays. The data is used in post\-processing software, for example OPM ResInsight, to visualize the static grid properties and the tabular PVT and relative permeability data, and is not used per se by the simulator. 
The data is written to file if the [INIT](#-refheading-toc45789-719036256) keyword in the [GRID](#-refheading-toc38674-784232322) section has been activated \([Error: Reference source not found\)](#6390init-activate-the-init-file-option). Similar to the EGRID file,  the [INIT](#-refheading-toc45789-719036256) file can either be written out in formatted form as ASCII i.e. text files, if the [FMTOUT](#-refheading-toc46651-1640804870) keyword has been activated, or binary format if the [FMTOUT](#-refheading-toc46651-1640804870) keyword has not been activated. Normally, this option is always activated by the user and when activated the binary form of the file is used.
There are two files types associated with the [INIT](#-refheading-toc45789-719036256) data:
        - an index file \([INIT](#-refheading-toc45789-719036256) Index\) that contains a list of variables, the array type \(character, integer, or real\) and the size of the arrays that are written out to the initialization data file and,
        - the initialization data file \([INIT](#-refheading-toc45789-719036256) Data\) that contains the actual data written out at the beginning of the run once the model has been initialized.
    -
-

The commercial simulator writes out both files, whereas OPM Flow only writes out the [INIT](#-refheading-toc45789-719036256) Data file, as the data can be read by most post\-processing software, including OPM ResInsight, using only the [INIT](#-refheading-toc45789-719036256) Data file as input.
The following sections outline the format for these two file types.
        - INIT Index File
    -
-

This file type is not supported or required by OPM Flow or OPM ResInsight to read or write the static data written to the [INIT](#-refheading-toc45789-719036256) Data file.

        - INIT Data File Specification
    -
-

This file type contains the global and any [LGR](#-refheading-toc55049-4106839650) grid property data present in the model2
       Several *k**eywords *are used for both global and [LGR](#-refheading-toc55049-4106839650) grids, for example the INTEHEAD, LOGIHEAD, DOUBHEAD, PROPERTY, and REGION keywords and arrays., for example porosity \([PORO](#-refheading-toc45797-719036256)\) and permeability data arrays \([PERMX](#-refheading-toc45791-719036256), [PERMY](#-refheading-toc45793-719036256), and [PERMZ](#-refheading-toc45795-719036256)\) for properties allocated to each grid cell, as well as the fluid and rock property functions tabular data. The overall structure of this file is similar to the [RESTART](#-refheading-toc135629-1317547213) file with the individual keywords being structured as shown in Table A.13.
| Reference | Section | Global Section keywords | Global Data keywords | [LGR](#-refheading-toc55049-4106839650) Section keywords | [LGR](#-refheading-toc55049-4106839650) Data keywords | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| A.6.3 |  | INTEHEAD LOGIHEAD DOUBHEAD |  |  |  | Global grid header keywords that defines the integer, logical, and double precision variables for this header keyword. |
| A.6.4 |  | Property Keywords | [PORV](#-refheading-toc96547-718313858) |  |  | Global grid property keywords that defines the global grid property data defined in the [GRID](#-refheading-toc38674-784232322) and Edit sections. For example, [PORV](#-refheading-toc96547-718313858), [NTG](#-refheading-toc33334-784232322),  [PERMX](#-refheading-toc45791-719036256), etc.\) |
| [PORO](#-refheading-toc45797-719036256) |  |  |  |  |  |  |
| etc. |  |  |  |  |  |  |
| A.6.5 |  |  |  | [LGR](#-refheading-toc55049-4106839650) LGRHEADI LGRHEADQ LGRHEADD |  | Defines the start of an [LGR](#-refheading-toc55049-4106839650) section of keywords and the [LGR](#-refheading-toc55049-4106839650) header keywords. |
| A.6.5 |  |  |  | INTEHEAD LOGIHEAD DOUBHEAD |  | [LGR](#-refheading-toc55049-4106839650) grid header keywords defining the same data as the global keywords, except for the given [LGR](#-refheading-toc55049-4106839650). This set of keywords are only written once for each [LGR](#-refheading-toc55049-4106839650). |
| A.6.4 |  |  |  | Property Keywords | [PORV](#-refheading-toc96547-718313858) | [LGR](#-refheading-toc55049-4106839650) property keywords; same format as the global grid keywords. |
| [PORO](#-refheading-toc45797-719036256) |  |  |  |  |  |  |
| etc. |  |  |  |  |  |  |
| A.6.5 |  |  |  | [LGR](#-refheading-toc55049-4106839650) LGRHEADI LGRHEADQ LGRHEADD |  | The [LGR](#-refheading-toc55049-4106839650) header keywords. |
| A.6.5 |  |  |  | INTEHEAD LOGIHEAD DOUBHEA |  | The [LGR](#-refheading-toc55049-4106839650) header keywords which are only written once for each [LGR](#-refheading-toc55049-4106839650). |
| A.6.4 |  |  |  | Property Keywords | [PORV](#-refheading-toc96547-718313858) | [LGR](#-refheading-toc55049-4106839650) property keywords. |
| [PORO](#-refheading-toc45797-719036256) |  |  |  |  |  |  |
| etc. |  |  |  |  |  |  |
|  |  |  |  | etc. |  | Repeated for each [LGR](#-refheading-toc55049-4106839650) in the model. |
| A.6.5 |  |  |  | LGRSGONE |  | Marks the end of [LGR](#-refheading-toc55049-4106839650) section of keywords. |
| A.6.7 |  | [TABDIMS](#-refheading-toc89327-327352552) |  |  |  | [TABDIMS](#-refheading-toc89327-327352552) defines the tables dimensions, for the subsequent TAB keywords. |
| A.6.8 |  | TAB |  |  |  | Rock and fluid tabular property data keywords. |
| A.6.8 |  | CON |  |  |  | CON keyword defines the constant PVT dead oil data \(the data associated with [RSCONST](#-refheading-toc138398-332691817), [RSCONSTT](#-refheading-toc138400-332691817), [RVCONST](#-refheading-toc329587-516898843), and [RVCONSTT](#-refheading-toc138400-3326918171) keywords\). |
| A.6.4 |  | Region Keywords | [PVTNUM](#-refheading-toc68366-2752266063) |  |  | Region property data for the global grid as defined in the REGION section \([PVTNUM](#-refheading-toc68366-2752266063), [SATNUM](#-refheading-toc71136-2752266063), etc.\). The keyword is repeated to account for all region property data. |
| [SATNUM](#-refheading-toc71136-2752266063) |  |  |  |  |  |  |
| etc. |  |  |  |  |  |  |
| A.6.5 |  |  |  | [LGR](#-refheading-toc55049-4106839650) LGRHEADI LGRHEADQ LGRHEADD |  | The [LGR](#-refheading-toc55049-4106839650) header keywords. |
| A.6.4 |  |  |  | Region Keywords | [PVTNUM](#-refheading-toc68366-2752266063) | [LGR](#-refheading-toc55049-4106839650) region property data for the [LGR](#-refheading-toc55049-4106839650) grid. |
| [SATNUM](#-refheading-toc71136-2752266063) |  |  |  |  |  |  |
| etc. |  |  |  |  |  |  |
| A.6.5 |  |  |  | [LGR](#-refheading-toc55049-4106839650) LGRHEADI LGRHEADQ LGRHEADD |  | The [LGR](#-refheading-toc55049-4106839650) header keywords. |
| A.6.4 |  |  |  | Region Keywords | [PVTNUM](#-refheading-toc68366-2752266063) | [LGR](#-refheading-toc55049-4106839650) region property data for the [LGR](#-refheading-toc55049-4106839650) grid. |
| [SATNUM](#-refheading-toc71136-2752266063) |  |  |  |  |  |  |
| etc. |  |  |  |  |  |  |
|  |  |  |  | etc. |  | Repeated for each [LGR](#-refheading-toc55049-4106839650) in the model. |
| A.6.5 |  |  |  | LGRSGONE |  | Marks the end of [LGR](#-refheading-toc55049-4106839650) section of keywords. |
| A.6.4 |  | End\-Point Keywords | [SWATINIT](#-refheading-toc323952-1728001293) |  |  | Global grid saturation and end\-point data keywords. The keyword uses the same keywords outlined in the [GRID](#-refheading-toc38674-784232322) and [PROPS](#-refheading-toc39329-784232322) section, for example, the [SWL](#-refheading-toc22881-7842323221), [SWATINIT](#-refheading-toc323952-1728001293), [KRG](#-refheading-toc97393-621662414),  [PCW](#-refheading-toc84164-621662414),  etc. arrays |
| [SWL](#-refheading-toc22881-7842323221) |  |  |  |  |  |  |
| etc. |  |  |  |  |  |  |
| A.6.5 |  |  |  | [LGR](#-refheading-toc55049-4106839650) LGRHEADI LGRHEADQ LGRHEADD |  | The [LGR](#-refheading-toc55049-4106839650) header keywords. |
| A.6.4 |  |  |  | End\-Point Keywords | [SWATINIT](#-refheading-toc323952-1728001293) | [LGR](#-refheading-toc55049-4106839650) grid saturation and end\-point data keywords. |
| [SWL](#-refheading-toc22881-7842323221) |  |  |  |  |  |  |
| etc. |  |  |  |  |  |  |
| A.6.5 |  |  |  | [LGR](#-refheading-toc55049-4106839650) LGRHEADI LGRHEADQ LGRHEADD |  | The [LGR](#-refheading-toc55049-4106839650) header keywords. |
| A.6.4 |  |  |  | End\-Point Keywords | [SWATINIT](#-refheading-toc323952-1728001293) | [LGR](#-refheading-toc55049-4106839650) grid saturation and end\-point data keywords. |
| [SWL](#-refheading-toc22881-7842323221) |  |  |  |  |  |  |
| etc. |  |  |  |  |  |  |
|  |  |  |  | etc. |  |  |
| A.6.5 |  |  |  | LGRSGONE |  | Marks the end of [LGR](#-refheading-toc55049-4106839650) section of keywords. |
| A.6.4 |  | [NNC](#-refheading-toc63285-718313858) Keywords | TRANNC |  |  | Non\-neighbor connection property data \(“NNC”\) for the global grid. The keyword is repeated to account for various [NNC](#-refheading-toc63285-718313858) arrays. |
| HEATNNC |  |  |  |  |  |  |
| etc. |  |  |  |  |  |  |
| A.6.5 |  |  |  | [LGR](#-refheading-toc55049-4106839650) LGRHEADI LGRHEADQ LGRHEADD |  | The [LGR](#-refheading-toc55049-4106839650) header keywords. |
| A.6.4 |  |  |  | [NNC](#-refheading-toc63285-718313858) Keywords | TRANNC | [LGR](#-refheading-toc55049-4106839650) [NNC](#-refheading-toc63285-718313858) property data. |
| [TRANGL](#-refheading-toc1306682-4250154414) |  |  |  |  |  |  |
| etc. |  |  |  |  |  |  |
| A.6.5 |  |  |  | [LGR](#-refheading-toc55049-4106839650) LGRHEADI LGRHEADQ LGRHEADD |  | The [LGR](#-refheading-toc55049-4106839650) header keywords. |
| A.6.4 |  |  |  | [NNC](#-refheading-toc63285-718313858) Keywords | TRANNC | [LGR](#-refheading-toc55049-4106839650) [NNC](#-refheading-toc63285-718313858) property data. |
| [TRANGL](#-refheading-toc1306682-4250154414) |  |  |  |  |  |  |
| etc. |  |  |  |  |  |  |
|  |  |  |  | etc. |  | Repeated for each [LGR](#-refheading-toc55049-4106839650) in the model. |
| A.6.5 |  |  |  | LGRSGONE |  | Marks the end of [LGR](#-refheading-toc55049-4106839650) section of keywords. |
| Notes: - Cells shaded in gray indicate the combination is not applicable and cells colored orange indicate that this item is not currently supported by OPM Flow. |  |  |  |  |  |  |

Table A.13:  INIT Data File Structure

        - INIT Data – Static Data Header Keywords
    -
-

The [INIT](#-refheading-toc45789-719036256) Data – Static Data Header Keyword section is the first data set that should be read or written to the [INIT](#-refheading-toc45789-719036256) Data file. This data set includes INTEHEAD, LOGIHEAD, and DOUBHEAD keywords that define versus parameters used in subsequent keywords in the [INIT](#-refheading-toc45789-719036256) Data file.   This is then followed by a series of global grid PROPERTY data keywords that define the various global grid property arrays for each grid cell in the model, as well as the static tabular data \(relative permeability tables and PVT tables\), etc. 
The structure for this set of keywords is defined in Table A.14.
| No. | keyword Name | [INIT](#-refheading-toc45789-719036256) Data – Static Data Header Keywords Table A.14 |  |  | Status or Value |
| --- | --- | --- | --- | --- | --- |
|  | INTEHEAD | Global static header keyword for the [INIT](#-refheading-toc45789-719036256) Data file that defines the start of [INIT](#-refheading-toc45789-719036256) static data set, and contains the integer variables for this header keyword. NIHEAD is the number of entries associated with this keyword, and is dependent on the features being used in the model. |  |  | Required |
| 1\-1 | Format | INTEHEAD | NIHEAD | INTE |  |
| 2\-1 |  | Undefined. |  |  | 0 |
| 2\-2 |  | Undefined. |  |  | 0 |
| 2\-3 | Data | Unit system used in the simulation, set to 1 for metric, 2 for field, and 3 for laboratory. |  |  |  |
| 2\-4 to 2\-8 |  | Undefined. |  |  | 0 |
| 2\-9 | Data | [DIMENS](#-refheading-toc20387-2267116897) key word in the [RUNSPEC](#-refheading-toc55591-1778172979) section \- the number of grid blocks in the x\-direction. |  |  | NX |
| 2\-10 | Data | [DIMENS](#-refheading-toc20387-2267116897) key word in the [RUNSPEC](#-refheading-toc55591-1778172979) section \- the number of grid blocks in the y\-direction. |  |  | NY |
| 2\-11 | Data | [DIMENS](#-refheading-toc20387-2267116897) key word in the [RUNSPEC](#-refheading-toc55591-1778172979) section \- the number of grid blocks in the z\-direction. |  |  | NZ |
| 2\-12 | Data | Number of global active cells in the model. |  |  | NACTIV |
| 2\-13 | Data | Not used. |  |  | 0 |
| 2\-14 | Data | Type of grid, set to 0 for Irregular Corner\-Point Grids, 1 for Unstructured Grids, or 2 for a mixture of Irregular Corner\-Point, Unstructured Grids \(Mixed Grids\) and 3 for Cartesian grids. |  |  | 1 |
| 2\-15 | Data | Type of phases in the model, set to 1 for oil, 2 for water, 3 for oil\-water, 4 for gas, 5 for oil\-gas, 6 for gas\-water and 7 for oil\-water\-gas. |  |  | PHASE |
| 2\-16 to 2\-64 |  | Undefined. |  |  | 0 |
| 2\-65 | Data | First part of start date of the run, DAY, the value should be greater than or equal to one and less than or equal to 31 for the calendar days. |  |  | DAY |
| 2\-66 | Data | Second part of start date of the run, MONTH, the value should be greater than or equal to one and less than or equal to 12 for the calendar month. |  |  | MONTH |
| 2\-77 | Data | Third part of start date of run,  YEAR, a positive four digit integer value of the start year, which must be specified fully by four digits, that is 1986. |  |  | YEAR |
| 2\-68 to 2\-94 |  | Undefined. |  |  | 0 |
| 2\-95 | Data | Simulator code used to generate the file, set to 100 for Schlumberger’s ECLIPSE 100, 300 for Schlumberger’s ECLIPSE 300, 500 for Schlumberger’s ECLIPSE 300 Thermal, 700 for Schlumberger’s INTERSECT simulator, 800 for Schlumberger’s FrontSim simulator, or a negative value for other simulators. OPM Flow uses a value of 100. |  |  | IPROG |
| 2\-96 to 206 |  | Undefined. |  |  | 0 |
| 2\-207 | Data | The first part of the current simulation time in the form HH:MM:SS, that is HH for hours. The value should be greater than or equal to zero and less than or equal to 23. |  |  | IHOURZ |
| 2\-208 | Data | The second part of the current simulation time in the form HH:MM:SS, that is MM for minutes. The value should be greater than or equal to zero and less than or equal to 59. |  |  | IMINTS |
| 2\-209 to 410 |  | Undefined. |  |  | 0 |
| 411 | Data | The third part of the current simulation time in the form HH:MM:SS, that is SS for seconds. The value should be greater than or equal to zero and less than or equal to 59. |  |  | ISECND |
|  | LOGIHEAD | Global static data keyword for the [INIT](#-refheading-toc45789-719036256) Data file that defines the logical variables \(T for true and F for false\) for this keyword.  NLHEAD is the number of entries associated with this keyword, and is dependent on the features being used in the model. Undefined items should be set to F \(False\). |  |  | Required |
| 1\-1 | Format | LOGIHEAD | NLHEAD | LOGI |  |
| 2\-1 | Data | Dissolved gas is present in the model indicator, set to T if present in the model else set to F. |  |  | [DISGAS](#-refheading-toc39767-2267116897) |
| 2\-2 | Data | Vaporized oil is present in the model indicator, set to T if present in the model else set to F. |  |  | [VAPOIL](#-refheading-toc56610-2267116897) |
| 2\-3 | Data | [SATOPTS](#-refheading-toc37029-327352552) in the [RUNSPEC](#-refheading-toc55591-1778172979) section \- directional relative permeability curves are active in the model. |  |  | DIRECT |
| 2\-4 | Data | [SATOPTS](#-refheading-toc37029-327352552) keyword in the [RUNSPEC](#-refheading-toc55591-1778172979) section \- reversible relative permeability \(black\-oil\) are active in the model. |  |  | IRREVERS |
| Radial grid geometry has been used for a compositional model indicator, set to T or F. Note that currently OPM Flow does not support radial grids and therefore this item should be set to F. |  |  | [RADIAL](#-refheading-toc51752-2905512151) |  |  |
| 2.5 | Data | Radial grid geometry has been used for a black\-oil model indicator, set to T or F. Note that currently OPM Flow does not support radial grids and therefore this item should be set to F. |  |  | [RADIAL](#-refheading-toc51752-2905512151) |
| Reversible relative permeability \(compositional\) are active in the model. |  |  | IRREVERS |  |  |
| 2.6 |  | Undefined. |  |  | F |
| 2\-7 | Data | The hysteresis option has been activated in the model indicator, set to T or F. |  |  | HYSTER |
| 2\-8 to 2\-14 | Data | Undefined. |  |  | F |
| 2\-15 | Data | The dual porosity option has been activated in the model indicator, set to T or F. Note that currently OPM Flow does not support dual porosity grids and therefore this item should be set to F. |  |  | [DUALPORO](#-refheading-toc241173-1772380413) |
| 2\-16 |  | Undefined. |  |  | F |
| 2\-17 | Data | [ENDSCALE](#-refheading-toc68146-2267116897) keyword in the [RUNSPEC](#-refheading-toc55591-1778172979) section \- enable end\-point scaling indicator. |  |  | [ENDSCALE](#-refheading-toc68146-2267116897) |
| 2\-18 | Data | [ENDSCALE](#-refheading-toc68146-2267116897) keyword in the [RUNSPEC](#-refheading-toc55591-1778172979) section \- directional end\-point scaling indicator. |  |  | DIRECT |
| 2.19 | Data | [ENDSCALE](#-refheading-toc68146-2267116897) keyword in the [RUNSPEC](#-refheading-toc55591-1778172979) section \- reversible end\-point scaling indicator. |  |  | IRREVERS |
| 2\-20 | Data | [SCALECRS](#-refheading-toc2086108-3315222525) keyword in the [PROPS](#-refheading-toc39329-784232322) section \- alternative three point end\-point scaling indicator. |  |  | [SCALECRS](#-refheading-toc2086108-3315222525) |
| 2\-21 to 2\-35 |  | Undefined. |  |  | F |
| 2\-36 | Data | Miscible displacement has been activated in the model indicator, set to T or F.  See the [Error: Reference source not found](#5227miscible-define-miscibility-todd-longstaff-parameters) keyword in the [RUNSPEC](#-refheading-toc55591-1778172979) section for further information. |  |  |  |
| 2\-37 to 2\-55 |  | Undefined. |  |  | F |
| 2\-56 | Data | The scale water capillary pressure at maximum water saturation \(that is minimum pressure\) has been activated in the model, set to T or F. |  |  |  |
| 2\-57 | Data | The scale water capillary pressure at maximum water saturation \(that is minimum pressure\) has been activated in the model, set to T or F. |  |  |  |
| 2\-58 to 2\-127 |  | Undefined. |  |  | 0 |
| 2\-128 | Data | Coal Bed Methane option has been activated in the compositional model indicator, set to T or F. Note that currently OPM Flow does not support the Coal Bed Methane option and therefore this item should be set to F. |  |  | F |
|  | DOUBHEAD | Global static data keyword for the [INIT](#-refheading-toc45789-719036256) Data file that defines the double precision REAL variables for this keyword. NDHEAD is the number of entries associated with this keyword, and is dependent on the features being used in the model. |  |  | Required |
| 1\-1 | Format | DOUBHEAD | NDHEAD | DOUB |  |
| 2\-1 to 2\-185 |  | Undefined. |  |  | 0.0 |
| Notes: - Rows shaded in gray indicate the start of a keyword. - Cells colored orange in the No. column indicate that this item is not supported by OPM Flow and those colored red are either “Not Used” or “Undefined”. - For formatted output all character variables, including the keywords should be enclosed in single quotes, for example the SEQNUM should be written out as ‘SEQNUM   ’. |  |  |  |  |  |

Table A.14: INIT Data – Static Data Header Keywords

#### <a id="-refheading-toc716945-3964674244"></a>Example: INIT Data – Static  Header Keywords

The following example shows a typical formatted [INIT](#-refheading-toc45789-719036256) Data header set of keywords.
```eclipse
 'INTEHEAD'         249 'INTE'
  -955283513      200400           2       -2345       -2345       -2345
       -2345       -2345          10          10           1         100
          10       -2345           7       -2345           0           1
           0           2           2           0           0           0
         110         108         109           3          97          93
       -2345       -2345          19          38          53       -2345
          97          93         146           5           0           1
          15          24           8           5           2           4
           0           0           0           0           0           0
           0           0           0           0           0           0
           0           0           0           0          19          10
        1982           0           0           0           1           0
           0           0           0           0           1          10
           0           0          12           1          25           1
  ………………………….……………..
 'LOGIHEAD'          79 'LOGI'
  T  F  F  T  F  F  F  F  T  F  F  F  F  F  F  F  T  F  T  F  F  F  F  F  F
  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F
  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F
  F  F  F  F
 'DOUBHEAD'         185 'DOUB'
   0.00000000000000D+00   0.10000000000000D+01   0.36500000000000D+03
   0.10000000149012D+00   0.15000000596046D+00   0.30000000000000D+01
   0.30000001192093D+00   0.10000000149012D+00   0.10000000149012D+00
  -0.10000000200409D+21   0.10000000000000D+01   0.10000000000000D+01
   0.10000000000000D+01   0.00000000000000D+00   0.00000000000000D+00
   0.10000000000000D+01   0.10000000000000D-03
  ………………………….……………..
```

End of Example

        - INIT Data – Static Grid Array Data Keywords
    -
-

This series of keywords define various static global and [LGR](#-refheading-toc55049-4106839650) grid property arrays for each grid cell in the model. The grid array keywords use the same grid property keywords described in the [GRID](#-refheading-toc38674-784232322) section of the manual. For example, the [DEPTH](#-refheading-toc58139-3701168388), [PORO](#-refheading-toc45797-719036256), [PERMX](#-refheading-toc45791-719036256), [PERMY](#-refheading-toc45793-719036256), [PERMZ](#-refheading-toc45795-719036256), [NTG](#-refheading-toc33334-784232322), [TOPS](#-refheading-toc55283-3701168388) arrays etc. In addition, the keywords also include the calculated pore volumes \([PORV](#-refheading-toc96547-718313858)\) and transmissibility arrays \([TRANX](#-refheading-toc93085-718313858), [TRANY](#-refheading-toc93087-718313858), and [TRANZ](#-refheading-toc93089-718313858)\) after processing the [GRID](#-refheading-toc38674-784232322) and [EDIT](#-refheading-toc40641-784232322) sections. Note the first property should always be the [PORV](#-refheading-toc96547-718313858) array for both global and [LGR](#-refheading-toc55049-4106839650) grid types.  
This format is also used to define the global grid REGION, [NNC](#-refheading-toc63285-718313858), and ENPOINTS section arrays, with the keyword name corresponding to the array name. For example, for the REGION keywords the same keywords outlined in the REGION section of the manual; that is [EQLNUM](#-refheading-toc73734-2752266063), [FIPNUM](#-refheading-toc77229-2752266063), [PVTNUM](#-refheading-toc68366-2752266063), [ROCKNUM](#-refheading-toc118210-2939291539), and [SATNUM](#-refheading-toc71136-2752266063) are utilized as the keywords in this section.  
The structure for this type of data and the keywords are defined in Table A.15.
| No. | keyword Name | [INIT](#-refheading-toc45789-719036256) Data – Static Grid Array Data keywords Table A.15 |  |  | Status or Value |
| --- | --- | --- | --- | --- | --- |
|  | PROPERTY | The PROPERTY keyword defines the start of a grid property array section of the [INIT](#-refheading-toc45789-719036256) file. PROPERTY is the keyword name of the array being written out, as outlined in the [GRID](#-refheading-toc38674-784232322) section. For example, [DEPTH](#-refheading-toc58139-3701168388), [PORO](#-refheading-toc45797-719036256),  [PERMX](#-refheading-toc45791-719036256), [PERMY](#-refheading-toc45793-719036256), [PERMZ](#-refheading-toc45795-719036256), [NTG](#-refheading-toc33334-784232322), [TOPS](#-refheading-toc55283-3701168388) keywords and the calculated [PORV](#-refheading-toc96547-718313858), [TRANX](#-refheading-toc93085-718313858), [TRANY](#-refheading-toc93087-718313858), and [TRANZ](#-refheading-toc93089-718313858) arrays. The PROPERTY keyword \(items 1\-1 and 2\-1\) is repeated for each grid property. The [PORV](#-refheading-toc96547-718313858) property must be the first data set for this keyword type and is written out in full for each cell in the model \(that is NXYZ = NX x NY x NZ values\). Note the [PORV](#-refheading-toc96547-718313858) array values for inactive cells are set to a constant value of zero. Subsequent grid property arrays can be in any order and only the active cells are written out \(NACTIV\). |  |  | Required |
| 1\-1 | Format | PROPERTY | NXYZ or NACTIV | REAL |  |
| 2\-1 | Data | PROPERTY data set. |  |  |  |
| [LGR](#-refheading-toc55049-4106839650) Property Data for Each [LGR](#-refheading-toc55049-4106839650) Keyword and Data |  |  |  |  |  |
| Table and Constant Keywords \([TABDIMS](#-refheading-toc89327-327352552), TAB, and CON\) |  |  |  |  |  |
|  | REGION | The REGION keyword defines the start of the grid region array section. REGION is the keyword name of the region array being written out, as outlined in the [REGIONS](#-refheading-toc40648-784232322) section. For example, [EQLNUM](#-refheading-toc73734-2752266063), [FIPNUM](#-refheading-toc77229-2752266063), [PVTNUM](#-refheading-toc68366-2752266063), [ROCKNUM](#-refheading-toc118210-2939291539), [SATNUM](#-refheading-toc71136-2752266063), etc. For analytical aquifers in the model, the AQUIFERA variable name is used to indicate which cells are connected to a given aquifer. If a cell is connected to an aquifer number N, then the cell value will be set to 2\(N\-1\) in the array. The REGION keyword \(items 1\-1 and 2\-1\) is repeated for each global region array and the arrays can be written out in any order. |  |  | Required |
| 1\-1 | Format | REGION | NACTIV | INTE |  |
| 2\-1 | Data | REGION data set. |  |  |  |
| [LGR](#-refheading-toc55049-4106839650) Region Keywords and Data for Each Grid |  |  |  |  |  |
|  | ENDPOINT | The ENDPOINT keywords define the start of a grid's saturation and end\-point data arrays. ENDPOINT is the keyword name of the saturation \([SWL](#-refheading-toc22881-7842323221), [SWATINIT](#-refheading-toc323952-1728001293), etc.\) array or end\-point array \([PCW](#-refheading-toc84164-621662414), [KRORW](#-refheading-toc70191-335817223), etc.\) being written out, as described in the [GRID](#-refheading-toc38674-784232322) and [PROPS](#-refheading-toc39329-784232322) sections. The type of data for the keyword should be set to REAL for arrays with real values \([SWL](#-refheading-toc22881-7842323221), [SWATINIT](#-refheading-toc323952-1728001293), etc\) or INTE for integer arrays \([ENDNUM](#-refheading-toc123125-83452205), etc\).  ENDPOINT arrays can be in any order and only the active cells are written out \(NACTIV\). This keyword \(items 1\-1 and 2\-1\) is repeated for each saturation and end\-point array being written out. The data written out is dependent on the various options declared in the [RUNSPEC](#-refheading-toc55591-1778172979) section as well as the data declared in the [GRID](#-refheading-toc38674-784232322) and [PROPS](#-refheading-toc39329-784232322) sections. |  |  | Required |
| 1\-1 | Keyword | ENDPOINTS | NACTIV | INTE or REAL |  |
| 2\-1 | Data | ENDPOINT data set. |  |  |  |
| [LGR](#-refheading-toc55049-4106839650) Saturation End\-Point Keywords and Data for Each [LGR](#-refheading-toc55049-4106839650) |  |  |  |  |  |
|  | [NNC](#-refheading-toc63285-718313858) | The [NNC](#-refheading-toc63285-718313858) keyword defines the start of a grid's non\-neighbor connection array data. [NNC](#-refheading-toc63285-718313858) is the keyword name of the non\-neighbor connection array being written out, and should be set to one of the following keywords: - TRANNNC: the non\-neighbor connection transmissibilities within the grid. Always required even if there are no [NNC](#-refheading-toc63285-718313858), in which case NUMNCC is set to zero. - DIFFNNC: the non\-neighbor connection diffusivities within the grid. Only required if the Diffusivity option has been activated by the [DIFFUSE](#-refheading-toc349951-1539708736) keyword in the [RUNSPEC](#-refheading-toc55591-1778172979) section. This option is currently not supported by OPM Flow - HEATNNC: the non\-neighbor connection thermal transmissibilities within the grid. Only required if OPM Flow’s [THERMAL](#-refheading-toc137276-650382403) option has been activated by the [THERMAL](#-refheading-toc137276-650382403) keyword in the [RUNSPEC](#-refheading-toc55591-1778172979) section. The following two additional [NNC](#-refheading-toc63285-718313858) keywords are required for when the data for an [LGR](#-refheading-toc55049-4106839650) is being defined: - TRANCC: the non\-neighbor connection transmissibilities within the [LGR](#-refheading-toc55049-4106839650) \(always required for an [LGR](#-refheading-toc55049-4106839650)\). - [TRANGL](#-refheading-toc1306682-4250154414): the non\-neighbor connections transmissibilities between the [LGR](#-refheading-toc55049-4106839650) and the global grid \(always required for an [LGR](#-refheading-toc55049-4106839650)\). The number of data values for this keyword data set should set to the number of non\-neighbor connection to be read or written out \(NUMNNC\) for the TRANNC,  DIFFNNC, HEATNCC, TRANCC, and [TRANGL](#-refheading-toc1306682-4250154414) arrays. The [NNC](#-refheading-toc63285-718313858) keyword \(items 1\-1 and 2\-1\) are repeated for each non\-neighbor connection array being written out. |  |  | Required |
| 1\-1 | Format | [NNC](#-refheading-toc63285-718313858) | NUMNCC | REAL |  |
| 2\-1 | Data | [NNC](#-refheading-toc63285-718313858) data set. |  |  |  |
| [LGR](#-refheading-toc55049-4106839650) Non\-Neighbor Connection Keywords for Each [LGR](#-refheading-toc55049-4106839650) |  |  |  |  |  |
| Notes: - Rows shaded in gray indicate the start of a keyword and rows colored orange indicate the location of [LGR](#-refheading-toc55049-4106839650) data if LGRs are present in the model. - For formatted output all character variables, including the keyword should be enclosed in single quotes, for example the [PORV](#-refheading-toc96547-718313858) and PROPERTY fields should be written out as ‘PORV    ’ and ‘DEPTH  ’, etc. |  |  |  |  |  |

Table A.15: INIT Data – Static Grid Array Data Keywords

#### <a id="-refheading-toc716947-3964674244"></a>Example: INIT Data – Static Grid Array Data Keywords

The following example shows a typical formatted global grid property data keyword.
```eclipse
 'PORV    '         100 'REAL'
   0.10686456E+07   0.10686456E+07   0.10686456E+07   0.10686456E+07
   0.10686456E+07   0.10686456E+07   0.10686456E+07   0.10686456E+07
  ………………………….……………..
   0.10686456E+07   0.10686456E+07   0.10686456E+07   0.10686456E+07
   0.10686456E+07   0.10686456E+07   0.10686456E+07   0.10686456E+07
 'DX      '         100 'REAL'
   0.10000000E+04   0.10000000E+04   0.10000000E+04   0.10000000E+04
   0.10000000E+04   0.10000000E+04   0.10000000E+04   0.10000000E+04
  ………………………….……………..
   0.10000000E+04   0.10000000E+04   0.10000000E+04   0.10000000E+04
   0.10000000E+04   0.10000000E+04   0.10000000E+04   0.10000000E+04
 'DY      '         100 'REAL'
   0.10000000E+04   0.10000000E+04   0.10000000E+04   0.10000000E+04
   0.10000000E+04   0.10000000E+04   0.10000000E+04   0.10000000E+04
  ………………………….……………..
   0.10000000E+04   0.10000000E+04   0.10000000E+04   0.10000000E+04
   0.10000000E+04   0.10000000E+04   0.10000000E+04   0.10000000E+04
 'DZ      '         100 'REAL'
   0.20000000E+02   0.20000000E+02   0.20000000E+02   0.20000000E+02
   0.20000000E+02   0.20000000E+02   0.20000000E+02   0.20000000E+02
   ………………………….……………..
   0.20000000E+02   0.20000000E+02   0.20000000E+02   0.20000000E+02
   0.20000000E+02   0.20000000E+02   0.20000000E+02   0.20000000E+02
 'PERMX   '         100 'REAL'
   0.50000000E+03   0.50000000E+03   0.50000000E+03   0.50000000E+03
   ………………………….……………..
   0.50000000E+03   0.50000000E+03   0.50000000E+03   0.50000000E+03
   0.50000000E+03   0.50000000E+03   0.50000000E+03   0.50000000E+03
………………………….……………..
TABULAR DATA
………………………….……………..
 'PVTNUM  '         100 'INTE'
           1           1           1           1           1           1
           1           1           1           1           1           1
………………………….……………..
           1           1           1           1           1           1
 'SATNUM  '         100 'INTE'
           1           1           1           1           1           2
           1           1           1           2           2           2
………………………….……………..
 'EQLNUM  '         100 'INTE'
           1           1           1           1           1           1
           1           1           1           1           1           1
 ………………………….……………..
```

End of Example
        - INIT Data - LGR Static Data Header Keywords
    -
-

The file structure for this series of keywords consists of two sets of keywords, the first set is repeated each time an [LGR](#-refheading-toc55049-4106839650) data set is written out and the second set, which is the same as global static header keywords in section INIT Data – Static Data Header Keywords, is only written once.  The first set of keywords defines an [LGR](#-refheading-toc55049-4106839650)’s properties, [LGR](#-refheading-toc55049-4106839650) Name for example, and always proceeds an [LGR](#-refheading-toc55049-4106839650) data set for a given [LGR](#-refheading-toc55049-4106839650); that is this series of keywords are repeated for each [LGR](#-refheading-toc55049-4106839650) data set in the model.  This is then followed by the second set of static data header keywords, or the actual array or table keywords. Termination of the [LGR](#-refheading-toc55049-4106839650) data set occurs after the last [LGR](#-refheading-toc55049-4106839650) data set has been written out using the LGRSGONE keyword, which switches input back to the global grid properties. Table A.16 outlines the structure of the [INIT](#-refheading-toc45789-719036256) Data \- [LGR](#-refheading-toc55049-4106839650) Static Header Keywords and their affiliated data.
Note that currently OPM Flow does not support [LGR](#-refheading-toc55049-4106839650) grids and therefore this set of keywords cannot be used by OPM Flow.
| No. | Keyword Name | [INIT](#-refheading-toc45789-719036256) Data \- [LGR](#-refheading-toc55049-4106839650) Static Header Keywords Table A.16 \(Repeated Each Time  an [LGR](#-refheading-toc55049-4106839650) Each Data Set is Written Out\) |  |  | Status or Value |
| --- | --- | --- | --- | --- | --- |
|  | [LGR](#-refheading-toc55049-4106839650) | [LGR](#-refheading-toc55049-4106839650) static data header keyword for the [INIT](#-refheading-toc45789-719036256) Data file that defines the name of the [LGR](#-refheading-toc55049-4106839650). |  |  | Always Required |
| 1\-1 | Keyword | [LGR](#-refheading-toc55049-4106839650) | 1 | CHAR |  |
| 2\-1 | Data | Name of the [LGR](#-refheading-toc55049-4106839650). |  |  |  |
|  | LGRHEADI | [LGR](#-refheading-toc55049-4106839650) that defines the integer variables for this keyword. |  |  | Always Required |
| 1\-1 | Format | LGRHEADI | 45 | INTE |  |
| 2\-1 to 2\-45 | Data | Undefined. |  |  |  |
|  | LGRHEADQ | [LGR](#-refheading-toc55049-4106839650) grid keyword for the [INIT](#-refheading-toc45789-719036256) Data file that defines the logical variables \(T for true and F for false\) for this keyword. |  |  | Always Required |
| 1\-1 | Format | LGRHEADQ | 5 | LOGI |  |
| 2\-1 to 2\-5 | Data | Undefined. |  |  |  |
|  | LGRHEADD | [LGR](#-refheading-toc55049-4106839650) grid keyword for the [INIT](#-refheading-toc45789-719036256) Data file that defines the double precision REAL variables for this keyword. |  |  | Always Required |
| 1\-1 | Format | LGRHEADD | 5 | DOUB | 5 |
| 2\-1 to 2\-5 | Data | Undefined. |  |  |  |
|  | LGRSGONE | The LGRSGONE keyword marks the end of the [LGR](#-refheading-toc55049-4106839650) section. Number of entries is always set to zero. There is no data set associated with this keyword. |  |  | Always Required |
| 1\-1 | Format | LGRSGONE | 0 | MESG |  |
|  | INTEHEAD | The keywords are the same as the [INIT](#-refheading-toc45789-719036256) Data Static Data Header keywords but the data pertains to the current [LGR](#-refheading-toc55049-4106839650). See Table A.14 for a detailed description of this keyword type. |  |  | Required Only Once |
|  | LOGIHEAD | See Table A.14 for a detailed description of this keyword type. |  |  | Required Only Once |
|  | DOUBHEAD | See Table A.14 for a detailed description of this keyword type. |  |  | Required Only Once |
| Notes: - Rows shaded in gray indicate the start of a keyword. - Cells colored orange in the No. column indicate that this item is not supported by OPM Flow and those colored red are either “Not Used” or “Undefined”. - For formatted output all character variables, including the keyword name should be enclosed in single quotes, for example the [LGR](#-refheading-toc55049-4106839650) keyword should be written out as ‘LGR     ’. |  |  |  |  |  |

Table A.16: INIT Data \- LGR Static Data Header Keywords

This series of keywords are repeated for each [LGR](#-refheading-toc55049-4106839650) in the model followed by the pertinent data and in the order outlined in Table A.13 and with the last [LGR](#-refheading-toc55049-4106839650) data set terminated by the LGRSGONE keyword to mark the end of the [LGR](#-refheading-toc55049-4106839650) input section.

| Note The [LGR](#-refheading-toc55049-4106839650), LGRHEADI, LGRHEADQ, and LGRHEADD keywords always proceeds and [LGR](#-refheading-toc55049-4106839650) data sets and the LGRSGONE keyword terminates the end of the [LGR](#-refheading-toc55049-4106839650) data section, which causes the data to revert back to the global grid data. |
| --- |

#### <a id="-refheading-toc716949-3964674244"></a>Example: INIT Data \- LGR Static Header Keywords

The following example shows a typical formatted [INIT](#-refheading-toc45789-719036256) Data \- [LGR](#-refheading-toc55049-4106839650) Grid Header Keyword data set for a single [LGR](#-refheading-toc55049-4106839650) grid named LGR\-1.  As this is the first time [LGR](#-refheading-toc55049-4106839650) data is being written out both sets of [LGR](#-refheading-toc55049-4106839650) header keywords are written out followed by the property array data.
```eclipse
 'LGR     '           1 'CHAR'
 'LGR-1   '
 'LGRHEADI'          45 'INTE'
           1         100       -2345       -2345       -2345       -2345
       -2345       -2345       -2345       -2345       -2345       -2345
       -2345       -2345       -2345       -2345       -2345       -2345
       -2345       -2345       -2345       -2345       -2345       -2345
       -2345       -2345       -2345       -2345       -2345       -2345
       -2345       -2345       -2345       -2345       -2345       -2345
       -2345       -2345       -2345       -2345       -2345       -2345
       -2345       -2345       -2345
 'LGRHEADQ'           5 'LOGI'
  F  F  F  F  F
 'LGRHEADD'           5 'DOUB'
   0.00000000000000D+00  -0.10000000200409D+21  -0.10000000200409D+21
  -0.10000000200409D+21  -0.10000000200409D+21
………………………….……………..

 'INTEHEAD'         249 'INTE'
  -955283513      200400           2       -2345       -2345       -2345
       -2345       -2345           2           2           2           8
………………………….……………..
           1           6           1          10           1          10
           1           1           1           0          30           3
          18          10           9
 'LOGIHEAD'          79 'LOGI'
  T  F  F  T  F  F  F  F  T  F  F  F  F  F  F  F  T  F  T  F  F  F  F  F  F
  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F
  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F
  F  F  F  F
 'DOUBHEAD'         185 'DOUB'
   0.00000000000000D+00   0.10000000000000D+01   0.36500000000000D+03
   0.10000000149012D+00   0.15000000596046D+00   0.30000000000000D+01
………………………….……………..
   0.10000000000000D+01   0.00000000000000D+00   0.00000000000000D+00
   0.10000000000000D+01   0.10000000000000D-03
………………………….……………..
 'PORV    '           8 'REAL'
   0.13358070E+06   0.13358070E+06   0.13358070E+06   0.13358070E+06
   0.13358070E+06   0.13358070E+06   0.13358070E+06   0.13358070E+06
 'DX      '           8 'REAL'
   0.50000000E+03   0.50000000E+03   0.50000000E+03   0.50000000E+03
   0.50000000E+03   0.50000000E+03   0.50000000E+03   0.50000000E+03
 'DY      '           8 'REAL'
   0.50000000E+03   0.50000000E+03   0.50000000E+03   0.50000000E+03
   0.50000000E+03   0.50000000E+03   0.50000000E+03   0.50000000E+03
 'DZ      '           8 'REAL'
   0.10000000E+02   0.10000000E+02   0.10000000E+02   0.10000000E+02
   0.10000000E+02   0.10000000E+02   0.10000000E+02   0.10000000E+02
 'PERMX   '           8 'REAL'
   0.50000000E+03   0.50000000E+03   0.50000000E+03   0.50000000E+03
   0.50000000E+03   0.50000000E+03   0.50000000E+03   0.50000000E+03
………………………….……………..
```

End of Example

        - INIT Data - LGR Grid Array Data Keywords
    -
-

The file structure for this set of keywords is identical to the Static Grid Array Data Keywords described in Table A.15, except that [LGR](#-refheading-toc55049-4106839650) header keywords prefix the actual data keywords. Both the [LGR](#-refheading-toc55049-4106839650) header and data keywords are repeated for each [LGR](#-refheading-toc55049-4106839650) in the model, and the last [LGR](#-refheading-toc55049-4106839650) data set is terminated by the LGRSGONE keyword to mark the end of the [LGR](#-refheading-toc55049-4106839650) input section. The keyword description for this type of data set is outlined in Table A.17. 
Note that currently OPM Flow does not support [LGR](#-refheading-toc55049-4106839650) grids and therefore this series of keywords cannot be used by OPM Flow.
| No. | Keyword Name | [INIT](#-refheading-toc45789-719036256) Data \- [LGR](#-refheading-toc55049-4106839650) Grid Array Data Keywords Table A.17 \(Repeated for Each [LGR](#-refheading-toc55049-4106839650) in the Model\) | Status or Value |
| --- | --- | --- | --- |
| 1\-1 | [LGR](#-refheading-toc55049-4106839650) | [LGR](#-refheading-toc55049-4106839650) Header Keywords \(see Table A.16\). | Required |
| LGRHEADI |  |  |  |
| LGRHEADQ |  |  |  |
| LGRHEADD |  |  |  |
| 1\-2 | INTEHEAD | [LGR](#-refheading-toc55049-4106839650) Header Keywords \(see Table A.16\). | Required Only Once |
| LOGIHEAD |  |  |  |
| DOUBHEAD |  |  |  |
| 1\-3 | PROPERTY REGION [NNC](#-refheading-toc63285-718313858) or ENPOINIT | [LGR](#-refheading-toc55049-4106839650) array data set for the current [LGR](#-refheading-toc55049-4106839650) – same format as the [INIT](#-refheading-toc45789-719036256) Data \- Grid Array Data Keywords \(see Table A.15\). | Required |
| 1\-4 | LGRSGONE | [LGR](#-refheading-toc55049-4106839650) Header Section termination keyword \(see Table A.16\). | Required |
| Notes: - Rows shaded in gray indicate the start of a keyword. - Cells colored orange in the No. column indicate that this item is not supported by OPM Flow. - For formatted output all character variables, including the keyword should be enclosed in single quotes, for example the [LGR](#-refheading-toc55049-4106839650) keyword should be written out as ‘LGR     ’. |  |  |  |

Table A.17: INIT Data \- LGR Grid Array Data Keywords

This keyword data set is repeated for each [LGR](#-refheading-toc55049-4106839650) in the model with the last [LGR](#-refheading-toc55049-4106839650) data set terminated by the LGRSGONE keyword to mark the end of the [LGR](#-refheading-toc55049-4106839650) data section.

#### <a id="-refheading-toc716951-3964674244"></a>Example: INIT Data \- LGR Static Grid Array Data Keywords

The following example shows a typical formatted [INIT](#-refheading-toc45789-719036256) Data \- [LGR](#-refheading-toc55049-4106839650) Static Grid Array Data Keywords for the region data set with two [LGR](#-refheading-toc55049-4106839650) grids named LGR\-1 and LGR\-2.
```eclipse
 'LGR     '           1 'CHAR'
 'LGR-1   '
 'LGRHEADI'          45 'INTE'
           1         100       -2345       -2345       -2345       -2345
       -2345       -2345       -2345       -2345       -2345       -2345
       -2345       -2345       -2345       -2345       -2345       -2345
       -2345       -2345       -2345       -2345       -2345       -2345
       -2345       -2345       -2345       -2345       -2345       -2345
       -2345       -2345       -2345       -2345       -2345       -2345
       -2345       -2345       -2345       -2345       -2345       -2345
       -2345       -2345       -2345
 'LGRHEADQ'           5 'LOGI'
  F  F  F  F  F
 'LGRHEADD'           5 'DOUB'
   0.00000000000000D+00  -0.10000000200409D+21  -0.10000000200409D+21
  -0.10000000200409D+21  -0.10000000200409D+21
 'PVTNUM  '           8 'INTE'
           1           1           1           1           1           1
           1           1
 'SATNUM  '           8 'INTE'
           1           1           1           1           2           2
           2           2
 'EQLNUM  '           8 'INTE'
           1           1           1           1           1           1
           1           1
 'FIPNUM  '           8 'INTE'
           1           1           1           1           1           1
           1           1
 'LGR     '           1 'CHAR'
 'LGR-2   '
 'LGRHEADI'          45 'INTE'
           2         100       -2345       -2345       -2345       -2345
       -2345       -2345       -2345       -2345       -2345       -2345
       -2345       -2345       -2345       -2345       -2345       -2345
       -2345       -2345       -2345       -2345       -2345       -2345
       -2345       -2345       -2345       -2345       -2345       -2345
       -2345       -2345       -2345       -2345       -2345       -2345
       -2345       -2345       -2345       -2345       -2345       -2345
       -2345       -2345       -2345
 'LGRHEADQ'           5 'LOGI'
  F  F  F  F  F
 'LGRHEADD'           5 'DOUB'
   0.00000000000000D+00  -0.10000000200409D+21  -0.10000000200409D+21
  -0.10000000200409D+21  -0.10000000200409D+21
 'PVTNUM  '           8 'INTE'
           1           1           1           1           1           1
           1           1
 'SATNUM  '           8 'INTE'
           1           2           1           2           2           1
           2           1
 'EQLNUM  '           8 'INTE'
           1           1           1           1           1           1
           1           1
 'FIPNUM  '           8 'INTE'
           1           1           1           1           1           1
           1           1
 'LGRSGONE'           0 'MESS'
```

End of Example
        - INIT Data – Static Tabular Data Header Keyword
    -
-

The [INIT](#-refheading-toc45789-719036256) Data – Static Tabular Data Header Keyword precedes the TAB keyword and consists of just one keyword followed by a series of integer values that define the dimensions of the data in the TAB keyword.  [TABDIMS](#-refheading-toc89327-327352552) is then followed by the TAB keyword that contains the actual tabular data in one continuous array.
The structure for this keyword is defined in Table A.18.
| No. | keyword  Name | [INIT](#-refheading-toc45789-719036256) Data – Static Tabular Data Header Keyword Table A.18 |  |  | Status or Value |
| --- | --- | --- | --- | --- | --- |
|  | [TABDIMS](#-refheading-toc89327-327352552) | Tabular header keyword for the [INIT](#-refheading-toc45789-719036256) Data file that defines the start of the tabular data and contains the base addresses and dimension of subsequent tabular array keyword TAB. Missing values should be defaulted to one. |  |  | Required |
| 1\-1 | Format | [TABDIMS](#-refheading-toc89327-327352552) | 100 | INTE |  |
| 2\-1 | Data | Total size of TAB data array, value should be the same as that on the TAB keyword. |  |  | NTABDA |
| 2\-2 | Data | Location of the first entry in the TAB array for the rock property table. |  |  | IBROCK |
| 2\-3 | Data | Maximum number of rock property tables. |  |  | NTROCK |
| 2\-4 | Data | Location of the first entry in the TAB array of rock compaction data. |  |  | IBROCC |
| 2\-5 | Data | Maximum number of pressure nodes in rock compaction data table. |  |  | NPROCC |
| 2\-6 | Data | Maximum number of rock compaction data tables. |  |  | NTROCC |
| 2\-7 | Data | Location of the first entry in the TAB array for the oil PVT property tables. |  |  | IBPVTO |
| 2\-8 | Data | Location of the first entry in the TAB array for the oil pressure nodes. |  |  | JBPVTO |
| 2\-9 | Data | Maximum number of composition nodes in oil PVT tables. |  |  | NRPVTO |
| 2\-10 | Data | Maximum number of pressure nodes in oil PVT tables. |  |  | NPPVTO |
| 2\-11 | Data | Maximum number of oil PVT property tables. |  |  | NTPVTO |
| 2\-12 | Data | Location of the first entry in the TAB array for water PVT property tables. |  |  | IBPVTW |
| 2\-13 | Data | Maximum number of water property tables. |  |  | NTPVTW |
| 2\-14 | Data | Location of the first entry in the TAB array for gas PVT property tables. |  |  | IBPVTG |
| 2\-15 | Data | Location of the first entry in the TAB array for the gas pressure nodes. |  |  | JBPVTG |
| 2\-16 | Data | Maximum number of composition nodes in the gas PVT tables. |  |  | NRPVTG |
| 2\-17 | Data | Maximum number of pressure nodes in the gas PVT tables. |  |  | NPPVTG |
| 2\-18 | Data | Maximum number of gas PVT property tables. |  |  | NTPVTG |
| 2\-19 | Data | Location of the first entry in the TAB array for surface density tables. |  |  | IBDENS |
| 2\-20 | Data | Maximum number of surface densities tables. |  |  | NTDENS |
| 2\-21 | Data | Location of the first entry in the TAB array for water saturation tables. |  |  | IBSWFN |
| 2\-22 | Data | Maximum number of saturation nodes in water saturation tables. |  |  | NSSWFN |
| 2\-23 | Data | Maximum number of water saturation tables. |  |  | NTSWFN |
| 2\-24 | Data | Location of the first entry in the TAB array for gas saturation tables. |  |  | IBSGFN |
| 2\-25 | Data | Maximum number of saturation nodes in gas saturation tables. |  |  | NSSGFN |
| 2\-26 | Data | Maximum number of gas saturation tables. |  |  | NTSGFN |
| 2\-27 | Data | Location of the first entry in the TAB array for oil saturation tables. |  |  | IBSOFN |
| 2\-28 | Data | Location of the first entry in the TAB array for array of connate water saturations. |  |  | IBSWCO |
| 2\-29 | Data | Maximum number of saturation nodes in the oil saturation tables. |  |  | NSSOFN |
| 2\-30 | Data | Maximum number of oil saturation tables. |  |  | NTSOFN |
| 2\-31 to 40 |  | Undefined. |  |  | 1 |
| 2\-41 | Data | Location of the first entry in the TAB array to the [VE](#-refheading-toc557797-487874538) table data. |  |  | IBVETB |
| 2\-42 | Data | Maximum number of items in a [VE](#-refheading-toc557797-487874538) table. |  |  | NSVETB |
| 2\-43 | Data | Maximum number of [VE](#-refheading-toc557797-487874538) tables. |  |  | NTVETB |
| 2\-44 | Data | Location of the first entry in the TAB array to the threshold pressure array. |  |  | IBTHPR |
| 2.45 | Data | Location of the first entry in the TAB array to [SCALELIM](#-refheading-toc612233-516898843-copy-1) data |  |  | IBSLIM |
| 2.46 | Data | Maximum number of end\-point versus depth nodes. |  |  | NSENDP |
| 2.47 | Data | Maximum number of end\-point versus depth tables. |  |  | NTENDP |
| 2.48 | Data | Location of the first entry in the TAB array to the reference temperature [RTEMP](#-refheading-toc146399-3544483072) used in [PVZG](#-refheading-toc350298-501926209) keyword in the PROPD section. |  |  | IBRTEM |
| 2.49 | Data | Location of the first entry in the TAB array to the value specified by the [TOLCRIT](#-refheading-toc138557-1496523326) keyword. Note that this is a single value applied to all the saturation tables. |  |  | IBCTOL |
| 2.50 |  | Undefined. |  |  | 1 |
| 2\-51 | Data | Location of the first entry in the TAB array to [LANGMUIR](#-refheading-toc214338-2843394514) table. |  |  | IBLANG |
| 2\-52 | Data | Maximum number of columns in [LANGMUIR](#-refheading-toc214338-2843394514) tables. |  |  | NCLANG |
| 2\-53 | Data | Maximum number of rows in the [LANGMUIR](#-refheading-toc214338-2843394514) tables. |  |  | NSLANG |
| 2\-54 | Data | Maximum number of [LANGMUIR](#-refheading-toc214338-2843394514) tables |  |  | NTLANG |
| 2\-55 | Data | Location of the first entry in the TAB array to a [LANGSOLV](#-refheading-toc219914-2843394514) table. |  |  | IBLNG2 |
| 2\-56 | Data | Location of the first entry in the TAB array to a [COALPP](#-refheading-toc253787-3519154785) table. |  |  | IBCADP |
| 2\-57 | Data | Location of the first entry in the TAB array to a [COALADS](#-refheading-toc248981-3519154785) table. |  |  | IBCADS |
| 2\-58 | Data | Location of the first entry in the TAB array to a [ROCKPAMA](#-refheading-toc241588-516898843) table. |  |  | IBROCP |
| 2\-59 | Data | Maximum number of [ROCKPAMA](#-refheading-toc241588-516898843) tables. |  |  | NTRPMA |
| 2\-60 to 2\-100 |  | Undefined. |  |  | 1 |
| Notes: - Rows shaded in gray indicate the start of a keyword. - Cells colored orange in the No. column indicate that this item is not supported by OPM Flow and those colored red are either “Not Used” or “Undefined”. - For formatted output all character variables, including the keywords should be enclosed in single quotes, for example the [PORV](#-refheading-toc96547-718313858) and PROPERTY fields should be written out as ‘PORV    ’ and  ‘DEPTH  ‘, etc. |  |  |  |  |  |

Table A.18: INIT Data – Static Tabular Data Header Keyword

#### <a id="-refheading-toc716953-3964674244"></a>Example: INIT Data – Static Tabular Data Header Keyword

The following example shows a typical formatted [INIT](#-refheading-toc45789-719036256) Data – Static Tabular Data Header Keyword and the affiliated data.
```eclipse
 'TABDIMS '         100 'INTE'
       77006           1           2           1          60           1
          17       36017          60          60           2       36799
           2       37139       73139          60          60           2
           5           2       36809          33           2       73259
          33           2       36137       36797          66           2
       73589           5       73644          20           5       74044
          20           5           0           0       74444          25
           2       74494       75835          20           1       77003
           0           0           0           0           0           0
           0           0           0           0           0           0
           0           0           0           0           0           0
           0           0           0           0           0           0
           0           0           0           0           0           0
           0           0           0           0           0           0
           0           0           0           0           0           0
           0           0           0           0           0           0
           0           0           0           0
```

End of Example

        - INIT Data – Static Tabular and Constant Data Array Keywords
    -
-

The [INIT](#-refheading-toc45789-719036256) Data – Static Tabular and Constant Data Array Keyword section contains the actual tabular data in one continuous array, followed by the constant data array. The tabular array data is parse according to the phases present in the model and the location and dimension data given by the [TABDIMS](#-refheading-toc89327-327352552) keyword.
The structure for this set of keywords is defined in Table A.19.
| No. | keyword or Variable Name | [INIT](#-refheading-toc45789-719036256) Data – Static Tabular and Constant Data Array Keyword Table A.19 |  |  | Status or Value |
| --- | --- | --- | --- | --- | --- |
|  | TAB | Tabular data array keyword for the [INIT](#-refheading-toc45789-719036256) Data file that defines the start of the tabular data array. The total number of entries is given by the NTABDA and the value should be the same as declared on the [TABDIMS](#-refheading-toc89327-327352552) keyword. |  |  | Required |
| 1\-1 | Format | [TABDIMS](#-refheading-toc89327-327352552) | NTABDA | DOUB |  |
| 2\-1 | Data | Tabular data array. The data should be written out in double precision and missing data should be set to less than or equal to \-10.0 x 1020 or greater than or equal to 10.0 x 1020. |  |  |  |
|  | CON | Constant data array that contains the constant dead oil, dead vaporized oil, and saturation pressure PVT entered via the [RSCONST](#-refheading-toc138398-332691817)/[RSCONSTT](#-refheading-toc138400-332691817) and [RVCONST](#-refheading-toc329587-516898843)/[RVCONSTT](#-refheading-toc138400-3326918171) keywords in the [PROPS](#-refheading-toc39329-784232322) section. |  |  | Required |
| 1\-1 | Format | CON | NPVT x 3 | DOUB |  |
| 2\-1 | Data | The data consists of three values for each PVT data set \(NPVT\), [RS](#-refheading-toc137361-1317547213), [RV](#-refheading-toc137365-1317547213), and the saturation pressure of the active phase in the model \(bubble\-point or dew point\). |  |  |  |
| Notes: - Rows shaded in gray indicate the start of a keyword. - Note both TAB and CON keywords should be enclosed in single quotation marks, that is  ‘TAB     ’ and ‘CON     ’. |  |  |  |  |  |

Table A.19: INIT Data – Static Tabular and Constant Data Array Keywords

The phases present in the model are given on the INTEHEAD keyword \(Table A.14\) in location 2\-15 where the type of phases in the model are set via an integer: 1 for oil, 2 for water, 3 for oil\-water, 4 for gas, 5 for oil\-gas, 6 for gas\-water, and 7 for oil\-water\-gas.  This data is used to access the phase dependent data \(PVT, saturation functions tables, etc.\) combine with the location \(or base address\) and the dimension data given on the [TABDIMS](#-refheading-toc89327-327352552) keyword in Table A.18. 
Note that data given in  Table A.18 refers to the maximum values and therefore missing data should be set to the default value. 

#### <a id="-refheading-toc716955-3964674244"></a>Example: INIT Data – Static Tabular and Constant Data Array Keywords

The following example shows a typical formatted data set for this type set of keywords and the affiliated data. Here the CON array has two PVT tables but the values are all set to zero indicating that dead oil and vaporized dead oil are not active phases in the model.  
```eclipse
'TAB     '       73576 'DOUB'
   0.49700000000000D-05   0.24800000000000D-05   0.00000000000000D+00
  -0.20000000000000D+21  -0.20000000000000D+21  -0.20000000000000D+21
  -0.20000000000000D+21  -0.20000000000000D+21  -0.20000000000000D+21
 ………………………….……………..
  -0.20000000000000D+21  -0.20000000000000D+21  -0.20000000000000D+21
   0.52100000000000D-05   0.26100000000000D-05   0.00000000000000D+00
  -0.20000000000000D+21  -0.20000000000000D+21  -0.20000000000000D+21
'CON     '           6 'DOUB'
   0.00000000000000D+00   0.00000000000000D+00   0.00000000000000D+00
   0.00000000000000D+00   0.00000000000000D+00   0.00000000000000D+00
 ………………………….……………..
```

End of Example

    - LOG File – OPM Flow Terminal Output
-

The LOG file for the commercial simulator contains an ASCII copy of the output from the terminal. The file itself is not generated by the commercial simulator but by an auxiliary program, ECLRUN, that is used to call and execute all the commercial simulators. 
OPM Flow does not generate a LOG file; however, the file can be generated by using the Linux tee command, for example:
```eclipse
	flow CASENAME | tee CASENAME.LOG
```

Which will copy the terminal output to the CASENAME.LOG file. Alternatively, one can use OPMRUN, the Graphical User Interface \(“GUI”\) program for OPM Flow, that provides similar functionality to the commercial simulator’s auxiliary program. 
The OPM Flow terminal output differs from that generated by the commercial simulator. This section outlines the format of the OPM Flow specific Terminal Output \(LOG File\) illustrated with examples.
Note that the OPM Flow terminal output is generally also sent in the Print \(PRT\) file. In addition to the terminal output, the Print file also includes:
- the name of the machine the simulation was run on,
- the operating system,
- the start time for the simulation,
- a list of the command line arguments specified when running OPM Flow,
- the property tree for the linear solver,
- any output reports requested by the user \(for example, using the [RPTPROPS](#-refheading-toc55372-3218818441) keyword in the [PROPS](#-refheading-toc39329-784232322) section, the [RPTSOL](#-refheading-toc135631-1317547213) keyword in the [SOLUTION](#-refheading-toc43947-784232322) section, the [RPTSCHED](#-refheading-toc268459-1366622701) keyword in the [SCHEDULE](#-refheading-toc43945-784232322) section, and so forth\), and finally
- an error summary giving the total number of Warnings, Problems, Errors, and so forth reported during the simulation.

Also note that the contents of the LOG file will vary depending on the model being simulated, the command line parameters, and the numerical performance of the simulator. The main simulation loop for example may contain additional messages other than those illustrated including: when the simulator changes the control mode for a well, when a time step fails to converge, and so forth.
        - LOG File - Header
    -
-

At the start of the LOG file OPM Flow writes a header giving the software version followed by information about the number of MPI processes if applicable. The following example is taken from the LOG file generated for the Norne model \([NORNE\_ATW2013](https://github.com/OPM/opm-tests/blob/master/norne/NORNE_ATW2013.DATA)\):
```eclipse
**********************************************************************
*                                                                    *
*                        This is flow 2024.04                        *
*                                                                    *
* Flow is a simulator for fully implicit three-phase black-oil flow, *
*             including solvent and polymer capabilities.            *
*          For more information, see https://opm-project.org         *
*                                                                    *
**********************************************************************

Using 8 MPI processes with 2 OMP threads on each
```

In this example OPM Flow version 2024.04 has been run using eight MPI processes and each MPI process may itself use 2 OpenMP threads.
        - LOG File – Reading Deck
    -
-

Next OPM Flow parses the input deck including any files referenced with the [INCLUDE](#-refheading-toc55749-2479612490) keyword. As each keyword is parsed and it’s data records are read, the simulator reports the keyword name, the file it is located in, and the corresponding line number. Any warning messages about unsupported keywords or unsupported keyword items found in the deck are then reported. See the following shortened example:
```eclipse
Reading deck file 'NORNE_ATW2013.data'
    0 Reading RUNSPEC  in NORNE_ATW2013.data line 9
    1 Reading DIMENS   in NORNE_ATW2013.data line 11
...
 1342 Reading DATES    in /.../norne/INCLUDE/BC0407_HIST01122006.SCH line 9565
#[34;1m
Warning: Unsupported keywords or keyword items:

  NSTACK: keyword not supported
  In file: NORNE_ATW2013.data, line 102
...
  RPTRST: invalid value '0' for item 1
  In file: /.../norne/INCLUDE/BC0407_HIST01122006.SCH, line 9245
  RPTRST(RPTRST): invalid option or unsupported integer control format#[0m
```

In this example OPM Flow reports that the [NSTACK](#-refheading-toc34963-1640804870) keyword in the main data file is not currently supported, and that an invalid option has been specified for item 1 on the [RPTRST](#-refheading-toc210154-2884651453) keyword in an include file.
Note that OPM Flow outputs text formatting to the terminal to provide color highlighting of warning messages etc. \(for example, “\#\[34;1m”\). This formatting may not be displayed in a text editor.
        - LOG File – Processing Data
    -
-

The input that was read in is now processed. First the grid structure and the fault model is created, and in this example the tracers are initialized:
```eclipse
Creating corner-point grid from keywords COORD, ZCORN and others

Initializing tracers from TRACER in NORNE_ATW2013.data line 268
...

Loading faults from FAULTS in /.../norne/INCLUDE/FAULT/FAULT_JUN_05.INC line 9

Applying MULTFLT in /.../norne/INCLUDE/FAULT/FAULTMULT_AUG-2006.INC line 8
...
```

  
In the above example, the fault structure is read in from an include file \(FAULT\_JUN\_05.INC\), and then the corresponding fault multipliers are read from different include files \(FAULTMULT\_AUG\-2006.INC, etc.\).
Next the dynamic information from the [SCHEDULE](#-refheading-toc43945-784232322) section is processed to prepare the report steps: 
```eclipse
Processing dynamic information from
NORNE_ATW2013.data line 449
Initializing report step 0/247 at 1997-11-06 0 DAYS line 449
Processing keyword DRSDT at line 452
...
Reading from: /.../norne/INCLUDE/VFP/NEW_D2_GAS_0.00003.VFP line 62
Processing keyword VFPPROD at line 62
#[34;1m
Warning: VFPPROD table 5 has 7 non-monotonic points of BHP(THP)
In /.../norne/INCLUDE/VFP/NEW_D2_GAS_0.00003.VFP line 62
This may cause convergence issues due to switching between BHP and THP control.
#[0m
...
Complete report step 1 (8 DAYS) at 1997-11-14 (0 DAYS)

Initializing report step 2/247 at 1997-11-14 (0 DAYS) line 204
Processing keyword WCONHIST at line 208
Processing keyword WCONINJE at line 212
Complete report step 2 (17 DAYS) at 1997-12-01 (8 DAYS)
...
```

In the above example where key values have been highlighted in yellow, the simulation will start the first report step \(out of a total of 247\) at the simulation start time of 6 November 1997; and will complete it after advancing the simulation by 8 days to 14 November 1997. 
Whilst, initializing the first report step, lift table \([VFPPROD](#-refheading-toc121919-2556401936) table 5\) is processed and OPM Flow reports that it has found 7 non\-monotonic points of BHP versus THP, and warns that this may cause convergence issues. At this point the user may decide to adjust the table or continue with the unmodified table.
The simulation will then continue with report step 2 of 247 starting on 14 November 1997; and will complete report step 2 after advancing the simulation by a further 17 days to 1 December 1997 \(elapsed time 25 days\).
During report step 2 the [WCONHIST](#-refheading-toc134880-2055188184) and [WCONINJE](#-refheading-toc146750-4203985108) keywords have been processed. These modify the well production and injection controls effective from the start of the report step.
Note that OPM Flow only reports the initialization of the first five report steps.
Note at this point the dynamic data is only being processed to set up the report step; and the simulation has not yet started.
The grid is then processed after which the simulator reports the number of active cells in the model along with their total pore volume. The number of cells removed from the model due to the cut\-off values applied and the resulting reduction in total pore volume are also reported. For example:
```eclipse
Processing grid
Total number of active cells: 44431 / total pore volume: 673248728 RM3
Removed 496 cells with a pore volume of 100450 RM3 (0.015 %) due to MINPV/MINPVV
```

  
For parallel runs information about the load balancing between the processes is then reported: 
```eclipse
Load balancing distributes 44431 active cells on 8 processes as follows:
  rank   owned cells   overlap cells   total cells
--------------------------------------------------
     0          5821            3382          9203
     1          6104            1771          7875
...
--------------------------------------------------
   sum         44431           13568         57999

Load balancing distributed the wells as follows:
  well name            ranks with perforated cells
---------------------------------------------------
           B-1AH       4
            B-2H       1
...
```

Finally, warning messages about unsupported keywords are reported, for example:
```eclipse
#[34;1m
Warning: Unhandled summary keyword DATE/DAY
In /.../norne/INCLUDE/SUMMARY/summary.data line 9#[0m
...
```

        - LOG File – Saturation Function Diagnostics
    -
-

Having processed the input data the simulator reports diagnostic information about the saturation functions including: the fluid system, the saturation function family, and the number of saturation function regions. For example:
```eclipse
===============Saturation Functions Diagnostics===============

System:  Black-oil system.
Relative permeability input format: Saturation Family I.
Number of saturation regions: 2
```

In the above example a black\-oil system has been specified, saturation function family I has been used, and there are two saturation function regions.
        - LOG File – Main Simulation Loop
    -
-

The simulator now enters the main simulation loop and reports the progress of the simulation as it advances from the start date to each of the report times specified in the input deck, for example:
```eclipse
================ Starting main simulation loop ===============

Report step  0/247 at day 0/3312, date = 06-Nov-1997
Using Newton nonlinear solver.

Starting time step 0, stepsize 1 days, at day 0/8, date = 06-Nov-1997
Restart file written for report step   0/247, date = 06-Nov-1997 00:00:00
 Newton its= 3, linearizations= 4 (0.1sec), linear its= 15 (0.1sec)

Starting time step 1, stepsize 3 days, at day 1/8, date = 07-Nov-1997
 Newton its= 2, linearizations= 3 (0.0sec), linear its= 21 (0.1sec)

Starting time step 2, stepsize 4 days, at day 4/8, date = 10-Nov-1997
 Newton its= 2, linearizations= 3 (0.0sec), linear its= 33 (0.1sec)

Report step  1/247 at day 8/3312, date = 14-Nov-1997
...
Report step 246/247 at day 3298/3312, date = 17-Nov-2006

Starting time step 0, stepsize 14 days, at day 3298/3312, date = 17-Nov-2006
 Newton its= 3, linearizations= 4 (0.0sec), linear its= 70 (0.2sec)
```

In the example above, the simulation starts the first report step number 0 \(out of a total of 247 report steps\)  on 6 November 1997 an elapsed time of 0 days \(of a total of 3312 days\). 
The simulator reports that it is using the Newton nonlinear solver. 
A restart file is written at the start of the first report step number 0 \(out of a total of 247 report steps\) on 6 November 1997 at 00:00:00.
The simulator then attempts to advance the simulation by a first time step of 1 day starting from 6 November 1997 an elapsed time of 0 days \(towards the next report time at an elapsed time of 8 days\). The time step is successfully completed after three Newton iterations, four linearizations \(taking 0.1s\) and 15 linear iterations \(taking 0.1s\).
The simulator then attempts to advance the simulation by a second time step of 3 days starting on 7 November 1997 an elapsed time of 1 day \(towards the next report time at an elapsed time of 8 days\). The time step is successfully completed after two Newton iterations, three linearizations \(taking 0.0s\), and 21 linear iterations \(taking 0.1s\). Note that since the previous time step successfully converged the time step size has been increased by OPM Flow’s time stepping algorithm.
The simulator then attempts to advance the simulation by a third time step of 4 days starting on 10 November 1997 an elapsed time of 4 days \(towards the next report time at an elapsed time of 8 days\). The time step is successfully completed after two Newton iterations, three linearizations \(taking 0.0s\), and 33 linear iterations \(taking 0.1s\). Note the time step size has been constrained to advance the simulation to the next report time.
The simulation has now reached the start of report step 1 \(of 247\) on 14 November 1997 an elapsed time of 8 days \(out of a total of 3312 days\).
The above example now skips the intermediate report steps and jumps to the end of the simulation.
The simulation starts the final report step number 246 \(of 247\) on 17 November 2006 an elapsed time of 3298 days \(out of a total of 3312 days\). 
The simulator then attempts to advance the simulation by a single time step of 14 days starting on 17 November 2006 an elapsed time of 3298 days \(towards the final report time at an elapsed time of 3312 days\). The time step is successfully completed after three Newton iterations, four linearizations \(taking 0.0s\), and 70 linear iterations \(taking 0.2s\). The simulation ends on 1 December 2006.
        - LOG File – End of Simulation
    -
-

The final section of the LOG file reports the numerical performance of the simulation including the number of processors, the simulation time, and the total numbers of linearizations, Newton iterations, and linear iterations, for example:
```eclipse
================    End of simulation     ===============

Number of MPI processes:         8
Threads per MPI process:         2
Setup time:                      8.40 s
  Deck input:                    5.18 s
Number of timesteps:           369
Simulation time:               240.47 s
  Assembly time:                22.44 s (Wasted: 0.0 s; 0.0%)
    Well assembly:               2.74 s (Wasted: 0.0 s; 0.0%)
  Linear solve time:            83.22 s (Wasted: 0.0 s; 0.0%)
    Linear setup:                8.16 s (Wasted: 0.0 s; 0.0%)
  Props/update time:            21.69 s (Wasted: 0.0 s; 0.0%)
  Pre/post step:                35.75 s (Wasted: 0.0 s; 0.0%)
  Output write time:            69.24 s
Overall Linearizations:       1903      (Wasted:     0; 0.0%)
Overall Newton Iterations:    1534      (Wasted:     0; 0.0%)
Overall Linear Iterations:   22713      (Wasted:     0; 0.0%)
```

In the above example, the simulation took 8.4s to setup followed by 240.47s of simulation time during which it performed at total of 369 time steps, which required a total of 1534 Newton iterations. The summary includes a breakdown of the simulation time; of which the linear solve time was the largest component in this example.
The total linear solve time was 83.22s of which 0.0s \(or 0.0% of the total\) was wasted due to convergence failures \(since there were no convergence failures in this example\). Similarly, there were a total of 1,534 Newton iterations of which zero were wasted due to convergence failures.

## 

    - RESTART Files – Dynamic Data (Solution, Groups, Wells, Connections, Aquifers, etc.)
-

[RESTART](#-refheading-toc135629-1317547213) files contain the solution data arrays for each active cell in the model, and represents a “snapshot” of the reservoir state at a reporting time step, for example the pressure \([PRESSURE](#-refheading-toc135627-1317547213), PPCW, and PPCG\), fluid saturations \([SGAS](#-refheading-toc137369-1317547213), [SOIL](#-refheading-toc137371-1317547213), and [SWAT](#-refheading-toc137373-1317547213)\), and fluid state \([RS](#-refheading-toc137361-1317547213) and [RV](#-refheading-toc137365-1317547213)\) for all active cells.  The PPCW and PPCG arrays are the water and capillary solution arrays and the [RS](#-refheading-toc137361-1317547213) and [RV](#-refheading-toc137365-1317547213) arrays are the gas\-oil and vaporized\-oil ratio \(condensate\-gas ratio\) solution arrays. The data written to the [RESTART](#-refheading-toc135629-1317547213) file is dependent on the fluid phases and options invoked in the model, as well as any additional user requested solution data. The default arrays written out are always sufficient to enable the simulator to restart from a previous run3
       For example in a three phase \(oil, gas, and water\) runs only two phase saturations are needed for a “restart” run, as the third phase can be calculated in  by summing two phases and subtracting from one..  This was the original purpose of the [RESTART](#-refheading-toc135629-1317547213) file, that is saving the reservoir state in such a manner, is to enable a “restart” of the simulation. 
[RESTART](#-refheading-toc135629-1317547213) files also contain the necessary information to do restart runs for Groups, Wells, Connections, Aquifer data, etc. This information enables restart runs based on Schedule information read from the Restart file only, using the [SKIPREST](#-refheading-toc117631-2179381650) keyword in the [SCHEDULE](#-refheading-toc43945-784232322) section.
As of the OPM Flow 2019\-04 release the simulator can  “restart” from the commercial simulator’s generated [RESTART](#-refheading-toc135629-1317547213) files as well as the commercial simulator being to “restart” from the OPM Flow’s generated [RESTART](#-refheading-toc135629-1317547213) files. See section [Error: Reference source not found](#22running-opm-flow-2019-04-from-the-command-line) [Error: Reference source not found](#22running-opm-flow-2019-04-from-the-command-line) for additional information.
As [RESTART](#-refheading-toc135629-1317547213) files contain a complete description of the reservoir state, they are also used in post processing software to visualize the reservoir solutions through time, for example by OPM ResInsight. And as the functionality of the both OPM Flow and the commercial simulator have expanded over time additional solution arrays have been added to the [RESTART](#-refheading-toc135629-1317547213) file to enable “restarts” \([POLYMER](#-refheading-toc38609-2267116897) – polymer saturations\), as well as to write out additional user specific solution arrays \(FIPOIL \- fluid in\-place oil array\), that are not necessary for a “restart”, but are consider useful in understanding the reservoir performance.
The frequency and type of data written to the [RESTART](#-refheading-toc135629-1317547213) file is controlled via the [RPTSCHED](#-refheading-toc268459-1366622701) and [RPTRST](#-refheading-toc210154-2884651453) keywords in the [SCHEDULE](#-refheading-toc43945-784232322), with the latter having greater functionality and flexibility. For example, to request that the standard restart data be written out every month using the [RPTRST](#-refheading-toc210154-2884651453) keyword:
```eclipse
--
--       RESTART CONTROL BASIC = 4 (YEARLY) 5 (MONTHLY)
--
RPTRST
         BASIC=5                                                               /
```

The next example requests that the standard restart data be written at every report time step until this switch is reset and all the restarts are kept. In addition to the standard data, the gas, oil, and water relative permeability data will also be written out at each report time step.
```eclipse
--
--       RESTART CONTROL BASIC = 4 (YEARLY) 5 (MONTHLY)
--
RPTRST
         BASIC=2  KRG   KRO   KRW                                             /
```

[RESTART](#-refheading-toc135629-1317547213) solution data is written out via two separate files; the [RESTART](#-refheading-toc135629-1317547213) Index file that specifies and defines the format and data type written to the [RESTART](#-refheading-toc135629-1317547213) Data file, and the [RESTART](#-refheading-toc135629-1317547213) Data file that contains the solution data for each active cell in the model for the requested report time steps. The commercial simulator writes out both files, where as OPM Flow only writes out the [RESTART](#-refheading-toc135629-1317547213) Data file, as the data can be read by most post\-processing software, including OPM ResInsight, using only the [RESTART](#-refheading-toc135629-1317547213) Data file as input. Secondly, both the commercial simulator and OPM Flow can be “restarted” using just the [RESTART](#-refheading-toc135629-1317547213) Data file.
The following sections outline the format for these two file types.
        - RESTART Index Files
    -
-

This file type is not supported or required by OPM Flow or OPM ResInsight to read or write restart files.

        - RESTART Data File Specification
    -
-

This file type contains the global and [LGR](#-refheading-toc55049-4106839650) grid solution data property data4
       Several keywords are used for both global and [LGR](#-refheading-toc55049-4106839650) grids, for example the INTEHEAD, LOGIHEAD, and DOUBHEAD keywords and [SOLUTION](#-refheading-toc43947-784232322) arrays. \([PRESSURE](#-refheading-toc135627-1317547213), [SGAS](#-refheading-toc137369-1317547213), [SOIL](#-refheading-toc137371-1317547213), and [SWAT](#-refheading-toc137373-1317547213)\) and the group, well, and connection data5
       The group, well, and connection production data is not stored on the [RESTART](#-refheading-toc135629-1317547213) file, but is instead stored on the [SUMMARY](#-refheading-toc43949-784232322) file. The [RESTART](#-refheading-toc135629-1317547213) file contains the group, well, and connection configurations as the they change versus time. For example, the status of a well \(OPEN or SHUT\), or the connections open to flow in a well..  The overall structure of this file is similar to the [INIT](#-refheading-toc45789-719036256) file, and the individual data keywords are structured as presented in Table A.20. 
| Reference | Section | Global Section keywords | Global Data keywords | [LGR](#-refheading-toc55049-4106839650) Data keywords | Global Section keywords | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| A.8.3 |  | SEQNUM |  |  |  | Global grid header keyword that defines the start of a [RESTART](#-refheading-toc135629-1317547213) global grid time step data set. |
| A.8.3 |  | INTEHEAD LOGIHEAD DOUBHEAD |  |  |  | Global grid header keyword that defines the integer, logical, and double precision variables for this header keyword. |
| A.8.4 |  | IGRP SGRP etc. |  |  |  | Group, well, and connection data status keywords for this reporting time step. |
| A.8.6 |  | IAAQ SAAQ ect. |  |  |  | Aquifer definition arrays. |
| A.8.7 |  | HIDDEN |  |  |  | Defines HIDDEN solution data, that is a list of solution arrays NOT to be read by post processing software. |
| A.8.8 |  | STARTSOL |  |  |  | This keyword marks the start of the solution variable section for the global grid. |
| A.8.8 |  |  | [PRESSURE](#-refheading-toc135627-1317547213) |  |  | Solution array section \([PRESSURE](#-refheading-toc135627-1317547213), [SGAS](#-refheading-toc137369-1317547213), [SOIL](#-refheading-toc137371-1317547213), [SWAT](#-refheading-toc137373-1317547213), etc.\) for the Global grid. |
| [SWAT](#-refheading-toc137373-1317547213) |  |  |  |  |  |  |
| etc. |  |  |  |  |  |  |
| A.8.8 |  | LGRNAMES |  |  |  | A list of LGRs in this report step. |
| A.8.8 |  | ENDSOL |  |  |  | Marks the end of the solution variable section for the global grid. |
| A.5.1 |  |  |  | [LGR](#-refheading-toc55049-4106839650) LGRHEADI LGRHEADQ LGRHEADD |  | [LGR](#-refheading-toc55049-4106839650) grid header keyword for that defines the start of a [RESTART](#-refheading-toc135629-1317547213) [LGR](#-refheading-toc55049-4106839650) data set. |
| A.8.3 |  |  |  | INTEHEAD LOGIHEAD DOUBHEAD |  | [LGR](#-refheading-toc55049-4106839650) header keyword and defines the integer, logical, and double precision variables for this header keyword. |
| A.8.4 |  |  |  | IGRP SGRP etc. |  | Group, well, and connection data status keywords for this reporting time step. |
| A.8.7 |  |  |  | HIDDEN |  | Defines HIDDEN solution data section. |
| A.8.8 |  |  |  | STARTSOL |  | Start of [LGR](#-refheading-toc55049-4106839650) solution array section. |
| A.8.8 |  |  |  | Solution Keywords | [PRESSURE](#-refheading-toc135627-1317547213) | [LGR](#-refheading-toc55049-4106839650) solution array section – same as global grid. |
| SWAT |  |  |  |  |  |  |
| etc. |  |  |  |  |  |  |
| A.8.8 |  |  |  | ENDSOL |  | End of the solution variable section for the current [LGR](#-refheading-toc55049-4106839650) grid. |
| A.5.1 |  |  |  | ENDLGR |  | End of current [LGR](#-refheading-toc55049-4106839650) section. |
| A.5.1 |  |  |  | [LGR](#-refheading-toc55049-4106839650) LGRHEADI LGRHEADQ LGRHEADD |  | [LGR](#-refheading-toc55049-4106839650) grid header keywords. |
| A.8.4 |  |  |  | IGRP SGRP etc. |  | Group, well, and connection data status keywords for this reporting time step. |
| A.8.7 |  |  |  | HIDDEN |  | Defines HIDDEN solution data section. |
| A.8.8 |  |  |  | STARTSOL |  | Start of solution array section. |
| A.8.8 |  |  |  | Solution Keywords | [PRESSURE](#-refheading-toc135627-1317547213) | [LGR](#-refheading-toc55049-4106839650) solution array section. |
|  |  | SWAT |  |  |  |  |
| etc. |  |  |  |  |  |  |
| A.8.8 |  |  |  | ENDSOL |  | End of the solution variable section. |
| A.5.1 |  |  |  | ENDLGR |  | End of current [LGR](#-refheading-toc55049-4106839650) section. |
| A.8.3 |  | SEQNUM |  |  |  | Global grid header keyword that defines the start of a [RESTART](#-refheading-toc135629-1317547213) global grid time step data set. |
| Notes: - Cells shaded in gray indicate the combination is not applicable and cells colored orange indicate that this item is not currently supported by OPM Flow. |  |  |  |  |  |  |

Table A.20: RESTART Data File Structure

The individual keywords are described in the following sections.

        - RESTART Data - Header Keywords
    -
-

This set of keywords6
       The [RESTART](#-refheading-toc135629-1317547213) Data – Header *k**eywords are* used both for global and [LGR](#-refheading-toc55049-4106839650) grids with the global grid data for the global grid and the individual [LGR](#-refheading-toc55049-4106839650) data for the [LGR](#-refheading-toc55049-4106839650) grids. The [LGR](#-refheading-toc55049-4106839650) data is preceded by a series of [LGR](#-refheading-toc55049-4106839650) header keywords and terminated by an [LGR](#-refheading-toc55049-4106839650) termination keyword.  are the first set of keywords that should be read or written to the [RESTART](#-refheading-toc135629-1317547213) file. This data set includes INTEHEAD, LOGIHEAD, and DOUBHEAD keywords that define versus parameters used in subsequent keywords in the [RESTART](#-refheading-toc135629-1317547213) file for the global and [LGR](#-refheading-toc55049-4106839650) grids.   
The structure for this type of keyword is defined in Table A.21.
| No. | keyword Name | [RESTART](#-refheading-toc135629-1317547213) Data \- Header keywords Table A.21 |  |  |  |  | Status or Value |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | SEQNUM | Global grid header keyword for the [RESTART](#-refheading-toc135629-1317547213) Data file that defines the start of a [RESTART](#-refheading-toc135629-1317547213) global grid time step data set for unified restart files only. |  |  |  |  | Optional |
| 1\-1 | Format | SEQNUM |  | 1 |  | INTE |  |
| 2\-1 | Data | Report time step number. |  |  |  |  | 0 |
|  | INTEHEAD | Global grid header keyword for the [RESTART](#-refheading-toc135629-1317547213) Data file that defines the  integer variables for this time step. NIHEAD is the number of entries associated with this keyword, and is dependent on the features being used in the model. Undefined values should be set to zero. |  |  |  |  | Required |
| 1\-1 | Format | INTEHEAD |  | NIHEAD |  | INTE |  |
| 2\-1 | Data | An encoded integer corresponding to the time the file was created. For files not originating from the commercial simulator, this value may be set to zero. |  |  |  |  | ISNUM |
| 2\-2 | Data | Simulator version, should be set to zero. |  |  |  |  | VERSION |
| 2\-3 | Data | Unit system used in the simulation, set to 1 for metric, 2 for field, and 3 for laboratory |  |  |  |  |  |
| 2\-4 to 2\-8 | Data | Undefined. |  |  |  |  | 0 |
| 2\-9 | Data | [DIMENS](#-refheading-toc20387-2267116897) key word in the [RUNSPEC](#-refheading-toc55591-1778172979) section \- the number of grid blocks in the x\-direction. |  |  |  |  | NX |
| 2\-10 | Data | [DIMENS](#-refheading-toc20387-2267116897) key word in the [RUNSPEC](#-refheading-toc55591-1778172979) section \- the number of grid blocks in the y\-direction. |  |  |  |  | NY |
| 2\-11 | Data | [DIMENS](#-refheading-toc20387-2267116897) key word in the [RUNSPEC](#-refheading-toc55591-1778172979) section \- the number of grid blocks in the z\-direction. |  |  |  |  | NZ |
| 2\-12 | Data | Number of global active cells in the model . |  |  |  |  | NACTIV |
| 2\-13 | Data | Not used. |  |  |  |  | 0 |
| 2\-14 | Data | Not used. |  |  |  |  | 0 |
| 2\-15 | Data | Type of phases in the model, set to 1 for oil, 2 for water, 3 for oil\-water, 4 for gas, 5 for oil\-gas, 6 for gas\-water, and 7 for oil\-water\-gas. |  |  |  |  | PHASE |
| 2\-16 | Data | Undefined. |  |  |  |  | 0 |
| 2\-17 | Data | Number of wells in the model. |  |  |  |  | NWELLS |
| 2\-18 | Data | Maximum number of grid block connections per well. |  |  |  |  | NCWMAX |
| 2\-19 | Data | Actual number of groups. |  |  |  |  | NGRP |
| 2\-20 | Data | Maximum number of wells belonging to a group in the model. |  |  |  |  | NWGMAX |
| 2\-21 | Data | Maximum number of groups for this model. |  |  |  |  | NGMAXZ |
| 2\-22 to 2\-24 | Data | Not used. |  |  |  |  |  |
| 2\-25 | Data | Number of values per well in the IWEL array \(default value is 97\). |  |  |  |  | NIWELZ |
| 2\-26 | Data | Number of values per well in the SWEL array. |  |  |  |  | NSWELZ |
| 2.27 | Data | Number of values per well in the XWEL array. |  |  |  |  | NXWELZ |
| 2\-28 | Data | Number of eight character words per well in the ZWEL array. |  |  |  |  | NZWELZ |
| 2\-29 to 2\-32 | Data | Not used. [nested table] |  |  |  |  |  |
| 2\-33 | Data | Number of values per completion in ICON array \(default 19\). |  |  |  |  | NICONZ |
| 2\-34 | Data | Number of values per completion in SCON array. |  |  |  |  | NSCONZ |
| 2\-35 | Data | Number of values per completion in XCON array. |  |  |  |  | NXCONZ |
| 2\-36 |  | Not used. |  |  |  |  | 0 |
| 2\-37 | Data | Number of values per group in IGRP array. |  |  |  |  | NIGRPZ |
| 2\-38 | Data | Number of values per group in SGRP array. |  |  |  |  | NISGRPZ |
| 2\-39 | Data | Number of values per group in XGRP array. |  |  |  |  | NIXGRPZ |
| 2\-40 | Data | Number of values per group in ZGRP array. |  |  |  |  | NIZGRPZ |
| 2\-41 |  | Not used. |  |  |  |  |  |
| 2\-42 | Data | Maximum number of analytical aquifer connections. |  |  |  |  | NCAMAX |
| 2\-43 | Data | Number of values per aquifer in the IAAQ array. |  |  |  |  | NIAAQZ |
| 2\-44 | Data | Number of values per aquifer in the SAAQ array. |  |  |  |  | NSAAQZ |
| 2\-45 | Data | Number of values per aquifer in the XAAQ array. |  |  |  |  | NXAAQZ |
| 2\-46 | Data | Number of values per aquifer connection in the ICAQ array. |  |  |  |  | NICAQZ |
| 2\-47 | Data | Number of values per aquifer connection in the SCAQ array. |  |  |  |  | NSCAQZ |
| 2\-48 | Data | Number of values per aquifer connection in the ACAQ array. |  |  |  |  | NXCAQZ |
| 2\-49 to 2\-51 |  | Not used. |  |  |  |  |  |
| 2\-52 | Data | Index indicating if group control is used or not \(1 – for [GCONPROD](#-refheading-toc146746-4203985108) group control, 2 for [GCONINJE](#-refheading-toc134874-2055188184) control,  or 0 if no group control\) |  |  |  |  | NGCTRL |
| 2\-53 to 2.58 |  | Undefined. |  |  |  |  |  |
| 2\-59 | Data | Parameter to determine the nominated phase for the guide rate. |  |  |  |  | NGRNPH |
| 2\-60 to 2\-64 |  | Undefined. |  |  |  |  |  |
| 2\-65 | Data | Calendar day of report step, the value should be greater than or equal to one and less than or equal to 31 for the calendar days. |  |  |  |  | DAY |
| 2\-66 | Data | Calendar month of report step, the value should be greater than or equal to one and less than or equal to 12 for the calendar month. |  |  |  |  | MONTH |
| 2\-67 | Data | Calendar year of report step, a positive four digit integer value of the start year, which must be specified fully by four digits, that is 2019. |  |  |  |  | YEAR |
| 2\-68 | Data | Numerical solver step, that is the number of solver steps the simulator has performed so far. |  |  |  |  | NUM\_SOLVER\_STEP |
| 2\-69 | Data | Report step. |  |  |  |  | REPORT\_STEP |
| 2\-70 to 2\-71 |  | Undefined. |  |  |  |  | 0 |
| 2\-72 | Data | Index for [WHISTCTL](#-refheading-toc268465-1366622701) keyword. |  |  |  |  | WHISTC |
| 2\-73 to 2\-80 |  | Undefined. |  |  |  |  |  |
| 2\-81 | Data | [TUNING](#-refheading-toc146744-4203985108) keyword in the [SCHEDULE](#-refheading-toc43945-784232322) section \- the maximum number of Newton iterations for a time step. |  |  |  |  | NEWTMX |
| 2\-82 | Data | [TUNING](#-refheading-toc146744-4203985108) keyword in the [SCHEDULE](#-refheading-toc43945-784232322) section \- the minimum number of Newton iterations for a time step |  |  |  |  | NEWTMN |
| 2\-83 | Data | [TUNING](#-refheading-toc146744-4203985108) keyword in the [SCHEDULE](#-refheading-toc43945-784232322) section \- the maximum number of linear iterations within a Newton iteration. |  |  |  |  | LITMAX |
| 2\-84 | Data | [TUNING](#-refheading-toc146744-4203985108) keyword in the [SCHEDULE](#-refheading-toc43945-784232322) section \- the minimum number of linear iterations within a Newton iteration. |  |  |  |  | LITMIN |
| 2\-85 |  | Undefined. |  |  |  |  |  |
| 2\-86 |  | Undefined. |  |  |  |  |  |
| 2\-87 | Data | [TUNING](#-refheading-toc146744-4203985108) keyword in the [SCHEDULE](#-refheading-toc43945-784232322) section \- the maximum number of iterations within a well flow calculation. |  |  |  |  | MXWSIT |
| 2\-88 | Data | [TUNING](#-refheading-toc146744-4203985108) keyword in the [SCHEDULE](#-refheading-toc43945-784232322) section \- the maximum number of iterations for solving the bottom\-hole pressure for wells under tubing head pressure control within a well flow calculation. |  |  |  |  | MXWPIT |
| 2\-89 |  | Undefined. |  |  |  |  |  |
| 2\-90 | Data | [REGDIMS](#-refheading-toc70161-327352552) and [TABDIMS](#-refheading-toc89327-327352552) keywords in the [RUNSPEC](#-refheading-toc55591-1778172979) section. The maximum number of regions in the [FIPNUM](#-refheading-toc77229-2752266063) region array. Note that this parameter may also be set on the [TABDIMS](#-refheading-toc89327-327352552) keyword as well. If NTFIP is set in both places then the maximum value should be used. |  |  |  |  | NTFIP |
| 2\-91 to 2\-94 |  | Undefined. |  |  |  |  |  |
| 2\-95 | Data | Simulator code used to generate the file, set to 100 for Schlumberger’s ECLIPSE 100, 300 for Schlumberger’s ECLIPSE 300, 500 for Schlumberger’s ECLIPSE 300 Thermal, 700 for Schlumberger’s INTERSECT simulator, 800 for Schlumberger’s FrontSim simulator, or a negative value for other simulators. OPM Flow uses a value of 100. |  |  |  |  | IPROG |
| 2\-96 to 2\-99 |  | Undefined. |  |  |  |  | 0 |
| 2\-100 | Data | [REGDIMS](#-refheading-toc70161-327352552) keyword in the [RUNSPEC](#-refheading-toc55591-1778172979) section. The total maximum number of regions. The [FIPNUM](#-refheading-toc77229-2752266063) regions are defined by \(2\-90\). If additional sets of fluid in\-place regions are used, as per the FIPxxx series of fluid in\-place region keywords, then NMFIPR is the sum of all [FIP](#-refheading-toc250560-252421755) regions. |  |  |  |  | NMFIPR |
| 2\-101 to 2\- 131 |  |  |  |  |  |  |  |
| 2\-132 | Data | [NETWORK](#-refheading-toc311583-1841740821) keyword in the [RUNSPEC](#-refheading-toc55591-1778172979) section \- maximum number of nodes in an extended network model or zero if the extended network option has not been activated. |  |  |  |  | NODMAX |
| 2\-133 | Data | [NETWORK](#-refheading-toc311583-1841740821) keyword in the [RUNSPEC](#-refheading-toc55591-1778172979) section \- maximum number of branches in an extended network model or zero if the extended network option has not been activated. |  |  |  |  | NBRMAX |
| 2\-134 | Data | Number of items per branch in the IBRAN array when the extended network model is active, or zero if the extended network option has not been activated. |  |  |  |  | NIBRAN |
| 2\-135 | Data | Number of items per branch in the RBRAN array when the extended network model is active, or zero if the extended network option has not been activated. |  |  |  |  | NRBRAN |
| 2\-136 | Data | Number of items per node in the INODE array when the extended network model is active, or zero if the extended network option has not been activated. |  |  |  |  | NINODE |
| 2\-137 | Data | Number of items per node in the RNODE array when the extended network model is active, or zero if the extended network option has not been activated. |  |  |  |  | NRNODE |
| 2\-138 | Data | Number of items per node in the ZNODE array when the extended network model is active, or zero if the extended network option has not been activated. |  |  |  |  | NZNODE |
| 2\-139 | Data | Number of items in the INOBR array. |  |  |  |  | NINOBR |
| 2\-140 to 2\-156 |  | Undefined. |  |  |  |  | 0 |
| 2\-157 | Data | The number of actions in the data set. |  |  |  |  | NO\_ACT |
| 2\-158 | Data | Maximum number of lines of schedule data for [ACTION](#-refheading-toc148342-63720426) keyword \- including [ENDACTIO](#-refheading-toc109407-332691817). |  |  |  |  | MAX\_LINES |
| 2\-159 | Data | Maximum number of eight character strings per input line of Action data \(rounded up from input deck\). |  |  |  |  | MAXSPRLINE |
| 2\-160 to 2\-162 |  | Undefined. |  |  |  |  |  |
| 2\-163 | Data | Maximum number of aquifer connections actually used in the model. |  |  |  |  | NGCAUS |
| 2\-164 | Data | Maximum number of wells in the model. |  |  |  |  | NWMAXZ |
| 2\-165 to 2\-174 |  | Undefined. |  |  |  |  | 0 |
| 2\-175 | Data | Number of multi\-segmented wells defined with the [WELSEGS](#-refheading-toc97661-3261743917) keyword in the [SCHEDULE](#-refheading-toc43945-784232322) section, for when multi\-segment wells have been activated, or zero otherwise. |  |  |  |  | NSEGWL |
| 2\-176 | Data | [WSEGDIMS](#-refheading-toc104259-3115110868) keyword in the [RUNSPEC](#-refheading-toc55591-1778172979) section \- maximum number of multi\-segment wells, for when multi\-segment wells have been activated, or zero otherwise. |  |  |  |  | NSWLMX |
| 2\-177 | Data | [WSEGDIMS](#-refheading-toc104259-3115110868) keyword in the [RUNSPEC](#-refheading-toc55591-1778172979) section \- maximum number of segments per multi\-segment well, for when multi\-segment wells have been activated, or zero otherwise. |  |  |  |  | NSEGMX |
| 2\-178 | Data | [WSEGDIMS](#-refheading-toc104259-3115110868) keyword in the [RUNSPEC](#-refheading-toc55591-1778172979) section \- maximum number of branches per multi\-segment well, including the main branch, for when multi\-segment wells have been activated, or zero otherwise. |  |  |  |  | NLBRMX |
| 2\-179 | Data | Number of entries per segment in the multi\-segment well ISEG array, for when multi\-segment wells have been activated, or zero otherwise. |  |  |  |  | NISEGZ |
| 2\-180 | Data | Number of entries per segment in the multi\-segment well RSEG array, for when multi\-segment wells have been activated, or zero otherwise. The number of data items per well segment in the RSEG restart vector is dependent on the number of active phases \(oil, gas, water\) in the simulation run. In particular, the following relations hold: |  |  |  |  | NRSEGZ |
| Scenario | Phases |  | NRSEGZ |  |  |  |  |
| Single Phase | Oil, Gas, or Water |  | 126 |  |  |  |  |
| Two Phase | Oil/Gas, Oil/Water, Gas/Water |  | 134 |  |  |  |  |
| Three Phase | Oil/Gas/Water |  | 146 |  |  |  |  |
| 2\-181 | Data | Number of entries per segment in the multi\-segment well ILBR array, for when multi\-segment wells have been activated, or zero otherwise. |  |  |  |  | NILBRZ |
| 2\-181 to 2\-206 |  | Undefined. |  |  |  |  | 0 |
| 2\-207 | Data | The first part of the current simulation time in the form HH:MM:SS, that is HH for hours. The value should be greater than or equal to zero and less than or equal to 23. |  |  |  |  | IHOURZ |
| 2\-208 | Data | The second part of the current simulation time in the form HH:MM:SS, that is MM for minutes. The value should be greater than or equal to zero and less than or equal to 59. |  |  |  |  | IMINTS |
| 2\-209 to 2\-223 |  | Undefined. |  |  |  |  | 0 |
| 2\-224 | Data | Number of INTEGER lines in the [AQUNUM](#-refheading-toc4430-421927891) data set. |  |  |  |  | NILAQN |
| 2\-225 | Data | Number of REAL lines in the [AQUNUM](#-refheading-toc4430-421927891) data set. |  |  |  |  | NIRAQN |
| 2\-226 |  | Undefined. |  |  |  |  | 0 |
| 2\-227 | Data | Number of entries in the [AQUNUM](#-refheading-toc4430-421927891) data set. |  |  |  |  | NUMAQN |
| 2\-228 to 2\-234 |  | Undefined. |  |  |  |  | 0 |
| 2\-235 | Data | Number of items in the ICOT array. |  |  |  |  | NICOTZ |
| 2\-236 | Data | Number of items in the XCOT array. |  |  |  |  | NXCOTZ |
| 2\-237 | Data | Number of items in the IWET array. |  |  |  |  | NIWETZ |
| 2\-238 | Data | Number of items in the XWET array. |  |  |  |  | NXWETZ |
| 2\-239 | Data | Number of items in the IGRT array. |  |  |  |  | NIGRTZ |
| 2\-240 | Data | Number of items in the XGRT array. |  |  |  |  | NXGRTZ |
| 2\-241 | Data | Number of tracers in the model plus two. |  |  |  |  | NSTRA2 |
| 2\-242 to 2\-245 |  | Undefined. |  |  |  |  | 0 |
| 2\-246 | Data | Maximum number of conditions per action. |  |  |  |  | MAXACTC |
| 2\-253 | Data | Maximum number of analytical aquifers in the model. |  |  |  |  | MAAQID |
| 2.254 to 2\-262 |  | Undefined. |  |  |  |  | 0 |
| 2\-263 | Data | Number of Field [UDQ](#-refheading-toc161095-2932703077) data \(parameters\). |  |  |  |  | NOFUDQS |
| 2\-264 | Data | Number of Group [UDQ](#-refheading-toc161095-2932703077) data \(parameters\). |  |  |  |  | NOGUDQS |
| 2\-265 |  | Undefined. |  |  |  |  |  |
| 2\-266 |  | Undefined. |  |  |  |  |  |
| 2\-267 | Data | Number of Well [UDQ](#-refheading-toc161095-2932703077) data \(parameters\). |  |  |  |  | NOWUDQS |
| 2\-268 | Data | Integer seed value for the RAND. |  |  |  |  | UDQPAR\_1 |
| 2\-269 |  | Undefined. |  |  |  |  |  |
| 2\-270 |  | Undefined. |  |  |  |  |  |
| 2.271 | Data | Maximum number of Chord segment links per multi\-segment well for when multi\-segment wells have been activated, or zero otherwise. |  |  |  |  | NCRDMX |
| 2\-272 to 2\-290 |  | Undefined. |  |  |  |  | 0 |
| 2\-291 |  | Number of integer IUADs. |  |  |  |  | NOIUADS |
| 2\-292 |  | Number of integer IUAPs. |  |  |  |  | NOIUAPS |
| 2\-293 to 2\-296 |  | Undefined. |  |  |  |  |  |
| 2\-297 | Data |  |  |  |  |  | RSEED |
| 2\-298 to 2\-410 |  | Undefined. |  |  |  |  |  |
| 2\-411 | Data | The third part of the current simulation time in the form HH:MM:SS, that is SS for seconds. The value should be greater than or equal to zero and less than or equal to 59. |  |  |  |  | ISECND |
|  | LOGIHEAD | Global grid keyword for the [RESTART](#-refheading-toc135629-1317547213) Data file that defines the logical variables \(T for true and F for false\) for this time step. NLHEAD is the number of entries associated with this keyword, and is dependent on the features being used in the model. Undefined items should be set to F \(False\). |  |  |  |  | Required |
| 1\-1 | Format | LOGIHEAD |  | NLHEAD |  | LOGI |  |
| 2\-1 | Data | Dissolved gas is present in the model indicator, set to T if present in the model else set to F. |  |  |  |  | [DISGAS](#-refheading-toc39767-2267116897) |
| 2\-2 | Data | Vaporized oil is present in the model indicator, set to T if present in the model else set to F. |  |  |  |  | [VAPOIL](#-refheading-toc56610-2267116897) |
| 2\-3 | Data | [SATOPTS](#-refheading-toc37029-327352552) in the [RUNSPEC](#-refheading-toc55591-1778172979) section \- directional relative permeability curves are active in the model. |  |  |  |  | DIRECT |
| 2\-4 | Data | [SATOPTS](#-refheading-toc37029-327352552) keyword in the [RUNSPEC](#-refheading-toc55591-1778172979) section \- reversible relative permeability curves \(black\-oil\) are active in the model. |  |  |  |  | IRREVERS |
| Radial grid geometry has been used for a compositional model indicator, set to T or F. Note that currently OPM Flow does not support radial grids and therefore this item should be set to F. |  |  |  |  | [RADIAL](#-refheading-toc51752-2905512151) |  |  |
| 2\-5 | Data | Radial grid geometry has been used for a black\-oil model indicator, set to T or F. Note that currently OPM Flow does not support radial grids and therefore this item should be set to F. |  |  |  |  | [RADIAL](#-refheading-toc51752-2905512151) |
| Reversible relative permeability \(compositional\) are active in the model. |  |  |  |  | IRREVERS |  |  |
| 2\-6 |  | Undefined. |  |  |  |  |  |
| 2\-7 | Data | Enable hysteresis indicator. |  |  |  |  | HYSER |
| 2.8 to 2\-14 |  | Undefined. |  |  |  |  | F |
| 2\-15 | Data | The dual porosity option has been activated in the model indicator, set to T or F. Note that currently OPM Flow does not support dual porosity grids and therefore this item should be set to F. |  |  |  |  | [DUALPORO](#-refheading-toc241173-1772380413) |
| 2\-16 |  | Undefined. |  |  |  |  | F |
| 2\-17 | Data | [ENDSCALE](#-refheading-toc68146-2267116897) keyword in the [RUNSPEC](#-refheading-toc55591-1778172979) section \- enable end\-point scaling indicator. |  |  |  |  | [ENDSCALE](#-refheading-toc68146-2267116897) |
| 2\-18 | Data | [ENDSCALE](#-refheading-toc68146-2267116897) keyword in the [RUNSPEC](#-refheading-toc55591-1778172979) section \- directional end\-point scaling indicator. |  |  |  |  | DIRECT |
| 2\-19 | Data | [ENDSCALE](#-refheading-toc68146-2267116897) keyword in the [RUNSPEC](#-refheading-toc55591-1778172979) section \- reversible end\-point scaling indicator. |  |  |  |  | IRREVERS |
| 2\-20 | Data | [SCALECRS](#-refheading-toc2086108-3315222525) keyword in the [PROPS](#-refheading-toc39329-784232322) section \- alternative three point end\-point scaling indicator. |  |  |  |  | [SCALECRS](#-refheading-toc2086108-3315222525) |
| 2\-21 to 2\-30 |  | Undefined. |  |  |  |  | F |
| 2\-31 | Data | Coal Bed Methane option in the black\-oil model indicator, set to T or F. Note that currently OPM Flow does not support the Coal Bed Methane option and therefore this item should be set to F. |  |  |  |  | F |
| 2\-32 to 2\-38 |  | Undefined. |  |  |  |  | F |
| 2\-39 | Data | Constant oil compressibility \([PVCDO](#-refheading-toc104054-57619843)\) indicator. |  |  |  |  | ConstCo |
| 2\-40 to 2\-75 |  | Undefined. |  |  |  |  |  |
| 2\-76 | Data | Multi\-segment wells are present in the model indicator. |  |  |  |  | HasMSWells |
| 2\-77 to 2\-127 |  | Undefined. |  |  |  |  |  |
| 2\-128 |  | Coal Bed Methane option in the compositional model indicator, set to T or F. Note that currently OPM Flow does not support the Coal Bed Methane option and therefore this item should be set to F. |  |  |  |  | F |
|  | DOUBHEAD | Global grid keyword for the [RESTART](#-refheading-toc135629-1317547213) Data file that defines the double precision REAL variables for this time step. NDHEAD is the number of entries associated with this keyword, and is dependent on the features being used in the model. Undefined values should be set to zero. |  |  |  |  | Required |
| 1\-1 | Format | DOUBHEAD |  | NDHEAD |  | DOUB |  |
| 2\-1 | Data | The simulation REPORT [TIME](#-refheading-toc1252966-4250154414) STEP, expressed in days for all units, except for the [LAB](#-refheading-toc72458-2267116897) system of units which should be expressed in hours. |  |  |  |  |  |
| 2\-2 | Data | [TUNING](#-refheading-toc146744-4203985108) keyword in the [SCHEDULE](#-refheading-toc43945-784232322) section \- maximum length of next time step. |  |  |  |  | TSINIT |
| 2\-3 | Data | [TUNING](#-refheading-toc146744-4203985108) keyword in the [SCHEDULE](#-refheading-toc43945-784232322) section \- maximum length of time step after next. |  |  |  |  | TSMAXZ |
| 2\-4 | Data | [TUNING](#-refheading-toc146744-4203985108) keyword in the [SCHEDULE](#-refheading-toc43945-784232322) section \- minimum length of all time steps. |  |  |  |  | TSMINZ |
| 2\-5 | Data | [TUNING](#-refheading-toc146744-4203985108) keyword in the [SCHEDULE](#-refheading-toc43945-784232322) section \- minimum length of all chopped time steps. |  |  |  |  | TSMCHP |
| 2\-6 | Data | [TUNING](#-refheading-toc146744-4203985108) keyword in the [SCHEDULE](#-refheading-toc43945-784232322) section \- maximum growth rate a time step can be increased by, subject to the maximum allowable time step size set by TSMAXZ. |  |  |  |  | TSFMAX |
| 2\-7 | Data | [TUNING](#-refheading-toc146744-4203985108) keyword in the [SCHEDULE](#-refheading-toc43945-784232322) section \- minimum decay rate a time step can be decreased by, subject to the minimum allowable time step size set by TSMINZ. |  |  |  |  | TSFMIN |
| 2\-8 | Data | [TUNING](#-refheading-toc146744-4203985108) keyword in the [SCHEDULE](#-refheading-toc43945-784232322) section \- the decay rate a time step can be decreased by after the number of target iterations has been exceeded. |  |  |  |  | TSFCNV |
| 2\-9 | Data | [TUNING](#-refheading-toc146744-4203985108) keyword in the [SCHEDULE](#-refheading-toc43945-784232322) section \- the time truncation error target. |  |  |  |  | TRGTTE |
| 2\-10 | Data | [TUNING](#-refheading-toc146744-4203985108) keyword in the [SCHEDULE](#-refheading-toc43945-784232322) section \- thee non\-linear convergence error. |  |  |  |  | TRGCNV |
| 2\-11 | Data | [TUNING](#-refheading-toc146744-4203985108) keyword in the [SCHEDULE](#-refheading-toc43945-784232322) section \- the target material balance error. |  |  |  |  | TRGMBE |
| 2\-12 | Data | [TUNING](#-refheading-toc146744-4203985108) keyword in the [SCHEDULE](#-refheading-toc43945-784232322) section \- the linear convergence error target. |  |  |  |  | TRGLCV |
| 2\-13 to 2\-16 |  | Undefined. |  |  |  |  |  |
| 2\-17 | Data | [TUNING](#-refheading-toc146744-4203985108) keyword in the [SCHEDULE](#-refheading-toc43945-784232322) section \- the maximum time truncation error. |  |  |  |  | XXXTTE |
| 2\-18 | Data | [TUNING](#-refheading-toc146744-4203985108) keyword in the [SCHEDULE](#-refheading-toc43945-784232322) section \- the maximum non\-linear convergence error. |  |  |  |  | XXXCNV |
| 2\-19 | Data | [TUNING](#-refheading-toc146744-4203985108) keyword in the [SCHEDULE](#-refheading-toc43945-784232322) section \- the maximum mass balance error. |  |  |  |  | XXXMBE |
| 2\-20 | Data | [TUNING](#-refheading-toc146744-4203985108) keyword in the [SCHEDULE](#-refheading-toc43945-784232322) section \- the maximum linear convergence error. |  |  |  |  | XXXLCV |
| 2\-21 | Data | [TUNING](#-refheading-toc146744-4203985108) keyword in the [SCHEDULE](#-refheading-toc43945-784232322) section \- the maximum well flow convergence error. |  |  |  |  | XXXWFL |
| 2\-22 to 2\-82 |  | Undefined. |  |  |  |  |  |
| 2\-83 | Data | [TUNING](#-refheading-toc146744-4203985108) keyword in the [SCHEDULE](#-refheading-toc43945-784232322) section \- target pressure change within a time step. |  |  |  |  | TRGDPR |
| 2\-84 | Data | [TUNING](#-refheading-toc146744-4203985108) keyword in the [SCHEDULE](#-refheading-toc43945-784232322) section \- time step growth factor of the time step after a convergence failure. |  |  |  |  | TFDIFF |
| 2\-85 | Data | [TUNING](#-refheading-toc146744-4203985108) keyword in the [SCHEDULE](#-refheading-toc43945-784232322) section \- the maximum pressure change at the last Newton iteration. |  |  |  |  | DDPLIM |
| 2.86 | Data | [TUNING](#-refheading-toc146744-4203985108) keyword in the [SCHEDULE](#-refheading-toc43945-784232322) section \- the maximum saturation change at the last Newton iteration. |  |  |  |  | DDSLIM |
| 2.87 |  | Undefined. |  |  |  |  |  |
| 2\-88 | Data | [GUIDERAT](#-refheading-toc193039-2026549522) keyword in the [SCHEDULE](#-refheading-toc43945-784232322) section \- guide rate parameter A. |  |  |  |  | GRPAR\_A |
| 2\-89 | Data | [GUIDERAT](#-refheading-toc193039-2026549522) keyword in the [SCHEDULE](#-refheading-toc43945-784232322) section \- guide rate parameter B. |  |  |  |  | GRPAR\_B |
| 2\-90 | Data | [GUIDERAT](#-refheading-toc193039-2026549522) keyword in the [SCHEDULE](#-refheading-toc43945-784232322) section \- guide rate parameter C. |  |  |  |  | GRPAR\_C |
| 2\-91 | Data | [GUIDERAT](#-refheading-toc193039-2026549522) keyword in the [SCHEDULE](#-refheading-toc43945-784232322) section \- guide rate parameter D. |  |  |  |  | GRPAR\_D |
| 2\-92 | Data | [GUIDERAT](#-refheading-toc193039-2026549522) keyword in the [SCHEDULE](#-refheading-toc43945-784232322) section \- guide rate parameter E. |  |  |  |  | GRPAR\_E |
| 2\-93 | Data | [GUIDERAT](#-refheading-toc193039-2026549522) keyword in the [SCHEDULE](#-refheading-toc43945-784232322) section \- guide rate parameter F. |  |  |  |  | GRPAR\_F |
| 2\-94 to 2\-97 |  | Undefined. |  |  |  |  |  |
| 2.98 | Data | Guide rate parameter delay interval. |  |  |  |  | GRPAR\_INT |
| 2\-99 |  | Undefined. |  |  |  |  |  |
| 2\-100 | Data | [TUNING](#-refheading-toc146744-4203985108) keyword in the [SCHEDULE](#-refheading-toc43945-784232322) section \- the maximum throughput ratio over a time step. |  |  |  |  | THRURPT |
| 2\-101 | Data | [TUNING](#-refheading-toc146744-4203985108) keyword in the [SCHEDULE](#-refheading-toc43945-784232322) section \- maximum tolerable pressure change within a time step. |  |  |  |  | XXXDPR |
| 2\-102 | Data | [TUNING](#-refheading-toc146744-4203985108) keyword in the [SCHEDULE](#-refheading-toc43945-784232322) section \- the target fluid in\-place error in Local Grid Refinements. |  |  |  |  | TRGFIP |
| 2\-103 | Data | [TUNING](#-refheading-toc146744-4203985108) keyword in the [SCHEDULE](#-refheading-toc43945-784232322) section \- target surfactant change when the Surfactant Model is active in the run. |  |  |  |  | TRGSFT |
| 2\-104 to 2\-144 |  | Undefined. |  |  |  |  |  |
| 2\-145 | Data | Guide rate parameter damping factor. |  |  |  |  | GRPAR\_DAMP |
| 2\-146 to 2\-161 |  | Undefined. |  |  |  |  |  |
| 2\-161 | Data | The simulation [START](#-refheading-toc39156-327352552) time, expressed in days for all units, except for the [LAB](#-refheading-toc72458-2267116897) system of units which should expressed in hours. |  |  |  |  |  |
| 2\-162 | Data | Cumulative time from the start of the simulation, expressed in days for all units, except for the [LAB](#-refheading-toc72458-2267116897) system of units which should expressed in hours. That is the sum of values \(2\-1\) and \(2\-161\). |  |  |  |  |  |
| 2\-163 to 2\-212 |  | Undefined. |  |  |  |  | 0 |
| 2\-213 | Data | [UDQPARAM](#-refheading-toc161093-2932703077) item number 2 \(Permitted range \(\+/\-\) of user\-defined quantities\). |  |  |  |  | UDQPAR\_2 |
| 2\-214 | Data | [UDQPARAM](#-refheading-toc161093-2932703077) item number 3 \(Value given to undefined elements when outputting data\). |  |  |  |  | UDQPAR\_3 |
| 2\-215 | Data | [UDQPARAM](#-refheading-toc161093-2932703077) item number 4 \(fractional equality tolerance used in == <= etc. functions\). |  |  |  |  | UDQPAR\_4 |
| Notes: - Rows shaded in gray indicate the start of a keyword. - Cells colored red in the No. column indicate that this item is either “Not Used” or “Undefined”. - For formatted output all character variables, including the keyword should be enclosed in single quotes, for example the DOUBHEAD keyword should be written out as ‘DOUBHEAD’. |  |  |  |  |  |  |  |

Table A.21: RESTART Data \- Header Keywords

#### <a id="-refheading-toc716957-3964674244"></a>Example: RESTART Data \- Header Keywords

The following example shows a typical formatted [RESTART](#-refheading-toc135629-1317547213) Data \- Header keywords.
```eclipse
 'INTEHEAD'         249 'INTE'
  -955283513      200400           2       -2345       -2345       -2345
       -2345       -2345          10          10           1         100
          10       -2345           7       -2345           0           1
           0           2           2           0           0           0
         110         108         109           3          97          93
       -2345       -2345          19          38          53       -2345
          97          93         146           5           0           1
          15          24           8           5           2           4
           0           0           0           0           0           0
           0           0           0           0           0           0
           0           0           0           0          19          10
        1982           0           0           0           1           0
           0           0           0           0           1          10
           0           0          12           1          25           1
       -2345       -2345           8           8           5           1
           2           1           2           0         100           2
           7           0         -11           1           0           1
           0           0           0          10          10           1
         100           1           1           1           1          10
          10           1          19           1           0           0
           0           0           0           1           1           1
           0           0           0           0           0           0
           0          14          10          10          16           1
           1           1           1           1           2           1
           1           1           1           1           1          31
         108           0           0           0           0           0
           0          50          10           4           5           9
           0           2           8           8          12           1
          25           1      -32767      -32767      -32767      -32767
           0           1           1           1          18          86
           5           1           1           1           1          18
          86      -32767      -32767           0           0         109
          53         146           8           0          19         110
           0           0           1           1          86           0
           0           0           0           0           0           1
           0           0           0           0           1           0
           0           1           0          -1          12           0
           0          10          13           1           0           0
           0           0           2           0           0        3600
           1           6           1          10           1          10
           1           1           1           0          30           3
          18          10           9
 'LOGIHEAD'          79 'LOGI'
  T  F  F  T  F  F  F  F  T  F  F  F  F  F  F  F  T  F  T  F  F  F  F  F  F
  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F
  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F
  F  F  F  F
 'DOUBHEAD'         185 'DOUB'
   0.00000000000000D+00   0.10000000000000D+01   0.36500000000000D+03
   0.10000000149012D+00   0.15000000596046D+00   0.30000000000000D+01
   0.30000001192093D+00   0.10000000149012D+00   0.10000000149012D+00
  ………………………….……………..
  -0.10000000200409D+21   0.10000000000000D+01   0.10000000000000D+01
   0.10000000000000D+01   0.00000000000000D+00   0.00000000000000D+00
   0.10000000000000D+01   0.10000000000000D-03
```

End of Example
        - RESTART Data – Group, Well, and Connection Data Keywords
    -
-

The Restart Data – Well and Group Completion Keywords7
       The [RESTART](#-refheading-toc135629-1317547213) Data – Group, Well and Connection *k**eywords are* used both for global and [LGR](#-refheading-toc55049-4106839650) grids with groups, well, and connection data for the global grid, and wells and connection data for wells contained in the individual [LGR](#-refheading-toc55049-4106839650)s for the [LGR](#-refheading-toc55049-4106839650) grids. The [LGR](#-refheading-toc55049-4106839650) data is preceded by a series of [LGR](#-refheading-toc55049-4106839650) header keywords and terminated by an [LGR](#-refheading-toc55049-4106839650) termination keyword.  define various parameters associated with groups, wells, and connection keywords in the [RESTART](#-refheading-toc135629-1317547213) file for both global and [LGR](#-refheading-toc55049-4106839650) grids. 
The structure for this type of keyword is based on the data type as summarized below:
        - The group data set keywords are specified in Table A.22 and consists of the IGRP, SGRP, XGRP,  and ZGRP keywords.
        - Table A.23 contains the multi\-segment well keywords that consist of the ISEG, RSEG, ILBS, ILBR, and ICRD keywords.
        - For wells the keywords are IWEL, SWEL, XWEL, and ZWEL and Table A.24 describes these keywords.
        - Well connection keywords are specified in Table A.25 and consist of the ICON, SCON, and XCON keywords.
        - Tracer keywords are listed in Table A.26 and consists of the ICOT, XCOT, IWET, XWET, IGRT, and XGRT keywords.
        - Finally, the network keywords INODE, IBRAN, INOBR, RNODE, RBRAN, and ZNODE are specified in Table A.27.
    -
-

Note that if multi\-segment wells, tracers, and networks are absent from the simulation deck then this data will not be written to the [RESTART](#-refheading-toc135629-1317547213) Data file.
The following table outlines the keywords for groups.
| No. | keyword Name | [RESTART](#-refheading-toc135629-1317547213) Data – Group, Well, and Connection keywords Table A.22 \- Group Keywords |  |  | Status or Value |
| --- | --- | --- | --- | --- | --- |
|  | IGRP | Keyword defines the integer Group, well, and connection data for this time step. Undefined values should be set to zero. |  |  | Required |
| 1\-1 | Format | IGRP | NSGRPZ x NGMAXZ | INTE |  |
| 2\-1 to 2\-NWGMAX | Data | Integer group data array IGRP\(NIGRPZ, NGMAXZ\) where NIGRPZ and NGMAXZ are defined on the INTEHEAD keyword. Entries 1 to NWGMAX define the index of each well in the group, if this is a well group, or the index of each child group in this group if it is a node group. Note that undefined items in this array may be set to zero. |  |  |  |
| 2 \- \(NWGMAX \+ 1\) |  |  |  |  |  |
| 2 \- \(NWGMAX \+ 2\) |  | - NONE or [FIELD](#-refheading-toc71850-2267116897). - Oil rate. - Water rate. - Gas rate. - Liquid rate. - Reservoir volume rate. |  |  |  |
| 2 \- \(NWGMAX \+ 6\) |  | - If group is injection group. |  |  |  |
| 2 \- \(NWGMAX \+ 7\) |  | - No group guide rate, or the group is the [FIELD](#-refheading-toc71850-2267116897) group. - Unknown. - Unknown. - Unknown. - Unknown. - Unknown. - Unknown. - Unknown. - Group guide rate defined and higher level guide rate control. |  |  |  |
| 2 \- \(NWGMAX \+ 8\) |  | - [FIELD](#-refheading-toc71850-2267116897) group. |  |  |  |
| 2 \- \(NWGMAX \+ 11\) |  | - NONE or [FIELD](#-refheading-toc71850-2267116897). - Oil rate. - Water rate. - Gas rate. - Liquid rate. - Reservoir volume rate. |  |  |  |
| 2 \- \(NWGMAX \+ 17\) |  | - NONE or [FIELD](#-refheading-toc71850-2267116897). - Rate. - Reservoir volume rate. - Re\-injection fraction. - Voidage replacement. |  |  |  |
| 2 \- \(NWGMAX \+ 18\) |  |  |  |  |  |
| 2 \- \(NWGMAX \+ 22\) |  | - NONE or [FIELD](#-refheading-toc71850-2267116897). - Rate. - Reservoir volume rate. - Re\-injection fraction. - Voidage replacement. |  |  |  |
| 2 \- \(NWGMAX \+ 23\) |  |  |  |  |  |
| 2 \- \(NWGMAX \+ 27\) |  | - for a well group. - for a node group. - for a satellite group. - for a slave group. |  |  |  |
| 2 \- \(NWGMAX \+ 28\) |  |  |  |  |  |
| 2 \- \(NWGMAX \+ 29\) |  |  |  |  |  |
| 2 \- \(NWGMAX \+ 34\) |  |  |  |  |  |
| 2 \- \(NWGMAX \+ 89\) |  |  |  |  |  |
|  | SGRP | Keyword defines the real group data array SGRP\(NIGRPZ, NGMAXZ\) where NIGRPZ and NGMAXZ are defined on the INTEHEAD keyword. |  |  | Required |
| 1\-1 | Format | SGRP | NSGRPZ x NGMAXZ | REAL |  |
| 2\-1 to 2\-6 |  | Undefined. |  |  |  |
| 2\-7 | Data | Group's oil production target/limit. |  |  |  |
| 2\-8 | Data | Group's water production target/limit. |  |  |  |
| 2\-9 | Data | Group's gas production target/limit. |  |  |  |
| 2\-10 | Data | Group's liquid production target/limit. |  |  |  |
| 2\-11 | Data | Group's oil surface volume injection rate target/limit. |  |  |  |
| 2\-12 | Data | Group's oil reservoir volume injection rate target/limit. |  |  |  |
| 2\-13 | Data | Group's oil re\-injection fraction target/limit. |  |  |  |
| 2\-14 | Data | Group's oil voidage injection fraction target/limit. |  |  |  |
| 2\-15 |  | Undefined. |  |  |  |
| 2\-16 | Data | Group's water surface volume injection rate target/limit. |  |  |  |
| 2\-17 | Data | Group's water reservoir volume injection rate target/limit. |  |  |  |
| 2\-18 | Data | Group's water re\-injection fraction target/limit. |  |  |  |
| 2\-19 | Data | Group's water voidage injection fraction target/limit. |  |  |  |
| 2\-20 |  | Undefined. |  |  |  |
| 2\-21 | Data | Group's gas surface volume injection rate target/limit. |  |  |  |
| 2\-22 | Data | Group's gas reservoir volume injection rate target/limit. |  |  |  |
| 2\-23 | Data | Group's gas re\-injection fraction target/limit. |  |  |  |
| 2\-24 | Data | Group's gas voidage injection fraction target/limit. |  |  |  |
|  | XGRP | Keyword defines the double precision group data array XGRP\(NIGRPZ, NGMAXZ\) where NIGRPZ and NGMAXZ are defined on the INTEHEAD keyword. |  |  | Required |
| 1\-1 | Format | XGRP | NSGRPZ x NGMAXZ | DOUB |  |
| 2\-1 | Data | Group's oil production rate. |  |  |  |
| 2\-2 | Data | Group's water production rate. |  |  |  |
| 2\-3 | Data | Group's gas production rate. |  |  |  |
| 2\-4 | Data | Group's liquid production rate. |  |  |  |
| 2\-5 |  | Undefined. |  |  |  |
| 2\-6 | Data | Group's water injection rate. |  |  |  |
| 2\-7 | Data | Group's gas injection rate. |  |  |  |
| 2\-8 |  | Undefined. |  |  |  |
| 2\-9 | Data | Group's producing water cut. |  |  |  |
| 2\-10 | Data | Group's producing gas/oil ratio. |  |  |  |
| 2\-11 | Data | Group's total cumulative oil production. |  |  |  |
| 2\-12 | Data | Group's total cumulative water production. |  |  |  |
| 2\-13 | Data | Group's total cumulative gas production. |  |  |  |
| 2\-14 | Data | Group's total cumulative reservoir voidage production. |  |  |  |
| 2\-15 | Data | Undefined. |  |  |  |
| 2\-16 | Data | Group's total cumulative water injection. |  |  |  |
| 2\-17 | Data | Group's total cumulative gas injection. |  |  |  |
| 2\-18 | Data | Group's total cumulative reservoir volume injection. |  |  |  |
| 2\-19 |  | Undefined. |  |  |  |
| 2\-20 |  | Undefined. |  |  |  |
| 2\-21 |  | Undefined. |  |  |  |
| 2\-22 |  | Undefined. |  |  |  |
| 2\-23 | Data | Group's oil production potential. |  |  |  |
| 2\-24 | Data | Group's water production potential. |  |  |  |
| 2\-25 to 2\-86 |  | Undefined. |  |  |  |
| 2\-86 | Data | Group's producer guide rate for oil. |  |  |  |
| 2\-87 | Data | Group's producer guide rate for water. |  |  |  |
| 2\-88 | Data | Group's producer guide rate for gas. |  |  |  |
| 2\-89 | Data | Group's producer guide rate for reservoir voidage volume. |  |  |  |
| 2\-90 | Data | Group's injection guide rate for oil. |  |  |  |
| 2\-91 |  | Undefined. |  |  |  |
| 2\-92 | Data | Group's injection guide rate for water. |  |  |  |
| 2\-93 | Data | Second copy of group's injection guide rate for water. Not fully characterized. |  |  |  |
| 2\-94 | Data | Groups injection guide rate for gas. |  |  |  |
| 2\-95 to 2\-127 |  | Undefined. |  |  |  |
| 2\-128 | Data | Second copy of group's producer guide rate for oil. Not fully characterized. |  |  |  |
| 2\-129 | Data | Second copy of group's producer guide rate for water. Not fully characterized. |  |  |  |
| 2\-130 | Data | Second copy of group's producer guide rate for gas. Not fully characterized. |  |  |  |
| 2\-131 | Data | Second copy of group's producer guide rate for reservoir voidage volume. Not fully characterized. |  |  |  |
| 2\-132 to 2\-135 |  | Undefined. |  |  |  |
| 2\-136 | Data | Group's total cumulative oil production \(observed/historical rates\). |  |  |  |
| 2\-137 |  | Undefined. |  |  |  |
| 2\-138 |  | Undefined. |  |  |  |
| 2\-139 |  | Undefined. |  |  |  |
| 2\-140 | Data | Group's total cumulative water production \(observed/historical rates\). |  |  |  |
| 2\-141 | Data | Group's total cumulative water injection \(observed/historical rates\). |  |  |  |
| 2\-142 |  | Undefined. |  |  |  |
| 2\-143 |  | Undefined. |  |  |  |
| 2\-144 | Data | Group's total cumulative gas production \(observed/historical rates\). |  |  |  |
| 2\-145 | Data | Group's total cumulative gas injection \(observed/historical rates\). |  |  |  |
|  | ZGRP | Keyword defines the character GROUP data for this keyword. |  |  | Required |
| 1\-1 | Format | ZGRP | NSGRPZ x NGMAXZ | CHAR |  |
| 2\-1 | Data | Character group data array ZGRP\(NIGRPZ, NGMAXZ\) where NIGRPZ and NGMAXZ are defined on the INTEHEAD keyword. |  |  |  |

Table A.22: RESTART Data – Group, Well, and Connection Keywords \(Groups\)

The next table \(Table A.23\) contains the multi\-segment well keywords that consist of the ISEG, RSEG, ILBS, ILBR, and ICRD keywords.
| No. | keyword Name | [RESTART](#-refheading-toc135629-1317547213) Data – Group, Well, and Connection keywords Table A.23 \- Multi\-Segment Well Keywords |  |  | Status or Value |
| --- | --- | --- | --- | --- | --- |
|  | ISEG | Integer multi\-segment well data array ISEG\(NISEGZ, NSEGMX, NSWLMX\) where NISEGZ, NSEGMX, and NSWLMX are defined on the INTEHEAD keyword. |  |  | Optional |
| 1\-1 | Format | ISEG | NISEGZ x NSEGMX x NSWLMX | INTE |  |
| 2\-1 | Data | Segment number \(one\-based\). Special ordering – see code for details. |  |  |  |
| 2\-2 | Data | Outlet segment \(one\-based\). Defines the multi\-segment outlet segment number starting with 0 for the segment nearest wellhead \(NISEGZ = 2\). |  |  |  |
| 2\-3 | Data | Inflow segment current branch \(one\-based\). |  |  |  |
| 2\-4 | Data | Branch number \(one\-based\). Defines the multi\-segment branch for this segment number 1 for main stem and 0 if not active \(NISEGZ = 4\). |  |  |  |
| 2\-5 to 2\-11 |  | Undefined. |  |  |  |
| 2\-12 | Data | Segment type. |  |  |  |
| 2\-123 to 2\-18 |  | Undefined. |  |  |  |
| 2\-19 | Data | ICD scaling mode. |  |  |  |
| 2\-20 | Data | ICD open/shut flag. |  |  |  |
|  | RSEG | Double precision multi\-segment well data array RSEG\(NISEGZ, NSEGMX, NSWLMX\) where NISEGZ, NSEGMX, and NSWLMX are defined on the INTEHEAD keyword. |  |  | Optional |
| 1\-1 | Format | RSEG | NISEGZ x NSEGMX x NSWLMX | DOUB |  |
| 2\-1 | Data | Segment's distance to outlet. |  |  |  |
| 2\-2 | Data | Segment's depth differential to outlet. |  |  |  |
| 2\-3 | Data | Internal diameter of segment. |  |  |  |
| 2\-4 | Data | Roughness parameter of segment. |  |  |  |
| 2\-5 | Data | Cross\-sectional area of segment. |  |  |  |
| 2\-6 | Data | Physical volume of segment. |  |  |  |
| 2\-7 | Data | Segment's distance to BHP reference node. |  |  |  |
| 2\-8 | Data | Segment's depth differential to BHP reference node. |  |  |  |
| 2\-9 | Data | Normalized total segment flow rate. |  |  |  |
| 2\-10 | Data | Normalized water flow rate fraction. |  |  |  |
| 2\-11 | Data | Normalized gas flow rate fraction. |  |  |  |
| 2\-12 | Data | Segment pressure. |  |  |  |
| 2\-13 to 2\-30 |  | Undefined. |  |  |  |
| 2\-31 | Data | Very close to normalized water flow rate fraction. |  |  |  |
| 2\-32 to 2\-39 |  | Undefined. |  |  |  |
| 2\-40 | Data | Undefined. |  |  |  |
| 2\-41 | Data | Length of valve. |  |  |  |
| 2\-42 | Data | Cross\-sectional area of valve. |  |  |  |
| 2\-43 | Data | Valve's dimensionless flow coefficient. |  |  |  |
| 2\-44 | Data | Maximal cross\-sectional valve area. |  |  |  |
| 2\-45 to 2\-86 |  | Undefined. |  |  |  |
| 2\-87 | Data | Device base strength. |  |  |  |
| 2\-88 |  | Undefined. |  |  |  |
| 2\-89 | Data | Calibrated fluid density. |  |  |  |
| 2\-90 | Data | Calibrated fluid viscosity. |  |  |  |
| 2\-91 | Data | Critical water fraction. |  |  |  |
| 2\-92 | Data | Transition region width. |  |  |  |
| 2\-93 | Data | Maximum emulsion ratio. |  |  |  |
| 2\-94 to 2\-97 |  | Undefined. |  |  |  |
| 2\-98 | Data | Maximum valid flow rate. |  |  |  |
| 2\-99 to 2\-102 |  | Undefined. |  |  |  |
| 2\-103 | Data | ICD length. |  |  |  |
| 2\-104 | Data | Valve area fraction. |  |  |  |
| 2\-105 to 2\-111 |  | Undefined. |  |  |  |
|  | ILBS | Integer multi\-segment well data array for lateral branches ILBR\(NLBRMX, NSWLMX\) where NLBRMX and NSWLMX are defined on the INTEHEAD keyword. |  |  | Optional |
| 1\-1 | Format | ILBS | NLBRMX x  NSWLMX | INTE |  |
| 2\-1 to no\_branches | Data | The segment number of the first segment in the branch for branch number two and upwards. |  |  |  |
|  | ILBR | Integer multi\-segment well data array for chords ILBR\(NILBRZ, NLBRMX, NSWLMX\) where NILBRZ, NLBRMX, and NSWLMX are defined on the INTEHEAD keyword. |  |  | Optional |
| 1\-1 | Format | ILBR | NILBRZ x NLBRMX x NSWLMX | INTE |  |
| 2\-1 | Data | Outlet segment number. |  |  |  |
| 2\-2 | Data | Number of segments in the branch. |  |  |  |
| 2.3 | Data | First segment in branch. |  |  |  |
| 2\-4 | Data | Last segment in branch. |  |  |  |
| 2\-5 | Data | Branch number minus one. |  |  |  |
|  | ICRD | Integer multi\-segment well data array for chords ICRD\(2, NCRDMX, NSWLMX\) where NCRDMX, and NSWLMX are defined on the INTEHEAD keyword. |  |  | Optional |
| 1\-1 | Format | ILBR | 2 x NCRDMX x NSWLMX | INTE |  |
| 2\-1 | Data | ICRD \(2, NCRDMX, NSWLMX\) array. |  |  |  |

Table A.23: RESTART Data – Group, Well, and Connection Keywords \(Multi\-Segment Wells\)

The wells keywords are IWEL, SWEL, XWEL, and ZWEL and Table A.24 below describes these keywords in detail.
| No. | keyword Name | [RESTART](#-refheading-toc135629-1317547213) Data – Group, Well, and Connection keywords Table A.24 \- Well Keywords |  |  | Status or Value |
| --- | --- | --- | --- | --- | --- |
|  | IWEL | Well integer data array IWEL\(NIWELZ, NWELLS\) where NIWELX and NWELS are defined on the INTEHEAD keyword. Undefined values should be set to zero. |  |  |  |
| 1\-1 | Format | IWEL | NIWELZ x NWELLS | INTE | Required |
| 2\-1 | Data | Defines the location of the wellhead in the grid for the I dimension \(NIWELZ = 1\). |  |  |  |
| 2\-2 | Data | Defines the location of the wellhead in the grid for the J dimension \(NIWELZ = 2\). |  |  |  |
| 2\-3 | Data | Layer ID \(one\-based\) of top/first connection. |  |  |  |
| 2\-4 | Data | Layer ID \(one\-based\) of bottom/last connection. |  |  |  |
| 2\-5 | Data | Number of active cells connected to a well. |  |  |  |
| 2\-6 | Data | Index \(one\-based\) of well's current group. |  |  |  |
| 2\-7 | Data | Defines the well type, set 1 for a production well, 2 for an oil injection well, 3 for a water injection well, or 4 for a gas injection well \(NIWELZ = 7\). |  |  |  |
| 2\-8 | Data | Well's active target control mode \(constraint\). |  |  |  |
| 2\-9 |  | Undefined. |  |  |  |
| 2\-10 |  | Undefined. |  |  |  |
| 2\-11 | Data | Defines the well status, set to greater than zero for producing and less than or equal to zero for being shut \(NIWELZ =11\). |  |  |  |
| 2\-12 | Data | ID \(one\-based\) of well's current VFP table. |  |  |  |
| 2\-13 |  | Undefined. |  |  |  |
| 2\-14 |  | Undefined. |  |  |  |
| 2\-15 |  | Undefined. |  |  |  |
| 2\-16 | Data | Well's requested control mode from simulation deck \([WCONINJE](#-refheading-toc146750-4203985108), [WCONPROD](#-refheading-toc146754-4203985108)\). |  |  |  |
| 2\-17 to 2\-22 |  | Undefined. |  |  |  |
| 2\-23 | Data | Cross flow indicator. |  |  |  |
| 2\-24 to 2\-42 |  | Undefined. |  |  |  |
| 2\-43 | Data | Defines the [LGR](#-refheading-toc55049-4106839650) index for a well with local completions in a [LGR](#-refheading-toc55049-4106839650) \(NIWELZ = 43\). |  |  |  |
| 2\-44 to 2\-48 |  | Undefined. |  |  |  |
| 2\-49 | Data | Defines the well friction indicator, set to non\-zero for horizontal wells \(NIWELZ = 49\). |  |  |  |
| 2\-50 | Data | Well's requested control mode from simulation deck \([WCONHIST](#-refheading-toc134880-2055188184), [WCONINJH](#-refheading-toc146752-4203985108)\). |  |  |  |
| 2\-51 to 2\-70 |  | Undefined. |  |  |  |
| 2\-71 | Data | Multi\-segment well ID; value of one for regular wells, or zero for multi\-segment wells. |  |  |  |
| 2\-72 | Data | Number of well segments: value of one for regular wells, or the number of segments for multi\-segment wells. |  |  |  |
| 2\-73 to 2\-98 |  | Undefined. |  |  |  |
| 2\-99 | Data | Well's completion ordering scheme, set to: - Connections ordered along well track \(increasing MD\) - Connections ordered by increasing true vertical depth. Not really supported in OPM Flow. - Connections listed in order of appearance in simulation model's [COMPDAT](#-refheading-toc97651-3261743917) keyword. |  |  |  |
|  | SWEL | Well real data array SWEL\(NSWELZ, NWELLS\) where NSWELX and NWELS are defined on the INTEHEAD record. |  |  |  |
| 1\-1 | Format | SWEL | NSWELZ x NWELLS | REAL | Required |
| 2\-1 | Data | Well's current oil rate production target. |  |  |  |
| 2\-2 | Data | Well's current water rate production target. |  |  |  |
| 2\-3 | Data | Well's current gas rate production target. |  |  |  |
| 2\-4 | Data | Well's current liquid rate production target. |  |  |  |
| 2\-5 | Data | Well's current reservoir voidage rate production target. |  |  |  |
| 2\-6 | Data | Well's tubing head pressure target. |  |  |  |
| 2\-7 | Data | Well's bottom hole pressure target. |  |  |  |
| 2\-8 |  | Undefined. |  |  |  |
| 2\-9 |  | Undefined. |  |  |  |
| 2\-10 |  | Well's reference depth for BHP. |  |  |  |
| 2\-11 |  | Well's artificial lift quantity. |  |  |  |
| 2\-12 to 2\-17 |  | Undefined. |  |  |  |
| 2\-18 |  | Well's drainage radius \- item seven from the [WELSPECS](#-refheading-toc268463-1366622701) keyword. |  |  |  |
| 2\-19 to 2\-20 |  | Undefined. |  |  |  |
| 2\-25 |  | Item two from [WEFAC](#-refheading-toc48856-327352552); this value is repeated at two locations. |  |  |  |
| 2\-26 to 2\-31 |  | Undefined. |  |  |  |
| 2\-32 |  | Item two from [WEFAC](#-refheading-toc48856-327352552) keyword. |  |  |  |
| 2\-33 |  | Undefined. |  |  |  |
| 2\-34 |  | Well's historical/observed liquid rate target/limit. |  |  |  |
| 2\-35 to 2\-54 |  | Undefined. |  |  |  |
| 2\-55 |  | Well's historical/observed gas rate target/limit. |  |  |  |
| 2\-56 |  | Well's historical/observed bottom hole pressure target/limit. |  |  |  |
|  | XWEL | Well's injection and production data array XWEL\(NXWELZ, NWELLS\). |  |  |  |
| 1\-1 | Format | XWEL | NSWELZ x NWELLS | DOUB | Required |
| 2\-1 | Data | Well's oil production rate. |  |  |  |
| 2\-2 | Data | Well's water production rate. |  |  |  |
| 2\-3 | Data | Well's gas production rate. |  |  |  |
| 2\-4 | Data | Well's liquid production rate. |  |  |  |
| 2\-5 | Data | Well's reservoir voidage production rate. |  |  |  |
| 2\-6 | Data | Well's tubing head pressure. |  |  |  |
| 2\-7 | Data | Well's flowing/producing bottom hole pressure. |  |  |  |
| 2\-8 | Data | Well's producing water cut. |  |  |  |
| 2\-9 | Data | Well's producing gas/oil ratio. |  |  |  |
| 2\-10 to 2\-18 |  | Undefined. |  |  |  |
| 2\-19 | Data | Well's total cumulative oil production. |  |  |  |
| 2\-20 | Data | Well's total cumulative water production. |  |  |  |
| 2\-21 | Data | Well's total cumulative gas production. |  |  |  |
| 2\-22 | Data | Well's total cumulative reservoir voidage production. |  |  |  |
| 2\-23 |  | Undefined. |  |  |  |
| 2\-24 | Data | Well's total cumulative water injection. |  |  |  |
| 2\-25 | Data | Well's total cumulative gas injection. |  |  |  |
| 2\-26 | Data | Well's total cumulative reservoir volume injection. |  |  |  |
| 2\-27 to 2\-34 |  | Undefined. |  |  |  |
| 2\-35 | Data | Well's producing gas formation volume factor. |  |  |  |
| 2\-36 |  | Undefined. |  |  |  |
| 2\-37 |  | Undefined. |  |  |  |
| 2\-38 |  | Undefined. |  |  |  |
| 2\-39 to 2\-41 |  | Undefined. |  |  |  |
| 2\-42 | Data | Well's current BHP Target/Limit. |  |  |  |
| 2\-43 to 2\-48 |  | Undefined. |  |  |  |
| 2\-49 | Data | Well's "primary" guide rate \(oil for producers, preferred phase for injectors\). |  |  |  |
| 2\-50 | Data | Well's producer guide rate for water. |  |  |  |
| 2\-51 | Data | Well's producer guide rate for gas. |  |  |  |
| 2\-52 to 2\-68 | Data | Undefined. |  |  |  |
| 2\-69 | Data | Well's producer guide rate for reservoir voidage volume. |  |  |  |
| 2\-70 to 2\-75 |  | Undefined. |  |  |  |
| 2\-76 | Data | Well's total cumulative oil production \(observed/historical rates\). |  |  |  |
| 2\-77 | Data | Well's total cumulative water production observed/historical rates\). |  |  |  |
| 2\-78 | Data | Well's total cumulative gas production \(observed\(historical rates\). |  |  |  |
| 2\-79 to 2\-81 |  | Undefined. |  |  |  |
| 2\-82 | Data | Well's total cumulative water injection \(observed/historical rates\). |  |  |  |
| 2\-83 | Data | Well's total cumulative gas injection \(observed/historical rates\). |  |  |  |
| 2\-84 to 2\-91 |  | Undefined. |  |  |  |
| 2\-92 |  | Second copy of well's primary guide rate. Not fully characterized. |  |  |  |
| 2\-93 | Data | Second copy of well's producer guide rate for water. Not fully characterized. |  |  |  |
| 2\-94 | Data | Second copy of well's producer guide rate for gas. Not fully characterized. |  |  |  |
| 2\-95 | Data | Second copy of well's producer guide rate for reservoir voidage. Not fully characterized. |  |  |  |
| 2\-96 to 2\-122 |  | Undefined. |  |  |  |
| 2\-123 | Data | Well's voidage production rate. |  |  |  |
| 2\-124 | Data | Well's voidage production rate. |  |  |  |
|  | ZWEL | Well character data array ZWEL\(NXWELZ, NWELLS\) where NXWELX and NWELS are defined on the INTEHEAD keyword. All strings are eight characters in length. |  |  |  |
| 1\-1 | Format | ZWEL | NSWELZ x NWELLS | CHAR | Required |
| 2\-1 | Data | Defines the well name consisting of eight characters \(NXWELZ = 1\). |  |  |  |
| 2\-2 | Data | Defines the name of the Well List the well belongs to, set to “blank” for the well does not belong to Well List \(NXWELZ = 2\), that is the [ACTIONX](#-refheading-toc152227-2992482751) name. |  |  |  |
| 2\-3 | Data | Defines the end of time step action for the well \(NXWELZ = 3\). |  |  |  |

Table A.24: RESTART Data – Group, Well, and Connection Keywords \(Wells\)

The well connection keywords are specified in Table A.25 and consist of the ICON, SCON, and XCON keywords.
| No. | keyword Name | [RESTART](#-refheading-toc135629-1317547213) Data – Group, Well, and Connection keywords Table A.25 \- Connection Keywords |  |  | Status or Value |
| --- | --- | --- | --- | --- | --- |
|  | ICON | Connection integer data array ICON\(NICONZ, NCWMAX, NWELLS\) where NICONZ, NCWMAX, and NWELLS are defined on the INTEHEAD keyword. Data keywords are required for each completion in the well and the number of data items, N, should be NICONZ x NCWMAX  x NWELLS. Undefined values should be set to zero. |  |  |  |
| 1\-1 | Format | ICON | N | INTE |  |
| 2\-1 | Data | Defines the well connect index \(NICONZ = 1\). |  |  | 0 |
| 2\-2 | Data | Defines the location of connection in the grid for the I dimension \(NICONZ = 2\). |  |  | 0 |
| 2\-3 | Data | Defines the location of connection in the grid for the J dimension \(NICONZ = 3\). |  |  | 0 |
| 2\-4 | Data | Defines the location of connection in the grid for the K dimension \(NICONZ = 4\). |  |  | 0 |
| 2\-5 |  | Undefined. |  |  | 0 |
| 2\-6 | Data | Defines the status of the connection, set to less than or equal to zero for being shut or greater than zero for being open \(NICONZ = 5\). |  |  | 0 |
| 2\-7 |  | Drainage saturation function table number. |  |  | 0 |
| 2\-8 |  | Undefined. |  |  | 0 |
| 2\-9 |  | Undefined. |  |  | 0 |
| 2\-10 |  | Imbibition saturation function table number. |  |  | 0 |
| 2\-11 |  | Undefined. |  |  | 0 |
| 2\-12 |  | Undefined. |  |  | 0 |
| 2\-13 |  | Completion ID \(1\-based\). |  |  | 0 |
| 2\-14 | Data | Defines the direction of connection, set to one for the x\-direction, two for the y\-direction, or three for the z\-direction. The default value of zero indicates the z\-direction \(NICONZ = 14\). |  |  | 0 |
| 2\-15 | Data | Defines, for multi\-segment wells, the segment number the connect belongs to, for conventional wells the default value of zero should be used \(NICONZ = 15\). |  |  |  |
|  | SCON | Connection real data array SCON\(NSCONZ, NCWMAX, NWELLS\) where NSCONZ, NCWMAX, and NWELLS are defined on the INTEHEAD keyword. Data are required for each completion in the well and the number of data items, N, should be NSCONZ x NCWMAX  x NWELLS. |  |  | Required |
| 1\-1 | Format | ICON | N | REAL |  |
| 2\-1 | Data | Connection transmissibility factor NSCONZ = 1 in the SCON array. |  |  |  |
| 2\-2 | Data | Connection center depth. |  |  |  |
| 2\-3 | Data | Connection diameter. |  |  |  |
| 2\-4 | Data | Connection KH, that is the net thickness times the permeability, NSCONZ = 4 in the SCON array. |  |  |  |
| 2\-5 | Data | Skin factor \- item 'SKIN' from [COMPDAT](#-refheading-toc97651-3261743917) keyword in the [SCHEDULE](#-refheading-toc43945-784232322) section. |  |  |  |
| 2\-6 to 2\-11 |  | Undefined. |  |  |  |
| 2\-12 | Data | Connection transmissibility factor. |  |  |  |
| 2\-13 to 2\-20 |  | Undefined. |  |  |  |
| 2\-21 | Data | Distance to end of connection in segment. |  |  |  |
| 2\-22 | Data | Distance to start of connection in segment. |  |  |  |
| 2\-23 to 2\-29 |  | Undefined. |  |  |  |
| 2\-30 | Data | Undefined. |  |  |  |
| 2\-31 | Data | Undefined. |  |  |  |
| 2\-32 to 2\-40 |  | Undefined. |  |  |  |
| 2\-41 | Data | Connection factor defined in input deck \(set to one\), or zero for undefined in input deck. |  |  |  |
|  | XCON | Connection double precision data array XCON\(NXCONZ, NCWMAX, NWELLS\) where NXCONZ, NCWMAX, and NWELLS are defined on the INTEHEAD keyword.  The number of data items, N, should be NXCONZ x NCWMAX  x NWELLS |  |  | Required |
| 1\-1 | Format | ICON | N | DOUB |  |
| 2\-1 | Data | Oil surface rate. |  |  |  |
| 2\-2 | Data | Water surface rate. |  |  |  |
| 2\-3 | Data | Gas surface rate. |  |  |  |
| 2\-4 to 2\-34 |  | Undefined. |  |  |  |
| 2\-35 |  | Connection pressure value. |  |  |  |
| 2\-36 to 2\-49 |  | Undefined. |  |  |  |
| 2\-50 |  | Reservoir voidage rate. |  |  |  |

Table A.25: RESTART Data – Group, Well, and Connection Keywords \(Connections\)

The tracer keywords are listed in Table A.26 and consists of the ICOT, XCOT, IWET, XWET, IGRT, and XGRT keywords. Note that this series of keywords are only available if tracers are present in the run.

| No. | keyword Name | [RESTART](#-refheading-toc135629-1317547213) Data – Group, Well, and Connection keywords Table A.26 \- Tracer Keywords |  |  | Status or Value |
| --- | --- | --- | --- | --- | --- |
| Keyword | No. of Entries | Data Type |  |  |  |
|  | ICOT | Tracer connection integer data array ICOT\(NICOTZ, NSTRA2, NCWMAX, NWELLS\) where NICOTZ, NSTRA2, NCWMAX, and NWELLS are defined on the INTEHEAD keyword.  The number of data items, N, should be NICONZ x NSTRA2 x NCWMAX  x NWELLS. |  |  | Optional |
| 1\-1 | Format | ICOT | N | INTE |  |
| 2\-1 | Data | ICOT\(NICOTZ, NSTRA2, NCWMAX, NWELLS\) array. |  |  |  |
|  | XCOT | Tracer connection double precision data array ICOT\(NICOTZ, NSTRA2, NCWMAX, NWELLS\) where NICOTZ, NSTRA2, NCWMAX, and NWELLS are defined on the INTEHEAD keyword.  The number of data items, N, should be NICONZ x NSTRA2 x NCWMAX x NWELLS. |  |  | Optional |
| 1\-1 | Format | XCOT | N | DOUB |  |
| 2\-1 | Data | XCOT\(NICOTZ, NSTRA2, NCWMAX, NWELLS\) array. |  |  |  |
|  | IWET | Tracer well integer data array IWET\(NIWETZ, NSTRA2, NWMAXZ, NWELLS\) where NIWETZ, NSTRA2, and NWMAXZ are defined on the INTEHEAD keyword. The number of items, N, should be NIWETNZ x NSTRA2 x NWMAXZ. |  |  | Optional |
| 1\-1 | Format | IWET | N | INTE |  |
| 2\-1 | Data | IWET\(NIWETZ, NSTRA2, NWMAXZ, NWELLS\) array. |  |  |  |
|  | XWET | Tracer connection double precision data array XWET\(NXWETZ, NSTRA2, NWMAXZ\) where NXWETZ, NSTRA2, and NWMAXZ are defined on the INTEHEAD keyword.  The number of items, N, should be NXWETNZ x NSTRA2 x NWMAXZ. |  |  | Optional |
| 1\-1 | Format | XWET | N | DOUB |  |
| 2\-1 | Data | XWET\(NXWETZ, NSTRA2, NWMAXZ\) array. |  |  |  |
|  | IGRT | Tracer well integer data array IGRT\(NIGRTZ, NSTRA2, NWMAXZ, NWELLS\) where NIGRTZ, NSTRA2, and NWMAXZ are defined on the INTEHEAD keyword. The number of elements, N, should be NIGRTNZ x NSTRA2 x NWMAXZ. |  |  | Optional |
| 1\-1 | Format | IGRT | N | INTE |  |
| 2\-1 | Data | IGRT\(NIGRTZ, NSTRA2, NWMAXZ, NWELLS\) array. |  |  |  |
|  | XGRT | Tracer connection double precision data array XGRT\(NXGRTZ, NSTRA2, NWMAXZ\) where NXGRTZ, NSTRA2, and NWMAXZ are defined in the INTEHEAD keyword.  The number of data items, N, should be NXGRTNZ x NSTRA2 x NWMAXZ. |  |  | Optional |
| 1\-1 | Format | XGRT | N | DOUB |  |
| 2\-1 | Data | XWET\(NXWETZ, NSTRA2, NWMAXZ\) array. |  |  |  |

Table A.26: RESTART Data – Group, Well, and Connection Keywords \(Tracers\)

Finally, the network keywords INODE, IBRAN, INOBR, RNODE, RBRAN, and ZNODE are specified in Table A.27. Again, this series of keywords are only available if networks are present in the run.
| No. | keyword Name | [RESTART](#-refheading-toc135629-1317547213) Data – Group, Well, and Connection keywords Table A.27 \- Network Keywords |  |  | Status or Value |
| --- | --- | --- | --- | --- | --- |
| Keyword | No. of Entries | Data Type |  |  |  |
|  | INODE | Network node integer data array INODE\(NINODE, NODMAX\) where NINODE and NODMAX are defined in the INTEHEAD keyword. |  |  | Optional |
| 1\-1 | Format | INODE | NINODE x NODMAX | INTE |  |
| 2\-1 | Data | INODE\(NINODE, NODMAX\) array |  |  |  |
|  | IBRAN | Network node branch integer data array IBRAN\(NIBRAN, NBRMAX\) where NIBRAN and NBRMAX are defined in the INTEHEAD keyword. |  |  | Optional |
| 1\-1 | Format | IBRAN | NIBRAN x NBRMAX | INTE |  |
| 2\-1 | Data | IBRAN\(NIBRAN, NBRMAX\) |  |  |  |
|  | INOBR | Network node\-branch integer data array INOBR\(NIOBR\) where NIOBR are defined in the INTEHEAD keyword. |  |  | Optional |
| 1\-1 |  | INOBR | NIOBR | INTE |  |
| 2\-1 |  | INOBR\(NIOBR\) array. |  |  |  |
|  | RNODE | Network node double precision data array RNODE\(NRNODE, NODMAX\) where NRNODE and NODMAX are defined in the INTEHEAD keyword. |  |  | Optional |
| 1\-1 | Format | RNODE | NRNODE x NODMAX | DOUB |  |
| 2\-1 | Data | RNODE\(NRNODE, NODMAX\) array. |  |  |  |
|  | RBRAN | Network node branch integer data array RBRAN\(NRBRAN, NBRMAX\) where NRBRAN and NBRMAX are defined in the INTEHEAD keyword. |  |  | Optional |
| 1\-1 | Format | RBRAN | NRBRAN x NBRMAX | DOUB |  |
| 2\-1 | Data | RBRAN\(NRBRAN, NBRMAX\) array. |  |  |  |
|  | ZNODE | Network node character data array ZNODE\(NZNODE, NODMAX\) where NZNODE and NODMAX are defined in the INTEHEAD keyword. |  |  | Optional |
| 1\-1 | Format | ZNODE | NZNODE x NODMAX | CHAR |  |
| 2\-1 | Data | ZNODE\(NZNODE, NODMAX\) array. |  |  |  |
| Notes: - Rows shaded in gray indicate the start of a keyword. - Cells colored red in the No. column indicate that this item is either “Not Used” or “Undefined”. - For formatted output all character variables, including the keyword, should be enclosed in single quotes, for example the ZNODE keyword should be written out as ‘ZNODE   ’. |  |  |  |  |  |

Table A.27: RESTART Data – Group, Well, and Connection Keywords \(Network\)

#### <a id="-refheading-toc165446-2189581950"></a>Example: RESTART Data – Group, Well, and Connection Keywords

The following example shows a typical formatted [RESTART](#-refheading-toc135629-1317547213) Data – Group, Well, and Connection keyword data set, showing the IGRP, SGRP, XGRP, and ZGRP keywords.

```eclipse
  'IGRP    '        2864 'INTE'
           1           0           0           0           0           0
           0           0           0           0           0           0
           0           0           0           0           0           0
           0           0           0           0           0           0
  ………………………….……………..
           0           0           0           0           0           0
           0           0           0           0           0           0
           0           0           0           0           0           0
           0           0           0           0           0          16
          16           0           0           0           0           0
 'SGRP    '        1488 'REAL'
   0.10000000E+21   0.10000000E+21  -0.10000000E+21   0.10000000E+21
   0.00000000E+00   0.00000000E+00   0.10000000E+21   0.10000000E+21
   0.10000000E+21   0.10000000E+21   0.10000000E+21   0.10000000E+21
  ………………………….……………..
   0.00000000E+00   0.00000000E+00   0.10000000E+21   0.10000000E+21
   0.00000000E+00   0.10000000E+21   0.00000000E+00   0.00000000E+00
   0.00000000E+00   0.00000000E+00   0.00000000E+00   0.00000000E+00
   0.00000000E+00   0.00000000E+00   0.00000000E+00   0.10000000E+01
 'XGRP    '        2784 'DOUB'
   0.00000000000000D+00   0.00000000000000D+00   0.00000000000000D+00
   0.00000000000000D+00   0.00000000000000D+00   0.00000000000000D+00
   0.00000000000000D+00   0.00000000000000D+00   0.00000000000000D+00
  ………………………….……………..
   0.00000000000000D+00   0.00000000000000D+00   0.00000000000000D+00
   0.00000000000000D+00   0.00000000000000D+00   0.00000000000000D+00
   0.00000000000000D+00   0.00000000000000D+00   0.00000000000000D+00
   0.00000000000000D+00
 'ZGRP    '          80 'CHAR'
 'MANI-C  ' '        ' '        ' '        ' '        ' 'B1-DUMMY' '        '
 '        ' '        ' '        ' 'MANI-D1 ' '        ' '        ' '        '
 '        ' 'INJE    ' '        ' '        ' '        ' '        ' 'PROD    '
 '        ' '        ' '        ' '        ' 'MANI-B2 ' '        ' '        '
 '        ' '        ' 'MANI-B1 ' '        ' '        ' '        ' '        '
 'MANI-D2 ' '        ' '        ' '        ' '        ' 'MANI-E1 ' '        '
 '        ' '        ' '        ' 'MANI-E2 ' '        ' '        ' '        '
 '        ' 'MANI-K1 ' '        ' '        ' '        ' '        ' 'MANI-K2 '
 '        ' '        ' '        ' '        ' 'MANI-F  ' '        ' '        '
 '        ' '        ' 'WI-GSEG ' '        ' '        ' '        ' '        '
 'D2-DUMMY' '        ' '        ' '        ' '        ' 'FIELD   ' '        '
 '        ' '        ' '        '
```

End of Example

        - RESTART Data – UDQ and ACTIONX Keywords
    -
-

The restart data for the [UDQ](#-refheading-toc161095-2932703077) and [ACTIONX](#-refheading-toc152227-2992482751) keywords are written out in a set of [UDQ](#-refheading-toc161095-2932703077) and [ACTIONX](#-refheading-toc152227-2992482751) arrays. If there are no [UDQ](#-refheading-toc161095-2932703077) or [ACTIONX](#-refheading-toc152227-2992482751) data, the corresponding arrays are not written to the restart file and only the relevant arrays are written out. 
The structure for this type of keyword is based on the data type as summarized below:
        - The [UDQ](#-refheading-toc161095-2932703077) data set keywords are specified in Table A.28 and consists of the IUDQ, IUAD, ZUDN, ZUDL, IGPH, IUAP, DUDW, DUDG, and DUDF keywords.
        - The [ACTIONX](#-refheading-toc152227-2992482751) data set keywords are specified in Table A.29 and consists of the keywords IACT, SACT, ZACT, ZLACT, ZACN, IACN, and SACN.
    -
-

| No. | keyword Name | [RESTART](#-refheading-toc135629-1317547213) Data – [UDQ](#-refheading-toc161095-2932703077) and [ACTIONX](#-refheading-toc152227-2992482751) keywords Table A.28 \- [UDQ](#-refheading-toc161095-2932703077) Keywords |  |  | Status or Value |
| --- | --- | --- | --- | --- | --- |
|  | IUDQ | Keyword defines the integer properties as per the [UDQ](#-refheading-toc161095-2932703077) variable. |  |  | Required |
| 1\-1 | Format | IUDQ | No. [UDQ](#-refheading-toc161095-2932703077)’s x 3 | INTE |  |
| 2\-1 | Data | - ASSIGN [UDQ](#-refheading-toc161095-2932703077) - Undefined. - DEFINE [UDQ](#-refheading-toc161095-2932703077) |  |  |  |
| 2\-2 | Data | \-4 :   ASSIGN [UDQ](#-refheading-toc161095-2932703077) \(\-1\) times the number of operators in expression: DEFINE [UDQ](#-refheading-toc161095-2932703077)  \(see code for details\) |  |  |  |
| 2\-3 | Data |  |  |  |  |
|  | IUAD | This keyword defines the various controls for wells, groups, etc. |  |  | Required |
| 1\-1 | Format | IUAD | No. IUAD’s x 5 | INTE |  |
| 2\-1 | Data | Set to: - 200000 \+ 19 for [GCONPROD](#-refheading-toc146746-4203985108)  and  ORAT - 300000 \+ 19 for [GCONPROD](#-refheading-toc146746-4203985108)  and  WRAT - 400000 \+ 19 for [GCONPROD](#-refheading-toc146746-4203985108)  and  GRAT - 500000 \+ 19 for [GCONPROD](#-refheading-toc146746-4203985108)  and   LRAT - 300000 \+ 4   for [WCONPROD](#-refheading-toc146754-4203985108) \+ ORAT - 400000 \+ 4   for [WCONPROD](#-refheading-toc146754-4203985108) \+ WRAT - 500000 \+ 4   for [WCONPROD](#-refheading-toc146754-4203985108) \+ GRAT - 600000 \+ 4   for [WCONPROD](#-refheading-toc146754-4203985108) \+ LRAT - 300000 \+ 3   for [WCONINJE](#-refheading-toc146750-4203985108)   \+ ORAT - 400000 \+ 3   for [WCONINJE](#-refheading-toc146750-4203985108)   \+ RATE \(surface rate\) - 500000 \+ 3   for [WCONINJE](#-refheading-toc146750-4203985108)   \+ RESV \(reservoir vol rate\) - 1000000 \+ 27 for [CECON](#-refheading-toc27331-3671211675)  \+ minimum oil rate |  |  |  |
| 2\-2 | Data | Sequence number of [UDQ](#-refheading-toc161095-2932703077) used \(from input sequence\) for the actual constraint/target. |  |  |  |
| 2\-3 | Data | Set to one \(1\). |  |  |  |
| 2\-4 | Data | Number of times the [UDQ](#-refheading-toc161095-2932703077) variable is used. |  |  |  |
| 2\-5 | Data | The sequence number for the first use of the actual [UDQ](#-refheading-toc161095-2932703077), equal to one \(1\) plus the \(sum over the earlier [UDQ](#-refheading-toc161095-2932703077)’s of the number of uses of the respective [UDQ](#-refheading-toc161095-2932703077)’s\). |  |  |  |
|  | IUAP | The keyword defines the sequence number of the actual well, group, etc. for each [UDQ](#-refheading-toc161095-2932703077) use in [WCONPROD](#-refheading-toc146754-4203985108), [GCONPROD](#-refheading-toc146746-4203985108), [GCONINJE](#-refheading-toc134874-2055188184), etc. |  |  | Required |
| 1\-1 | Format | IUAP | No. IUAP’s | INTE |  |
| 2\-1 | Data | Equals the well, group, etc. sequence number for the UDQ\-Variable used in actual target, limit. |  |  |  |
|  | IGPH | This keyword defines an integer number per group, and for the [FIELD](#-refheading-toc71850-2267116897) which is the last group in the list. |  |  | Required |
| 1\-1 | Format | IGPH | Max Number Groups in the Field plus one. | INTE |  |
| 2\-1 | Data | The value of the integer denotes the phase \(or component\) for injection group control \([GCONINJE](#-refheading-toc134874-2055188184)\): - No injection control. - Oil phase injection control. - Water phase injection. - Gas injection. |  |  |  |
|  | ZUDN | Keyword pairs of data for each [UDQ](#-refheading-toc161095-2932703077). |  |  | Required |
| 1\-1 | Format | ZUDN | No. [UDQ](#-refheading-toc161095-2932703077)’s x 2 | CHAR |  |
| 2\-1 | Data | [UDQ](#-refheading-toc161095-2932703077) name \(maximum of eight characters per [UDQ](#-refheading-toc161095-2932703077)\). |  |  |  |
| 2\-2 | Data | [UDQ](#-refheading-toc161095-2932703077)’s units \(maximum of eight characters per [UDQ](#-refheading-toc161095-2932703077)\). |  |  |  |
|  | ZUDL | This keyword contains the EXPRESSION variable \(item three\) on the [UDQ](#-refheading-toc161095-2932703077) keyword in the input deck  “Data for operation”. |  |  | Required |
| 1\-1 | Format | ZUDL | No. [UDQ](#-refheading-toc161095-2932703077)’s x 16 | CHAR |  |
| 2\-1 to 2\-16 | Data | A character string that defines the EXPRESSION variable, “Data for operation”, split into strings of eight characters each. |  |  |  |
|  | DUDW | Keyword containing the values of all the well [UDQ](#-refheading-toc161095-2932703077)’s. |  |  | Required |
| 1\-1 | Format | DUDW | No. Well UDQs x Max No. of Wells. | DOUBLE |  |
| 2\-1 to no of well [UDQ](#-refheading-toc161095-2932703077)’s | Data | The value of the [UDQ](#-refheading-toc161095-2932703077) for the actual well  \(repeated for all wells in the well input sequence\). |  |  |  |
|  | DUDG | Keyword containing the values of all the group [UDQ](#-refheading-toc161095-2932703077)’s. |  |  | Required |
| 1\-1 | Format | DUDG | No. Group\_UDQs x Max No. of Groups | DOUBLE |  |
| 2\-1 to no of group [UDQ](#-refheading-toc161095-2932703077)’s | Data | The value of [UDQ](#-refheading-toc161095-2932703077) for the actual group \(repeated for all groups in the group input sequence\). |  |  |  |
|  | DUDF | Keyword containing the values of all the field [UDQ](#-refheading-toc161095-2932703077)’s. |  |  | Required |
| 1\-1 | Format | DUDF | No. Field UDQs | DOUBLE |  |
| 2\-1 to no of field  [UDQ](#-refheading-toc161095-2932703077)’s | Data | Value of [UDQ](#-refheading-toc161095-2932703077) for field UDQs. |  |  |  |

Table A.28: RESTART Data – [UDQ](#-refheading-toc161095-2932703077) Keywords

    -
-

| No. | keyword Name | [RESTART](#-refheading-toc135629-1317547213) Data – [UDQ](#-refheading-toc161095-2932703077) and [ACTIONX](#-refheading-toc152227-2992482751) keywords Table A.29 \- [ACTIONX](#-refheading-toc152227-2992482751) Keywords |  |  | Status or Value |
| --- | --- | --- | --- | --- | --- |
|  | IACT | The keyword defines the integer properties for the [ACTIONX](#-refheading-toc152227-2992482751) variable. |  |  | Required |
| 1\-1 | Format | IACT | No. of Actions x 9 | INTE |  |
| 2\-1 | Data | - Undefined. |  |  |  |
| 2\-2 | Data | Number of lines of [SCHEDULE](#-refheading-toc43945-784232322) data. |  |  |  |
| 2\-3 | Data | - For condition and previous condition equal to AND, and combinations OR/AND - For all conditions and previous conditions equal to OR. |  |  |  |
| 2\-4 | Data | - Undefined. |  |  |  |
| 2\-5 | Data | - Undefined. |  |  |  |
| 2\-6 | Data |  |  |  |  |
| 2\-7 | Data | - Undefined. |  |  |  |
| 2\-8 | Data | - Undefined. |  |  |  |
| 2\-9 | Data |  |  |  |  |
|  | IACN | Keyword defines various parameters for |  |  | Required |
| 1\-1 | Format | IACN | No. Actions x 26 x  Max No. Conditions per Action. | INTE |  |
| 2\-1 to 2\-10 | Data | - Undefined. |  |  |  |
| 2\-11 | Data | The type of quantity for the condition: - For a field quantity \(number of flowing producing wells\). - For a well quantity - For a \(node\) group quantity. - For a well group quantity - For the DAY. - For the MONTH. - For the YEAR. |  |  |  |
| 2\-12 | Data | Quantity type for the Right Hand Side \(“RHS”\) quantity: - For field variables. - For well variables? - For group variables. - For constant values. |  |  |  |
| 2\-13 | Data | Index for relational operator \(<, =, \> \): - For LHS quantity greater RHS quantity. - For LHS quantity less than or equal to RHS quantity. |  |  |  |
| 2\-14 | Data | Relates to operator: - AND - OR |  |  |  |
| 2\-17 | Data | Defines the operator used in [ACTIONX](#-refheading-toc152227-2992482751) for defined quantities: - For the \> operator. - For the <  operator. - For the \>=   operator. - For the <=   operator. - For the =  operator. |  |  |  |
| 2\-18 | Data | The value relates to the operator for the triggering condtion and if the right hand quantity is a constant or not. There is one value for each condition and the value is determined as follows: - For the first condition in an [ACTIONX](#-refheading-toc152227-2992482751) statement iacn\[17\] =  0 - For the second, third etc. conditions iacn\[17\] is determined using the following logic: If the previous condition has a constant rhs =\> iacn\[17\] =  0. If previous rhs is of type \{W,G, F\} and If previous boolean operator is AND =\> iacn\[17\] =  1 If previous boolean operator is OR  =\> iacn\[17\] =  0 Note as mentioned previously, the No. column in this table and all tables in APPENDIX A:,  the count is based on one \(offset one\); however, in C\+\+ the base is zero \(offset zero\) and therefore C\+\+ programmers must subtract one from this column to obtain the correct reference.  Hence, the iacn\[17\] reference is the correct reference for C\+\+. |  |  |  |
|  | SACT | Keyword defines various parameters for an [ACTIONX](#-refheading-toc152227-2992482751) keyword |  |  | Required |
| 1\-1 | Format | SACT | No. Actions x 5 | REAL |  |
| 2\-1 to 2\-5 | Data | - Undefined. |  |  |  |
|  | ZACT | Keyword defines the name of an action |  |  | Required |
| 1\-1 | Format | ZACT | No. Actions x 4 | CHAR |  |
| 2\-1 | Data | The name of an ACTION \(maximum eight characters\). |  |  |  |
|  | ZLACT | Keyword containing the actions defined for an [ACTIONX](#-refheading-toc152227-2992482751) keyword. |  |  | Required |
| 1\-1 | Format | ZLACT | No\_Actions x Max No. of Input Lines x  Max No. Characters per Input Line. | CHAR |  |
| 2\-1 to 2\-? | Data | Contains the actions defined for an [ACTIONX](#-refheading-toc152227-2992482751) keyword. |  |  |  |
|  | ZACN | Keyword containing the EXPRESSION parameter \(item 3\) on the [UDQ](#-refheading-toc161095-2932703077) keyword, the “Data for operation”. |  |  | Required |
| 1\-1 | Format | ZACN | No\_Actions x Max No. of Conditions x 13 | CHAR |  |
| 2\-1 | Data | Left hand side quantity if \(DAY, MONTH or YEAR\). |  |  |  |
| 2\-2 | Data | Right hand side quantity if \(Well or Group\). |  |  |  |
| 2\-3 | Data | Operator. |  |  |  |
| 2\-4 | Data | Well name – left hand quantity, if it is a well quantity. |  |  |  |
| 2\-5 | Data | Well name – right hand quantity, if it is a well quantity. |  |  |  |
| 2\-6 | Data | Group name – left hand quantity, if it is a group quantity. |  |  |  |
| 2\-7 | Data | Group name – right hand quantity, if it is a group quantity. |  |  |  |
|  | SACN |  |  |  | Required |
| 1\-1 | Format | SACN | No. of Actions x Max No. Conditions x 16 | DOUBLE |  |
| 2\-1 | Data | - Undefined. |  |  |  |
| 2\-2 | Data | - Undefined. |  |  |  |
| 2\-3 | Data | Value of condition: - If Month otherwise zero. |  |  |  |
| 2\-4 | Data | - Undefined. |  |  |  |
| 2\-5 | Data | - Well or Field data, or - Group data. |  |  |  |
| 2\-6 | Data | Value of right hand side. |  |  |  |
| 2\-7 | Data | Value of left hand side. |  |  |  |
| 2\-8 | Data | Value of right hand side. |  |  |  |
| 2\-9 | Data | Value of left hand slide. |  |  |  |
| 2\-10 | Data | Value of right hand side. |  |  |  |

Table A.29: RESTART Data – ACTIONX Keywords

#### <a id="-refheading-toc716959-3964674244"></a>Example: RESTART Data – Group, Well, and Connection Keywords

The following example shows a typical formatted [RESTART](#-refheading-toc135629-1317547213) Data – [UDQ](#-refheading-toc161095-2932703077) – data.

```eclipse
 'ZUDN    '          22 'CHAR'
 'WUWI3   ' '        ' 'WUPR1   ' '        ' 'WUPR3   ' '        ' 'WUPR4   '
 '        ' 'WUPR5   ' '        ' 'GUOPR1  ' '        ' 'GULPR1  ' '        '
 'GUOPR2  ' '        ' 'GULPR2  ' '        ' 'GUOPR3  ' '        ' 'GULPR3  '
 '        '
 'ZUDL    '         176 'CHAR'
 '(GOPR 'L' 'OWER' *0' '.931 *0.' '50 *1)  ' '        ' '        ' '        '
 '        ' '        ' '        ' '        ' '        ' '        ' '        '
 '        ' '        ' '1/(WWCT ' ''OP*' ) ' '        ' '        ' '        '
 '        ' '        ' '        ' '        ' '        ' '        ' '        '
 '        ' '        ' '        ' '        ' 'SORTA(WU' 'PR1)    ' '        '
 '        ' '        ' '        ' '        ' '        ' '        ' '        '
 '        ' '        ' '        ' '        ' '        ' '        ' '1/(WWCT '
 ''OPU*' )' '        ' '        ' '        ' '        ' '        ' '        '
 '        ' '        ' '        ' '        ' '        ' '        ' '        '
 '        ' 'SORTA(WU' 'PR4)    ' '        ' '        ' '        ' '        '
 '        ' '        ' '        ' '        ' '        ' '        ' '        '
 '        ' '        ' '        ' '(2500 - ' 'GOPR LOW' 'ER *0.03' ' - GOPR '
 'UPPER *0' '.15) * 0' '.899    ' '        ' '        ' '        ' '        '
 '        ' '        ' '        ' '        ' '        ' '(4500 - ' 'GOPR LOW'
 'ER *0.03' ' - GOPR ' 'UPPER *0' '.15) * 0' '.899    ' '        ' '        '
 '        ' '        ' '        ' '        ' '        ' '        ' '        '
 '(2500 - ' 'GOPR LOW' 'ER *0.03' ' - GOPR ' 'UPPER *0' '.15) * 0' '.920    '
 '        ' '        ' '        ' '        ' '        ' '        ' '        '
 '        ' '        ' '(4500 - ' 'GOPR LOW' 'ER *0.03' ' - GOPR ' 'UPPER *0'
 '.15) * 0' '.920    ' '        ' '        ' '        ' '        ' '        '
 '        ' '        ' '        ' '        ' '(2500 - ' 'GOPR LOW' 'ER *0.03'
 ' - GOPR ' 'UPPER *0' '.15) * 0' '.880    ' '        ' '        ' '        '
 '        ' '        ' '        ' '        ' '        ' '        ' '(4500 - '
 'GOPR LOW' 'ER *0.03' ' - GOPR ' 'UPPER *0' '.15) * 0' '.880    ' '        '
 '        ' '        ' '        ' '        ' '        ' '        ' '        '
 '        '
 'IUDQ    '          33 'INTE'
           2          -4           1           2          -1           2
           2          -1           3           2          -1           4
           2          -1           5           2          -4           1
           2          -4           2           2          -4           3
           2          -4           4           2          -4           5
           2          -4           6
```

End of Example

        - RESTART Data – Aquifer Data Keywords
    -
-

This set of keywords are used to define the various aquifer arrays written out by OPM Flow. If there are no aquifers in the model then this set of keywords are skipped. If an analytical or numerical model aquifer is present in the model, a complete set of keywords, for a given aquifer type, should be written out. For example, if a numerical model is defined in the model then the IAQN and RAQN keywords should be written to the file.
The structure for this set of keywords is dependent on the aquifer type, for analytical aquifers the format is outlined in Table A.30 and numerical aquifers are characterized in Table A.31.
| No. | keyword Name | [RESTART](#-refheading-toc135629-1317547213) Data – Aquifer Data keywords Table A.30 \- Analytical Aquifer Keywords |  |  | Status or Value |
| --- | --- | --- | --- | --- | --- |
|  | IAAQ | Analytical aquifers integer data array IAAQ\(NIAAQZ, MAAQID\) where NIAAQZ and MAAQIDR are defined in the INTEHEAD keyword. |  |  | Optional |
| 1\-1 | Format | IAAQ | NIAAQZ x MAAQID | INTE |  |
| 2\-1 | Data | Aquifer connection number. |  |  |  |
| 2\-2 | Data | Water property table. |  |  | [PVTNUM](#-refheading-toc68366-2752266063) |
| 2\-3 to 2\-9 |  | Undefined. |  |  |  |
| 2\-10 | Data | Analytical aquifer type, set to zero for Fetkovich aquifers and one for                 CarterTracy aquifers. |  |  |  |
| 2\-11 | Data | Type Related 2. |  |  |  |
|  | SAAQ | Analytical aquifers real data array SAAQ\(NSAAQZ, MAAQID\) where NSAAQZ and MAAQIDR are defined in the INTEHEAD keyword. |  |  | Optional |
| 1\-1 | Format | SAAQ | NSAAQZ x MAAQID | REAL |  |
| 2\-1 | Data | Total Compressibility. |  |  | COMP |
| 2\-2 | Data | Fetkovich analytical aquifer pore volume. |  |  | [PORV](#-refheading-toc96547-718313858) |
| Carter\-Tracy aquifer external radius. |  |  | RE |  |  |
| 2\-3 | Data | Fetkovich analytical aquifer productivity index. |  |  | PI |
| Carter\-Tracy aquifer permeability. |  |  | PERM |  |  |
| 2\-4 | Data | Fetkovich analytical aquifer time constant. |  |  |  |
| Carter\-Tracy aquifer porosity. |  |  | [PORO](#-refheading-toc45797-719036256) |  |  |
| 2\-5 | Data | Analytical aquifer pressure. |  |  | PRESS |
| 2\-6 | Data | Analytical aquifer datum depth. |  |  | [DATUM](#-refheading-toc135613-1317547213) |
| 2\-7 | Data | Carter\-Tracy aquifer thickness. |  |  | [DZ](#-refheading-toc45769-719036256) |
| 2\-8 | Data | Carter\-Tracy aquifer influence angle. |  |  | ANGLE |
| 2\-9 | Data | Carter\-Tracy aquifer mass density of water. |  |  |  |
| 2\-10 | Data | Carter\-Tracy aquifer water viscosity. |  |  |  |
|  | XAAQ | Analytical aquifers double precision data array XAAQ\(NXAAQZ, MAAQID\) where NXAAQZ and MAAQIDR are defined in the INTEHEAD keyword. |  |  | Optional |
| 1\-1 | Format | XAAQ | NXAAQZ x MAAQID | DOUB |  |
| 2\-1 | Data | Aquifer flow rate \(AAQR: N\). |  |  |  |
| 2\-2 | Data | Dynamic aquifer pressure \(AAQP: N\). |  |  |  |
| 2\-3 | Data | Liquid volume produced from the aquifer into the reservoir \(AAQT: N\). |  |  |  |
| 2\-4 | Data | Total aquifer influx coefficient across all aquifer connections. |  |  |  |
| 2\-5 | Data | Reciprocal time constant for Carter\-Tracy aquifer. |  |  |  |
| 2\-6 | Data | Influx constant "beta" for Carter\-Tracy aquifer. |  |  |  |
| 2.7 | Data | Unknown. |  |  |  |
| 2\-8 | Data | Unknown. |  |  |  |
| 2\-9 | Data | Dimensionless time for Carter\-Tracy aquifer \(AAQTD: N\) |  |  |  |
| 2\-10 | Data | Dimensionless pressure for Carter\-Tracy aquifer \(AAQPD: N\) |  |  |  |
|  | IAQL | Analytical aquifers integer aquifer list data array IAQL\(NIAQLX, MXNALI, MXAAQL\) where NIAQLX, MXNALI, and MXAAQL are defined in the INTEHEAD keyword. |  |  | Optional |
| 1\-1 | Format | IAQL | NIAQLX x MXNALI x MXAAQL | INTE |  |
| 2\-1 | Data | IAQL\(NIAQLX, MXNALI, MXAAQL\) array. |  |  |  |
|  | ZAQL | Analytical aquifers character aquifer list data array ZAQL\(NZAQLX, MXNALI\) where NZAQLX, and MXNALI are defined in the INTEHEAD keyword. |  |  | Optional |
| 1\-1 | Format | ZAQL | NZAQLX x MXNALI | CHAR |  |
| 2\-1 | Data | ZAQL\(NZAQLX, MXNALI\) array. |  |  |  |
|  | ICAQ | Analytical aquifers integer aquifer connection data array MAAQID arrays, each of size ICAQ\(NICAQZ, NGCAUS\) where NICAQZ, NGCAUS, and MAAQID are defined in the INTEHEAD keyword. |  |  | Optional |
| 1\-1 | Format | ICAQ | NICAQZ x NGCAUS x MAAQID | INTE |  |
| 2\-1 | Data | Reservoir connecting cell in the I\-direction. |  |  | I |
| 2\-2 | Data | Reservoir connecting cell in the J\-direction. |  |  | J |
| 2\-3 | Data | Reservoir connecting cell in the K\-direction. |  |  | K |
| 2\-4 | Data | Connecting cell status, with active equal to one otherwise zero. |  |  |  |
| 2\-5 | Data | Connecting “face” of the reservoir cell, where I\- = 1, I\+ = 2, J\- = 3, J\+ = 4, K\- = 5,  and K\+ = 6. |  |  | AQUFACE |
|  | SCAQ | Analytical aquifers real aquifer connection data array MAAQID arrays, each of size SCAQ\(NSCAQZ, NGCAUS\) where NSCAQZ, NGCAUS, and MAAQID are defined in the INTEHEAD keyword. |  |  | Optional |
| 1\-1 | Format | SCAQ | NICAQZ x NGCAUS x MAAQID | REAL |  |
| 2\-1 | Data | Connection's fraction of total aquifer influx coefficient. |  |  |  |
| 2\-2 | Data | Connection's effective face area divided by aquifer's total influx coefficient. |  |  |  |
|  | ACAQ | Analytical aquifers double precision aquifer connection data array MAAQID arrays, each of size ACAQ\(NACAQZ, NGCAUS\) where NACAQZ, NGCAUS, and MAAQID are defined in the INTEHEAD keyword. |  |  | Optional |
| 1\-1 | Format | ACAQ | NACAQZ x NGCAUS x MAAQID | DOUB |  |
| 2\-1 | Data | ACAQ\( NSCAQZ, NGCAUS, MAAQID\) array. |  |  |  |
| Notes: - Rows shaded in gray indicate the start of a keyword. - For formatted output all character variables, including the keywords should be enclosed in single quotes, for example the ACAQ keyword should be written out as ‘ACAQ    ’. |  |  |  |  |  |

Table A.30: RESTART Data – Analytical Aquifer Data Keywords

And for numerical aquifers the format is outlined in Table A.31.

| No. | keyword Name | [RESTART](#-refheading-toc135629-1317547213) Data – Aquifer Data keywords Table A.31 \- Numerical Aquifer keywords |  |  | Status or Value |
| --- | --- | --- | --- | --- | --- |
| Keyword | No. of Entries | Data Type |  |  |  |
|  | IAQN | Numerical aquifers integer data array IAQN\(NIIAQN, NUMAQN\) where NIIAQN and NUMAQN are defined in the INTEHEAD keyword. |  |  | Optional |
| 1\-1 | Format | IAAQ | NIIAQN x NUMAQN | INTE |  |
| 2\-1 | Data | Aquifer identification number. |  |  | AQUID |
| 2\-2 | Data | Aquifer coordinate in the I\-direction |  |  | I |
| 2\-3 | Data | Aquifer coordinate in the J\-direction |  |  | J |
| 2\-4 | Data | Aquifer coordinate in the K\-direction |  |  | K |
| 2\-5 | Data | Aquifer Water Property Table. |  |  | [PVTNUM](#-refheading-toc68366-2752266063) |
| 2\-6 | Data | Aquifer [SATNUM](#-refheading-toc71136-2752266063) table. |  |  | [SATNUM](#-refheading-toc71136-2752266063) |
|  | RAQN | Numerical aquifers double precision data array RAQN\(NIRAQN, NUMAQN\) where NIIAQN and NUMAQN are defined in the INTEHEAD keyword. |  |  | Optional |
| 1\-1 | Format | RAAQ | NIRAQN x NUMAQN | REAL |  |
| 2\-1 | Data | Aquifer inflow area. |  |  | AREA |
| 2\-2 | Data | Aquifer length. |  |  | LENGTH |
| 2\-3 | Data | Aquifer porosity |  |  | [PORO](#-refheading-toc45797-719036256) |
| 2\-4 | Data | Aquifer permeability. |  |  | PERM |
| 2\-5 | Data | Aquifer datum depth. |  |  | [DATUM](#-refheading-toc135613-1317547213) |
| 2\-6 | Data | Aquifer pressure. |  |  | PRESS |
| 2\-7 | Data | Unknown |  |  |  |
| 2\-8 | Data | Unknown |  |  |  |
| 2\-9 | Data | Unknown |  |  |  |
| 2\-10 | Data | Total aquifer pore\-volume. |  |  |  |
| 2\-11 | Data | Aquifer inflow rate \(ANQR: N\). |  |  |  |
| 2\-12 | Data | Total liquid volume produced from aquifer \(AQNT: N\). |  |  |  |
| 2\-13 | Data | Dynamic aquifer pressure \(ANQP: N\). |  |  |  |
| Notes: - Rows shaded in gray indicate the start of a keyword. - For formatted output all character variables, including the keyword, should be enclosed in single quotes, for example the RAQN keyword should be written out as ‘RAQN    ’. |  |  |  |  |  |

Table A.31: RESTART Data – Numerical Aquifer Data Keywords

#### <a id="-refheading-toc195710-2189581950"></a>Example: RESTART Data – Aquifer Data Keywords

The following example shows a typical formatted [RESTART](#-refheading-toc135629-1317547213) Data – Aquifer Data keyword data set for an analytical aquifer.

```eclipse
  'IAAQ    '          15 'INTE'
           3           1           0           0           0           0
           0           0           0           1           1           1
           0           0           0
 'SAAQ    '          24 'REAL'
   0.29999999E-04   0.24000000E+04   0.20000000E+02   0.10000000E+00
   0.49619409E+04   0.54000000E+04   0.14000000E+03   0.13333334E-01
   0.63151001E+02   0.31000000E+00   0.00000000E+00   0.43846342E+00
   0.00000000E+00   0.00000000E+00   0.00000000E+00   0.00000000E+00
   0.00000000E+00   0.00000000E+00   0.00000000E+00   0.00000000E+00
   0.00000000E+00   0.00000000E+00   0.00000000E+00   0.00000000E+00
 'XAAQ    '           8 'DOUB'
   0.63857101611063D+03   0.49619408179004D+04   0.26831697328212D+05
   0.15000000000000D+06   0.23624684055200D-01   0.36097145428688D+02
   0.00000000000000D+00   0.00000000000000D+00
 'ICAQNUM '           1 'INTE'
           1
 'ICAQ    '          15 'INTE'
           5           1           1          13           2           5
           1           2          14           2           5           1
           3          15           2
 'SCAQNUM '           1 'INTE'
           1
 'SCAQ    '           6 'REAL'
   0.33333334E+00   0.33333334E+00   0.33333334E+00   0.33333334E+00
   0.33333334E+00   0.33333334E+00
```

End of Example
        - RESTART Data – Hidden Keyword
    -
-

This keyword8
       The [RESTART](#-refheading-toc135629-1317547213) Data – Hidden keyword format is used both for global and [LGR](#-refheading-toc55049-4106839650) grids.  defines solution arrays that have been exported by OPM Flow that should not be processed by post\-processing software.
The structure for this type of keyword is defined in Table A.32.
| No. | keyword Name | [RESTART](#-refheading-toc135629-1317547213) Data – Hidden keyword Table A.32 |  |  | Status or Value |
| --- | --- | --- | --- | --- | --- |
| Keyword | No. of Entries | Data Type |  |  |  |
|  | HIDDEN | The keyword defines the solution arrays that have not been exported by the simulator, where N is the number of solution variable names that have been “hidden”, each enclosed in single quotes and of eight characters in length. |  |  | Required |
| 1\-1 | Format | HIDDEN | N | CHAR |  |
| 2\-1 | Data | Character list of solution arrays to be hidden from post processing software. |  |  |  |
| Notes: - For formatted output all character variables, including the keyword, should be enclosed in single quotes, for example the HIDDEN keyword should be written out as 'HIDDEN  '. |  |  |  |  |  |

Table A.32: RESTART Data – Hidden Keyword

#### <a id="-refheading-toc165446-21895819501"></a>Example: RESTART Data – Hidden Keyword

The following example shows a typical formatted hidden data set, showing 51 Solution arrays that should be hidden.

```eclipse
 'HIDDEN  '          51 'CHAR'
 'ISTHGGI ' 'SWMAX   ' 'SWHY1   ' 'SWHY2   ' 'SWHY3   ' 'ISTHW   ' 'SOMAX   '
 'SGHY1   ' 'SGHY2   ' 'SGHY3   ' 'ISTHG   ' 'SGMAX   ' 'SHMAX   ' 'WATQUIES'
 'GASQUIES' 'PRESROCC' 'SPDOIL  ' 'SPDWATER' 'SPDGAS  ' 'SWINIT  ' 'SGINIT  '
 'POLYMAX ' 'EIP0    ' 'EIP     ' 'TINIT   ' 'IOCN    ' 'SGMIN   ' 'SGSTRD  '
 'SWSTRD  ' 'RISTRD  ' 'SGSTRI  ' 'SWSTRI  ' 'RISTRI  ' 'SGTRPD  ' 'SGSTRWD '
 'SGSTRWI ' 'SWMIN   ' 'SGSTRWS ' 'RPTHMW  ' 'PPCW    ' 'GRADWELL' 'GRADCONN'
 'SWHY4   ' 'SGHY4   ' 'GRADGRUP' 'GRADRESV' 'GRADFIP ' 'GRADSOL ' 'GRADEXP '
 'IAQN    ' 'RAQN    '
```

End of Example

        - RESTART Data - Solution Data keyword
    -
-

The solution data keywords9
       The [RESTART](#-refheading-toc135629-1317547213) Data \- Solution Data keywords *a**re* used both for global and [LGR](#-refheading-toc55049-4106839650) grids [SOLUTION](#-refheading-toc43947-784232322) arrays. The [LGR](#-refheading-toc55049-4106839650) data is preceded by a series of [LGR](#-refheading-toc55049-4106839650) head keywords and terminated by an [LGR](#-refheading-toc55049-4106839650) termination keyword.  define the solution for each active cell for both global and [LGR](#-refheading-toc55049-4106839650) grids.   This is then followed by a series of global data for a global entry or [LGR](#-refheading-toc55049-4106839650) data for a [LGR](#-refheading-toc55049-4106839650) entry. 
The structure for this type of keyword is defined in Table A.33 for standard solution data and Table A.34 for tracers.  A list of all solution names is tabulated in Table A.35.
| No. | keyword Name | [RESTART](#-refheading-toc135629-1317547213) Data \- Solution Data keyword Table A.33 |  |  | Status or Value |
| --- | --- | --- | --- | --- | --- |
| Keyword | No. of Entries | Data Type |  |  |  |
|  | STARTSOL | This keyword marks the start of the solution variable section for both global and local grids. Note that there is no data associated with this keyword. |  |  | Required |
| 1\-1 | Format | STARTSOL | 0 | MESG |  |
|  | LGRNAMES | This keyword defines a list of [LGR](#-refheading-toc55049-4106839650) names for the reporting time step, where N is the number of [LGR](#-refheading-toc55049-4106839650) names. |  |  |  |
| 1\-1 | Format | LGRNAMES | N | CHAR |  |
| 2\-1 | Data | A character list of [LGR](#-refheading-toc55049-4106839650) names with each name enclosed in single quotes and each having a length of eight characters. |  |  |  |
|  | [SOLUTION](#-refheading-toc43947-784232322) | The [SOLUTION](#-refheading-toc43947-784232322) keyword defines the start of a [SOLUTION](#-refheading-toc43947-784232322) array data set, where [SOLUTION](#-refheading-toc43947-784232322) is the name of the array being written out, as outlined in Table A.35. For example, [PRESSURE](#-refheading-toc135627-1317547213), [SWAT](#-refheading-toc137373-1317547213), [SGAS](#-refheading-toc137369-1317547213), [RS](#-refheading-toc137361-1317547213), [RV](#-refheading-toc137365-1317547213) etc. The [SOLUTION](#-refheading-toc43947-784232322) keyword \(items 1\-1 and 2\-1\) is repeated for each  [SOLUTION](#-refheading-toc43947-784232322) array being written out.  [SOLUTION](#-refheading-toc43947-784232322) arrays can be in any order and only the active cells are written out \(NACTIV\). |  |  | Required |
| 1\-1 | Format | [SOLUTION](#-refheading-toc43947-784232322) | NACTIV | REAL |  |
| 2\-1 | Data | [SOLUTION](#-refheading-toc43947-784232322) data set. |  |  |  |
|  | ENDSOL | This keyword marks the end of the solution variable section for both global and local grids. Note that there is no data associated with this keyword. |  |  | Required |
| 1\-1 | Format | ENDSOL | 0 | MESG |  |
| Notes: - Rows shaded in gray indicate the start of a keyword. - For formatted output all character variables, including the keyword, should be enclosed in single quotes, for example the [SOLUTION](#-refheading-toc43947-784232322) array for [PRESSURE](#-refheading-toc135627-1317547213) should be written out as ‘PRESSURE ’. |  |  |  |  |  |

Table A.33: RESTART Data \- Solution Data keyword

For [SOLUTION](#-refheading-toc43947-784232322) tracer concentration arrays the ZTRACER keyword must precede the [SOLUTION](#-refheading-toc43947-784232322) tracer data array – see  Table A.34 for a description of ZTRACER keyword.
| No. | keyword Name | [RESTART](#-refheading-toc135629-1317547213) Data – Solution Data keyword for Tracer Concentration Name Table A.34 |  |  | Status or Value |
| --- | --- | --- | --- | --- | --- |
|  | ZTRACER | This keyword marks the start of the solution variable section for both global and local grids.  The [TRACER](#-refheading-toc121485-83452205) in the Data field is the name of the tracer concentration being processed. |  |  | Optional |
| 1\-1 | Format | ZTRACER | 2 | CHAR |  |
| 2\-1 | Data | [TRACER](#-refheading-toc121485-83452205) | ‘           ‘ |  |  |
|  | [TRACER](#-refheading-toc121485-83452205) | [TRACER](#-refheading-toc121485-83452205) is the name of the tracer concentration that is contained on the next keyword. Tracer arrays can be in any order and only the active cells are written out \(NACTIV\). |  |  |  |
| 1\-1 | Format | [TRACER](#-refheading-toc121485-83452205) | NACTIV | REAL |  |
| 2\-1 | Data | Tracer solution data array. |  |  |  |
| Notes: - The ZTRACER and the [TRACER](#-refheading-toc121485-83452205) keywords are repeated for each tracer. - For formatted output all character variables, including the keyword, should be enclosed in single quotes, including the tracer name. |  |  |  |  |  |

Table A.34: RESTART Data – Solution Data Keyword for Tracer Concentration Name

The [SOLUTION](#-refheading-toc43947-784232322) keywords are listed in  Table A.35.
| Model Type |  | Model Option | Solution Data Keywords | Solution Variable Description | OPM Output   Status |
| --- | --- | --- | --- | --- | --- |
|  |  | STANDARD | 1OVERBO | Reciprocal of oil formation volume factor. |  |
|  |  | STANDARD | 1OVERBW | Reciprocal of water formation volume factor. |  |
|  |  | STANDARD | CNV\_DGAS | Worst cells depending on the gas saturation increment / Rv increment / Rs increment. |  |
|  |  | STANDARD | CNV\_DPRE | Worst cells depending on the pressure increment. |  |
|  |  | STANDARD | CNV\_DWAT | Worst cells depending on the water saturation increment. |  |
|  |  | STANDARD | CNV\_GAS | Worst cells depending on the residual of gas equation. |  |
|  |  | STANDARD | CNV\_OIL | Worst cells depending on the residual of the oil equation. |  |
|  |  | STANDARD | CNV\_WAT | Worst cells depending on the residual of the water equation. |  |
|  |  | STANDARD | CONV\_NEW | Number of Newtons required by each cell in order to satisfy the solution change convergence criteria at the last time step. |  |
|  |  | STANDARD | CONV\_PRU | Worst cells depending on the pressure update. |  |
|  |  | STANDARD | CONV\_VBR | Worst cells depending on the volume balance residual. |  |
|  |  | STANDARD | DRAINAGE | Drainage region numbers. |  |
|  |  | STANDARD | DRAINMIN | Drainage sink indicator. |  |
|  |  | STANDARD | FIPGAS | Gas fluid\-in\-place. |  |
|  |  | STANDARD | FIPOIL | Oil fluid\-in\-place. |  |
|  |  | STANDARD | FIPWAT | Water fluid\-in\-place. |  |
|  |  | STANDARD | GAS\_DEN | Gas density. |  |
|  |  | STANDARD | GAS\_POTN | Gas potential. |  |
|  |  | STANDARD | GAS\_PRES | Gas phase pressure. |  |
|  |  | STANDARD | GAS\_VISC | Gas viscosity. |  |
|  |  | STANDARD | IOVERBG | Reciprocal of gas formation volume factor. |  |
|  |  | STANDARD | ISTHG | Gas capillary pressure state. |  |
|  |  | STANDARD | ISTHW | Water capillary pressure state. |  |
|  |  | STANDARD | OIL\_DEN | Oil density. |  |
|  |  | STANDARD | OIL\_POTN | Oil potential. |  |
|  |  | STANDARD | OIL\_VISC | Oil viscosity. |  |
|  |  | STANDARD | [PBUB](#-refheading-toc135619-1317547213) | Bubble point pressure. |  |
|  |  | STANDARD | PCOG | Oil\-gas capillary pressure. |  |
|  |  | STANDARD | PCOW | Oil\-water capillary pressure. |  |
|  |  | STANDARD | [PDEW](#-refheading-toc135623-1317547213) | Dew point pressure. |  |
|  |  | STANDARD | [PORV](#-refheading-toc96547-718313858) | Pore volume at surface conditions. |  |
|  |  | STANDARD | [PRESSURE](#-refheading-toc135627-1317547213) | Pressure. |  |
|  |  | STANDARD | RFIPGAS | Gas fluid\-in\-place at reservoir conditions. |  |
|  |  | STANDARD | RFIPOIL | Oil fluid\-in\-place at reservoir conditions. |  |
|  |  | STANDARD | RFIPWAT | Water fluid\-in\-place at reservoir conditions. |  |
|  |  | STANDARD | RPORV | Pore volume at reservoir conditions. |  |
|  |  | STANDARD | [RS](#-refheading-toc137361-1317547213) | Gas\-oil ratio. |  |
|  |  | STANDARD | RSSAT | Saturated gas\-oil ratio. |  |
|  |  | STANDARD | [RV](#-refheading-toc137365-1317547213) | Oil\-gas ratio. |  |
|  |  | STANDARD | RVSAT | Saturated oil\-gas ratio. |  |
|  |  | STANDARD | SFIPGAS | Gas fluid\-in\-place at surface/separator conditions. |  |
|  |  | STANDARD | SFIPOIL | Oil fluid\-in\-place at surface/separator conditions. |  |
|  |  | STANDARD | SFIPWAT | Water fluid\-in\-place at surface/separator conditions. |  |
|  |  | STANDARD | [SGAS](#-refheading-toc137369-1317547213) | Gas saturation. |  |
|  |  | STANDARD | SGMAX | Maximum gas saturation. |  |
|  |  | STANDARD | SGMIN | Minimum gas saturation. |  |
|  |  | STANDARD | [SOIL](#-refheading-toc137371-1317547213) | Oil saturation. |  |
|  |  | STANDARD | SOMAX | Maximum oil saturation. |  |
|  |  | STANDARD | [SSOL](#-refheading-toc210160-2884651453) | Solvent saturation. |  |
|  |  | STANDARD | STATES | Gas\-oil state indicator. |  |
|  |  | STANDARD | [SWAT](#-refheading-toc137373-1317547213) | Water saturation. |  |
|  |  | STANDARD | SWMAX | Maximum water saturation. |  |
|  |  | STANDARD | SWMIN | Minimum water saturation. |  |
|  |  | STANDARD | WAT\_DEN | Water density. |  |
|  |  | STANDARD | WAT\_POTN | Water potential. |  |
|  |  | STANDARD | WAT\_PRES | Water phase pressure. |  |
|  |  | STANDARD | WAT\_VISC | Water viscosity. |  |
|  |  | STANDARD | XMF | Liquid mole fractions. |  |
|  |  | STANDARD | YMF | Vapor mole fractions. |  |
|  |  | STANDARD | ZMF | Total mole fractions. |  |
|  |  | [ALKALINE](#-refheading-toc197467-2366741785) | [ALKADS](#-refheading-toc192784-2366741785) | Alkaline adsorption. |  |
|  |  | [ALKALINE](#-refheading-toc197467-2366741785) | [ALKALINE](#-refheading-toc197467-2366741785) | Alkaline concentration. |  |
|  |  | [ALKALINE](#-refheading-toc197467-2366741785) | ALKMAX | Alkaline maximum historic concentration. |  |
|  |  | [ALKALINE](#-refheading-toc197467-2366741785) | PADMAX | Alkaline polymer maximum historic adsorption. |  |
|  |  | [ALKALINE](#-refheading-toc197467-2366741785) | PLADALK | Alkaline polymer adsorption multipliers. |  |
|  |  | [ALKALINE](#-refheading-toc197467-2366741785) | SFADALK | Alkaline surfactant adsorption multipliers. |  |
|  |  | [ALKALINE](#-refheading-toc197467-2366741785) | STMALK | Alkaline water/oil surface tension multipliers. |  |
|  |  | [API](#-refheading-toc4422-421927891) | SDENO | Oil surface densities. |  |
|  |  | [API](#-refheading-toc4422-421927891) | [OILAPI](#-refheading-toc240796-2928331029) | Oil [API](#-refheading-toc4422-421927891) values. |  |
|  |  | AQUIFER | HYDH | Hydraulic head aquifer. |  |
|  |  | AQUIFER | HYDHFW | Fresh water hydraulic head aquifer. |  |
|  |  | [BRINE](#-refheading-toc162083-289573908) | CNV\_DSAL | Worst cells depending on the brine concentration increment. |  |
|  |  | [BRINE](#-refheading-toc162083-289573908) | CNV\_SAL | Worst cells depending on the residual of the brine equation \(BRINEoption when used with polymer\). |  |
|  |  | [BRINE](#-refheading-toc162083-289573908) | ESALSUR | Effective salinity for surfactant. |  |
|  |  | [BRINE](#-refheading-toc162083-289573908) | [SALT](#-refheading-toc593214-516898843) | Brine concentration. |  |
|  |  | [COAL](#-refheading-toc234580-3519154785) | COALGAS | Coal gas concentration for coal bed methane option. |  |
|  |  | [COAL](#-refheading-toc234580-3519154785) | COALSOLV | Solvent concentration for coal bed methane option. |  |
|  |  | [COAL](#-refheading-toc234580-3519154785) | [GASSATC](#-refheading-toc216737-1190369742) | Initial coal gas saturated content for coal bed methane option. |  |
|  |  | [COAL](#-refheading-toc234580-3519154785) | [MLANG](#-refheading-toc580806-3181922006) | Langmuir scaling factors for coal bed methane option. |  |
|  |  | [COAL](#-refheading-toc234580-3519154785) | [MLANGSLV](#-refheading-toc580808-3181922006) | Langmuir scaling factors for solvent in coal bed methane option. |  |
|  |  | [ENDSCALE](#-refheading-toc68146-2267116897) | GASKR | Gas relative permeability. |  |
|  |  | [ENDSCALE](#-refheading-toc68146-2267116897) | OILKR | Oil relative permeability. |  |
|  |  | [ENDSCALE](#-refheading-toc68146-2267116897) | WATKR | Water relative permeability. |  |
|  |  | [EXCAVATE](#-refheading-toc259231-803326780) | EXCAVNUM | Excavation status identifier. |  |
|  |  | [EXCAVATE](#-refheading-toc259231-803326780) | TRANEXX/Y/Z | Transmissibilities in excavation runs. |  |
|  |  | [FOAM](#-refheading-toc171586-289573908) | [FOAM](#-refheading-toc171586-289573908) | Foam concentration. |  |
|  |  | [FOAM](#-refheading-toc171586-289573908) | FOAM\_HL | Foam half\-life. |  |
|  |  | [FOAM](#-refheading-toc171586-289573908) | [FOAMADS](#-refheading-toc224974-3519154785) | Foam adsorption. |  |
|  |  | [FOAM](#-refheading-toc171586-289573908) | FOAMCNM | Foam capillary numbers. |  |
|  |  | [FOAM](#-refheading-toc171586-289573908) | FOAMDCY | Foam decay. |  |
|  |  | [FOAM](#-refheading-toc171586-289573908) | FOAMMAX | Foam maximum historic concentration. |  |
|  |  | [FOAM](#-refheading-toc171586-289573908) | [FOAMMOB](#-refheading-toc224978-3519154785) | Foam mobility multiplier. |  |
|  |  | [GIMODEL](#-refheading-toc383678-1414963541) | CNV\_DGGI | Worst cells depending on the dry injection gas parameter \(Gi\) increment. |  |
|  |  | [GIMODEL](#-refheading-toc383678-1414963541) | CNV\_GGI | Worst cells depending on the residual of the Gi Pseudo\-Compositional modeL. |  |
|  |  | [GIMODEL](#-refheading-toc383678-1414963541) | GGI | [GI](#-refheading-toc372466-1414963541) injected gas ratio. |  |
|  |  | [GIMODEL](#-refheading-toc383678-1414963541) | RFIPGGI | Dry injection gas in place at reservoir conditions. |  |
|  |  | [GIMODEL](#-refheading-toc383678-1414963541) | SFIPGGI | Dry injection gas in place at surface conditions. |  |
|  |  | [POLYMER](#-refheading-toc38609-2267116897) | CABINnnn | This is for use with the [PLYTRRFA](#-refheading-toc258120-501926209) keyword only. |  |
|  |  | [POLYMER](#-refheading-toc38609-2267116897) | CNV\_DPLY | Worst cells depending on the polymer concentration increment. |  |
|  |  | [POLYMER](#-refheading-toc38609-2267116897) | CNV\_PLY | Worst cells depending on the residual of the polymer equation. |  |
|  |  | [POLYMER](#-refheading-toc38609-2267116897) | PADS | Adsorbed polymer concentrations. |  |
|  |  | [POLYMER](#-refheading-toc38609-2267116897) | POLYMAX | Maximum historic polymer concentration. |  |
|  |  | [POLYMER](#-refheading-toc38609-2267116897) | [POLYMER](#-refheading-toc38609-2267116897) | Polymer concentrations. |  |
|  |  | [POLYMER](#-refheading-toc38609-2267116897) | SFIPPLY,RFIPPLY | Polymer\-in\-place. |  |
|  |  | [POLYMER](#-refheading-toc38609-2267116897) | SFIPSAL,RFIPSAL | Salt\-in\-place \([BRINE](#-refheading-toc162083-289573908) option when used with polymer\). |  |
|  |  | [ROCKCOMP](#-refheading-toc55593-1778172979) | PRESROCC | Rock pressure values used for rock compaction model. |  |
|  |  | [SOLVENT](#-refheading-toc62787-1778172979) | CNV\_DSOL | Worst cells depending on the solvent concentration increment. |  |
|  |  | [SOLVENT](#-refheading-toc62787-1778172979) | CNV\_SOL | Worst cells depending on the residual of the solvent equation. |  |
|  |  | [SOLVENT](#-refheading-toc62787-1778172979) | RFIPSOL | Solvent\-in\-place at reservoir conditions. |  |
|  |  | [SOLVENT](#-refheading-toc62787-1778172979) | SFIPSOL | Solvent\-in\-place at surface conditions. |  |
|  |  | [SURFACT](#-refheading-toc863854-4250154414) | CATROCK | Divalent cation concentration associated with rock. |  |
|  |  | [SURFACT](#-refheading-toc863854-4250154414) | CATSURF | Divalent cation concentration associated with surfactant. |  |
|  |  | [SURFACT](#-refheading-toc863854-4250154414) | [SURFACT](#-refheading-toc863854-4250154414) | Surface interactions. |  |
|  |  | [SURFACT](#-refheading-toc863854-4250154414) | [SURFADS](#-refheading-toc883680-4250154414) | Adsorbed surfactant concentrations. |  |
|  |  | [SURFACT](#-refheading-toc863854-4250154414) | SURFCNM | Surfactant capillary numbers. |  |
|  |  | [SURFACT](#-refheading-toc863854-4250154414) | SURFMAX | Maximum surfactant concentrations. |  |
|  |  | [SURFACT](#-refheading-toc863854-4250154414) | [SURFST](#-refheading-toc1173151-4250154414) | Surface tension in surfactant runs. |  |
|  |  | [TEMP](#-refheading-toc146397-3544483072) | [TEMP](#-refheading-toc146397-3544483072) | Temperature. |  |
| OPM |  | [THERMAL](#-refheading-toc137276-650382403) | [TEMP](#-refheading-toc146397-3544483072) | Temperature. |  |
|  |  | [VE](#-refheading-toc557797-487874538) | EOGC | Maximum oil\-gas contact. |  |
|  |  | [VE](#-refheading-toc557797-487874538) | EOWC | Minimum oil\-water contact. |  |
|  |  | [VE](#-refheading-toc557797-487874538) | GWC | Gas\-water contact. |  |
|  |  | [VE](#-refheading-toc557797-487874538) | OGC | Oil\-gas contact. |  |
|  |  | [VE](#-refheading-toc557797-487874538) | OWC | Oil\-water contact. |  |
|  |  | [VE](#-refheading-toc557797-487874538) | POT\_CORR | Initial contact corrected potential. |  |
| Notes: - The Model Type columns indicate if the solution keyword applies to a black\-oil model, a compositional model or both. Since OPM Flow is a black\-oil model the compositional keywords are not valid, as shown by the orange cells under the Compositional column. - The Model Option column states the model option the solution keyword is associated with and a green cell in the Model Type column indicates that OPM Flow has this option. - Finally, the OPM Output Status column indicates if the current version of OPM Flow writes out the data associated with the solution keyword, with a green cell indicating it does and orange it does not. |  |  |  |  |  |

Table A.35: RESTART Data \- Solution Data Keywords

#### <a id="-refheading-toc174467-2189581950"></a>Example: RESTART Data – Solution Data Keyword

The following example shows a typical formatted global grid data set for this keyword set.
```eclipse
 'STARTSOL'           0 'MESS'
 'PRESSURE'       44431 'REAL'
   0.26889725E+03   0.26838983E+03   0.26826810E+03   0.26820352E+03
   0.26814493E+03   0.26809378E+03   0.26807767E+03   0.26806363E+03
   0.26802625E+03   0.26798474E+03   0.26795001E+03   0.26791434E+03
   0.26787915E+03   0.26783920E+03   0.26777118E+03   0.26769208E+03         ………………………….……………..
 'SWAT    '       44431 'REAL'
   0.10500000E+00   0.10500000E+00   0.10500000E+00   0.10500000E+00
   0.10500000E+00   0.10500000E+00   0.10500000E+00   0.14000000E+00
   0.14000000E+00   0.14500000E+00   0.14500000E+00   0.14500000E+00
   0.14500000E+00   0.14500000E+00   0.16000000E+00   0.16000000E+00
………………………….……………..
 'SGAS    '       44431 'REAL'
   0.00000000E+00   0.89499998E+00   0.89499998E+00   0.89499998E+00
   0.89499998E+00   0.89499998E+00   0.89499998E+00   0.86000001E+00
   0.86000001E+00   0.85500002E+00   0.85500002E+00   0.85500002E+00
………………………….……………..
 'RS      '       44431 'REAL'
   0.11697504E+03   0.12030303E+03   0.12023456E+03   0.12019825E+03
   0.12016528E+03   0.12013654E+03   0.12012746E+03   0.12011956E+03
   0.12009855E+03   0.12007520E+03   0.12005566E+03   0.12003561E+03
   0.12001582E+03   0.11999335E+03   0.11995509E+03   0.11991060E+03
   0.11987761E+03   0.11985194E+03   0.11983020E+03   0.11981972E+03
   0.11980798E+03   0.11977385E+03   0.11970672E+03   0.11963727E+03
  ………………………….……………..
 'RV      '       44431 'REAL'
   0.57879315E-04   0.57552861E-04   0.57483696E-04   0.57447018E-04
   0.57413723E-04   0.57384681E-04   0.57375513E-04   0.57367535E-04
   0.57346311E-04   0.57322733E-04   0.57302990E-04   0.57282738E-04
   0.57262747E-04   0.57240050E-04   0.57201407E-04   0.57156467E-04
   0.57123143E-04   0.57097215E-04   0.57075260E-04   0.57064670E-04
   0.57052810E-04   0.57018340E-04   0.56950528E-04   0.56880377E-04
………………………….……………..
 'TRFIELD '          28 'DOUB'
   0.00000000000000D+00   0.00000000000000D+00   0.00000000000000D+00
   0.00000000000000D+00   0.00000000000000D+00   0.00000000000000D+00
   0.00000000000000D+00   0.00000000000000D+00   0.00000000000000D+00
   0.00000000000000D+00   0.00000000000000D+00   0.00000000000000D+00
   0.00000000000000D+00   0.00000000000000D+00   0.00000000000000D+00
   0.00000000000000D+00   0.00000000000000D+00   0.00000000000000D+00
   0.00000000000000D+00   0.00000000000000D+00   0.00000000000000D+00
   0.00000000000000D+00   0.00000000000000D+00   0.00000000000000D+00
   0.00000000000000D+00   0.00000000000000D+00   0.00000000000000D+00
   0.00000000000000D+00
 'ZTRACER '           2 'CHAR'
 'SEAF    ' '        '
 'SEAF    '       44431 'REAL'
   0.00000000E+00   0.00000000E+00   0.00000000E+00   0.00000000E+00
   0.00000000E+00   0.00000000E+00   0.00000000E+00   0.00000000E+00
   0.00000000E+00   0.00000000E+00   0.00000000E+00   0.00000000E+00
   0.00000000E+00   0.00000000E+00   0.00000000E+00   0.00000000E+00
   0.00000000E+00   0.00000000E+00   0.00000000E+00   0.00000000E+00
   0.00000000E+00   0.00000000E+00   0.00000000E+00   0.00000000E+00
   0.00000000E+00   0.00000000E+00   0.00000000E+00   0.00000000E+00
………………………….……………..
```

End of Example
        - RESTART Data - LGR Solution Data Keywords
    -
-

The file structure for this series of keywords is similar to the global grid [RESTART](#-refheading-toc135629-1317547213) Data keywords described previously. However, additional data that the defines the [LGR](#-refheading-toc55049-4106839650) properties \([LGR](#-refheading-toc55049-4106839650) Name for example\) are included in this keyword definition and the [LGR](#-refheading-toc55049-4106839650) keyword is repeated for each [LGR](#-refheading-toc55049-4106839650) in the model. The keyword description is outlined in Table A.36. 
Note that currently OPM Flow does not support [LGR](#-refheading-toc55049-4106839650) grids and therefore this keyword format cannot be used by OPM Flow.
| No. | keyword Name | [RESTART](#-refheading-toc135629-1317547213) Data \- [LGR](#-refheading-toc55049-4106839650) Grid Property Data keyword Table A.36 \(Repeated for Each [LGR](#-refheading-toc55049-4106839650) in the Model\) | Status or Value |
| --- | --- | --- | --- |
|  | [LGR](#-refheading-toc55049-4106839650) | [LGR](#-refheading-toc55049-4106839650) Grid Header keyword. See section A.5.1 RESTART Data \- LGR Grid Header Keywords. | Required |
| LGRHEADI |  |  |  |
| LGRHEADQ |  |  |  |
| LGRHEADD |  |  |  |
| INTEHEAD | Header keyword. See section A.8.3 RESTART Data \- Header Keywords. |  |  |
| LOGIHEAD |  |  |  |
| DOUBHEAD |  |  |  |
|  | IGRP SGRP etc. | Group, well, and connection data status keywords for this reporting time step. See section A.8.4 RESTART Data – Group, Well, and Connection Data Keywords. | Required |
|  | IAAQ SAAQ ect. | Aquifer definition arrays, only applicable if an aquifer is connected to an [LGR](#-refheading-toc55049-4106839650). See section A.8.6 RESTART Data – Aquifer Data Keywords. | Optional |
|  | HIDDEN | HIDDEN solution data, that is a list of solution arrays NOT to be read by post processing software. See section A.8.7 RESTART Data – Hidden Keyword. | Required |
|  | [SOLUTION](#-refheading-toc43947-784232322) | [LGR](#-refheading-toc55049-4106839650) [SOLUTION](#-refheading-toc43947-784232322) array section \([PRESSURE](#-refheading-toc135627-1317547213), [SGAS](#-refheading-toc137369-1317547213), SOILS, WAT, etc.\). See section A.8.8 RESTART Data \- Solution Data keyword. | Required |
|  | ENDSOL | [LGR](#-refheading-toc55049-4106839650) [SOLUTION](#-refheading-toc43947-784232322) section termination keyword. See section A.8.8 RESTART Data \- Solution Data keyword. | Required |
|  | ENDLGR | [LGR](#-refheading-toc55049-4106839650) grid header section termination keywords. See section A.5.1 RESTART Data \- LGR Grid Header Keywords. | Required |
| Notes: - Rows shaded in gray indicate the start of a keyword. - Cells colored orange in the No. column indicate that this item is not supported by OPM Flow. - For formatted output all character variables, including the keyword, should be enclosed in single quotes, for example the [LGR](#-refheading-toc55049-4106839650) keyword should be written out as ‘LGR     ’. |  |  |  |

Table A.36: RESTART Data – LGR Solution Data Keywords

This set of keywords are repeated for each [LGR](#-refheading-toc55049-4106839650) in the model with the last [LGR](#-refheading-toc55049-4106839650) data set terminated by the ENDSOL and ENDLGR keywords to mark the end of the [LGR](#-refheading-toc55049-4106839650) input  \-  see the example.

#### <a id="-refheading-toc716963-3964674244"></a>Example: RESTART Data \- LGR Solution Data Keywords

The following example shows a typical formatted data set with two [LGR](#-refheading-toc55049-4106839650) grids named LGR\-1 and LGR\-2.
```eclipse
 'LGR     '           1 'CHAR'
 'LGR-1   '
 'LGRHEADI'          45 'INTE'
           1         100       -2345       -2345       -2345       -2345
………………………….……………..
       -2345       -2345       -2345
 'LGRHEADQ'           5 'LOGI'
  F  F  F  F  F
 'LGRHEADD'           5 'DOUB'
   0.00000000000000D+00  -0.10000000200409D+21  -0.10000000200409D+21
  -0.10000000200409D+21  -0.10000000200409D+21
 'INTEHEAD'         249 'INTE'
………………………….……………..
 'LOGIHEAD'          79 'LOGI'
………………………….……………..
 'DOUBHEAD'         185 'DOUB'
………………………….……………..
 'IGRP    '         358 'INTE'
           0           0           0           0           0           0
………………………….……………..
           0           0           0           0
 'SGRP    '         186 'REAL'
   0.00000000E+00   0.00000000E+00   0.00000000E+00   0.00000000E+00
………………………….……………..
   0.00000000E+00   0.10000000E+01
 'XGRP    '         348 'DOUB'
   0.00000000000000D+00   0.00000000000000D+00   0.00000000000000D+00
………………………….……………..
   0.00000000000000D+00   0.00000000000000D+00   0.00000000000000D+00
 'ZGRP    '          10 'CHAR'
 '        ' '        ' '        ' '        ' '        ' 'FIELD   ' '        '
 '        ' '        ' '        '
 'ICOT    '           0 'INTE'
 'XCOT    '           0 'DOUB'
 'IWET    '           0 'INTE'
 'XWET    '           0 'DOUB'
 'IGRT    '          18 'INTE'
………………………….……………..
 'XGRT    '         180 'DOUB'
   0.00000000000000D+00   0.00000000000000D+00   0.00000000000000D+00
………………………….……………..
   0.10000000200409D+21   0.10000000200409D+21   0.10000000200409D+21
 'DLYTIM  '          30 'DOUB'
   0.00000000000000D+00   0.00000000000000D+00   0.00000000000000D+00
………………………….……………..
   0.00000000000000D+00   0.00000000000000D+00   0.00000000000000D+00
 'HIDDEN  '          51 'CHAR'
 'ISTHGGI ' 'SWMAX   ' 'SWHY1   ' 'SWHY2   ' 'SWHY3   ' 'ISTHW   ' 'SOMAX   '………………………….……………..
 'IAQN    ' 'RAQN    '
 'STARTSOL'           0 'MESS'
 'PRESSURE'           9 'REAL'
   0.26823886E+03   0.26824997E+03   0.26826108E+03   0.26822879E+03
………………………….……………..
 'SWAT    '           9 'REAL'
   0.10500000E+00   0.10500000E+00   0.10500000E+00   0.10500000E+00
………………………….……………..
 'SGAS    '           9 'REAL'
   0.89499998E+00   0.89499998E+00   0.89499998E+00   0.89499998E+00
………………………….……………..
 'RS      '           9 'REAL'
   0.12021812E+03   0.12022437E+03   0.12023062E+03   0.12021246E+03
………………………….……………..
 'RV      '           9 'REAL'
   0.57467099E-04   0.57473411E-04   0.57479720E-04   0.57461380E-04
………………………….……………..
 'ENDSOL  '           0 'MESS'
 'ENDLGR  '           1 'INTE'
           1
 'LGR     '           1 'CHAR'
 'LGR-2   '
 'LGRHEADI'          45 'INTE'
………………………….……………..
 'LGRHEADQ'           5 'LOGI'
………………………….……………..
 'LGRHEADD'           5 'DOUB'
………………………….……………..
 'INTEHEAD'         249 'INTE'
………………………….……………..
 'LOGIHEAD'          79 'LOGI'
………………………….……………..
 'DOUBHEAD'         185 'DOUB'
………………………….……………..
 'IGRP    '         358 'INTE'
………………………….……………..
 'SGRP    '         186 'REAL'
………………………….……………..
 'XGRP    '         348 'DOUB'
………………………….……………..
 'ZGRP    '          10 'CHAR'
………………………….……………..
 'ICOT    '           0 'INTE'
 'XCOT    '           0 'DOUB'
 'IWET    '           0 'INTE'
 'XWET    '           0 'DOUB'
 'IGRT    '          18 'INTE'
………………………….……………..
 'XGRT    '         180 'DOUB'
………………………….……………..
 'DLYTIM  '          30 'DOUB'
………………………….……………..
 'HIDDEN  '          51 'CHAR'
………………………….……………..
 'STARTSOL'           0 'MESS'
 'PRESSURE'           9 'REAL'
………………………….……………..
 'SWAT    '           9 'REAL'
………………………….……………..
 'SGAS    '           9 'REAL'
………………………….……………..
 'RS      '           9 'REAL'
………………………….……………..
 'RV      '           9 'REAL'
………………………….……………..
 'ENDSOL  '           0 'MESS'
 'ENDLGR  '           1 'INTE'
           2
 'SEQNUM  '           1 'INTE'
           4
```

End of Example
    - RFT Files – Pressure, Saturation and Production Log Data
-

The Repeat Formation Tester \(“RFT”\) file contains a well’s depth pressure profile at the time the data is requested using the [WRFT](#-refheading-toc268467-1366622701) or [WRFTPLT](#-refheading-toc268469-1366622701) keywords in the [SCHEDULE](#-refheading-toc43945-784232322) section.  The data is meant to be used to compare the simulator’s pressure profile with the field measured data collected from one of the open hole wire line logging tools: Formation Interval Tester \(“FIT”\), Repeat Formation Tester \(“RFT”\) tool, Modular  Dynamics Tester \(“MDT”\), or similar tool. The keywords also export the fluid saturations for the well connections at the same time.

In addition to the pressure and saturation data, the [WRFTPLT](#-refheading-toc268469-1366622701) keyword can also active the writing out of each well connection’s fluid rates, connection factors and KH data, etc., collectively known as the Production Logging Tool \(“PLT”\) data. The PLT data is used to compare with measured data from wire line production logging tools. Currently, output of the PLT data is not supported by OPM Flow.
        - RFT Data File Specification
    -
-

The file structure for the RFT Data File consists of various keywords: a Time and Date keyword, a Well and Connection keyword followed by the requested optional keywords of RFT, PLT, Multi\-Segment Well, and River keywords, that are written out depending on the data requested. A brief description of the keywords is given in Table A.37.  A complete RFT data set is written to file for each well and time step as requested on the [WRFT](#-refheading-toc268467-1366622701) and [WRFTPLT](#-refheading-toc268469-1366622701) keywords.
| Reference Section | keyword Name | keyword Type | Description |
| --- | --- | --- | --- |
| A.9.2 | [TIME](#-refheading-toc1252966-4250154414) | Time and Date Date | This data set contains the simulated time and date information that the date was written out. |
| [DATE](#-refheading-toc210146-2884651453) |  |  |  |
| A.9.3 | WELLETC | Well and Connection Data | The Well and Connection keywords outlines the type and units being written out, the type of well and the well connections at the simulated time the data is written out to the RFT file. |
| CONIPOS |  |  |  |
| CONJPOS |  |  |  |
| CONKPOS |  |  |  |
| HOSTGRID |  |  |  |
| A.9.4 | [DEPTH](#-refheading-toc58139-3701168388) | RFT Solution Data | RFT keyword data consists of the pressure and saturations for each declared connection in the well at the simulated time the data is written out to file. |
| [PRESSURE](#-refheading-toc135627-1317547213) |  |  |  |
| [SWAT](#-refheading-toc137373-1317547213) |  |  |  |
| [SGAS](#-refheading-toc137369-1317547213) |  |  |  |
| CPLY |  |  |  |
| CPLAD |  |  |  |
| CBRI |  |  |  |
| A.9.5 |  | PLT Solution Data | PLT series of keywords contain the production logging data which consists of the mid\-point depth of each connection, the tubing length for the connection from the bottom\-hole reference depth, the pressures and fluid rates for the connections. In addition, this data also includes the well pressures, fluid rates, connection transmissibility and KH vales, for the given simulated time. Currently this data set is not supported. |
| A.9.6 |  | Multi\-Segment Well Data | The Multi\-Segment Well data set consists of pressure and flow rate data for segments and branches, currently this data set is not supported. |
| A.9.7 |  | River Data | Data pertaining to the Rivers option, this option is not supported by OPM Flow. |
| Notes: - Reference Section cells colored orange indicate that this item is not supported by OPM Flow. |  |  |  |

Table A.37: RFT Data File Format

        - RFT Data File – Time and Date keywords
    -
-

The time and date keywords define the start of an RFT data set and declares the time and date for the subsequent property data written to file. The structure for these two keywords is summarized in Table A.38.
| No. | keyword Name | RFT Data File – Time and Date keywords Table A.38 |  |  | Status or Value |
| --- | --- | --- | --- | --- | --- |
| Keyword | No. of Entries | Data Type |  |  |  |
|  | [TIME](#-refheading-toc1252966-4250154414) | This keyword marks the start of of an RFT file data set. |  |  | Required |
| 1\-1 | Format | [TIME](#-refheading-toc1252966-4250154414) | 1 | REAL |  |
| 2\-1 | Data | Simulation time the data is being written to file. |  |  |  |
|  | [DATE](#-refheading-toc210146-2884651453) | Three integer values representing the date of the data being written out. |  |  | Required |
| 1\-1 | Format | [DATE](#-refheading-toc210146-2884651453) | 3 | INTE |  |
| 2\-1 | Data | Calendar day and should range between one and 31. |  |  | DAY |
| 2\-2 | Data | Calendar month and should range between one and 12. |  |  | MONTH |
| 2\-3 | Data | Calendar year in four digits, that is 2020. |  |  | YEAR |
| Notes: - Rows shaded in gray indicate the start of a keyword. - For formatted output all character variables, including the keyword should be enclosed in single quotes, for example the [TIME](#-refheading-toc1252966-4250154414) should be written out as ‘TIME     ’. |  |  |  |  |  |

Table A.38: RFT Data File – Time and Date Keywords

The [DATE](#-refheading-toc210146-2884651453) keyword is immediate followed by the well and connection keywords.

        - RFT Data File – Well and Connection Data Keyword
    -
-

The well and connection data set of keywords specify the well and the well connection data as well as the system of units for the pressure and flow data being written to the RFT file. The structure for this set of keywords is outlined in Table A.39 and consists of WELLETC,  CONIPOS, CONJPOS, CONKPOS and HOSTGRID keywords. 
| No. | keyword Name | RFT Data File – Well and Connection Data keyword Table A.39 |  |  | Status or Value |
| --- | --- | --- | --- | --- | --- |
|  | WELLETC | This keyword marks the start of the well and connection data set and comprises of 16 character variables all enclose in single quotes. |  |  | Required |
| 1\-1 | Format | WELLETC | 16 | CHAR |  |
| 2\-1 | Data | Time units. |  |  |  |
| 2\-2 | Data | Well name. |  |  |  |
| 2\-3 | Data | Local Grid Refinement \(“LGR”\) name or left blank if the well is not in an [LGR](#-refheading-toc55049-4106839650). LGRs are not currently supported by OPM Flow. |  |  | Blank |
| 2\-4 | Data | Depth units. |  |  |  |
| 2\-5 | Data | Pressure units. |  |  |  |
| 2\-6 | Data | Type of data being written out in subsequent keywords and should be set to R for RFT data, P for PLT data, or S for Segment data. The Segment data option is not currently supported in OPM Flow. |  |  |  |
| 2.7 | Data | Well type data set to STANDARD for a standard well, [FRICTION](#-refheading-toc327648-803326780) for a wellbore friction well, and MULTSEG for a multi\-segment well. Only the STANDARD well option is currently supported by OPM Flow. |  |  |  |
| 2\-8 | Data | Liquid flow rate units. |  |  |  |
| 2\-9 | Data | Gas flow rate units. |  |  |  |
| 2\-10 | Data | Local volumetric flow rate units. |  |  |  |
| 2\-11 | Data | Flow velocity units. |  |  |  |
| 2\-12 | Data | Not used and should be a blank character string. |  |  | Blank |
| 2\-13 | Data | Liquid and gas viscosity units. |  |  |  |
| 2\-14 | Data | Polymer and Brine concentration units. |  |  |  |
| 2\-15 | Data | Polymer and Brine flow rate units. |  |  |  |
| 2\-16 | Data | Adsorbed Polymer concentration units. |  |  |  |
|  | CONIPOS | This keyword defines the grid index in the x direction \(I direction\) for all NCON connections in the well associated with the RFT data set. |  |  | Required |
| 1\-1 | Format | CONIPOS | NCON | INTE |  |
| 2\-1 | Data | Grid index in the I direction for each connection. |  |  |  |
|  | CONJPOS | This keyword defines the grid index in the y direction \(J direction\) for all NCON connections in the well associated with the RFT data set. |  |  | Required |
| 1\-1 | Format | CONJPOS | NCON | INTE |  |
| 2\-1 | Data | Grid index in the J direction for each connection. |  |  |  |
|  | CONKPOS | This keyword defines the grid index in the z direction \(K direction\) for all NCON connections in the well associated with the RFT data set. |  |  | Required |
| 1\-1 | Format | CONKPOS | NCON | INTE |  |
| 2\-1 | Data | Grid index in the K direction for each connection. |  |  |  |
|  | HOSTGRID | Defines the [LGR](#-refheading-toc55049-4106839650) name for each of the NCON connections. [LGR](#-refheading-toc55049-4106839650)’s have not been implemented in OPM Flow and therefore this keyword should contain NCON blank character strings. |  |  | Blank |
| 1\-1 | Format | HOSTGRID | NCON | CHAR | Blank |
| 2\-1 | Data | Connections host [LGR](#-refheading-toc55049-4106839650) grid name. |  |  |  |
| Notes: - Rows shaded in gray indicate the start of a keyword. - For formatted output all character variables, including the keyword, should be enclosed in single quotes, for example the WELLETC should be written out as ‘WELLETC  ’. |  |  |  |  |  |

Table A.39: RFT Data File – Well and Connection Data Keyword

This series of keywords are immediate followed by the RFT solution keywords: [DEPTH](#-refheading-toc58139-3701168388), [PRESSURE](#-refheading-toc135627-1317547213), [SWAT](#-refheading-toc137373-1317547213),  and [SGAS](#-refheading-toc137369-1317547213).

        - RFT Data File – RFT Solution Data Keyword
    -
-

The RFT solution keywords specify the actual solution data \(pressure, saturation etc.\) for each connection in the well, as described in Table A.40.
| No. | keyword Name | [RESTART](#-refheading-toc135629-1317547213) Data \- Solution Data keyword Table A.40 |  |  | Status or Value |
| --- | --- | --- | --- | --- | --- |
| Keyword | No. of Entries | Data Type |  |  |  |
| 1\-1 | [DEPTH](#-refheading-toc58139-3701168388) | Connection grid block depth. |  |  | Required |
| 1\-1 | Format | [DEPTH](#-refheading-toc58139-3701168388) | NCON | REAL |  |
| 2\-1 | Data | Depth data for each connection. |  |  |  |
|  | [PRESSURE](#-refheading-toc135627-1317547213) | Connection grid block pressure at the requested time. |  |  | Required |
| 1\-1 | Format | [PRESSURE](#-refheading-toc135627-1317547213) | NCON | REAL |  |
| 2\-1 | Data | Pressure data for each connection. |  |  |  |
|  | [SWAT](#-refheading-toc137373-1317547213) | Connection grid block water saturation at the requested time. |  |  | Required |
| 1\-1 | Format | [SWAT](#-refheading-toc137373-1317547213) | NCON | REAL |  |
| 2\-1 | Data | Water saturation data for each connection. |  |  |  |
| 2\-4 | [SGAS](#-refheading-toc137369-1317547213) | Connection grid block gas saturation at the requested time. |  |  | Required |
| 1\-1 | Format | [SGAS](#-refheading-toc137369-1317547213) | NCON | REAL |  |
| 2\-1 | Data | Gas saturation data for each connection. |  |  |  |
|  | CPLY | Connection grid block polymer concentration at the requested time. |  |  | Optional |
| 1\-1 | Format | CPLY | NCON | REAL |  |
| 2\-1 | Data | Polymer concentration data for each connection. |  |  |  |
|  | CPLAD | Connection grid block adsorbed polymer concentration at the requested time. |  |  | Optional |
| 1\-1 | Format | CPLAD | NCON | REAL |  |
| 2\-1 | Data | Adsorbed polymer concentration data for each connection. |  |  |  |
|  | CBRI | Connection grid block brine concentration at the requested time. |  |  | Optional |
| 1\-1 | Format | CBRI | NCON | REAL |  |
| 2\-1 | Data | Brine concentration data for each connection. |  |  |  |
| Notes: - Rows shaded in gray indicate the start of a keyword. - Cells colored orange in the No. column indicate that this item is not supported by OPM Flow. - For formatted output all character variables, including the keyword, should be enclosed in single quotes, for example the [PRESSURE](#-refheading-toc135627-1317547213) keyword should be written out as ‘PRESSURE ’. |  |  |  |  |  |

Table A.40: RFT Data File – RFT Solution Data Keywords

A complete standard RFT example showing the [TIME](#-refheading-toc1252966-4250154414), [DATE](#-refheading-toc210146-2884651453), WELLETC, CONIPOS, CONJPOS, CONKPOS, [DEPTH](#-refheading-toc58139-3701168388), [PRESSURE](#-refheading-toc135627-1317547213), [SWAT](#-refheading-toc137373-1317547213), and [SGAS](#-refheading-toc137369-1317547213) keywords, for one well at one time step is shown on the following page.

#### <a id="-refheading-toc716965-3964674244"></a>Example

The example shows all the keywords required to define a standard RFT data set for well B\-4H which has 20 connection as of March 29, 1998.  The units declared on the WELLETC keyword indicate the standard metric unit system. 
```eclipse
 'TIME    '           1 'REAL'
   0.14300000E+03
 'DATE    '           3 'INTE'
          29           3        1998
 'WELLETC '          16 'CHAR'
 '  DAYS  ' 'B-4H    ' '        ' ' METRES ' '  BARSA ' 'R       ' 'STANDARD'
 ' SM3/DAY' ' SM3/DAY' ' RM3/DAY' ' M/SEC  ' '        ' '   CP   ' ' KG/SM3 '
 ' KG/DAY ' '  KG/KG '
 'CONIPOS '          20 'INTE'
          10          10          10          10          10          10
          10          10          10           9           9           9
           9           9           9           9           9           9
           9           9
 'CONJPOS '          20 'INTE'
          32          32          32          32          32          32
          32          32          32          32          32          32
          32          32          32          32          32          31
          31          31
 'CONKPOS '          20 'INTE'
           1           2           3           5           6           7
           8           9          10          13          14          15
          16          17          18          19          20          20
          21          22
 'HOSTGRID'          20 'CHAR'
 '        ' '        ' '        ' '        ' '        ' '        ' '        '
 '        ' '        ' '        ' '        ' '        ' '        ' '        '
 '        ' '        ' '        ' '        ' '        ' '        '
 'DEPTH   '          20 'REAL'
   0.25333979E+04   0.25452786E+04   0.25577705E+04   0.25742898E+04
   0.25797493E+04   0.25855930E+04   0.25918203E+04   0.25966951E+04
   0.26071150E+04   0.26206902E+04   0.26333235E+04   0.26461284E+04
   0.26576768E+04   0.26637878E+04   0.26665945E+04   0.26786790E+04
   0.27012888E+04   0.27033108E+04   0.27381892E+04   0.27746746E+04
 'PRESSURE'          20 'REAL'
   0.27384171E+03   0.27406891E+03   0.27430649E+03   0.25063243E+03
   0.25072800E+03   0.25085713E+03   0.25126656E+03   0.25138820E+03
   0.25212048E+03   0.25290869E+03   0.25380568E+03   0.25471658E+03
   0.25669318E+03   0.25713290E+03   0.25733768E+03   0.26151834E+03
   0.26378452E+03   0.26398804E+03   0.28049472E+03   0.28405634E+03
 'SWAT    '          20 'REAL'
   0.79952940E-01   0.10493817E+00   0.16989987E+00   0.10517924E+00
   0.10518920E+00   0.14012721E+00   0.14357868E+00   0.80211885E-01
   0.80138676E-01   0.80140039E-01   0.90355128E-01   0.19185907E+00
   0.12343995E+00   0.29019111E+00   0.14448708E+00   0.32566309E+00
   0.10000000E+01   0.10000000E+01   0.10000000E+01   0.10000000E+01
 'SGAS    '          20 'REAL'
   0.92004704E+00   0.89506185E+00   0.83010012E+00   0.89231288E+00
   0.89236671E+00   0.14750090E+00   0.17341191E-01   0.64456672E-02
   0.00000000E+00   0.00000000E+00   0.00000000E+00   0.00000000E+00
   0.00000000E+00   0.00000000E+00   0.00000000E+00   0.00000000E+00
   0.00000000E+00   0.00000000E+00   0.00000000E+00   0.00000000E+00
```

End of Example
        - RFT Data File – Solution PLT Data Keywords
    -
-

This data set is currently not supported.
        - RFT Data File – Solution Multi-Segment Well Keywords
    -
-

This data set is currently not supported.
        - RFT Data File – Solution River Keywords
    -
-

This data set is currently not supported.
    - SUMMARY Files – Time Based Vector Data
-

The [SUMMARY](#-refheading-toc43949-784232322) files contain the variables requested to be written to the summary files via the keywords declared in the [SUMMARY](#-refheading-toc43949-784232322) section. The data are used to generate line graphs of properties such as oil flow rate versus time, grid block pressure versus time, etc.  See sections [Error: Reference source not found Error: Reference source not found](#112data-requirements) and [Error: Reference source not found Error: Reference source not found](#113keyword-definitions) that declare the variables to be written out to the [SUMMARY](#-refheading-toc43949-784232322) files. The default behavior is write out the requested variables at each time step. As this can lead to large files, especially for full field simulation models, the [Error: Reference source not found](#1024rptonly---activate-the-report-time-steps-only-option-for-the-summary-file) keyword allows one to write out the data only at a report time step instead.
There are three types of [SUMMARY](#-refheading-toc43949-784232322) files, the first [SUMMARY](#-refheading-toc43949-784232322) file is the OPM Flow specific Enhanced [SUMMARY](#-refheading-toc43949-784232322)  \(\*.ESMRY\) output file that is optimized for fast loading of selected vectors by post\-processing applications, including OPM ResInsight. This file type is standalone, that is there is no separate index file.
The other two files types associated with the time based vector data, is an index file \([SUMMARY](#-refheading-toc43949-784232322) Index\) that contains a list of variables and objects \(wells, groups, connections etc.\) that are to be written out to summary data file, and the summary data file \([SUMMARY](#-refheading-toc43949-784232322) Data\) that contains the actual data written out at the required time steps.  The commercial simulator uses the term “MINISTEP”  to describe the time the data is written, and as mentioned above, “MINISTEP” may be either a time step or a reporting time step.
        - Enhanced SUMMARY Data File Keywords
    -
-

Again, this is an OPM FLOW specific Enhanced [SUMMARY](#-refheading-toc43949-784232322)  \(\*.ESMRY\) output file format that is optimized for fast loading of selected vectors by post\-processing applications. The \*.ESMRY file is re\-written for every time step and load times are in the order of 30 times faster compared with fetching selected vectors using the \*.UNSMRY file format in post processing software.  The file type is compatible with OPM ResInsight and the option is activated via the enable\-esmry=true command line option. 
The structure for this series of keywords is outlined in Table A.41 and depends on the data requested to be written out to the [SUMMARY](#-refheading-toc43949-784232322) files.
| No. | keyword Name | Enhanced [SUMMARY](#-refheading-toc43949-784232322) File keywords Table A.41 |  |  | Status or Value |
| --- | --- | --- | --- | --- | --- |
|  | [START](#-refheading-toc39156-327352552) | Three integer values representing the start date of the simulation., and four integers representing the hour, minutes, seconds and micro seconds the start date. |  |  | Required |
| 1\-1 | Format | [START](#-refheading-toc39156-327352552) | 7 | INTE |  |
| 2\-1 | Data | First part of start date of the run, DAY, the value should be greater than or equal to one and less than or equal to 31 for the calendar days. |  |  | DAY |
| 2\-2 | Data | Second part of start date of the run, MONTH, the value should be greater than or equal to one and less than or equal to 12 for the calendar month. |  |  | MONTH |
| 2\-3 | Data | Third part of start date of run,  YEAR, a positive four digit integer value of the start year, which must be specified fully by four digits, for example 1986. |  |  | YEAR |
| 2\-4 | Data | The first part of the start time in the form HH:MM:SS:MS, that is HH for hours. The value should be greater than or equal to zero and less than or equal to 23. |  |  | IHOURZ |
| 2\-5 | Data | The second part of the start time in the form HH:MM:SS:MS, that is MM for minutes. The value should be greater than or equal to zero and less than or equal to 59. |  |  | IMINTS |
| 2\-6 | Data | The third part of the start time in the form HH:MM:SS:MS, that is SS for seconds. The value should be greater than or equal to zero and less than or equal to 59. |  |  | ISECND |
| 2\-7 | Data | The fourth part of the start time in the form HH:MM:SS:MS, that is MS for milliseconds. The value should be greater than or equal to zero and less than or equal to 999. |  |  |  |
|  | [RESTART](#-refheading-toc135629-1317547213) | [RESTART](#-refheading-toc135629-1317547213) is only present for restarted runs and contains the root file name \(absolute or relative path\) to the case which this run was restarted from. |  |  | Optional |
| 1\-1 | Format | [RESTART](#-refheading-toc135629-1317547213) | 1 | C0nn |  |
| 2\-1 | Data | The name of file, enclosed in quotes, which contains the name of the case the current run was re\-started from. The length of the character string is set by the Data Type, C0nn, for example, C125 would mean that the [RESTART](#-refheading-toc135629-1317547213) filename character length is 125 characters. |  |  |  |
|  | RSTNUM | The RSTNUM keyword is only present for restart runs and defines the report time step this case was restarted from. |  |  | Optional |
| 1\-1 | Format | RSTNUM | 1 | INTE |  |
| 2\-1 | Data | Restart report time step. number. |  |  |  |
|  | KEYCHECK | A list of all the summary variable mnemonics written to the file at each time step., where NLIST is the number of vectors and C0nn is the constant fixed length of each variable character string. For example: 'KEYCHECK'           6 'C010' 'TIME      ' 'YEARS     ' 'FOPR      ' 'GGOR:PROD ' 'TCPU      ' 'WOPR:PROD1' Where each vector name consists of 10 characters. For vectors associated with objects, groups, wells etc., the vector name is follows by a “:” and then the object name as shown in the above example. |  |  | Required |
| 1\-1 | Format | KEYCHECK | NLIST | C0nn |  |
| 2\-1 | Data | Each mnemonic string should be enclosed in quotes and have a character length of C0nn, for example ‘C010’ in the above example. |  |  |  |
|  | UNITS | Units |  |  | Required |
| 1\-1 | Format | UNITS | NLIST | CHAR |  |
| 2\-1 | Data | Units for the associated summary variable mnemonics. |  |  |  |
|  | RSTEP | An array that holds one integer value for each time step.  An integer value of one indicates time steps that are also report time steps and a zero  indicates time steps only. |  |  | Required |
| 1\-1 | Format | RSTEP | NSTEP | INTE |  |
| 2\-1 | Data | One value for each time step and the values should be either zero or one. |  |  |  |
|  | [TSTEP](#-refheading-toc118323-1596574740) | An array holding one integer value for each time step with the values representing the time step indices. Note that the values starts from zero, such that the Data will have values of the form 0, 1, 2, ..., NSTEP \- 1, that is unless the [RPTONLY](#-refheading-toc210150-2884651453) keyword has been used in the [SUMMARY](#-refheading-toc43949-784232322) section to write only the report time steps to the file. Values should range between 0 to NSTEP \- 1 |  |  | Required |
| 1\-1 | Format | [TSTEP](#-refheading-toc118323-1596574740) | NSTEP | INTE |  |
| 2\-1 | Data | One value for each time step. with the value ranging from zero to NSTEP \- 1. |  |  |  |
|  | VX | One data array \(length = NSTEP\) for each summary vector specified in array KEYCHECK. Naming of these arrays should be V0, V1, V2, … etc. |  |  | Required |
| 1\-1 | Format | VX | NSTEP | REAL |  |
| 2\-1 | Data | One real value for each time step for one specific summary vector VX vector, where X ranges from zero to NLIST – 1, for the NLIST variables declared via the KEYCHECK keyword. |  |  |  |
| Notes: - Keywords are order dependent. - For formatted output all character variables, including the keyword, should be enclosed in single quotes, for example the [START](#-refheading-toc39156-327352552) and KEYCHECK keywords should be written out as ‘START    ’ and  ‘KEYCHECK’. |  |  |  |  |  |

Table A.41: Enhanced SUMMARY File Keywords

#### Example: Enhanced SUMMARY File Keywords

The following example shows a typical formatted Enhanced [SUMMARY](#-refheading-toc43949-784232322) file set of keywords.
```eclipse
'START   '           7 'INTE'
           1          11        2018           0           0           0
           0
'KEYCHECK'           6 'C010'
'TIME      ' 'YEARS     ' 'FOPR      ' 'GGOR:PROD ' 'TCPU      ' 'WOPR:PROD1'
'UNITS   '           6 'CHAR'
'DAYS    ' '        ' 'SM3/DAY ' 'SM3/SM3 ' 'SECONDS ' 'SM3/DAY '
'RSTEP   '           4 'INTE'
           1           1           0           1
'TSTEP   '           4 'INTE'
           0           1           2           3
'V0      '           4 'REAL'
    1.0000000E+00    4.0000000E+00    9.0000000E+00    1.4000000E+01
'V1      '           4 'REAL'
    2.7378509E-03    1.0951404E-02    2.4640657E-02    3.8329910E-02
'V2      '           4 'REAL'
    0.0000000E+00    0.0000000E+00    0.0000000E+00    0.0000000E+00
'V3      '           4 'REAL'
    0.0000000E+00    0.0000000E+00    0.0000000E+00    0.0000000E+00
'V4      '           4 'REAL'
    6.0681427E-01    6.5710169E-01    7.0169014E-01    7.6383120E-01
'V5      '           4 'REAL'
    0.0000000E+00    0.0000000E+00    0.0000000E+00    0.0000000E+00
```

The example shows the file holding six summary vector and four time steps, with the first, second and fourth time steps being report time steps.  
        - SUMMARY Index File keywords
    -
-

The structure for this series of keywords is outlined in Table A.42, Table A.43, and Table A.44 and depends on the data requested to be written out to the [SUMMARY](#-refheading-toc43949-784232322) Data File.
| No. | keyword Name | [SUMMARY](#-refheading-toc43949-784232322) Index File keywords \(Global\) Table A.42 |  |  | Status or Value |
| --- | --- | --- | --- | --- | --- |
|  | INTEHEAD | The integer header keyword contains two values indicating the units system and the simulator used to generate the file. |  |  | Required |
| 1\-1 | Format | INTEHEAD | 2 | INTE |  |
| 2\-1 | Data | Unit system used in the simulation, set to 1 for metric, 2 for field, and 3 for laboratory |  |  |  |
| 2\-2 | Data | Simulator code used to generate the file, set to: 100 for Schlumberger’s ECLIPSE 100, 300 for Schlumberger’s ECLIPSE 300, 500 for Schlumberger’s ECLIPSE 300 Thermal, 700 for Schlumberger’s INTERSECT simulator, 800 for Schlumberger’s FrontSim simulator, or a negative value for other simulators. OPM Flow uses a value of 100. |  |  | 100 |
|  | [RESTART](#-refheading-toc135629-1317547213) | Contains the root file name of the case which this run was restarted from, if this was a restart run, other wise blank. |  |  | Required |
| 1\-1 | Format | [RESTART](#-refheading-toc135629-1317547213) | 9 | CHAR |  |
| 2\-1 | Data | Maximum of 72 characters divided into eight character words. For example, if the data file is restarted from NOR01\-PRED01\-OPM2004\-R00, then this data will be of the form: 'NOR01\-PR' 'ED01\-OPM' '2010\-R00' '        ' '        ' '        ' '        ' '        ' '        ' |  |  |  |
|  | [DIMENS](#-refheading-toc20387-2267116897) | This keyword contains the number of vectors and objects written to the [SUMMARY](#-refheading-toc43949-784232322) Data file at each time step. |  |  | Required |
| 1\-1 | Format | [DIMENS](#-refheading-toc20387-2267116897) | 6 | REAL |  |
| 2\-1 | Data | NLIST is the number of values stored at each time step on the [SUMMARY](#-refheading-toc43949-784232322) Data File. |  |  |  |
| 2\-2 | Data | The number of grid blocks in the x\-direction \(NX\). |  |  |  |
| 2\-3 | Data | The number of grid blocks in the y\-direction \(NY\). |  |  |  |
| 2\-4 | Data | The number of grid blocks in the z\-direction \(NZ\). |  |  |  |
| 2\-5 | Data | Not Used. |  |  | 0 |
| 2\-6 | Data | Report time step of the case which this run was restated from, if this was a restart run. |  |  | 0 |
|  | KEYWORDS | A list of all the summary variable mnemonics written to the [SUMMARY](#-refheading-toc43949-784232322) Data file at each time step. |  |  | Required |
| 1\-1 | Format | KEYWORDS | NLIST | CHAR |  |
| 2\-1 | Data | Each mnemonic string should be enclosed in quotes. |  |  |  |
|  | WGNAMES | A list of all well and group objects associated with summary variable mnemonics |  |  | Required |
| 1\-1 | Format | WGNAMES | NLIST | CHAR |  |
| 2\-1 | Data | Each well and group name should be enclosed in quotes |  |  |  |
|  | NUMS | Integer grid cell or region number associated with the summary variable mnemonics. |  |  | Required |
| 1\-1 | Format | NUMS | NLIST | INTE |  |
| 2\-1 | Data | Integer values. |  |  |  |
|  | LENGTHS | Horizontal well length. |  |  | Optional |
| 1\-1 | Format | LENGTHS | NLIST | REAL |  |
| 2\-1 | Data | The distance from the bottom\-hole reference depth to the completion depth for the associated summary variable mnemonics for horizontal wells |  |  |  |
|  | LENUNITS | Horizontal well length units. |  |  | Optional |
| 1\-1 | Format | LENUNITS | 1 | CHAR |  |
| 2\-1 | Data | Horizontal well length units. |  |  |  |
|  | MEASRMNT | Measurements associated with each summary variable mnemonic. |  |  | Optional |
| 1\-1 | Format | MEASRMNT | NBLOCK x NLIST | CHAR |  |
| 2\-1 | Data | NBLOCK is equal to the number of elements provided by this keyword divided by NLIST. |  |  |  |
|  | UNITS | Units |  |  | Required |
| 1\-1 | Format | UNITS | NLIST | CHAR |  |
| 2\-1 | Data | Units for the associated summary variable mnemonics. |  |  |  |
|  | STARTDAT | Three integer values representing the date and four integers representing the time of the data being written out. |  |  | Required |
| 1\-1 | Format | STARTDAT | 3 | INTE |  |
| 2\-1 | Data | Calendar day and should range between one and 31. |  |  | DAY |
| 2\-2 | Data | Calendar month should range between one and 12. |  |  | MONTH |
| 2\-3 | Data | Calendar year in four digits, that is 2020. |  |  | YEAR |
| 2\-4 | Data | Hour. |  |  | HOUR |
| 2\-5 | Data | Minutes. |  |  | MINUTE |
| 2\-6 | Data | Seconds in micro seconds, 0\-59:999:999 |  |  | SECOND |
| Notes: - Keywords up to and including the NUMS keyword are order dependent, after the NUMS keyword the keywords may be in any order. - Rows shaded in gray indicate the start of a keyword. - Cells colored orange in the No. column indicate that this item is not supported by OPM Flow and those colored red are either “Not Used” or “Undefined”. - For formatted output all character variables, including the keyword, should be enclosed in single quotes, for example the INTEHEAD and [DIMENS](#-refheading-toc20387-2267116897) keywords should be written out as ‘INTEHEAD ’ and  ‘DIMENS  ’. |  |  |  |  |  |

Table A.42: SUMMARY Index File Keywords \(Global\)
In addition, Table A.43 summarizes the [SUMMARY](#-refheading-toc43949-784232322) Index File keywords associated with Local Grid Refinements.

| No. | keyword Name | [SUMMARY](#-refheading-toc43949-784232322) Index File keywords \([LGR](#-refheading-toc55049-4106839650)\) Table A.43 |  |  | Status or Value |
| --- | --- | --- | --- | --- | --- |
|  | LGRS | Local Grid Refinement names associated summary variable mnemonic for [LGR](#-refheading-toc55049-4106839650) grids. |  |  | Optional |
| 1\-1 | Format | LGRS | NLIST | CHAR |  |
| 2\-1 | Data | Name of the LGRs. |  |  |  |
|  | NUMLX | This keyword defines the [LGR](#-refheading-toc55049-4106839650) grid index in the x direction \(I direction\)  for the associated summary variable mnemonic for [LGR](#-refheading-toc55049-4106839650) grids. |  |  | Optional |
| 1\-1 | Format | NUMLX | NLIST | INTE |  |
| 2\-1 | Data | [LGR](#-refheading-toc55049-4106839650) I location of local grid block data or the connection data. |  |  |  |
|  | NUMLY | This keyword defines the [LGR](#-refheading-toc55049-4106839650) grid index in the y direction \(J direction\)  for the associated summary variable mnemonic for [LGR](#-refheading-toc55049-4106839650) grids. |  |  | Optional |
| 1\-1 | Format | NUMLY | NLIST | INTE |  |
| 2\-1 | Data | [LGR](#-refheading-toc55049-4106839650) J location of local grid block data or the connection data. |  |  |  |
|  | NUMLZ | This keyword defines the [LGR](#-refheading-toc55049-4106839650) grid index in the z direction \(K direction\)  for the associated summary variable mnemonic for [LGR](#-refheading-toc55049-4106839650) grids. |  |  | Optional |
| 1\-1 | Format | NUMLX | NLIST | INTE |  |
| 2\-1 | Data | [LGR](#-refheading-toc55049-4106839650) K location of local grid block data or the connection data. |  |  |  |
|  | LGRNAMES | The names of all the LGRs in this case with the number of of LGRs in the case given by NLGR. |  |  | Optional |
| 1\-1 | Format | LGRNAMES | NLGR | CHAR |  |
| 2\-1 | Data | List of [LGR](#-refheading-toc55049-4106839650) names. |  |  |  |
|  | LGRVEC | Integer list of the number of summary variable mnemonics for each [LGR](#-refheading-toc55049-4106839650). |  |  | Optional |
| 1\-1 | Format | LGRVEC | NLGR | INTE |  |
| 2\-1 | Data | Number of summary variable mnemonics for each [LGR](#-refheading-toc55049-4106839650). |  |  |  |
|  | LGRTIMES | A list of the total number of local time steps for each [LGR](#-refheading-toc55049-4106839650). |  |  |  |
| 1\-1 | Format | LGRTIMES | NLGR | INTE |  |
| 2\-1 | Data | Number of local time steps for each [LGR](#-refheading-toc55049-4106839650). |  |  |  |
| Notes: - The [LGR](#-refheading-toc55049-4106839650) keywords may be in any order but must come after the NUMS keyword in Table A.42. - Rows shaded in gray indicate the start of a keyword. - Cells colored orange in the No. column indicate that this item is not supported by OPM Flow - For formatted output all character variables, including the keyword, should be enclosed in single quotes, for example the LGRTIMES keyword should be written out as ‘LGRTIMES’. |  |  |  |  |  |

Table A.43: SUMMARY Index File Keywords \(LGR\)

Finally, Table A.44 summarizes the [SUMMARY](#-refheading-toc43949-784232322) Index File keywords specific to the commercial simulator and are therefore not described in any detail.

| No. | keyword Name | [SUMMARY](#-refheading-toc43949-784232322) Index File keywords \(Commercial Simulator\) Table A.44 | Status or Value |
| --- | --- | --- | --- |
|  | RUNTIMEI | Run time monitoring – not supported. |  |
|  | RUNTIMED | Run time monitoring – not supported. |  |
|  | STEPRESN | Run time monitoring – not supported. |  |
|  | XCOORD | [OFM](#-refheading-toc234776-2928331029) Data – not supported. |  |
|  | YCOORD | [OFM](#-refheading-toc234776-2928331029) – not supported. |  |
|  | TIMESTMP | Not supported. |  |
| Notes: - Rows shaded in gray indicate the start of a keyword. - Cells colored orange in the No. column indicate that this item is not supported by OPM Flow. - For formatted output all character variables, including the keyword should be enclosed in single quotes. |  |  |  |

Table A.44: SUMMARY Index File Keywords \(Commercial Simulator\)

#### <a id="-refheading-toc716967-3964674244"></a>Example: SUMMARY Index File Keywords

The following example shows a typical formatted [SUMMARY](#-refheading-toc43949-784232322) Index file set of keywords.
```eclipse
 'INTEHEAD'           2 'INTE'
           1         100
 'RESTART '           9 'CHAR'
 '        ' '        ' '        ' '        ' '        ' '        ' '        '
 '        ' '        '
 'DIMENS  '           6 'INTE'
         164          10          10          10           0           0
 'KEYWORDS'         164 'CHAR'
 'TIME    ' 'YEARS   ' 'FGIP    ' 'FGIPG   ' 'FGIPL   ' 'FGIR    ' 'FGIT    '
 'FGOR    ' 'FGPR    ' 'FGPT    ' 'FOIP    ' 'FOIPG   ' 'FOIPL   ' 'FOIR    '
 'FOIT    ' 'FOPR    ' 'FOPT    ' 'FPR     ' 'FVIR    ' 'FVIT    ' 'FVPR    '
 'FVPT    ' 'FWCT    ' 'FWIP    ' 'FWIR    ' 'FWIT    ' 'FWPR    ' 'FWPT    '
 'GGIR    ' 'GGIT    ' 'GGOR    ' 'GGPR    ' 'GGPT    ' 'GOIR    ' 'GOIT    '
 'GOPR    ' 'GOPT    ' 'GVIR    ' 'GVIT    ' 'GVPR    ' 'GVPT    ' 'GWCT    '
 'GWIR    ' 'GWIT    ' 'GWPR    ' 'GWPT    ' 'SPR     ' 'SPR     ' 'SPR     '
 'SPR     ' 'SPR     ' 'SPR     ' 'SPR     ' 'SPR     ' 'SPR     ' 'SPR     '
  ………………………….……………..
 'WWCT    ' 'WWCT    ' 'WWIR    ' 'WWIR    ' 'WWIT    ' 'WWIT    ' 'WWPR    '

 'WWPR    ' 'WWPT    ' 'WWPT    '
 'WGNAMES '         164 'CHAR'
 ':+:+:+:+' ':+:+:+:+' ':+:+:+:+' ':+:+:+:+' ':+:+:+:+' ':+:+:+:+' ':+:+:+:+'
 ':+:+:+:+' ':+:+:+:+' ':+:+:+:+' ':+:+:+:+' ':+:+:+:+' ':+:+:+:+' ':+:+:+:+'
 ':+:+:+:+' ':+:+:+:+' ':+:+:+:+' ':+:+:+:+' ':+:+:+:+' ':+:+:+:+' ':+:+:+:+'
 ':+:+:+:+' ':+:+:+:+' ':+:+:+:+' ':+:+:+:+' ':+:+:+:+' ':+:+:+:+' ':+:+:+:+'
 'PLATFORM' 'PLATFORM' 'PLATFORM' 'PLATFORM' 'PLATFORM' 'PLATFORM' 'PLATFORM'
 'PLATFORM' 'PLATFORM' 'PLATFORM' 'PLATFORM' 'PLATFORM' 'PLATFORM' 'PLATFORM'
 'PLATFORM' 'PLATFORM' 'PLATFORM' 'PLATFORM' 'OP01    ' 'OP01    ' 'OP01    '
 'OP01    ' 'OP01    ' 'OP01    ' 'OP01    ' 'OP01    ' 'OP01    ' 'OP01    '
 'OP01    ' 'OP01    ' 'OP01    ' 'OP01    ' 'OP01    ' 'OP01    ' 'OP01    '
 'OP01    ' 'OP01    ' 'OP01    ' 'OP01    ' 'OP01    ' 'OP01    ' 'OP01    '
 'OP01    ' 'OP01    ' 'OP01    ' 'OP01    ' 'OP01    ' 'OP01    ' 'OP01    '
 'OP01    ' 'OP01    ' 'OP01    ' 'OP01    ' 'OP01    ' 'OP01    ' 'OP01    '
 'OP01    ' 'OP01    ' 'OP01    ' 'OP01    ' 'OP01    ' 'OP01    ' 'OP01    '
	  ………………………….……………..

 'WI01    ' 'OP01    ' 'WI01    '
 'NUMS    '         164 'INTE'
           0           0           0           0           0           0
           0           0           0           0           0           0
           0           0           0           0           0           0
           0           0           0           0           0           0
           0           0           0           0           0           0
           0           0           0           0           0           0
           0           0           0           0           0           0
           0           0           0           0           1           2
           3           4           5           6           7           8
           9          10          11          12          13          14
	  ………………………….……………..
         0           0
 'UNITS   '         164 'CHAR'
 'DAYS    ' 'YEARS   ' 'SM3     ' 'SM3     ' 'SM3     ' 'SM3/DAY ' 'SM3     '
 'SM3/SM3 ' 'SM3/DAY ' 'SM3     ' 'SM3     ' 'SM3     ' 'SM3     ' 'SM3/DAY '
 'SM3     ' 'SM3/DAY ' 'SM3     ' 'BARSA   ' 'RM3/DAY ' 'RM3     ' 'RM3/DAY '
 'RM3     ' 'SM3/SM3 ' 'SM3     ' 'SM3/DAY ' 'SM3     ' 'SM3/DAY ' 'SM3     '
	  ………………………….……………..
 'SM3/DAY ' 'SM3     ' 'SM3     '
 'STARTDAT'           6 'INTE'
           1           1        2020           0           0           0
```

End of Example
        - SUMMARY Data File Keywords
    -
-

The structure for this series of keywords is relatively simple compared to the [SUMMARY](#-refheading-toc43949-784232322) Index file, in that it only consists of four keyword types that are written out at the requested time steps, as outlined in Table A.45.
| No. | keyword Name | [SUMMARY](#-refheading-toc43949-784232322) Data File keywords Table A.45 |  |  | Status or Value |
| --- | --- | --- | --- | --- | --- |
|  | SEQNUM | This keyword contains a sequence data value corresponding to an encoded integer representing the time the file was created. Although required the data is not used. Secondly,  this keyword is written at each report step only and not for each inter leaving mini step, that is the file format is of the following format: SEQNUM                                                       Report step n   MINISTEP   PARAMS   MINISTEP   PARAMS   MINISTEP   PARAMS   INISTEP   PARAMS   SEQNUM                                                       Report step n \+ 1   MINISTEP   PARAMS   MINISTEP   PARAMS |  |  | Required |
| 1\-1 | Format | SEQNUM | 1 | INTE |  |
| 2\-1 | Data | The value entered is not used by either OPM Flow or OPM ResInsight |  |  | 0 |
|  | MINSTEP | The time step number starting from zero and incremented by one for each subsequent time step. |  |  | Required |
| 1\-1 | Format | MINISTEP | 1 | INTE |  |
| 2\-1 | Data | Time step. |  |  |  |
|  | PARAMS | This keyword contains the actual data for all the vectors and objects specified in the index file. |  |  | Required |
| 1\-1 | Format | PARAMS | NLIST | REAL |  |
| 2\-1 | Data | There should be NLIST values corresponding to the variable list declared on the corresponding [SUMMARY](#-refheading-toc43949-784232322) Index file. |  |  |  |
| Notes: - Rows shaded in gray indicate the start of a keyword. |  |  |  |  |  |

Table A.45: SUMMARY Data File Keywords

For LGRs, the global cell data is written to the standard [SUMMARY](#-refheading-toc43949-784232322) Data file containing an additional keyword that states the [LGR](#-refheading-toc55049-4106839650) name, as depicted in Table A.46.

| No. | keyword Name | [SUMMARY](#-refheading-toc43949-784232322) Data File keywords \([LGR](#-refheading-toc55049-4106839650)\) Table A.46 |  |  | Status or Value |
| --- | --- | --- | --- | --- | --- |
|  | SEQHDR | As per Table A.45 |  |  | Required |
|  | LGRNAME | Name of Local Grid Refinement. |  |  | Required |
|  | Format | LGRNAME | 1 | CHAR |  |
|  | Data | [LGR](#-refheading-toc55049-4106839650) name enclosed in single quotes. |  |  |  |
|  | MINSTEP | As per Table A.45. |  |  | Required |
|  | PARAMS | As per Table A.45. |  |  | Required |
| Notes: - Rows shaded in gray indicate the start of a keyword. |  |  |  |  |  |

Table A.46: SUMMARY Data File Keywords \(LGR\)

The data for the [LGR](#-refheading-toc55049-4106839650) time steps, as opposed to the global time step, are written out to a separate [SUMMARY](#-refheading-toc43949-784232322) Data File, with the suffix of [LGR](#-refheading-toc55049-4106839650) or FLG for fixed format output. In this case, the MINSTEP keyword states the “local” time step and the keyword is repeated for each local grid in the model.

#### <a id="-refheading-toc716969-3964674244"></a>Example: SUMMARY Data Data File keyword

The following example shows a typical formatted [SUMMARY](#-refheading-toc43949-784232322) Data File keyword data set for one complete report time step and part of a second report time step.
```eclipse
 'SEQHDR  '           1 'INTE'
           1
 'MINISTEP'           1 'INTE'
           0
 'PARAMS  '         164 'REAL'
   0.50000000E+00   0.13689254E-02   0.18381236E+11   0.51459348E+10
   0.13235301E+11   0.00000000E+00   0.00000000E+00   0.37649313E+03
   0.95391960E+07   0.47695980E+07   0.10947282E+09   0.30000488E+06
   0.10917282E+09   0.00000000E+00   0.00000000E+00   0.25336973E+05
   0.12668486E+05   0.27468176E+03   0.15571577E+05   0.77857886E+04
   0.63867320E+05   0.31933660E+05   0.12643164E-02   0.60474832E+08
   0.15000000E+05   0.75000000E+04   0.32074501E+02   0.16037251E+02
   0.00000000E+00   0.00000000E+00   0.37649313E+03   0.95391960E+07
   0.47695980E+07   0.00000000E+00   0.00000000E+00   0.25336973E+05
   0.12668486E+05   0.15571577E+05   0.77857886E+04   0.63867320E+05
   0.31933660E+05   0.12643164E-02   0.15000000E+05   0.75000000E+04
   0.32074501E+02   0.16037251E+02   0.26000000E+03   0.26172531E+03
   0.26362421E+03   0.26596732E+03   0.26747589E+03   0.26896045E+03
   ……………………….……………..
 'SEQHDR  '           1 'INTE'
           2
 'MINISTEP'           1 'INTE'
           1
 'PARAMS  '         164 'REAL'
   0.10000000E+01   0.27378509E-02   0.18377710E+11   0.51453399E+10
   0.13232370E+11   0.00000000E+00   0.00000000E+00   0.32637939E+03
  ………………………….……………..
```

End of Example
    - SAVE Files - Initialization and Solution Data
-

This file format is currently not supported by OPM Flow.
