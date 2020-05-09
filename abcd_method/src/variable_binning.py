from ROOT import TFile, TTree, TH1, TH1F, TCanvas, TPad, TPaveLabel, TLegend, TChain
from ROOT import gStyle, kBlue, kRed, gROOT
import math
import time
import os
import numpy as np
import ROOT
from array import array


VLQM = ['VLQM_0b_loose_not_tight_Wtagged','VLQM_0b_tight_Wtagged','VLQM_0b_not_loose_Wtagged','VLQM_2b_not_loose_Wtagged','VLQM_2b_tight_Wtagged','VLQM_2b_loose_not_tight_Wtagged']
VLQM_var_bin = np.array((800.,900.,1000.,1100.,1200.,1300.,1400.,1500.,1600.,1700.,1800.,1900.,2000.,2100.,2200.,2300.,2400.,2500.,3400.))
#VLQM_var_bin = np.array((400.,1000.,1100.,1200.,1300.,1400.,1500.,1600.,1700.,1800.,1900.,2000.,2100.,2200.,2300.,2400.,2500.,3400.))

jet_pt = ['jet_pt_0b_loose_not_tight_Wtagged','jet_pt_0b_tight_Wtagged','jet_pt_0b_not_loose_Wtagged','jet_pt_2b_not_loose_Wtagged','jet_pt_2b_tight_Wtagged','jet_pt_2b_loose_not_tight_Wtagged']
jet_pt_var_bin = np.array((350.,400.,500.,600.,700.,800.,1200.))

ljet_pt = ['ljet_pt_0b_loose_not_tight_Wtagged','ljet_pt_0b_tight_Wtagged','ljet_pt_0b_not_loose_Wtagged','ljet_pt_2b_not_loose_Wtagged','ljet_pt_2b_tight_Wtagged','ljet_pt_2b_loose_not_tight_Wtagged']
ljet_pt_var_bin = np.array((500.,550.,600.,650.,700.,750.,800.,850.,900.,1400.))

#Data & background samples
f1 = TFile.Open('/cephfs/user/s6marahm/output/abcd_data.root',"update")
for p in jet_pt:
    n_bincontent_one = f1.Get(p)
    n_bincontent_one.SetName(p+'_old')
    n_bincontent_one.Write()
    temp = ROOT.TH1F(p,p,(len(jet_pt_var_bin)-1),jet_pt_var_bin)
    temp.Sumw2()
    temp = n_bincontent_one.Rebin((len(jet_pt_var_bin)-1),p,jet_pt_var_bin)
    temp.Write()
for p in ljet_pt:
    n_bincontent_one = f1.Get(p)
    n_bincontent_one.SetName(p+'_old')
    n_bincontent_one.Write()
    temp = ROOT.TH1F(p,p,(len(ljet_pt_var_bin)-1),ljet_pt_var_bin)
    temp.Sumw2()
    temp = n_bincontent_one.Rebin((len(ljet_pt_var_bin)-1),p,ljet_pt_var_bin)
    temp.Write()
for p in VLQM:
    n_bincontent_one = f1.Get(p)
    n_bincontent_one.SetName(p+'_old')
    n_bincontent_one.Write()
    temp = ROOT.TH1F(p,p,(len(VLQM_var_bin)-1),VLQM_var_bin)
    temp.Sumw2()
    temp = n_bincontent_one.Rebin((len(VLQM_var_bin)-1),p,VLQM_var_bin)
    temp.SetBinContent(1, temp.GetBinContent(0) + temp.GetBinContent(1))
    temp.SetBinContent(temp.GetNbinsX(), temp.GetBinContent(temp.GetNbinsX()) + temp.GetBinContent(temp.GetNbinsX()+1))
    temp.ClearUnderflowAndOverflow()
    temp.Write()
f1.Close()



f2 = TFile.Open('/cephfs/user/s6marahm/output/abcd_background.root',"update")
for p in jet_pt:
    n_bincontent_one = f2.Get(p)
    n_bincontent_one.SetName(p+'_old')
    n_bincontent_one.Write()
    temp = ROOT.TH1F(p,p,(len(jet_pt_var_bin)-1),jet_pt_var_bin)
    temp.Sumw2()
    temp = n_bincontent_one.Rebin((len(jet_pt_var_bin)-1),p,jet_pt_var_bin)
    temp.Write()
for p in ljet_pt:
    n_bincontent_one = f2.Get(p)
    n_bincontent_one.SetName(p+'_old')
    n_bincontent_one.Write()
    temp = ROOT.TH1F(p,p,(len(ljet_pt_var_bin)-1),ljet_pt_var_bin)
    temp.Sumw2()
    temp = n_bincontent_one.Rebin((len(ljet_pt_var_bin)-1),p,ljet_pt_var_bin)
    temp.Write()
for p in VLQM:
    n_bincontent_one = f2.Get(p)
    n_bincontent_one.SetName(p+'_old')
    n_bincontent_one.Write()
    temp = ROOT.TH1F(p,p,(len(VLQM_var_bin)-1),VLQM_var_bin)
    temp.Sumw2()
    temp = n_bincontent_one.Rebin((len(VLQM_var_bin)-1),p,VLQM_var_bin)
    temp.SetBinContent(1, temp.GetBinContent(0) + temp.GetBinContent(1))
    temp.SetBinContent(temp.GetNbinsX(), temp.GetBinContent(temp.GetNbinsX()) + temp.GetBinContent(temp.GetNbinsX()+1))
    temp.ClearUnderflowAndOverflow()
    temp.Write()
f2.Close()



f3 = TFile.Open('/cephfs/user/s6marahm/output/abcd_dijets.root',"update")
for p in jet_pt:
    n_bincontent_one = f3.Get(p)
    n_bincontent_one.SetName(p+'_old')
    n_bincontent_one.Write()
    temp = ROOT.TH1F(p,p,(len(jet_pt_var_bin)-1),jet_pt_var_bin)
    temp.Sumw2()
    temp = n_bincontent_one.Rebin((len(jet_pt_var_bin)-1),p,jet_pt_var_bin)
    temp.Write()
for p in ljet_pt:
    n_bincontent_one = f3.Get(p)
    n_bincontent_one.SetName(p+'_old')
    n_bincontent_one.Write()
    temp = ROOT.TH1F(p,p,(len(ljet_pt_var_bin)-1),ljet_pt_var_bin)
    temp.Sumw2()
    temp = n_bincontent_one.Rebin((len(ljet_pt_var_bin)-1),p,ljet_pt_var_bin)
    temp.Write()
for p in VLQM:
    n_bincontent_one = f3.Get(p)
    n_bincontent_one.SetName(p+'_old')
    n_bincontent_one.Write()
    temp = ROOT.TH1F(p,p,(len(VLQM_var_bin)-1),VLQM_var_bin)
    temp.Sumw2()
    temp = n_bincontent_one.Rebin((len(VLQM_var_bin)-1),p,VLQM_var_bin)
    temp.SetBinContent(1, temp.GetBinContent(0) + temp.GetBinContent(1))
    temp.SetBinContent(temp.GetNbinsX(), temp.GetBinContent(temp.GetNbinsX()) + temp.GetBinContent(temp.GetNbinsX()+1))
    temp.ClearUnderflowAndOverflow()
    temp.Write()
f3.Close()



f4 = TFile.Open('/cephfs/user/s6marahm/output/abcd_Wjets.root',"update")
for p in jet_pt:
    n_bincontent_one = f4.Get(p)
    n_bincontent_one.SetName(p+'_old')
    n_bincontent_one.Write()
    temp = ROOT.TH1F(p,p,(len(jet_pt_var_bin)-1),jet_pt_var_bin)
    temp.Sumw2()
    temp = n_bincontent_one.Rebin((len(jet_pt_var_bin)-1),p,jet_pt_var_bin)
    temp.Write()
for p in ljet_pt:
    n_bincontent_one = f4.Get(p)
    n_bincontent_one.SetName(p+'_old')
    n_bincontent_one.Write()
    temp = ROOT.TH1F(p,p,(len(ljet_pt_var_bin)-1),ljet_pt_var_bin)
    temp.Sumw2()
    temp = n_bincontent_one.Rebin((len(ljet_pt_var_bin)-1),p,ljet_pt_var_bin)
    temp.Write()
for p in VLQM:
    n_bincontent_one = f4.Get(p)
    n_bincontent_one.SetName(p+'_old')
    n_bincontent_one.Write()
    temp = ROOT.TH1F(p,p,(len(VLQM_var_bin)-1),VLQM_var_bin)
    temp.Sumw2()
    temp = n_bincontent_one.Rebin((len(VLQM_var_bin)-1),p,VLQM_var_bin)
    temp.SetBinContent(1, temp.GetBinContent(0) + temp.GetBinContent(1))
    temp.SetBinContent(temp.GetNbinsX(), temp.GetBinContent(temp.GetNbinsX()) + temp.GetBinContent(temp.GetNbinsX()+1))
    temp.ClearUnderflowAndOverflow()
    temp.Write()
f4.Close()



f5 = TFile.Open('/cephfs/user/s6marahm/output/abcd_Zjets.root',"update")
for p in jet_pt:
    n_bincontent_one = f5.Get(p)
    n_bincontent_one.SetName(p+'_old')
    n_bincontent_one.Write()
    temp = ROOT.TH1F(p,p,(len(jet_pt_var_bin)-1),jet_pt_var_bin)
    temp.Sumw2()
    temp = n_bincontent_one.Rebin((len(jet_pt_var_bin)-1),p,jet_pt_var_bin)
    temp.Write()
for p in ljet_pt:
    n_bincontent_one = f5.Get(p)
    n_bincontent_one.SetName(p+'_old')
    n_bincontent_one.Write()
    temp = ROOT.TH1F(p,p,(len(ljet_pt_var_bin)-1),ljet_pt_var_bin)
    temp.Sumw2()
    temp = n_bincontent_one.Rebin((len(ljet_pt_var_bin)-1),p,ljet_pt_var_bin)
    temp.Write()
for p in VLQM:
    n_bincontent_one = f5.Get(p)
    n_bincontent_one.SetName(p+'_old')
    n_bincontent_one.Write()
    temp = ROOT.TH1F(p,p,(len(VLQM_var_bin)-1),VLQM_var_bin)
    temp.Sumw2()
    temp = n_bincontent_one.Rebin((len(VLQM_var_bin)-1),p,VLQM_var_bin)
    temp.SetBinContent(1, temp.GetBinContent(0) + temp.GetBinContent(1))
    temp.SetBinContent(temp.GetNbinsX(), temp.GetBinContent(temp.GetNbinsX()) + temp.GetBinContent(temp.GetNbinsX()+1))
    temp.ClearUnderflowAndOverflow()
    temp.Write()
f5.Close()



f6 = TFile.Open('/cephfs/user/s6marahm/output/abcd_Wt.root',"update")
for p in jet_pt:
    n_bincontent_one = f6.Get(p)
    n_bincontent_one.SetName(p+'_old')
    n_bincontent_one.Write()
    temp = ROOT.TH1F(p,p,(len(jet_pt_var_bin)-1),jet_pt_var_bin)
    temp.Sumw2()
    temp = n_bincontent_one.Rebin((len(jet_pt_var_bin)-1),p,jet_pt_var_bin)
    temp.Write()
for p in ljet_pt:
    n_bincontent_one = f6.Get(p)
    n_bincontent_one.SetName(p+'_old')
    n_bincontent_one.Write()
    temp = ROOT.TH1F(p,p,(len(ljet_pt_var_bin)-1),ljet_pt_var_bin)
    temp.Sumw2()
    temp = n_bincontent_one.Rebin((len(ljet_pt_var_bin)-1),p,ljet_pt_var_bin)
    temp.Write()
for p in VLQM:
    n_bincontent_one = f6.Get(p)
    n_bincontent_one.SetName(p+'_old')
    n_bincontent_one.Write()
    temp = ROOT.TH1F(p,p,(len(VLQM_var_bin)-1),VLQM_var_bin)
    temp.Sumw2()
    temp = n_bincontent_one.Rebin((len(VLQM_var_bin)-1),p,VLQM_var_bin)
    temp.SetBinContent(1, temp.GetBinContent(0) + temp.GetBinContent(1))
    temp.SetBinContent(temp.GetNbinsX(), temp.GetBinContent(temp.GetNbinsX()) + temp.GetBinContent(temp.GetNbinsX()+1))
    temp.ClearUnderflowAndOverflow()
    temp.Write()
f6.Close()



f7 = TFile.Open('/cephfs/user/s6marahm/output/abcd_ttbar.root',"update")
for p in jet_pt:
    n_bincontent_one = f7.Get(p)
    n_bincontent_one.SetName(p+'_old')
    n_bincontent_one.Write()
    temp = ROOT.TH1F(p,p,(len(jet_pt_var_bin)-1),jet_pt_var_bin)
    temp.Sumw2()
    temp = n_bincontent_one.Rebin((len(jet_pt_var_bin)-1),p,jet_pt_var_bin)
    temp.Write()
for p in ljet_pt:
    n_bincontent_one = f7.Get(p)
    n_bincontent_one.SetName(p+'_old')
    n_bincontent_one.Write()
    temp = ROOT.TH1F(p,p,(len(ljet_pt_var_bin)-1),ljet_pt_var_bin)
    temp.Sumw2()
    temp = n_bincontent_one.Rebin((len(ljet_pt_var_bin)-1),p,ljet_pt_var_bin)
    temp.Write()
for p in VLQM:
    n_bincontent_one = f7.Get(p)
    n_bincontent_one.SetName(p+'_old')
    n_bincontent_one.Write()
    temp = ROOT.TH1F(p,p,(len(VLQM_var_bin)-1),VLQM_var_bin)
    temp.Sumw2()
    temp = n_bincontent_one.Rebin((len(VLQM_var_bin)-1),p,VLQM_var_bin)
    temp.SetBinContent(1, temp.GetBinContent(0) + temp.GetBinContent(1))
    temp.SetBinContent(temp.GetNbinsX(), temp.GetBinContent(temp.GetNbinsX()) + temp.GetBinContent(temp.GetNbinsX()+1))
    temp.ClearUnderflowAndOverflow()
    temp.Write()
f7.Close()



f8 = TFile.Open('/cephfs/user/s6marahm/output/abcd_312335.root',"update")
for p in jet_pt:
    n_bincontent_one = f8.Get(p)
    n_bincontent_one.SetName(p+'_old')
    n_bincontent_one.Write()
    temp = ROOT.TH1F(p,p,(len(jet_pt_var_bin)-1),jet_pt_var_bin)
    temp.Sumw2()
    temp = n_bincontent_one.Rebin((len(jet_pt_var_bin)-1),p,jet_pt_var_bin)
    temp.Write()
for p in ljet_pt:
    n_bincontent_one = f8.Get(p)
    n_bincontent_one.SetName(p+'_old')
    n_bincontent_one.Write()
    temp = ROOT.TH1F(p,p,(len(ljet_pt_var_bin)-1),ljet_pt_var_bin)
    temp.Sumw2()
    temp = n_bincontent_one.Rebin((len(ljet_pt_var_bin)-1),p,ljet_pt_var_bin)
    temp.Write()
for p in VLQM:
    n_bincontent_one = f8.Get(p)
    n_bincontent_one.SetName(p+'_old')
    n_bincontent_one.Write()
    temp = ROOT.TH1F(p,p,(len(VLQM_var_bin)-1),VLQM_var_bin)
    temp.Sumw2()
    temp = n_bincontent_one.Rebin((len(VLQM_var_bin)-1),p,VLQM_var_bin)
    temp.SetBinContent(1, temp.GetBinContent(0) + temp.GetBinContent(1))
    temp.SetBinContent(temp.GetNbinsX(), temp.GetBinContent(temp.GetNbinsX()) + temp.GetBinContent(temp.GetNbinsX()+1))
    temp.ClearUnderflowAndOverflow()
    temp.Write()
f8.Close()