# CaesarCreekChallenge
This repository houses a report for a reverse-engineering challenge issued by Caesar Creek, a software company located in Ohio

# Abstract
This report presents an analysis of suspected malicious traffic, a capture-the-flag spirited reverse engineering \
challenge issued by Caesar Creek Software, a software company located in Ohio. By analyzing a pcap file of the \
suspected traffic, I was able to extract a malicious binary and apply static reverse engineering techniques that \
led to the decryption of traffic between the malware and its C2 server.

# Description of Files
### Conficker-19 Report: This is a pdf file that contains a report of the analysis \
### conficker: This is the extracted malicious binary. The binary is not actually malicious, as this was a capture-the-flag style challenge
#### MD5:3164c55b20427dbd7ab07b9bca8ed090
### conficker-19.pcapng: This is the original pcap file of the malicious traffic, which was the starting point of the analysis
### conficker_19.yar: This is the yara file that contains the detection rules
### solver.py: This is the solver script for the challenge

