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


fdijets_postfit = TFile.Open('/cephfs/user/s6marahm/output/abcd_dijets_postfit.root',"update")
fdijets = TFile.Open('/cephfs/user/s6marahm/output/abcd_dijets.root',"update")


print "Propagating scale factors from VR to SR in abcd_dijets.root..."
for r in region_calculated:
    for v in variable_calculated:
        ndijets_postfit = fdijets_postfit.Get(v+'_'+r+'_loose_not_tight_Wtagged')
        ndijets = fdijets.Get(v+'_'+r+'_loose_not_tight_Wtagged')
        ndijets_sr = fdijets.Get(v+'_'+r+'_tight_Wtagged')
        temp = ndijets_postfit.Clone()
        temp.Divide(ndijets)
        temp.SetName(v+'_'+r+'_tight_Wtagged_sf')
        temp.Write()
        #ndijets_sr.Multiply(temp)
fdijets.Close()

print "Applying scale factors to SR in abcd_dijets.root..."
fdijets = TFile.Open('/cephfs/user/s6marahm/output/abcd_dijets.root',"update")
for r in region_calculated:
    for v in variable_calculated:
        ndijets_sf = fdijets.Get(v+'_'+r+'_tight_Wtagged_sf')
        ndijets_sr = fdijets.Get(v+'_'+r+'_tight_Wtagged')
        ndijets_sr.Multiply(ndijets_sf)
        ndijets_sr.Write()
fdijets.Close()

print "abcd_dijets.root updated!"