# Comparative-Cognition-R-scripts

Contents of this repository:
There are four R scripts related to comparative cognition hand score data analysis:
Comparative Cognition Numerosity Cowlog Analysis.Rmd and 
Comparative Cognition Numerosity Analysis of Cowlog Data Part II.Rmd
Comparative Cognition Numerosity Analysis of Cowlog Data Part III.Rmd
Comparative Cognition Numerosity Analysis of Cowlog Data Part IV.Rmd

The first script takes the 300 or so cowlog score sheets from numerosity and makes a summary data frame from them. 
The second takes the resulting data frame and pulls out useful graphs and stats (all related to numerosity).
The third script adds in the detour maze information, analyzes it, and compares it to numerosity. 
There will soon be a fourth script that will add shuttlebox information in to this (as of April 10 2018)
A cowlog score sheet looks like this:

time	code	class
0.015	 top mirror	1
31.65	 top left thigmo	1
33.725	 center	1
35.325	 top mirror	1
37.475	 top left thigmo	1
...
...
...
206.6	 top mirror	1
210.35	 top right thigmo	1
211.15	 top mirror	1
235.425	END	0

Additionally, there is a script that takes the tracker output from numerosity (both numerosity log and designed to look like cowlog)
and compares it to the hand score numerosity data. 