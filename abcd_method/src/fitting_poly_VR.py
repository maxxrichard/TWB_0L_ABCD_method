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
#variable_calculated = ['VLQM']


ljet_pt_var_bin = np.array((500.,550.,600.,650.,700.,750.,800.,850.,900.,1400.))
ljet_eta_var_bin = np.array((-2.0,-1.5,-1.0,-0.5,0.,0.5,1.0,1.5,2.0))
ljet_m_var_bin = np.array((0.,20.,40.,60.,80.,100.,120.,140.,160.,180.,200.,220.,240.,260.))
jet_pt_var_bin = np.array((350.,400.,500.,600.,700.,800.,1200.))
jet_m_var_bin = np.array((0.,30.,60.,90.,120.,150.))
#VLQM_var_bin = np.array((400.,1000.,1100.,1200.,1300.,1400.,1500.,1600.,1700.,1800.,1900.,2000.,2100.,2200.,2300.,2400.,2500.,3400.))
VLQM_var_bin = np.array((800.,900.,1000.,1100.,1200.,1300.,1400.,1500.,1600.,1700.,1800.,1900.,2000.,2100.,2200.,2300.,2400.,2500.,3400.))



fRcorr = TFile.Open('/cephfs/user/s6marahm/output/abcd_correlation.root',"update")
fRcorr_polyfit = ROOT.TFile.Open("/cephfs/user/s6marahm/output/abcd_correlation_polyfit_VR.root","RECREATE")


def poly(i,coeff):
    #x5 = coeff[5]
    #x4 = coeff[4]
    x3 = coeff[3]
    x2 = coeff[2]
    x1 = coeff[1]
    x0 = coeff[0]
    return x3*i*i*i + x2*i*i + x1*i + x0


print "Applying polynomial fitting..."
for r in region_calculated:
    for v in variable_calculated:
        n1 = fRcorr.Get(v+'_'+r+'_loose_not_tight_Wtagged')
        temp = n1.Clone()
        temp.Sumw2()
        temp.Smooth()
        result = temp.Fit("pol3","S")

        if(v == 'ljet_pt'):
            print 'ljet_pt'
            for i in range(len(ljet_pt_var_bin)-1):
                temp.SetBinContent(i+1, poly((ljet_pt_var_bin[i]+ljet_pt_var_bin[i+1])/2, result.Parameters()))
        elif(v == 'ljet_eta'):
            print 'ljet_eta'
            for i in range(len(ljet_eta_var_bin)-1):
                temp.SetBinContent(i+1, poly((ljet_eta_var_bin[i]+ljet_eta_var_bin[i+1])/2, result.Parameters()))
        elif(v == 'ljet_m'):
            print 'ljet_m'
            for i in range(len(ljet_m_var_bin)-1):
                temp.SetBinContent(i+1, poly((ljet_m_var_bin[i]+ljet_m_var_bin[i+1])/2, result.Parameters()))
        elif(v == 'jet_pt'):
            print 'jet_pt'
            for i in range(len(jet_pt_var_bin)-1):
                temp.SetBinContent(i+1, poly((jet_pt_var_bin[i]+jet_pt_var_bin[i+1])/2, result.Parameters()))
        elif(v == 'jet_m'):
            print 'jet_m'
            for i in range(len(jet_m_var_bin)-1):
                temp.SetBinContent(i+1, poly((jet_m_var_bin[i]+jet_m_var_bin[i+1])/2, result.Parameters()))
        elif(v == 'VLQM'):
            print 'VLQM'
            for i in range(len(VLQM_var_bin)-1):
                temp.SetBinContent(i+1, poly((VLQM_var_bin[i]+VLQM_var_bin[i+1])/2, result.Parameters()))
        temp.Write()
fRcorr_polyfit.Close()

print "abcd_correlation_polyfit_VR.root created!"



print "Applying polynomial fitted Rcorr to the ABCD multijet in VR.."

fnocorr = TFile.Open('/cephfs/user/s6marahm/output/abcd_output_no_corr.root',"update")
fpolyfit = TFile.Open('/cephfs/user/s6marahm/output/abcd_correlation_polyfit_VR.root',"update")
fout = ROOT.TFile.Open("/cephfs/user/s6marahm/output/abcd_output_polyfit_VR.root","RECREATE")

for r in region_calculated:
    for v in variable_calculated:
        n2 = fnocorr.Get(v+'_'+r+'_loose_not_tight_Wtagged')
        n3 = fpolyfit.Get(v+'_'+r+'_loose_not_tight_Wtagged')
        temp = n2.Clone()
        temp.Multiply(n3)
        temp.Write()
fout.Close()

print "abcd_output_polyfit_VR.root created!"
