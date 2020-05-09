from ROOT import TFile, TTree, TH1, TH1F, TCanvas, TPad, TPaveLabel, TLegend, TChain
from ROOT import gStyle, kBlue, kRed, gROOT
import math
import time
import os
import numpy as np
import ROOT
import sys
from array import array


region_calculated = ['2b']
variable_calculated = ['ljet_pt','jet_pt','VLQM','ljet_m','jet_m','ljet_eta']

jet_pt_var_bin = np.array((350.,400.,500.,600.,700.,800.,1200.))
VLQM_var_bin = np.array((400.,1000.,1100.,1200.,1300.,1400.,1500.,1600.,1700.,1800.,1900.,2000.,2100.,2200.,2300.,2400.,2500.,3400.))
ljet_pt_var_bin = np.array((500.,550.,600.,650.,700.,750.,800.,850.,900.,1400.))


fn1 = TFile.Open('/cephfs/user/s6marahm/output/abcd_output_prefit_binbybin.root',"update")
fRcorr = TFile.Open('/cephfs/user/s6marahm/output/abcd_correlation.root',"update")
fsr = ROOT.TFile.Open("/cephfs/user/s6marahm/output/abcd_signal_region.root","RECREATE")


print "Applying ABCD method using Rcorr from validation region..."
for r in region_calculated:
    for v in variable_calculated:
        n1 = fn1.Get(v+'_'+r+'_tight_Wtagged')
        Rcorr = fRcorr.Get(v+'_'+r+'_loose_not_tight_Wtagged')
        temp = n1.Clone()
        temp.Multiply(Rcorr)
        temp.Write()
fsr.Close()
print "abcd_signal_region.root created!"