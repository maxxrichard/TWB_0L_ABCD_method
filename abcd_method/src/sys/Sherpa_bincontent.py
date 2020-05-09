from ROOT import TFile, TTree, TH1, TH1F, TCanvas, TPad, TPaveLabel, TLegend, TChain
from ROOT import gStyle, kBlue, kRed, gROOT
import math
import time
import os
import numpy as np
import ROOT
import sys
from array import array

f1 = TFile.Open('/cephfs/user/s6marahm/output_Sherpa/abcd_output_postfit_binbybin.root',"update")
n1 = f1.Get('VLQM_2b_loose_not_tight_Wtagged')
n1.SetBinContent(1, 0.0)
n1.SetBinError(1,0.0)
n1.Write()
f1.Close()
print 'Done!'