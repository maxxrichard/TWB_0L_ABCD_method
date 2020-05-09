from ROOT import TFile, TTree, TH1, TH1F, TCanvas, TPad, TPaveLabel, TLegend, TChain
from ROOT import gStyle, kBlue, kRed, gROOT
import math
import time
import os
import numpy as np
import ROOT
from array import array



f11 = TFile.Open('/cephfs/user/s6marahm/TRExFitter/fit_B_HI_ljet_pt/Histograms/CR_I_ljet_pt_postFit.root',"update")
f12 = TFile.Open('/cephfs/user/s6marahm/TRExFitter/fit_B_HI_jet_pt/Histograms/CR_I_jet_pt_postFit.root',"update")
f13 = TFile.Open('/cephfs/user/s6marahm/TRExFitter/fit_B_HI_VLQM/Histograms/CR_I_VLQM_postFit.root',"update")
f14 = TFile.Open('/cephfs/user/s6marahm/TRExFitter/fit_B_HI_ljet_m/Histograms/CR_I_ljet_m_postFit.root',"update")
f15 = TFile.Open('/cephfs/user/s6marahm/TRExFitter/fit_B_HI_jet_m/Histograms/CR_I_jet_m_postFit.root',"update")
f16 = TFile.Open('/cephfs/user/s6marahm/TRExFitter/fit_B_HI_ljet_eta/Histograms/CR_I_ljet_eta_postFit.root',"update")

f21 = TFile.Open('/cephfs/user/s6marahm/TRExFitter/fit_B_HI_ljet_pt/Histograms/CR_H_ljet_pt_postFit.root',"update")
f22 = TFile.Open('/cephfs/user/s6marahm/TRExFitter/fit_B_HI_jet_pt/Histograms/CR_H_jet_pt_postFit.root',"update")
f23 = TFile.Open('/cephfs/user/s6marahm/TRExFitter/fit_B_HI_VLQM/Histograms/CR_H_VLQM_postFit.root',"update")
f24 = TFile.Open('/cephfs/user/s6marahm/TRExFitter/fit_B_HI_ljet_m/Histograms/CR_H_ljet_m_postFit.root',"update")
f25 = TFile.Open('/cephfs/user/s6marahm/TRExFitter/fit_B_HI_jet_m/Histograms/CR_H_jet_m_postFit.root',"update")
f26 = TFile.Open('/cephfs/user/s6marahm/TRExFitter/fit_B_HI_ljet_eta/Histograms/CR_H_ljet_eta_postFit.root',"update")

f31 = TFile.Open('/cephfs/user/s6marahm/TRExFitter/fit_B_BC_ljet_pt/Histograms/CR_C_ljet_pt_postFit.root',"update")
f32 = TFile.Open('/cephfs/user/s6marahm/TRExFitter/fit_B_BC_jet_pt/Histograms/CR_C_jet_pt_postFit.root',"update")
f33 = TFile.Open('/cephfs/user/s6marahm/TRExFitter/fit_B_BC_VLQM/Histograms/CR_C_VLQM_postFit.root',"update")
f34 = TFile.Open('/cephfs/user/s6marahm/TRExFitter/fit_B_BC_ljet_m/Histograms/CR_C_ljet_m_postFit.root',"update")
f35 = TFile.Open('/cephfs/user/s6marahm/TRExFitter/fit_B_BC_jet_m/Histograms/CR_C_jet_m_postFit.root',"update")
f36 = TFile.Open('/cephfs/user/s6marahm/TRExFitter/fit_B_BC_ljet_eta/Histograms/CR_C_ljet_eta_postFit.root',"update")

f41 = TFile.Open('/cephfs/user/s6marahm/TRExFitter/fit_B_BC_ljet_pt/Histograms/CR_B_ljet_pt_postFit.root',"update")
f42 = TFile.Open('/cephfs/user/s6marahm/TRExFitter/fit_B_BC_jet_pt/Histograms/CR_B_jet_pt_postFit.root',"update")
f43 = TFile.Open('/cephfs/user/s6marahm/TRExFitter/fit_B_BC_VLQM/Histograms/CR_B_VLQM_postFit.root',"update")
f44 = TFile.Open('/cephfs/user/s6marahm/TRExFitter/fit_B_BC_ljet_m/Histograms/CR_B_ljet_m_postFit.root',"update")
f45 = TFile.Open('/cephfs/user/s6marahm/TRExFitter/fit_B_BC_jet_m/Histograms/CR_B_jet_m_postFit.root',"update")
f46 = TFile.Open('/cephfs/user/s6marahm/TRExFitter/fit_B_BC_ljet_eta/Histograms/CR_B_ljet_eta_postFit.root',"update")

#f51 = TFile.Open('/cephfs/user/s6marahm/TRExFitter/TWB_0L_maxx_abcd/Histograms/CR_G_ljet_pt_postFit.root',"update")
#f52 = TFile.Open('/cephfs/user/s6marahm/TRExFitter/TWB_0L_maxx_abcd/Histograms/CR_G_jet_pt_postFit.root',"update")
#f53 = TFile.Open('/cephfs/user/s6marahm/TRExFitter/TWB_0L_maxx_abcd/Histograms/CR_G_VLQM_postFit.root',"update")
#f54 = TFile.Open('/cephfs/user/s6marahm/TRExFitter/TWB_0L_maxx_abcd/Histograms/CR_G_ljet_m_postFit.root',"update")
#f55 = TFile.Open('/cephfs/user/s6marahm/TRExFitter/TWB_0L_maxx_abcd/Histograms/CR_G_jet_m_postFit.root',"update")
#f56 = TFile.Open('/cephfs/user/s6marahm/TRExFitter/TWB_0L_maxx_abcd/Histograms/CR_G_ljet_eta_postFit.root',"update")

#f61 = TFile.Open('/cephfs/user/s6marahm/TRExFitter/TWB_0L_maxx_abcd/Histograms/CR_A_ljet_pt_postFit.root',"update")
#f62 = TFile.Open('/cephfs/user/s6marahm/TRExFitter/TWB_0L_maxx_abcd/Histograms/CR_A_jet_pt_postFit.root',"update")
#f63 = TFile.Open('/cephfs/user/s6marahm/TRExFitter/TWB_0L_maxx_abcd/Histograms/CR_A_VLQM_postFit.root',"update")
#f64 = TFile.Open('/cephfs/user/s6marahm/TRExFitter/TWB_0L_maxx_abcd/Histograms/CR_A_ljet_m_postFit.root',"update")
#f65 = TFile.Open('/cephfs/user/s6marahm/TRExFitter/TWB_0L_maxx_abcd/Histograms/CR_A_jet_m_postFit.root',"update")
#f66 = TFile.Open('/cephfs/user/s6marahm/TRExFitter/TWB_0L_maxx_abcd/Histograms/CR_A_ljet_eta_postFit.root',"update")

f7 = ROOT.TFile.Open("/cephfs/user/s6marahm/output/abcd_dijets_postfit.root","RECREATE")



n11 = f11.Get('h_Multijets_postFit')
n12 = f12.Get('h_Multijets_postFit')
n13 = f13.Get('h_Multijets_postFit')
n14 = f14.Get('h_Multijets_postFit')
n15 = f15.Get('h_Multijets_postFit')
n16 = f16.Get('h_Multijets_postFit')

n21 = f21.Get('h_Multijets_postFit')
n22 = f22.Get('h_Multijets_postFit')
n23 = f23.Get('h_Multijets_postFit')
n24 = f24.Get('h_Multijets_postFit')
n25 = f25.Get('h_Multijets_postFit')
n26 = f26.Get('h_Multijets_postFit')

n31 = f31.Get('h_Multijets_postFit')
n32 = f32.Get('h_Multijets_postFit')
n33 = f33.Get('h_Multijets_postFit')
n34 = f34.Get('h_Multijets_postFit')
n35 = f35.Get('h_Multijets_postFit')
n36 = f36.Get('h_Multijets_postFit')

n41 = f41.Get('h_Multijets_postFit')
n42 = f42.Get('h_Multijets_postFit')
n43 = f43.Get('h_Multijets_postFit')
n44 = f44.Get('h_Multijets_postFit')
n45 = f45.Get('h_Multijets_postFit')
n46 = f46.Get('h_Multijets_postFit')

#n51 = f51.Get('h_Multijets_postFit')
#n52 = f52.Get('h_Multijets_postFit')
#n53 = f53.Get('h_Multijets_postFit')
#n54 = f54.Get('h_Multijets_postFit')
#n55 = f55.Get('h_Multijets_postFit')
#n56 = f56.Get('h_Multijets_postFit')

#n61 = f61.Get('h_Multijets_postFit')
#n62 = f62.Get('h_Multijets_postFit')
#n63 = f63.Get('h_Multijets_postFit')
#n64 = f64.Get('h_Multijets_postFit')
#n65 = f65.Get('h_Multijets_postFit')
#n66 = f66.Get('h_Multijets_postFit')


temp11 = n11.Clone()
temp12 = n12.Clone()
temp13 = n13.Clone()
temp14 = n14.Clone()
temp15 = n15.Clone()
temp16 = n16.Clone()

temp21 = n21.Clone()
temp22 = n22.Clone()
temp23 = n23.Clone()
temp24 = n24.Clone()
temp25 = n25.Clone()
temp26 = n26.Clone()

temp31 = n31.Clone()
temp32 = n32.Clone()
temp33 = n33.Clone()
temp34 = n34.Clone()
temp35 = n35.Clone()
temp36 = n36.Clone()

temp41 = n41.Clone()
temp42 = n42.Clone()
temp43 = n43.Clone()
temp44 = n44.Clone()
temp45 = n45.Clone()
temp46 = n46.Clone()

#temp51 = n51.Clone()
#temp52 = n52.Clone()
#temp53 = n53.Clone()
#temp54 = n54.Clone()
#temp55 = n55.Clone()
#temp56 = n56.Clone()

#temp61 = n61.Clone()
#temp62 = n62.Clone()
#temp63 = n63.Clone()
#temp64 = n64.Clone()
#temp65 = n65.Clone()
#temp66 = n66.Clone()


temp11.SetName("ljet_pt_0b_not_loose_Wtagged")
temp12.SetName("jet_pt_0b_not_loose_Wtagged")
temp13.SetName("VLQM_0b_not_loose_Wtagged")
temp14.SetName("ljet_m_0b_not_loose_Wtagged")
temp15.SetName("jet_m_0b_not_loose_Wtagged")
temp16.SetName("ljet_eta_0b_not_loose_Wtagged")

temp21.SetName("ljet_pt_0b_loose_not_tight_Wtagged")
temp22.SetName("jet_pt_0b_loose_not_tight_Wtagged")
temp23.SetName("VLQM_0b_loose_not_tight_Wtagged")
temp24.SetName("ljet_m_0b_loose_not_tight_Wtagged")
temp25.SetName("jet_m_0b_loose_not_tight_Wtagged")
temp26.SetName("ljet_eta_0b_loose_not_tight_Wtagged")

temp31.SetName("ljet_pt_2b_not_loose_Wtagged")
temp32.SetName("jet_pt_2b_not_loose_Wtagged")
temp33.SetName("VLQM_2b_not_loose_Wtagged")
temp34.SetName("ljet_m_2b_not_loose_Wtagged")
temp35.SetName("jet_m_2b_not_loose_Wtagged")
temp36.SetName("ljet_eta_2b_not_loose_Wtagged")

temp41.SetName("ljet_pt_2b_loose_not_tight_Wtagged")
temp42.SetName("jet_pt_2b_loose_not_tight_Wtagged")
temp43.SetName("VLQM_2b_loose_not_tight_Wtagged")
temp44.SetName("ljet_m_2b_loose_not_tight_Wtagged")
temp45.SetName("jet_m_2b_loose_not_tight_Wtagged")
temp46.SetName("ljet_eta_2b_loose_not_tight_Wtagged")

#temp51.SetName("ljet_pt_0b_tight_Wtagged")
#temp52.SetName("jet_pt_0b_tight_Wtagged")
#temp53.SetName("VLQM_0b_tight_Wtagged")
#temp54.SetName("ljet_m_0b_tight_Wtagged")
#temp55.SetName("jet_m_0b_tight_Wtagged")
#temp56.SetName("ljet_eta_0b_tight_Wtagged")

#temp61.SetName("ljet_pt_2b_tight_Wtagged")
#temp62.SetName("jet_pt_2b_tight_Wtagged")
#temp63.SetName("VLQM_2b_tight_Wtagged")
#temp64.SetName("ljet_m_2b_tight_Wtagged")
#temp65.SetName("jet_m_2b_tight_Wtagged")
#temp66.SetName("ljet_eta_2b_tight_Wtagged")


temp11.Write()
temp12.Write()
temp13.Write()
temp14.Write()
temp15.Write()
temp16.Write()

temp21.Write()
temp22.Write()
temp23.Write()
temp24.Write()
temp25.Write()
temp26.Write()

temp31.Write()
temp32.Write()
temp33.Write()
temp34.Write()
temp35.Write()
temp36.Write()

temp41.Write()
temp42.Write()
temp43.Write()
temp44.Write()
temp45.Write()
temp46.Write()

#temp51.Write()
#temp52.Write()
#temp53.Write()
#temp54.Write()
#temp55.Write()
#temp56.Write()

#temp61.Write()
#temp62.Write()
#temp63.Write()
#temp64.Write()
#temp65.Write()
#temp66.Write()

f7.Close()

print("Done! ")



#f9 = TFile.Open('/cephfs/user/s6marahm/output/abcd_dijets_postfit.root',"update")

#n91 = f9.Get('CR_A_ljet_pt_Multijets')
#n92 = f9.Get('CR_A_jet_pt_Multijets')
#n93 = f9.Get('CR_A_VLQM_Multijets')
#n94 = f9.Get('CR_A_ljet_m_Multijets')
#n95 = f9.Get('CR_A_jet_m_Multijets')
#n96 = f9.Get('CR_A_ljet_eta_Multijets')

#n91.SetName("ljet_pt_2b_loose_not_tight_Wtagged")
#n92.SetName("jet_pt_2b_loose_not_tight_Wtagged")
#n93.SetName("VLQM_2b_loose_not_tight_Wtagged")
#n94.SetName("ljet_m_2b_loose_not_tight_Wtagged")
#n95.SetName("jet_m_2b_loose_not_tight_Wtagged")
#n96.SetName("ljet_eta_2b_loose_not_tight_Wtagged")

#n91.Write()
#n92.Write()
#n93.Write()
#n94.Write()
#n95.Write()
#n96.Write()

#f9.Close()

#print("Done! Renaming")



