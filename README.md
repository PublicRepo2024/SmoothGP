# Smooth Sensitivity for Geo-Privacy
The repo contains the official code for the experiments implemented in "Smooth Sensitivity for Geo-Privacy".

The experiments were implemented in Python v3.10.
### Dependencies
numpy v1.23.5 <br/>
scipy v1.9.3 <br/>

### Data
The CENSUS dataset in the ./data folder has been compressed. Please de-compress prior to running the experiments.<br/>
The New York motor vehicle collision dataset can be downloaded from the official website provided in the paper.

### Secure random number generation
Implementations for the mechanisms which use a cryptographically secure random number generator have been added (functions suffixed with "_secure"). Note that for testing purposes, the regular implementations which use numpy for random number generation should be used, since they are more efficient.
