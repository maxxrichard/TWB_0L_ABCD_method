import ROOT 
import math
import time
import os
import numpy as np
import heapq
import sys
from array import array

background_Sherpa = ['user.abandyop.364679.Sherpa.DAOD_EXOT7.e6929_s3126_r9364_p3973.26th-Mar_21.2.113_v1nosys_output_root','user.abandyop.364680.Sherpa.DAOD_EXOT7.e6929_s3126_r9364_p3973.26th-Mar_21.2.113_v3nosys_output_root',
'user.abandyop.364681.Sherpa.DAOD_EXOT7.e6929_s3126_r9364_p3973.26th-Mar_21.2.113_v1nosys_output_root','user.abandyop.364682.Sherpa.DAOD_EXOT7.e6929_s3126_r9364_p3973.26th-Mar_21.2.113_v3nosys_output_root',
'user.abandyop.364683.Sherpa.DAOD_EXOT7.e6929_s3126_r9364_p3973.26th-Mar_21.2.113_v3nosys_output_root','user.abandyop.364684.Sherpa.DAOD_EXOT7.e6929_s3126_r9364_p3973.26th-Mar_21.2.113_v1nosys_output_root',
'user.abandyop.364685.Sherpa.DAOD_EXOT7.e6929_s3126_r9364_p3973.26th-Mar_21.2.113_v2nosys_output_root','user.abandyop.364679.Sherpa.DAOD_EXOT7.e6929_s3126_r10201_p3973.26th-Mar_21.2.113_v2nosys_output_root',
'user.abandyop.364680.Sherpa.DAOD_EXOT7.e6929_s3126_r10201_p3973.26th-Mar_21.2.113_v2nosys_output_root','user.abandyop.364681.Sherpa.DAOD_EXOT7.e6929_s3126_r10201_p3973.26th-Mar_21.2.113_v2nosys_output_root',
'user.abandyop.364682.Sherpa.DAOD_EXOT7.e6929_s3126_r10201_p3973.26th-Mar_21.2.113_v2nosys_output_root','user.abandyop.364683.Sherpa.DAOD_EXOT7.e6929_s3126_r10201_p3973.26th-Mar_21.2.113_v2nosys_output_root',
'user.abandyop.364684.Sherpa.DAOD_EXOT7.e6929_s3126_r10201_p3973.26th-Mar_21.2.113_v2nosys_output_root','user.abandyop.364685.Sherpa.DAOD_EXOT7.e6929_s3126_r10201_p3973.26th-Mar_21.2.113_v2nosys_output_root',
'user.abandyop.364679.Sherpa.DAOD_EXOT7.e6929_s3126_r10724_p3973.26th-Mar_21.2.115_v2nosys_output_root','user.abandyop.364680.Sherpa.DAOD_EXOT7.e6929_s3126_r10724_p3973.26th-Mar_21.2.115_v2nosys_output_root',
'user.abandyop.364681.Sherpa.DAOD_EXOT7.e6929_s3126_r10724_p3973.26th-Mar_21.2.115_v2nosys_output_root','user.abandyop.364682.Sherpa.DAOD_EXOT7.e6929_s3126_r10724_p3973.26th-Mar_21.2.115_v2nosys_output_root',
'user.abandyop.364683.Sherpa.DAOD_EXOT7.e6929_s3126_r10724_p3973.26th-Mar_21.2.115_v2nosys_output_root','user.abandyop.364684.Sherpa.DAOD_EXOT7.e6929_s3126_r10724_p3973.26th-Mar_21.2.113_v3nosys_output_root',
'user.abandyop.364685.Sherpa.DAOD_EXOT7.e6929_s3126_r10724_p3973.26th-Mar_21.2.113_v3nosys_output_root']

background_Herwig = ['user.abandyop.364922.H7EG.DAOD_EXOT7.e7482_s3126_r9364_p3973.26th-Mar_21.2.115_v1nosys_output_root','user.abandyop.364923.H7EG.DAOD_EXOT7.e7482_s3126_r9364_p3973.26th-Mar_21.2.115_v1nosys_output_root',
'user.abandyop.364924.H7EG.DAOD_EXOT7.e7482_s3126_r9364_p3973.26th-Mar_21.2.115_v1nosys_output_root','user.abandyop.364925.H7EG.DAOD_EXOT7.e7482_s3126_r9364_p3973.26th-Mar_21.2.115_v3nosys_output_root',
'user.abandyop.364926.H7EG.DAOD_EXOT7.e7482_s3126_r9364_p3973.26th-Mar_21.2.115_v1nosys_output_root','user.abandyop.364927.H7EG.DAOD_EXOT7.e7482_s3126_r9364_p3973.26th-Mar_21.2.115_v1nosys_output_root',
'user.abandyop.364928.H7EG.DAOD_EXOT7.e7482_s3126_r9364_p3973.26th-Mar_21.2.115_v1nosys_output_root','user.abandyop.364929.H7EG.DAOD_EXOT7.e7482_s3126_r9364_p3973.26th-Mar_21.2.115_v1nosys_output_root',
'user.abandyop.364922.H7EG.DAOD_EXOT7.e7482_s3126_r10201_p3973.26th-Mar_21.2.115_v2nosys_output_root','user.abandyop.364923.H7EG.DAOD_EXOT7.e7482_s3126_r10201_p3973.26th-Mar_21.2.115_v2nosys_output_root',
'user.abandyop.364924.H7EG.DAOD_EXOT7.e7482_s3126_r10201_p3973.26th-Mar_21.2.115_v2nosys_output_root','user.abandyop.364925.H7EG.DAOD_EXOT7.e7482_s3126_r10201_p3973.26th-Mar_21.2.115_v2nosys_output_root',
'user.abandyop.364926.H7EG.DAOD_EXOT7.e7482_s3126_r10201_p3973.26th-Mar_21.2.115_v2nosys_output_root','user.abandyop.364927.H7EG.DAOD_EXOT7.e7482_s3126_r10201_p3973.26th-Mar_21.2.115_v2nosys_output_root',
'user.abandyop.364928.H7EG.DAOD_EXOT7.e7482_s3126_r10201_p3973.26th-Mar_21.2.115_v2nosys_output_root','user.abandyop.364929.H7EG.DAOD_EXOT7.e7482_s3126_r10201_p3973.26th-Mar_21.2.115_v2nosys_output_root',
'user.abandyop.364922.H7EG.DAOD_EXOT7.e7482_s3126_r10724_p3973.26th-Mar_21.2.115_v2nosys_output_root','user.abandyop.364923.H7EG.DAOD_EXOT7.e7482_s3126_r10724_p3973.26th-Mar_21.2.115_v2nosys_output_root',
'user.abandyop.364924.H7EG.DAOD_EXOT7.e7482_s3126_r10724_p3973.26th-Mar_21.2.115_v2nosys_output_root','user.abandyop.364925.H7EG.DAOD_EXOT7.e7482_s3126_r10724_p3973.26th-Mar_21.2.115_v2nosys_output_root',
'user.abandyop.364926.H7EG.DAOD_EXOT7.e7482_s3126_r10724_p3973.26th-Mar_21.2.115_v2nosys_output_root','user.abandyop.364927.H7EG.DAOD_EXOT7.e7482_s3126_r10724_p3973.26th-Mar_21.2.115_v2nosys_output_root',
'user.abandyop.364928.H7EG.DAOD_EXOT7.e7482_s3126_r10724_p3973.26th-Mar_21.2.115_v2nosys_output_root','user.abandyop.364929.H7EG.DAOD_EXOT7.e7482_s3126_r10724_p3973.26th-Mar_21.2.115_v2nosys_output_root']


for background in background_Herwig:
    
    if 'r9364' in background:
        label = 'MC16a'
    elif 'r10201' in background:
        label = 'MC16d'
    else:
        label = 'MC16e'
    

    if '364679' in background:
        dsid = '364679'
    elif '364680' in background:
        dsid = '364680'
    elif '364681' in background:
        dsid = '364681'
    elif '364682' in background:
        dsid = '364682'
    elif '364683' in background:
        dsid = '364683'
    elif '364684' in background:
        dsid = '364684'
    elif '364685' in background:
        dsid = '364685'
    elif '364922' in background:
        dsid = '364922'
    elif '364923' in background:
        dsid = '364923'
    elif '364924' in background:
        dsid = '364924'
    elif '364925' in background:
        dsid = '364925'
    elif '364926' in background:
        dsid = '364926'
    elif '364927' in background:
        dsid = '364927'
    elif '364928' in background:
        dsid = '364928'
    else:
        dsid = '364929'

    location = '/cephfs/user/s6anband/ntuples/'
    file_names = []

    print background,dsid,label

    sumofeventsweighted_totalEventsWeighted = 0.
    sumofeventsweighted_totalEvents = 0.

    listOfFiles = os.listdir(location + background)
    sumWeights = ROOT.TChain("sumWeights")
    nominal = ROOT.TChain("nominal")
    for f in listOfFiles:
        f = location + background + '/' + f 
        if 'output_root/user.abandyop' not in f:
            continue
        sumWeights.Add(f)
        nominal.Add(f)


    for j in xrange(sumWeights.GetEntries()):
        sumWeights.GetEntry(j)
        sumweight_totalEventsWeighted = getattr(sumWeights,"totalEventsWeighted")
        sumofeventsweighted_totalEventsWeighted += sumweight_totalEventsWeighted

        sumweight_totalEvents = getattr(sumWeights,"totalEvents")
        sumofeventsweighted_totalEvents += sumweight_totalEvents


    if "3649" in background:
        os.chdir("/cephfs/user/s6marahm/output_Herwig/")
    else:
        os.chdir("/cephfs/user/s6marahm/output_Sherpa/")
    f0 = ROOT.TFile.Open("abcd_"+dsid+"_"+label+".root","update")


    region_calculated = ['2b','0b']
    tagger_calculated = ['tight_Wtagged','loose_not_tight_Wtagged','not_loose_Wtagged']
    variable_calculated = ['ljet_pt','jet_pt','VLQM','ljet_m','jet_m','ljet_eta']

    for t in tagger_calculated:
        for r in region_calculated:
            for v in variable_calculated:
                temp = f0.Get(v+'_'+r+'_'+t)
                n1 = temp.Clone()
                temp.SetName(v+'_'+r+'_'+t+'_old')
                temp.Write()
                if "3649" in background:
                    n1.Scale(sumofeventsweighted_totalEvents/sumofeventsweighted_totalEventsWeighted)
                else:
                    if "364679" in background or "364680" in background:
                        n1.Scale(sumofeventsweighted_totalEventsWeighted/sumofeventsweighted_totalEvents)
                    else:
                        n1.Scale(sumofeventsweighted_totalEvents/sumofeventsweighted_totalEventsWeighted)
                n1.Write()
    f0.Close()
    print "Done!"


#background=sys.argv[1]
#dsid=sys.argv[2]
#label = sys.argv[3]
#makeHists(background,dsid,label)