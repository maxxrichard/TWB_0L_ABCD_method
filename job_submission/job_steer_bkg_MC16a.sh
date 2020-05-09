#!/bin/bash

JOB_ID=$1
INPUT_FOLDER=$2
DSID=$3
TREE_NAME=$4
XS=$5
LABEL=$6
OUTPUT_FOLDER=$7
SIGNAL_ELEMENT=$8

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
python abcd_background_MC16a.py $INPUT_FOLDER $DSID $TREE_NAME $XS $LABEL $OUTPUT_FOLDER $SIGNAL_ELEMENT
#mv histo_${DSID}_${TREE_NAME}_${LABEL}_smooth3var80.root $BUDDY/$OUTPUT_FOLDER
cd ..
rm -rf code*
echo "Finishing job ${JOB_ID}..."





