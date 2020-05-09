#!/bin/bash

JOB_ID=$1
INPUT_FOLDER=$2
DSID=$3
LABEL=$4
OUTPUT_FOLDER=$5

echo "This is job ${JOB_ID}..."
source /etc/profile
cd /jwd
echo "Unpacking tarball..."
#Do this instead of transfer_input_files. Put all files needed for running your job in tarball.
tar -xvf $BUDDY/code_PFlow.tar
cd code_PFlow
setupATLAS
lsetup "root 6.14.04-x86_64-slc6-gcc62-opt"
lsetup "lcgenv -p LCG_94 x86_64-centos7-gcc62-opt numpy"
#Also setup if you need other packages
set -e
#Your commands for job here
python abcd_data_MC16a.py $INPUT_FOLDER $DSID $LABEL $OUTPUT_FOLDER
#mv histo_${DSID}_${LABEL}_smooth3var80.root $BUDDY/$OUTPUT_FOLDER
cd ..
rm -rf code*
echo "Finishing job ${JOB_ID}..."





