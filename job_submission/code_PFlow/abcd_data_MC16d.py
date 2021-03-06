import ROOT 
import math
import time
import os
import numpy as np
import heapq
import sys
from array import array

ROOT.gEnv.SetValue("TFile.AsyncReading","1")
ROOT.gEnv.SetValue("TFile.AsyncPrefetching","1")
ROOT.gEnv.SetValue("TTreeCache.Prefill","1")


def makeHists(data,dsid,label,weight_branch):
    
    location = '/cephfs/user/s6anband/ntuples/'

    tagger = ['allhad_2017_3var50_btag70','allhad_2017_3var50','allhad_2017_3var80_btag70','allhad_2017_3var80']

    file_names = []

    print data,dsid

    print "-------------------------------------------------------------------------------------------------------------- \n"
    print "\t \t DATA \n"


    sumofeventsweighted = 0.
    listOfFiles = os.listdir(location + data)
    nominal = ROOT.TChain("nominal")
    for f in listOfFiles:
        f = location + data + '/' + f 
        if 'output_root/user.abandyop' not in f:
            continue
        nominal.Add(f)

    if "output" not in weight_branch:
        os.chdir("/cephfs/user/s6marahm/output_sys/output_"+weight_branch+"/")
    else:
        os.chdir("/cephfs/user/s6marahm/output_sys/output/")
    f0 = ROOT.TFile.Open("abcd_"+dsid+"_"+label+".root","RECREATE")
    print "Made " , f0.GetName()
    file_names.append("abcd_"+dsid+"_"+label+".root")
    
    
    
    
    ljet_pt_2b_tight_Wtagged = ROOT.TH1F("ljet_pt_2b_tight_Wtagged","ljet_pt_2b_tight_Wtagged",18,500,1400)
    ljet_pt_2b_tight_Wtagged.Sumw2()
    ljet_eta_2b_tight_Wtagged = ROOT.TH1F("ljet_eta_2b_tight_Wtagged","ljet_eta_2b_tight_Wtagged",8,-2.0,2.0)
    ljet_eta_2b_tight_Wtagged.Sumw2()
    ljet_phi_2b_tight_Wtagged = ROOT.TH1F("ljet_phi_2b_tight_Wtagged","ljet_phi_2b_tight_Wtagged",10,-3.5,3.5)
    ljet_phi_2b_tight_Wtagged.Sumw2()
    ljet_m_2b_tight_Wtagged = ROOT.TH1F("ljet_m_2b_tight_Wtagged","ljet_m_2b_tight_Wtagged",13,0,260)
    ljet_m_2b_tight_Wtagged.Sumw2()
    ljet_e_2b_tight_Wtagged = ROOT.TH1F("ljet_e_2b_tight_Wtagged","ljet_e_2b_tight_Wtagged",20,0,3000)
    ljet_e_2b_tight_Wtagged.Sumw2()
    ljet_n_2b_tight_Wtagged = ROOT.TH1F("ljet_n_2b_tight_Wtagged","ljet_n_2b_tight_Wtagged",10,0,10)
    ljet_n_2b_tight_Wtagged.Sumw2()
    jet_pt_2b_tight_Wtagged = ROOT.TH1F("jet_pt_2b_tight_Wtagged","jet_pt_2b_tight_Wtagged",17,350,1200) #(59,25,1500)
    jet_pt_2b_tight_Wtagged.Sumw2()
    jet_eta_2b_tight_Wtagged = ROOT.TH1F("jet_eta_2b_tight_Wtagged","jet_eta_2b_tight_Wtagged",20,-4.5,4.5)
    jet_eta_2b_tight_Wtagged.Sumw2()
    jet_phi_2b_tight_Wtagged = ROOT.TH1F("jet_phi_2b_tight_Wtagged","jet_phi_2b_tight_Wtagged",10,-3.5,3.5)
    jet_phi_2b_tight_Wtagged.Sumw2()
    jet_e_2b_tight_Wtagged = ROOT.TH1F("jet_e_2b_tight_Wtagged","jet_e_2b_tight_Wtagged",20,25,2500)
    jet_e_2b_tight_Wtagged.Sumw2()
    jet_m_2b_tight_Wtagged = ROOT.TH1F("jet_m_2b_tight_Wtagged","jet_m_2b_tight_Wtagged",5,0,150)
    jet_m_2b_tight_Wtagged.Sumw2()
    jet_n_2b_tight_Wtagged = ROOT.TH1F("jet_n_2b_tight_Wtagged","jet_n_2b_tight_Wtagged",10,0,10)
    jet_n_2b_tight_Wtagged.Sumw2()
    sub_ljet_pt_2b_tight_Wtagged = ROOT.TH1F("sub_ljet_pt_2b_tight_Wtagged","sub_ljet_pt_2b_tight_Wtagged",20,0,2000)
    sub_ljet_pt_2b_tight_Wtagged.Sumw2()
    sub_ljet_eta_2b_tight_Wtagged = ROOT.TH1F("sub_ljet_eta_2b_tight_Wtagged","sub_ljet_eta_2b_tight_Wtagged",8,-2.0,2.0)
    sub_ljet_eta_2b_tight_Wtagged.Sumw2()
    sub_ljet_phi_2b_tight_Wtagged = ROOT.TH1F("sub_ljet_phi_2b_tight_Wtagged","sub_ljet_phi_2b_tight_Wtagged",10,-3.5,3.5)
    sub_ljet_phi_2b_tight_Wtagged.Sumw2()
    sub_ljet_m_2b_tight_Wtagged = ROOT.TH1F("sub_ljet_m_2b_tight_Wtagged","sub_ljet_m_2b_tight_Wtagged",13,0,260)
    sub_ljet_m_2b_tight_Wtagged.Sumw2()
    sub_ljet_e_2b_tight_Wtagged = ROOT.TH1F("sub_ljet_e_2b_tight_Wtagged","sub_ljet_e_2b_tight_Wtagged",20,0,3000)
    sub_ljet_e_2b_tight_Wtagged.Sumw2()
    VLQM_2b_tight_Wtagged = ROOT.TH1F("VLQM_2b_tight_Wtagged","VLQM_2b_tight_Wtagged",60,400,3400)
    VLQM_2b_tight_Wtagged.Sumw2()
    DeltaR_2b_tight_Wtagged = ROOT.TH1F("DeltaR_2b_tight_Wtagged","DeltaR_2b_tight_Wtagged",10,0,5)
    DeltaR_2b_tight_Wtagged.Sumw2()
    DeltaPhi_2b_tight_Wtagged = ROOT.TH1F("DeltaPhi_2b_tight_Wtagged","DeltaPhi_2b_tight_Wtagged",10,-5,5)
    DeltaPhi_2b_tight_Wtagged.Sumw2()
    DeltaR_bjet_2b_tight_Wtagged = ROOT.TH1F("DeltaR_bjet_2b_tight_Wtagged","DeltaR_bjet_2b_tight_Wtagged",10,0,5)
    DeltaR_bjet_2b_tight_Wtagged.Sumw2()


    ljet_pt_0b_tight_Wtagged = ROOT.TH1F("ljet_pt_0b_tight_Wtagged","ljet_pt_0b_tight_Wtagged",18,500,1400)
    ljet_pt_0b_tight_Wtagged.Sumw2()
    ljet_eta_0b_tight_Wtagged = ROOT.TH1F("ljet_eta_0b_tight_Wtagged","ljet_eta_0b_tight_Wtagged",8,-2.0,2.0)
    ljet_eta_0b_tight_Wtagged.Sumw2()
    ljet_phi_0b_tight_Wtagged = ROOT.TH1F("ljet_phi_0b_tight_Wtagged","ljet_phi_0b_tight_Wtagged",10,-3.5,3.5)
    ljet_phi_0b_tight_Wtagged.Sumw2()
    ljet_m_0b_tight_Wtagged = ROOT.TH1F("ljet_m_0b_tight_Wtagged","ljet_m_0b_tight_Wtagged",13,0,260)
    ljet_m_0b_tight_Wtagged.Sumw2()
    ljet_e_0b_tight_Wtagged = ROOT.TH1F("ljet_e_0b_tight_Wtagged","ljet_e_0b_tight_Wtagged",20,0,3000)
    ljet_e_0b_tight_Wtagged.Sumw2()
    ljet_n_0b_tight_Wtagged = ROOT.TH1F("ljet_n_0b_tight_Wtagged","ljet_n_0b_tight_Wtagged",10,0,10)
    ljet_n_0b_tight_Wtagged.Sumw2()
    jet_pt_0b_tight_Wtagged = ROOT.TH1F("jet_pt_0b_tight_Wtagged","jet_pt_0b_tight_Wtagged",17,350,1200)
    jet_pt_0b_tight_Wtagged.Sumw2()
    jet_eta_0b_tight_Wtagged = ROOT.TH1F("jet_eta_0b_tight_Wtagged","jet_eta_0b_tight_Wtagged",20,-4.5,4.5)
    jet_eta_0b_tight_Wtagged.Sumw2()
    jet_phi_0b_tight_Wtagged = ROOT.TH1F("jet_phi_0b_tight_Wtagged","jet_phi_0b_tight_Wtagged",10,-3.5,3.5)
    jet_phi_0b_tight_Wtagged.Sumw2()
    jet_e_0b_tight_Wtagged = ROOT.TH1F("jet_e_0b_tight_Wtagged","jet_e_0b_tight_Wtagged",20,25,2500)
    jet_e_0b_tight_Wtagged.Sumw2()
    jet_m_0b_tight_Wtagged = ROOT.TH1F("jet_m_0b_tight_Wtagged","jet_m_0b_tight_Wtagged",5,0,150)
    jet_m_0b_tight_Wtagged.Sumw2()
    jet_n_0b_tight_Wtagged = ROOT.TH1F("jet_n_0b_tight_Wtagged","jet_n_0b_tight_Wtagged",10,0,10)
    jet_n_0b_tight_Wtagged.Sumw2()
    sub_ljet_pt_0b_tight_Wtagged = ROOT.TH1F("sub_ljet_pt_0b_tight_Wtagged","sub_ljet_pt_0b_tight_Wtagged",20,0,2000)
    sub_ljet_pt_0b_tight_Wtagged.Sumw2()
    sub_ljet_eta_0b_tight_Wtagged = ROOT.TH1F("sub_ljet_eta_0b_tight_Wtagged","sub_ljet_eta_0b_tight_Wtagged",8,-2.0,2.0)
    sub_ljet_eta_0b_tight_Wtagged.Sumw2()
    sub_ljet_phi_0b_tight_Wtagged = ROOT.TH1F("sub_ljet_phi_0b_tight_Wtagged","sub_ljet_phi_0b_tight_Wtagged",10,-3.5,3.5)
    sub_ljet_phi_0b_tight_Wtagged.Sumw2()
    sub_ljet_m_0b_tight_Wtagged = ROOT.TH1F("sub_ljet_m_0b_tight_Wtagged","sub_ljet_m_0b_tight_Wtagged",13,0,260)
    sub_ljet_m_0b_tight_Wtagged.Sumw2()
    sub_ljet_e_0b_tight_Wtagged = ROOT.TH1F("sub_ljet_e_0b_tight_Wtagged","sub_ljet_e_0b_tight_Wtagged",20,0,3000)
    sub_ljet_e_0b_tight_Wtagged.Sumw2()
    VLQM_0b_tight_Wtagged = ROOT.TH1F("VLQM_0b_tight_Wtagged","VLQM_0b_tight_Wtagged",60,400,3400)
    VLQM_0b_tight_Wtagged.Sumw2()
    DeltaR_0b_tight_Wtagged = ROOT.TH1F("DeltaR_0b_tight_Wtagged","DeltaR_0b_tight_Wtagged",10,0,5)
    DeltaR_0b_tight_Wtagged.Sumw2()
    DeltaPhi_0b_tight_Wtagged = ROOT.TH1F("DeltaPhi_0b_tight_Wtagged","DeltaPhi_0b_tight_Wtagged",10,-5,5)
    DeltaPhi_0b_tight_Wtagged.Sumw2()
    
    
    ljet_pt_2b_loose_not_tight_Wtagged = ROOT.TH1F("ljet_pt_2b_loose_not_tight_Wtagged","ljet_pt_2b_loose_not_tight_Wtagged",18,500,1400)
    ljet_pt_2b_loose_not_tight_Wtagged.Sumw2()
    ljet_eta_2b_loose_not_tight_Wtagged = ROOT.TH1F("ljet_eta_2b_loose_not_tight_Wtagged","ljet_eta_2b_loose_not_tight_Wtagged",8,-2.0,2.0)
    ljet_eta_2b_loose_not_tight_Wtagged.Sumw2()
    ljet_phi_2b_loose_not_tight_Wtagged = ROOT.TH1F("ljet_phi_2b_loose_not_tight_Wtagged","ljet_phi_2b_loose_not_tight_Wtagged",10,-3.5,3.5)
    ljet_phi_2b_loose_not_tight_Wtagged.Sumw2()
    ljet_m_2b_loose_not_tight_Wtagged = ROOT.TH1F("ljet_m_2b_loose_not_tight_Wtagged","ljet_m_2b_loose_not_tight_Wtagged",13,0,260)
    ljet_m_2b_loose_not_tight_Wtagged.Sumw2()
    ljet_e_2b_loose_not_tight_Wtagged = ROOT.TH1F("ljet_e_2b_loose_not_tight_Wtagged","ljet_e_2b_loose_not_tight_Wtagged",20,0,3000)
    ljet_e_2b_loose_not_tight_Wtagged.Sumw2()
    ljet_n_2b_loose_not_tight_Wtagged = ROOT.TH1F("ljet_n_2b_loose_not_tight_Wtagged","ljet_n_2b_loose_not_tight_Wtagged",10,0,10)
    ljet_n_2b_loose_not_tight_Wtagged.Sumw2()
    jet_pt_2b_loose_not_tight_Wtagged = ROOT.TH1F("jet_pt_2b_loose_not_tight_Wtagged","jet_pt_2b_loose_not_tight_Wtagged",17,350,1200)
    jet_pt_2b_loose_not_tight_Wtagged.Sumw2()
    jet_eta_2b_loose_not_tight_Wtagged = ROOT.TH1F("jet_eta_2b_loose_not_tight_Wtagged","jet_eta_2b_loose_not_tight_Wtagged",20,-4.5,4.5)
    jet_eta_2b_loose_not_tight_Wtagged.Sumw2()
    jet_phi_2b_loose_not_tight_Wtagged = ROOT.TH1F("jet_phi_2b_loose_not_tight_Wtagged","jet_phi_2b_loose_not_tight_Wtagged",10,-3.5,3.5)
    jet_phi_2b_loose_not_tight_Wtagged.Sumw2()
    jet_e_2b_loose_not_tight_Wtagged = ROOT.TH1F("jet_e_2b_loose_not_tight_Wtagged","jet_e_2b_loose_not_tight_Wtagged",20,25,2500)
    jet_e_2b_loose_not_tight_Wtagged.Sumw2()
    jet_m_2b_loose_not_tight_Wtagged = ROOT.TH1F("jet_m_2b_loose_not_tight_Wtagged","jet_m_2b_loose_not_tight_Wtagged",5,0,150)
    jet_m_2b_loose_not_tight_Wtagged.Sumw2()
    jet_n_2b_loose_not_tight_Wtagged = ROOT.TH1F("jet_n_2b_loose_not_tight_Wtagged","jet_n_2b_loose_not_tight_Wtagged",10,0,10)
    jet_n_2b_loose_not_tight_Wtagged.Sumw2()
    sub_ljet_pt_2b_loose_not_tight_Wtagged = ROOT.TH1F("sub_ljet_pt_2b_loose_not_tight_Wtagged","sub_ljet_pt_2b_loose_not_tight_Wtagged",20,0,2000)
    sub_ljet_pt_2b_loose_not_tight_Wtagged.Sumw2()
    sub_ljet_eta_2b_loose_not_tight_Wtagged = ROOT.TH1F("sub_ljet_eta_2b_loose_not_tight_Wtagged","sub_ljet_eta_2b_loose_not_tight_Wtagged",8,-2.0,2.0)
    sub_ljet_eta_2b_loose_not_tight_Wtagged.Sumw2()
    sub_ljet_phi_2b_loose_not_tight_Wtagged = ROOT.TH1F("sub_ljet_phi_2b_loose_not_tight_Wtagged","sub_ljet_phi_2b_loose_not_tight_Wtagged",10,-3.5,3.5)
    sub_ljet_phi_2b_loose_not_tight_Wtagged.Sumw2()
    sub_ljet_m_2b_loose_not_tight_Wtagged = ROOT.TH1F("sub_ljet_m_2b_loose_not_tight_Wtagged","sub_ljet_m_2b_loose_not_tight_Wtagged",13,0,260)
    sub_ljet_m_2b_loose_not_tight_Wtagged.Sumw2()
    sub_ljet_e_2b_loose_not_tight_Wtagged = ROOT.TH1F("sub_ljet_e_2b_loose_not_tight_Wtagged","sub_ljet_e_2b_loose_not_tight_Wtagged",20,0,3000)
    sub_ljet_e_2b_loose_not_tight_Wtagged.Sumw2()
    VLQM_2b_loose_not_tight_Wtagged = ROOT.TH1F("VLQM_2b_loose_not_tight_Wtagged","VLQM_2b_loose_not_tight_Wtagged",60,400,3400)
    VLQM_2b_loose_not_tight_Wtagged.Sumw2()
    DeltaR_2b_loose_not_tight_Wtagged = ROOT.TH1F("DeltaR_2b_loose_not_tight_Wtagged","DeltaR_2b_loose_not_tight_Wtagged",10,0,5)
    DeltaR_2b_loose_not_tight_Wtagged.Sumw2()
    DeltaPhi_2b_loose_not_tight_Wtagged = ROOT.TH1F("DeltaPhi_2b_loose_not_tight_Wtagged","DeltaPhi_2b_loose_not_tight_Wtagged",10,-5,5)
    DeltaPhi_2b_loose_not_tight_Wtagged.Sumw2()
    DeltaR_bjet_2b_loose_not_tight_Wtagged = ROOT.TH1F("DeltaR_bjet_2b_loose_not_tight_Wtagged","DeltaR_bjet_2b_loose_not_tight_Wtagged",10,0,5)
    DeltaR_bjet_2b_loose_not_tight_Wtagged.Sumw2()


    ljet_pt_0b_loose_not_tight_Wtagged = ROOT.TH1F("ljet_pt_0b_loose_not_tight_Wtagged","ljet_pt_0b_loose_not_tight_Wtagged",18,500,1400)
    ljet_pt_0b_loose_not_tight_Wtagged.Sumw2()
    ljet_eta_0b_loose_not_tight_Wtagged = ROOT.TH1F("ljet_eta_0b_loose_not_tight_Wtagged","ljet_eta_0b_loose_not_tight_Wtagged",8,-2.0,2.0)
    ljet_eta_0b_loose_not_tight_Wtagged.Sumw2()
    ljet_phi_0b_loose_not_tight_Wtagged = ROOT.TH1F("ljet_phi_0b_loose_not_tight_Wtagged","ljet_phi_0b_loose_not_tight_Wtagged",10,-3.5,3.5)
    ljet_phi_0b_loose_not_tight_Wtagged.Sumw2()
    ljet_m_0b_loose_not_tight_Wtagged = ROOT.TH1F("ljet_m_0b_loose_not_tight_Wtagged","ljet_m_0b_loose_not_tight_Wtagged",13,0,260)
    ljet_m_0b_loose_not_tight_Wtagged.Sumw2()
    ljet_e_0b_loose_not_tight_Wtagged = ROOT.TH1F("ljet_e_0b_loose_not_tight_Wtagged","ljet_e_0b_loose_not_tight_Wtagged",20,0,3000)
    ljet_e_0b_loose_not_tight_Wtagged.Sumw2()
    ljet_n_0b_loose_not_tight_Wtagged = ROOT.TH1F("ljet_n_0b_loose_not_tight_Wtagged","ljet_n_0b_loose_not_tight_Wtagged",10,0,10)
    ljet_n_0b_loose_not_tight_Wtagged.Sumw2()
    jet_pt_0b_loose_not_tight_Wtagged = ROOT.TH1F("jet_pt_0b_loose_not_tight_Wtagged","jet_pt_0b_loose_not_tight_Wtagged",17,350,1200)
    jet_pt_0b_loose_not_tight_Wtagged.Sumw2()
    jet_eta_0b_loose_not_tight_Wtagged = ROOT.TH1F("jet_eta_0b_loose_not_tight_Wtagged","jet_eta_0b_loose_not_tight_Wtagged",20,-4.5,4.5)
    jet_eta_0b_loose_not_tight_Wtagged.Sumw2()
    jet_phi_0b_loose_not_tight_Wtagged = ROOT.TH1F("jet_phi_0b_loose_not_tight_Wtagged","jet_phi_0b_loose_not_tight_Wtagged",10,-3.5,3.5)
    jet_phi_0b_loose_not_tight_Wtagged.Sumw2()
    jet_e_0b_loose_not_tight_Wtagged = ROOT.TH1F("jet_e_0b_loose_not_tight_Wtagged","jet_e_0b_loose_not_tight_Wtagged",20,25,2500)
    jet_e_0b_loose_not_tight_Wtagged.Sumw2()
    jet_m_0b_loose_not_tight_Wtagged = ROOT.TH1F("jet_m_0b_loose_not_tight_Wtagged","jet_m_0b_loose_not_tight_Wtagged",5,0,150)
    jet_m_0b_loose_not_tight_Wtagged.Sumw2()
    jet_n_0b_loose_not_tight_Wtagged = ROOT.TH1F("jet_n_0b_loose_not_tight_Wtagged","jet_n_0b_loose_not_tight_Wtagged",10,0,10)
    jet_n_0b_loose_not_tight_Wtagged.Sumw2()
    sub_ljet_pt_0b_loose_not_tight_Wtagged = ROOT.TH1F("sub_ljet_pt_0b_loose_not_tight_Wtagged","sub_ljet_pt_0b_loose_not_tight_Wtagged",20,0,2000)
    sub_ljet_pt_0b_loose_not_tight_Wtagged.Sumw2()
    sub_ljet_eta_0b_loose_not_tight_Wtagged = ROOT.TH1F("sub_ljet_eta_0b_loose_not_tight_Wtagged","sub_ljet_eta_0b_loose_not_tight_Wtagged",8,-2.0,2.0)
    sub_ljet_eta_0b_loose_not_tight_Wtagged.Sumw2()
    sub_ljet_phi_0b_loose_not_tight_Wtagged = ROOT.TH1F("sub_ljet_phi_0b_loose_not_tight_Wtagged","sub_ljet_phi_0b_loose_not_tight_Wtagged",10,-3.5,3.5)
    sub_ljet_phi_0b_loose_not_tight_Wtagged.Sumw2()
    sub_ljet_m_0b_loose_not_tight_Wtagged = ROOT.TH1F("sub_ljet_m_0b_loose_not_tight_Wtagged","sub_ljet_m_0b_loose_not_tight_Wtagged",13,0,260)
    sub_ljet_m_0b_loose_not_tight_Wtagged.Sumw2()
    sub_ljet_e_0b_loose_not_tight_Wtagged = ROOT.TH1F("sub_ljet_e_0b_loose_not_tight_Wtagged","sub_ljet_e_0b_loose_not_tight_Wtagged",20,0,3000)
    sub_ljet_e_0b_loose_not_tight_Wtagged.Sumw2()
    VLQM_0b_loose_not_tight_Wtagged = ROOT.TH1F("VLQM_0b_loose_not_tight_Wtagged","VLQM_0b_loose_not_tight_Wtagged",60,400,3400)
    VLQM_0b_loose_not_tight_Wtagged.Sumw2()
    DeltaR_0b_loose_not_tight_Wtagged = ROOT.TH1F("DeltaR_0b_loose_not_tight_Wtagged","DeltaR_0b_loose_not_tight_Wtagged",10,0,5)
    DeltaR_0b_loose_not_tight_Wtagged.Sumw2()
    DeltaPhi_0b_loose_not_tight_Wtagged = ROOT.TH1F("DeltaPhi_0b_loose_not_tight_Wtagged","DeltaPhi_0b_loose_not_tight_Wtagged",10,-5,5)
    DeltaPhi_0b_loose_not_tight_Wtagged.Sumw2()

    
    ljet_pt_2b_not_loose_Wtagged = ROOT.TH1F("ljet_pt_2b_not_loose_Wtagged","ljet_pt_2b_not_loose_Wtagged",18,500,1400)
    ljet_pt_2b_not_loose_Wtagged.Sumw2()
    ljet_eta_2b_not_loose_Wtagged = ROOT.TH1F("ljet_eta_2b_not_loose_Wtagged","ljet_eta_2b_not_loose_Wtagged",8,-2.0,2.0)
    ljet_eta_2b_not_loose_Wtagged.Sumw2()
    ljet_phi_2b_not_loose_Wtagged = ROOT.TH1F("ljet_phi_2b_not_loose_Wtagged","ljet_phi_2b_not_loose_Wtagged",10,-3.5,3.5)
    ljet_phi_2b_not_loose_Wtagged.Sumw2()
    ljet_m_2b_not_loose_Wtagged = ROOT.TH1F("ljet_m_2b_not_loose_Wtagged","ljet_m_2b_not_loose_Wtagged",13,0,260)
    ljet_m_2b_not_loose_Wtagged.Sumw2()
    ljet_e_2b_not_loose_Wtagged = ROOT.TH1F("ljet_e_2b_not_loose_Wtagged","ljet_e_2b_not_loose_Wtagged",20,0,3000)
    ljet_e_2b_not_loose_Wtagged.Sumw2()
    ljet_n_2b_not_loose_Wtagged = ROOT.TH1F("ljet_n_2b_not_loose_Wtagged","ljet_n_2b_not_loose_Wtagged",10,0,10)
    ljet_n_2b_not_loose_Wtagged.Sumw2()
    jet_pt_2b_not_loose_Wtagged = ROOT.TH1F("jet_pt_2b_not_loose_Wtagged","jet_pt_2b_not_loose_Wtagged",17,350,1200)
    jet_pt_2b_not_loose_Wtagged.Sumw2()
    jet_eta_2b_not_loose_Wtagged = ROOT.TH1F("jet_eta_2b_not_loose_Wtagged","jet_eta_2b_not_loose_Wtagged",20,-4.5,4.5)
    jet_eta_2b_not_loose_Wtagged.Sumw2()
    jet_phi_2b_not_loose_Wtagged = ROOT.TH1F("jet_phi_2b_not_loose_Wtagged","jet_phi_2b_not_loose_Wtagged",10,-3.5,3.5)
    jet_phi_2b_not_loose_Wtagged.Sumw2()
    jet_e_2b_not_loose_Wtagged = ROOT.TH1F("jet_e_2b_not_loose_Wtagged","jet_e_2b_not_loose_Wtagged",20,25,2500)
    jet_e_2b_not_loose_Wtagged.Sumw2()
    jet_m_2b_not_loose_Wtagged = ROOT.TH1F("jet_m_2b_not_loose_Wtagged","jet_m_2b_not_loose_Wtagged",5,0,150)
    jet_m_2b_not_loose_Wtagged.Sumw2()
    jet_n_2b_not_loose_Wtagged = ROOT.TH1F("jet_n_2b_not_loose_Wtagged","jet_n_2b_not_loose_Wtagged",10,0,10)
    jet_n_2b_not_loose_Wtagged.Sumw2()
    sub_ljet_pt_2b_not_loose_Wtagged = ROOT.TH1F("sub_ljet_pt_2b_not_loose_Wtagged","sub_ljet_pt_2b_not_loose_Wtagged",20,0,2000)
    sub_ljet_pt_2b_not_loose_Wtagged.Sumw2()
    sub_ljet_eta_2b_not_loose_Wtagged = ROOT.TH1F("sub_ljet_eta_2b_not_loose_Wtagged","sub_ljet_eta_2b_not_loose_Wtagged",8,-2.0,2.0)
    sub_ljet_eta_2b_not_loose_Wtagged.Sumw2()
    sub_ljet_phi_2b_not_loose_Wtagged = ROOT.TH1F("sub_ljet_phi_2b_not_loose_Wtagged","sub_ljet_phi_2b_not_loose_Wtagged",10,-3.5,3.5)
    sub_ljet_phi_2b_not_loose_Wtagged.Sumw2()
    sub_ljet_m_2b_not_loose_Wtagged = ROOT.TH1F("sub_ljet_m_2b_not_loose_Wtagged","sub_ljet_m_2b_not_loose_Wtagged",13,0,260)
    sub_ljet_m_2b_not_loose_Wtagged.Sumw2()
    sub_ljet_e_2b_not_loose_Wtagged = ROOT.TH1F("sub_ljet_e_2b_not_loose_Wtagged","sub_ljet_e_2b_not_loose_Wtagged",20,0,3000)
    sub_ljet_e_2b_not_loose_Wtagged.Sumw2()
    VLQM_2b_not_loose_Wtagged = ROOT.TH1F("VLQM_2b_not_loose_Wtagged","VLQM_2b_not_loose_Wtagged",60,400,3400)
    VLQM_2b_not_loose_Wtagged.Sumw2()
    DeltaR_2b_not_loose_Wtagged = ROOT.TH1F("DeltaR_2b_not_loose_Wtagged","DeltaR_2b_not_loose_Wtagged",10,0,5)
    DeltaR_2b_not_loose_Wtagged.Sumw2()
    DeltaPhi_2b_not_loose_Wtagged = ROOT.TH1F("DeltaPhi_2b_not_loose_Wtagged","DeltaPhi_2b_not_loose_Wtagged",10,-5,5)
    DeltaPhi_2b_not_loose_Wtagged.Sumw2()
    DeltaR_bjet_2b_not_loose_Wtagged = ROOT.TH1F("DeltaR_bjet_2b_not_loose_Wtagged","DeltaR_bjet_2b_not_loose_Wtagged",10,0,5)
    DeltaR_bjet_2b_not_loose_Wtagged.Sumw2()


    ljet_pt_0b_not_loose_Wtagged = ROOT.TH1F("ljet_pt_0b_not_loose_Wtagged","ljet_pt_0b_not_loose_Wtagged",18,500,1400)
    ljet_pt_0b_not_loose_Wtagged.Sumw2()
    ljet_eta_0b_not_loose_Wtagged = ROOT.TH1F("ljet_eta_0b_not_loose_Wtagged","ljet_eta_0b_not_loose_Wtagged",8,-2.0,2.0)
    ljet_eta_0b_not_loose_Wtagged.Sumw2()
    ljet_phi_0b_not_loose_Wtagged = ROOT.TH1F("ljet_phi_0b_not_loose_Wtagged","ljet_phi_0b_not_loose_Wtagged",10,-3.5,3.5)
    ljet_phi_0b_not_loose_Wtagged.Sumw2()
    ljet_m_0b_not_loose_Wtagged = ROOT.TH1F("ljet_m_0b_not_loose_Wtagged","ljet_m_0b_not_loose_Wtagged",13,0,260)
    ljet_m_0b_not_loose_Wtagged.Sumw2()
    ljet_e_0b_not_loose_Wtagged = ROOT.TH1F("ljet_e_0b_not_loose_Wtagged","ljet_e_0b_not_loose_Wtagged",20,0,3000)
    ljet_e_0b_not_loose_Wtagged.Sumw2()
    ljet_n_0b_not_loose_Wtagged = ROOT.TH1F("ljet_n_0b_not_loose_Wtagged","ljet_n_0b_not_loose_Wtagged",10,0,10)
    ljet_n_0b_not_loose_Wtagged.Sumw2()
    jet_pt_0b_not_loose_Wtagged = ROOT.TH1F("jet_pt_0b_not_loose_Wtagged","jet_pt_0b_not_loose_Wtagged",17,350,1200)
    jet_pt_0b_not_loose_Wtagged.Sumw2()
    jet_eta_0b_not_loose_Wtagged = ROOT.TH1F("jet_eta_0b_not_loose_Wtagged","jet_eta_0b_not_loose_Wtagged",20,-4.5,4.5)
    jet_eta_0b_not_loose_Wtagged.Sumw2()
    jet_phi_0b_not_loose_Wtagged = ROOT.TH1F("jet_phi_0b_not_loose_Wtagged","jet_phi_0b_not_loose_Wtagged",10,-3.5,3.5)
    jet_phi_0b_not_loose_Wtagged.Sumw2()
    jet_e_0b_not_loose_Wtagged = ROOT.TH1F("jet_e_0b_not_loose_Wtagged","jet_e_0b_not_loose_Wtagged",20,25,2500)
    jet_e_0b_not_loose_Wtagged.Sumw2()
    jet_m_0b_not_loose_Wtagged = ROOT.TH1F("jet_m_0b_not_loose_Wtagged","jet_m_0b_not_loose_Wtagged",5,0,150)
    jet_m_0b_not_loose_Wtagged.Sumw2()
    jet_n_0b_not_loose_Wtagged = ROOT.TH1F("jet_n_0b_not_loose_Wtagged","jet_n_0b_not_loose_Wtagged",10,0,10)
    jet_n_0b_not_loose_Wtagged.Sumw2()
    sub_ljet_pt_0b_not_loose_Wtagged = ROOT.TH1F("sub_ljet_pt_0b_not_loose_Wtagged","sub_ljet_pt_0b_not_loose_Wtagged",20,0,2000)
    sub_ljet_pt_0b_not_loose_Wtagged.Sumw2()
    sub_ljet_eta_0b_not_loose_Wtagged = ROOT.TH1F("sub_ljet_eta_0b_not_loose_Wtagged","sub_ljet_eta_0b_not_loose_Wtagged",8,-2.0,2.0)
    sub_ljet_eta_0b_not_loose_Wtagged.Sumw2()
    sub_ljet_phi_0b_not_loose_Wtagged = ROOT.TH1F("sub_ljet_phi_0b_not_loose_Wtagged","sub_ljet_phi_0b_not_loose_Wtagged",10,-3.5,3.5)
    sub_ljet_phi_0b_not_loose_Wtagged.Sumw2()
    sub_ljet_m_0b_not_loose_Wtagged = ROOT.TH1F("sub_ljet_m_0b_not_loose_Wtagged","sub_ljet_m_0b_not_loose_Wtagged",13,0,260)
    sub_ljet_m_0b_not_loose_Wtagged.Sumw2()
    sub_ljet_e_0b_not_loose_Wtagged = ROOT.TH1F("sub_ljet_e_0b_not_loose_Wtagged","sub_ljet_e_0b_not_loose_Wtagged",20,0,3000)
    sub_ljet_e_0b_not_loose_Wtagged.Sumw2()
    VLQM_0b_not_loose_Wtagged = ROOT.TH1F("VLQM_0b_not_loose_Wtagged","VLQM_0b_not_loose_Wtagged",60,400,3400)
    VLQM_0b_not_loose_Wtagged.Sumw2()
    DeltaR_0b_not_loose_Wtagged = ROOT.TH1F("DeltaR_0b_not_loose_Wtagged","DeltaR_0b_not_loose_Wtagged",10,0,5)
    DeltaR_0b_not_loose_Wtagged.Sumw2()
    DeltaPhi_0b_not_loose_Wtagged = ROOT.TH1F("DeltaPhi_0b_not_loose_Wtagged","DeltaPhi_0b_not_loose_Wtagged",10,-5,5)
    DeltaPhi_0b_not_loose_Wtagged.Sumw2()

    nominal.SetCacheSize(100000000)
    nominal.AddBranchToCache("*", True)
    
    
    for l in xrange(nominal.GetEntries()):
        leadjet_p4 = ROOT.TLorentzVector()
        jet_p4 = ROOT.TLorentzVector()
        lead_bjet_p4 = ROOT.TLorentzVector()
        sub_bjet_p4 = ROOT.TLorentzVector()
        VLQ_p4 = ROOT.TLorentzVector()
        VLQM = 0
        DeltaR = 0
        DeltaR_bjet = 0
        DeltaPhi = 0
        leadjetpt = []
        leadjeteta = []
        leadjetphi = []
        leadjetm = []
        leadjete = []
        leadjet3varW80 = []
        leadjet3varW50 = []
        leadjetdnnW80 = []
        jetpt_btag = []
        jeteta_btag = []
        jetphi_btag = []
        jete_btag = []
        jetpt = []
        jeteta = []
        jetphi = []
        jete = []
        jetbtag70 = []
        jetbtag = []
        jetbtag60 = []
        index = []
        forward = False
        
        nominal.GetEntry(l)
        weight = 1.0
        tag2017_tight = getattr(nominal,tagger[0])
        tag2017_tight_0b = getattr(nominal,tagger[1])
        tag2017_loose = getattr(nominal,tagger[2])
        tag2017_loose_0b = getattr(nominal,tagger[3])
        leadjet_pt = getattr(nominal,'ljet_pt')
        leadjet_eta = getattr(nominal,'ljet_eta')
        leadjet_phi = getattr(nominal,'ljet_phi')
        leadjet_m = getattr(nominal,'ljet_m')
        leadjet_e = getattr(nominal,'ljet_e')
        leadjet_3varW80 = getattr(nominal,'ljet_good_3VarW80')
        leadjet_3varW50 = getattr(nominal,'ljet_good_3VarW50')
        leadjet_dnnW80 = getattr(nominal,'ljet_good_dnn_contained80')
        jet_pt = getattr(nominal,'jet_pt')
        jet_eta = getattr(nominal,'jet_eta')
        jet_phi = getattr(nominal,'jet_phi')
        jet_e = getattr(nominal,'jet_e')
        met_met = getattr(nominal,'met_met')
        jet_btag70 = getattr(nominal,"jet_isbtagged_DL1r_70")
        jet_btag60 = getattr(nominal,"jet_isbtagged_DL1r_60")

        
        for x in xrange(leadjet_pt.size()):
            leadjetpt.append(leadjet_pt[x])
            leadjeteta.append(leadjet_eta[x])
            leadjetphi.append(leadjet_phi[x])
            leadjetm.append(leadjet_m[x])
            leadjete.append(leadjet_e[x])
            leadjet3varW80.append(leadjet_3varW80[x])
            leadjet3varW50.append(leadjet_3varW50[x])
            leadjetdnnW80.append(leadjet_dnnW80[x])
        leadjetpt = np.array(leadjetpt)
        leadjeteta = np.array(leadjeteta)
        leadjetphi = np.array(leadjetphi)
        leadjetm = np.array(leadjetm)
        leadjete = np.array(leadjete)
        leadjetdnnW80 = np.array(leadjetdnnW80)
        leadjet3varW80 = np.array(leadjet3varW80)
        leadjet3varW50 = np.array(leadjet3varW50)
        tight = leadjet3varW50
        loose = leadjet3varW80
        top = leadjetdnnW80
        idx_ljet = leadjetpt.argmax()

        if len(leadjetpt) > 1:
            idx = heapq.nlargest(2, leadjetpt)
            idx_subjet = leadjetpt.tolist().index(idx[1])
        
        
        for y in xrange(jet_pt.size()):
            jetpt.append(jet_pt[y])
            jeteta.append(jet_eta[y])
            jetphi.append(jet_phi[y])
            jete.append(jet_e[y])
            jetbtag60.append(jet_btag60[y])
            jetbtag70.append(jet_btag70[y])
        jetpt = np.array(jetpt)
        jeteta = np.array(jeteta)
        jetphi = np.array(jetphi)
        jete = np.array(jete)
        jetbtag70 = np.array(jetbtag70)
        jet_btag = jetbtag70
        
        
        for k in xrange(jet_eta.size()):
            if jet_btag[k] != '\x01' and abs(jet_eta[k]) > 2.5:
                forward = True
                break     
            else:
                forward = False


        for j in xrange(jet_btag.size):
            if jet_btag[j] == '\x01':
                jetpt_btag.append(jetpt[j])
                jeteta_btag.append(jeteta[j])
                jetphi_btag.append(jetphi[j])
                jete_btag.append(jete[j])
                index.append(j)
            else:
                continue
        
        jetpt_btag = np.array(jetpt_btag)
        jeteta_btag = np.array(jeteta_btag)
        jetphi_btag = np.array(jetphi_btag)
        jete_btag = np.array(jete_btag)

        if len(jetpt_btag) >= 1:
            idx_jet = index[jetpt_btag.argmax()]
        else:
            idx_jet = jetpt.argmax()
        #print len(jetpt_btag), loose[idx_ljet], jetpt[idx_jet], leadjetpt[idx_ljet], tag2017 
        #print leadjetpt.size, leadjet_pt.size()
 


        
        jet_p4.SetPtEtaPhiE(jetpt[idx_jet],jeteta[idx_jet],jetphi[idx_jet],jete[idx_jet])
        leadjet_p4.SetPtEtaPhiE(leadjetpt[idx_ljet],leadjeteta[idx_ljet],leadjetphi[idx_ljet],leadjete[idx_ljet])
        DeltaR = leadjet_p4.DeltaR(jet_p4)


        if len(jetpt_btag) > 1:
            lead_bjet_p4.SetPtEtaPhiE(jetpt_btag[0],jeteta_btag[0],jetphi_btag[0],jete_btag[0])
            sub_bjet_p4.SetPtEtaPhiE(jetpt_btag[1],jeteta_btag[1],jetphi_btag[1],jete_btag[1])
            DeltaR_bjet = lead_bjet_p4.DeltaR(sub_bjet_p4)
        



        if len(jetpt_btag) == 1:
            if len(jetpt) > 2:
                if jetpt[idx_jet] == jetpt[0] or jetpt[idx_jet] == jetpt[1]:
                    lead_bjet_p4.SetPtEtaPhiE(jetpt[idx_jet],jeteta[idx_jet],jetphi[idx_jet],jete[idx_jet])
                    sub_bjet_p4.SetPtEtaPhiE(jetpt[2],jeteta[2],jetphi[2],jete[2])
                else:
                    lead_bjet_p4.SetPtEtaPhiE(jetpt[idx_jet],jeteta[idx_jet],jetphi[idx_jet],jete[idx_jet])
                    sub_bjet_p4.SetPtEtaPhiE(jetpt[1],jeteta[1],jetphi[1],jete[1])
                DeltaR_bjet = lead_bjet_p4.DeltaR(sub_bjet_p4)
            else:
                DeltaR_bjet = 1.0



        if forward == True:
            if len(jetpt_btag) > 0 and abs(jeteta[idx_jet]) < 2.5 and DeltaR > 1.0 and met_met < 120e3 and tight[idx_ljet] == 1 and jetpt[idx_jet] > 350e3 and leadjetpt[idx_ljet] > 500e3 and tag2017_tight == 1: #2b_tight_Wtagged
                jet_pt_2b_tight_Wtagged.Fill(jetpt[idx_jet]/1000,weight)
                jet_eta_2b_tight_Wtagged.Fill(jeteta[idx_jet],weight)
                jet_phi_2b_tight_Wtagged.Fill(jetphi[idx_jet],weight)
                jet_e_2b_tight_Wtagged.Fill(jete[idx_jet]/1000,weight)
                jet_p4.SetPtEtaPhiE(jetpt[idx_jet],jeteta[idx_jet],jetphi[idx_jet],jete[idx_jet])
                jet_m_2b_tight_Wtagged.Fill(jet_p4.M()/1000,weight)
                jet_n_2b_tight_Wtagged.Fill(jet_pt.size(),weight)
                ljet_pt_2b_tight_Wtagged.Fill(leadjetpt[idx_ljet]/1000,weight)
                ljet_eta_2b_tight_Wtagged.Fill(leadjeteta[idx_ljet],weight)
                ljet_phi_2b_tight_Wtagged.Fill(leadjetphi[idx_ljet],weight)
                ljet_m_2b_tight_Wtagged.Fill(leadjetm[idx_ljet]/1000,weight)
                ljet_e_2b_tight_Wtagged.Fill(leadjete[idx_ljet]/1000,weight)
                ljet_n_2b_tight_Wtagged.Fill(leadjet_pt.size(),weight)
                leadjet_p4.SetPtEtaPhiE(leadjetpt[idx_ljet],leadjeteta[idx_ljet],leadjetphi[idx_ljet],leadjete[idx_ljet])
                VLQ_p4 = ROOT.TLorentzVector()
                VLQ_p4 = leadjet_p4 + jet_p4
                VLQM = VLQ_p4.M()
                DeltaR = leadjet_p4.DeltaR(jet_p4)
                DeltaPhi = leadjet_p4.DeltaPhi(jet_p4)
                VLQM_2b_tight_Wtagged.Fill(VLQM/1000,weight)
                DeltaR_2b_tight_Wtagged.Fill(DeltaR,weight)
                DeltaR_bjet_2b_tight_Wtagged.Fill(DeltaR_bjet,weight)
                DeltaPhi_2b_tight_Wtagged.Fill(DeltaPhi,weight)
                if len(leadjetpt) > 1:
                    sub_ljet_pt_2b_tight_Wtagged.Fill(leadjetpt[idx_subjet]/1000,weight)
                    sub_ljet_eta_2b_tight_Wtagged.Fill(leadjeteta[idx_subjet],weight)
                    sub_ljet_phi_2b_tight_Wtagged.Fill(leadjetphi[idx_subjet],weight)
                    sub_ljet_m_2b_tight_Wtagged.Fill(leadjetm[idx_subjet]/1000,weight)
                    sub_ljet_e_2b_tight_Wtagged.Fill(leadjete[idx_subjet]/1000,weight)
                #jet_pt_nb_tight_Wtagged.Fill(jetpt[idx_jet]/1000,weight)
                #jet_eta_nb_tight_Wtagged.Fill(jeteta[idx_jet],weight)


        

            elif len(jetpt_btag) == 0 and abs(jeteta[idx_jet]) < 2.5 and DeltaR > 1.0 and met_met < 120e3 and tight[idx_ljet] == 1 and jetpt[idx_jet] > 350e3 and leadjetpt[idx_ljet] > 500e3 and tag2017_tight_0b == 1: #0b_tight_Wtagged
                jet_pt_0b_tight_Wtagged.Fill(jetpt[idx_jet]/1000,weight)
                jet_eta_0b_tight_Wtagged.Fill(jeteta[idx_jet],weight)
                jet_phi_0b_tight_Wtagged.Fill(jetphi[idx_jet],weight)
                jet_e_0b_tight_Wtagged.Fill(jete[idx_jet]/1000,weight)
                jet_p4.SetPtEtaPhiE(jetpt[idx_jet],jeteta[idx_jet],jetphi[idx_jet],jete[idx_jet])
                jet_m_0b_tight_Wtagged.Fill(jet_p4.M()/1000,weight)
                jet_n_0b_tight_Wtagged.Fill(jet_pt.size(),weight)
                ljet_pt_0b_tight_Wtagged.Fill(leadjetpt[idx_ljet]/1000,weight)
                ljet_eta_0b_tight_Wtagged.Fill(leadjeteta[idx_ljet],weight)
                ljet_phi_0b_tight_Wtagged.Fill(leadjetphi[idx_ljet],weight)
                ljet_m_0b_tight_Wtagged.Fill(leadjetm[idx_ljet]/1000,weight)
                ljet_e_0b_tight_Wtagged.Fill(leadjete[idx_ljet]/1000,weight)
                ljet_n_0b_tight_Wtagged.Fill(leadjet_pt.size(),weight)
                leadjet_p4.SetPtEtaPhiE(leadjetpt[idx_ljet],leadjeteta[idx_ljet],leadjetphi[idx_ljet],leadjete[idx_ljet])
                VLQ_p4 = ROOT.TLorentzVector()
                VLQ_p4 = leadjet_p4 + jet_p4
                VLQM = VLQ_p4.M()
                DeltaR = leadjet_p4.DeltaR(jet_p4)
                DeltaPhi = leadjet_p4.DeltaPhi(jet_p4)
                VLQM_0b_tight_Wtagged.Fill(VLQM/1000,weight)
                DeltaR_0b_tight_Wtagged.Fill(DeltaR,weight)
                DeltaPhi_0b_tight_Wtagged.Fill(DeltaPhi,weight)
                if len(leadjetpt) > 1:
                    sub_ljet_pt_0b_tight_Wtagged.Fill(leadjetpt[idx_subjet]/1000,weight)
                    sub_ljet_eta_0b_tight_Wtagged.Fill(leadjeteta[idx_subjet],weight)
                    sub_ljet_phi_0b_tight_Wtagged.Fill(leadjetphi[idx_subjet],weight)
                    sub_ljet_m_0b_tight_Wtagged.Fill(leadjetm[idx_subjet]/1000,weight)
                    sub_ljet_e_0b_tight_Wtagged.Fill(leadjete[idx_subjet]/1000,weight)


            elif len(jetpt_btag) > 0 and abs(jeteta[idx_jet]) < 2.5 and DeltaR > 1.0 and met_met < 120e3 and loose[idx_ljet] == 1 and tight[idx_ljet] != 1 and jetpt[idx_jet] > 350e3 and leadjetpt[idx_ljet] > 500e3 and (tag2017_loose == 1 and tag2017_tight != 1): #2b_loose_not_tight_Wtagged
                jet_pt_2b_loose_not_tight_Wtagged.Fill(jetpt[idx_jet]/1000,weight)
                jet_eta_2b_loose_not_tight_Wtagged.Fill(jeteta[idx_jet],weight)
                jet_phi_2b_loose_not_tight_Wtagged.Fill(jetphi[idx_jet],weight)
                jet_e_2b_loose_not_tight_Wtagged.Fill(jete[idx_jet]/1000,weight)
                jet_p4.SetPtEtaPhiE(jetpt[idx_jet],jeteta[idx_jet],jetphi[idx_jet],jete[idx_jet])
                jet_m_2b_loose_not_tight_Wtagged.Fill(jet_p4.M()/1000,weight)
                jet_n_2b_loose_not_tight_Wtagged.Fill(jet_pt.size(),weight)
                ljet_pt_2b_loose_not_tight_Wtagged.Fill(leadjetpt[idx_ljet]/1000,weight)
                ljet_eta_2b_loose_not_tight_Wtagged.Fill(leadjeteta[idx_ljet],weight)
                ljet_phi_2b_loose_not_tight_Wtagged.Fill(leadjetphi[idx_ljet],weight)
                ljet_m_2b_loose_not_tight_Wtagged.Fill(leadjetm[idx_ljet]/1000,weight)
                ljet_e_2b_loose_not_tight_Wtagged.Fill(leadjete[idx_ljet]/1000,weight)
                ljet_n_2b_loose_not_tight_Wtagged.Fill(leadjet_pt.size(),weight)
                leadjet_p4.SetPtEtaPhiE(leadjetpt[idx_ljet],leadjeteta[idx_ljet],leadjetphi[idx_ljet],leadjete[idx_ljet])
                VLQ_p4 = ROOT.TLorentzVector()
                VLQ_p4 = leadjet_p4 + jet_p4
                VLQM = VLQ_p4.M()
                DeltaR = leadjet_p4.DeltaR(jet_p4)
                DeltaPhi = leadjet_p4.DeltaPhi(jet_p4)
                VLQM_2b_loose_not_tight_Wtagged.Fill(VLQM/1000,weight)
                DeltaR_2b_loose_not_tight_Wtagged.Fill(DeltaR,weight)
                DeltaR_bjet_2b_loose_not_tight_Wtagged.Fill(DeltaR_bjet,weight)
                DeltaPhi_2b_loose_not_tight_Wtagged.Fill(DeltaPhi,weight)
                if len(leadjetpt) > 1:
                    sub_ljet_pt_2b_loose_not_tight_Wtagged.Fill(leadjetpt[idx_subjet]/1000,weight)
                    sub_ljet_eta_2b_loose_not_tight_Wtagged.Fill(leadjeteta[idx_subjet],weight)
                    sub_ljet_phi_2b_loose_not_tight_Wtagged.Fill(leadjetphi[idx_subjet],weight)
                    sub_ljet_m_2b_loose_not_tight_Wtagged.Fill(leadjetm[idx_subjet]/1000,weight)
                    sub_ljet_e_2b_loose_not_tight_Wtagged.Fill(leadjete[idx_subjet]/1000,weight)
                #jet_pt_nb_loose_not_tight_Wtagged.Fill(jetpt[idx_jet]/1000,weight)
                #jet_eta_nb_loose_not_tight_Wtagged.Fill(jeteta[idx_jet],weight)
            
        
            elif len(jetpt_btag) == 0 and abs(jeteta[idx_jet]) < 2.5 and DeltaR > 1.0 and met_met < 120e3 and loose[idx_ljet] == 1 and tight[idx_ljet] != 1 and jetpt[idx_jet] > 350e3 and leadjetpt[idx_ljet] > 500e3 and (tag2017_loose_0b == 1 and tag2017_tight_0b != 1): #0b_loose_not_tight_Wtagged
                jet_pt_0b_loose_not_tight_Wtagged.Fill(jetpt[idx_jet]/1000,weight)
                jet_eta_0b_loose_not_tight_Wtagged.Fill(jeteta[idx_jet],weight)
                jet_phi_0b_loose_not_tight_Wtagged.Fill(jetphi[idx_jet],weight)
                jet_e_0b_loose_not_tight_Wtagged.Fill(jete[idx_jet]/1000,weight)
                jet_p4.SetPtEtaPhiE(jetpt[idx_jet],jeteta[idx_jet],jetphi[idx_jet],jete[idx_jet])
                jet_m_0b_loose_not_tight_Wtagged.Fill(jet_p4.M()/1000,weight)
                jet_n_0b_loose_not_tight_Wtagged.Fill(jet_pt.size(),weight)
                ljet_pt_0b_loose_not_tight_Wtagged.Fill(leadjetpt[idx_ljet]/1000,weight)
                ljet_eta_0b_loose_not_tight_Wtagged.Fill(leadjeteta[idx_ljet],weight)
                ljet_phi_0b_loose_not_tight_Wtagged.Fill(leadjetphi[idx_ljet],weight)
                ljet_m_0b_loose_not_tight_Wtagged.Fill(leadjetm[idx_ljet]/1000,weight)
                ljet_e_0b_loose_not_tight_Wtagged.Fill(leadjete[idx_ljet]/1000,weight)
                ljet_n_0b_loose_not_tight_Wtagged.Fill(leadjet_pt.size(),weight)
                leadjet_p4.SetPtEtaPhiE(leadjetpt[idx_ljet],leadjeteta[idx_ljet],leadjetphi[idx_ljet],leadjete[idx_ljet])
                VLQ_p4 = ROOT.TLorentzVector()
                VLQ_p4 = leadjet_p4 + jet_p4
                VLQM = VLQ_p4.M()
                DeltaR = leadjet_p4.DeltaR(jet_p4)
                DeltaPhi = leadjet_p4.DeltaPhi(jet_p4)
                VLQM_0b_loose_not_tight_Wtagged.Fill(VLQM/1000,weight)
                DeltaR_0b_loose_not_tight_Wtagged.Fill(DeltaR,weight)
                DeltaPhi_0b_loose_not_tight_Wtagged.Fill(DeltaPhi,weight)
                if len(leadjetpt) > 1:
                    sub_ljet_pt_0b_loose_not_tight_Wtagged.Fill(leadjetpt[idx_subjet]/1000,weight)
                    sub_ljet_eta_0b_loose_not_tight_Wtagged.Fill(leadjeteta[idx_subjet],weight)
                    sub_ljet_phi_0b_loose_not_tight_Wtagged.Fill(leadjetphi[idx_subjet],weight)
                    sub_ljet_m_0b_loose_not_tight_Wtagged.Fill(leadjetm[idx_subjet]/1000,weight)
                    sub_ljet_e_0b_loose_not_tight_Wtagged.Fill(leadjete[idx_subjet]/1000,weight)
            
            
            elif len(jetpt_btag) > 0 and abs(jeteta[idx_jet]) < 2.5 and DeltaR > 1.0 and met_met < 120e3 and loose[idx_ljet] != 1 and jetpt[idx_jet] > 350e3 and leadjetpt[idx_ljet] > 500e3: #2b_not_loose_Wtagged
                jet_pt_2b_not_loose_Wtagged.Fill(jetpt[idx_jet]/1000,weight)
                jet_eta_2b_not_loose_Wtagged.Fill(jeteta[idx_jet],weight)
                jet_phi_2b_not_loose_Wtagged.Fill(jetphi[idx_jet],weight)
                jet_e_2b_not_loose_Wtagged.Fill(jete[idx_jet]/1000,weight)
                jet_p4.SetPtEtaPhiE(jetpt[idx_jet],jeteta[idx_jet],jetphi[idx_jet],jete[idx_jet])
                jet_m_2b_not_loose_Wtagged.Fill(jet_p4.M()/1000,weight)
                jet_n_2b_not_loose_Wtagged.Fill(jet_pt.size(),weight)
                ljet_pt_2b_not_loose_Wtagged.Fill(leadjetpt[idx_ljet]/1000,weight)
                ljet_eta_2b_not_loose_Wtagged.Fill(leadjeteta[idx_ljet],weight)
                ljet_phi_2b_not_loose_Wtagged.Fill(leadjetphi[idx_ljet],weight)
                ljet_m_2b_not_loose_Wtagged.Fill(leadjetm[idx_ljet]/1000,weight)
                ljet_e_2b_not_loose_Wtagged.Fill(leadjete[idx_ljet]/1000,weight)
                ljet_n_2b_not_loose_Wtagged.Fill(leadjet_pt.size(),weight)
                leadjet_p4.SetPtEtaPhiE(leadjetpt[idx_ljet],leadjeteta[idx_ljet],leadjetphi[idx_ljet],leadjete[idx_ljet])
                VLQ_p4 = ROOT.TLorentzVector()
                VLQ_p4 = leadjet_p4 + jet_p4
                VLQM = VLQ_p4.M()
                DeltaR = leadjet_p4.DeltaR(jet_p4)
                DeltaPhi = leadjet_p4.DeltaPhi(jet_p4)
                VLQM_2b_not_loose_Wtagged.Fill(VLQM/1000,weight)
                DeltaR_2b_not_loose_Wtagged.Fill(DeltaR,weight)
                DeltaR_bjet_2b_not_loose_Wtagged.Fill(DeltaR_bjet,weight)
                DeltaPhi_2b_not_loose_Wtagged.Fill(DeltaPhi,weight)
                if len(leadjetpt) > 1:
                    sub_ljet_pt_2b_not_loose_Wtagged.Fill(leadjetpt[idx_subjet]/1000,weight)
                    sub_ljet_eta_2b_not_loose_Wtagged.Fill(leadjeteta[idx_subjet],weight)
                    sub_ljet_phi_2b_not_loose_Wtagged.Fill(leadjetphi[idx_subjet],weight)
                    sub_ljet_m_2b_not_loose_Wtagged.Fill(leadjetm[idx_subjet]/1000,weight)
                    sub_ljet_e_2b_not_loose_Wtagged.Fill(leadjete[idx_subjet]/1000,weight)
            

        
            elif len(jetpt_btag) == 0 and abs(jeteta[idx_jet]) < 2.5 and DeltaR > 1.0 and met_met < 120e3 and loose[idx_ljet] != 1 and jetpt[idx_jet] > 350e3 and leadjetpt[idx_ljet] > 500e3: #0b_not_loose_Wtagged
                jet_pt_0b_not_loose_Wtagged.Fill(jetpt[idx_jet]/1000,weight)
                jet_eta_0b_not_loose_Wtagged.Fill(jeteta[idx_jet],weight)
                jet_phi_0b_not_loose_Wtagged.Fill(jetphi[idx_jet],weight)
                jet_e_0b_not_loose_Wtagged.Fill(jete[idx_jet]/1000,weight)
                jet_p4.SetPtEtaPhiE(jetpt[idx_jet],jeteta[idx_jet],jetphi[idx_jet],jete[idx_jet])
                jet_m_0b_not_loose_Wtagged.Fill(jet_p4.M()/1000,weight)
                jet_n_0b_not_loose_Wtagged.Fill(jet_pt.size(),weight)
                ljet_pt_0b_not_loose_Wtagged.Fill(leadjetpt[idx_ljet]/1000,weight)
                ljet_eta_0b_not_loose_Wtagged.Fill(leadjeteta[idx_ljet],weight)
                ljet_phi_0b_not_loose_Wtagged.Fill(leadjetphi[idx_ljet],weight)
                ljet_m_0b_not_loose_Wtagged.Fill(leadjetm[idx_ljet]/1000,weight)
                ljet_e_0b_not_loose_Wtagged.Fill(leadjete[idx_ljet]/1000,weight)
                ljet_n_0b_not_loose_Wtagged.Fill(leadjet_pt.size(),weight)
                leadjet_p4.SetPtEtaPhiE(leadjetpt[idx_ljet],leadjeteta[idx_ljet],leadjetphi[idx_ljet],leadjete[idx_ljet])
                VLQ_p4 = ROOT.TLorentzVector()
                VLQ_p4 = leadjet_p4 + jet_p4
                VLQM = VLQ_p4.M()
                DeltaR = leadjet_p4.DeltaR(jet_p4)
                DeltaPhi = leadjet_p4.DeltaPhi(jet_p4)
                VLQM_0b_not_loose_Wtagged.Fill(VLQM/1000,weight)
                DeltaR_0b_not_loose_Wtagged.Fill(DeltaR,weight)
                DeltaPhi_0b_not_loose_Wtagged.Fill(DeltaPhi,weight)
                if len(leadjetpt) > 1:
                    sub_ljet_pt_0b_not_loose_Wtagged.Fill(leadjetpt[idx_subjet]/1000,weight)
                    sub_ljet_eta_0b_not_loose_Wtagged.Fill(leadjeteta[idx_subjet],weight)
                    sub_ljet_phi_0b_not_loose_Wtagged.Fill(leadjetphi[idx_subjet],weight)
                    sub_ljet_m_0b_not_loose_Wtagged.Fill(leadjetm[idx_subjet]/1000,weight)
                    sub_ljet_e_0b_not_loose_Wtagged.Fill(leadjete[idx_subjet]/1000,weight)

            else:
                continue
        else:
            continue

        
    
    
	#Handling Overflow bins
    ljet_pt_2b_tight_Wtagged.SetBinContent(ljet_pt_2b_tight_Wtagged.GetNbinsX(), ljet_pt_2b_tight_Wtagged.GetBinContent(ljet_pt_2b_tight_Wtagged.GetNbinsX()) + ljet_pt_2b_tight_Wtagged.GetBinContent(ljet_pt_2b_tight_Wtagged.GetNbinsX()+1))
    ljet_m_2b_tight_Wtagged.SetBinContent(ljet_m_2b_tight_Wtagged.GetNbinsX(), ljet_m_2b_tight_Wtagged.GetBinContent(ljet_m_2b_tight_Wtagged.GetNbinsX()) + ljet_m_2b_tight_Wtagged.GetBinContent(ljet_m_2b_tight_Wtagged.GetNbinsX()+1))
    ljet_e_2b_tight_Wtagged.SetBinContent(ljet_e_2b_tight_Wtagged.GetNbinsX(), ljet_e_2b_tight_Wtagged.GetBinContent(ljet_e_2b_tight_Wtagged.GetNbinsX()) + ljet_e_2b_tight_Wtagged.GetBinContent(ljet_e_2b_tight_Wtagged.GetNbinsX()+1))
    ljet_n_2b_tight_Wtagged.SetBinContent(ljet_n_2b_tight_Wtagged.GetNbinsX(), ljet_n_2b_tight_Wtagged.GetBinContent(ljet_n_2b_tight_Wtagged.GetNbinsX()) + ljet_n_2b_tight_Wtagged.GetBinContent(ljet_n_2b_tight_Wtagged.GetNbinsX()+1))
    jet_pt_2b_tight_Wtagged.SetBinContent(jet_pt_2b_tight_Wtagged.GetNbinsX(), jet_pt_2b_tight_Wtagged.GetBinContent(jet_pt_2b_tight_Wtagged.GetNbinsX()) + jet_pt_2b_tight_Wtagged.GetBinContent(jet_pt_2b_tight_Wtagged.GetNbinsX()+1))
    jet_m_2b_tight_Wtagged.SetBinContent(jet_m_2b_tight_Wtagged.GetNbinsX(), jet_m_2b_tight_Wtagged.GetBinContent(jet_m_2b_tight_Wtagged.GetNbinsX()) + jet_m_2b_tight_Wtagged.GetBinContent(jet_m_2b_tight_Wtagged.GetNbinsX()+1))
    jet_e_2b_tight_Wtagged.SetBinContent(jet_e_2b_tight_Wtagged.GetNbinsX(), jet_e_2b_tight_Wtagged.GetBinContent(jet_e_2b_tight_Wtagged.GetNbinsX()) + jet_e_2b_tight_Wtagged.GetBinContent(jet_e_2b_tight_Wtagged.GetNbinsX()+1))
    jet_n_2b_tight_Wtagged.SetBinContent(jet_n_2b_tight_Wtagged.GetNbinsX(), jet_n_2b_tight_Wtagged.GetBinContent(jet_n_2b_tight_Wtagged.GetNbinsX()) + jet_n_2b_tight_Wtagged.GetBinContent(jet_n_2b_tight_Wtagged.GetNbinsX()+1))
    sub_ljet_pt_2b_tight_Wtagged.SetBinContent(sub_ljet_pt_2b_tight_Wtagged.GetNbinsX(), sub_ljet_pt_2b_tight_Wtagged.GetBinContent(sub_ljet_pt_2b_tight_Wtagged.GetNbinsX()) + sub_ljet_pt_2b_tight_Wtagged.GetBinContent(sub_ljet_pt_2b_tight_Wtagged.GetNbinsX()+1))
    sub_ljet_m_2b_tight_Wtagged.SetBinContent(sub_ljet_m_2b_tight_Wtagged.GetNbinsX(), sub_ljet_m_2b_tight_Wtagged.GetBinContent(sub_ljet_m_2b_tight_Wtagged.GetNbinsX()) + sub_ljet_m_2b_tight_Wtagged.GetBinContent(sub_ljet_m_2b_tight_Wtagged.GetNbinsX()+1))
    sub_ljet_e_2b_tight_Wtagged.SetBinContent(sub_ljet_e_2b_tight_Wtagged.GetNbinsX(), sub_ljet_e_2b_tight_Wtagged.GetBinContent(sub_ljet_e_2b_tight_Wtagged.GetNbinsX()) + sub_ljet_e_2b_tight_Wtagged.GetBinContent(sub_ljet_e_2b_tight_Wtagged.GetNbinsX()+1))
    VLQM_2b_tight_Wtagged.SetBinContent(VLQM_2b_tight_Wtagged.GetNbinsX(), VLQM_2b_tight_Wtagged.GetBinContent(VLQM_2b_tight_Wtagged.GetNbinsX()) + VLQM_2b_tight_Wtagged.GetBinContent(VLQM_2b_tight_Wtagged.GetNbinsX()+1))
    DeltaR_2b_tight_Wtagged.SetBinContent(DeltaR_2b_tight_Wtagged.GetNbinsX(), DeltaR_2b_tight_Wtagged.GetBinContent(DeltaR_2b_tight_Wtagged.GetNbinsX()) + DeltaR_2b_tight_Wtagged.GetBinContent(DeltaR_2b_tight_Wtagged.GetNbinsX()+1))
    DeltaR_bjet_2b_tight_Wtagged.SetBinContent(DeltaR_bjet_2b_tight_Wtagged.GetNbinsX(), DeltaR_bjet_2b_tight_Wtagged.GetBinContent(DeltaR_bjet_2b_tight_Wtagged.GetNbinsX()) + DeltaR_bjet_2b_tight_Wtagged.GetBinContent(DeltaR_bjet_2b_tight_Wtagged.GetNbinsX()+1))
    DeltaPhi_2b_tight_Wtagged.SetBinContent(DeltaPhi_2b_tight_Wtagged.GetNbinsX(), DeltaPhi_2b_tight_Wtagged.GetBinContent(DeltaPhi_2b_tight_Wtagged.GetNbinsX()) + DeltaPhi_2b_tight_Wtagged.GetBinContent(DeltaPhi_2b_tight_Wtagged.GetNbinsX()+1))


    ljet_pt_0b_tight_Wtagged.SetBinContent(ljet_pt_0b_tight_Wtagged.GetNbinsX(), ljet_pt_0b_tight_Wtagged.GetBinContent(ljet_pt_0b_tight_Wtagged.GetNbinsX()) + ljet_pt_0b_tight_Wtagged.GetBinContent(ljet_pt_0b_tight_Wtagged.GetNbinsX()+1))
    ljet_m_0b_tight_Wtagged.SetBinContent(ljet_m_0b_tight_Wtagged.GetNbinsX(), ljet_m_0b_tight_Wtagged.GetBinContent(ljet_m_0b_tight_Wtagged.GetNbinsX()) + ljet_m_0b_tight_Wtagged.GetBinContent(ljet_m_0b_tight_Wtagged.GetNbinsX()+1))
    ljet_e_0b_tight_Wtagged.SetBinContent(ljet_e_0b_tight_Wtagged.GetNbinsX(), ljet_e_0b_tight_Wtagged.GetBinContent(ljet_e_0b_tight_Wtagged.GetNbinsX()) + ljet_e_0b_tight_Wtagged.GetBinContent(ljet_e_0b_tight_Wtagged.GetNbinsX()+1))
    ljet_n_0b_tight_Wtagged.SetBinContent(ljet_n_0b_tight_Wtagged.GetNbinsX(), ljet_n_0b_tight_Wtagged.GetBinContent(ljet_n_0b_tight_Wtagged.GetNbinsX()) + ljet_n_0b_tight_Wtagged.GetBinContent(ljet_n_0b_tight_Wtagged.GetNbinsX()+1))
    jet_pt_0b_tight_Wtagged.SetBinContent(jet_pt_0b_tight_Wtagged.GetNbinsX(), jet_pt_0b_tight_Wtagged.GetBinContent(jet_pt_0b_tight_Wtagged.GetNbinsX()) + jet_pt_0b_tight_Wtagged.GetBinContent(jet_pt_0b_tight_Wtagged.GetNbinsX()+1))
    jet_m_0b_tight_Wtagged.SetBinContent(jet_m_0b_tight_Wtagged.GetNbinsX(), jet_m_0b_tight_Wtagged.GetBinContent(jet_m_0b_tight_Wtagged.GetNbinsX()) + jet_m_0b_tight_Wtagged.GetBinContent(jet_m_0b_tight_Wtagged.GetNbinsX()+1))
    jet_e_0b_tight_Wtagged.SetBinContent(jet_e_0b_tight_Wtagged.GetNbinsX(), jet_e_0b_tight_Wtagged.GetBinContent(jet_e_0b_tight_Wtagged.GetNbinsX()) + jet_e_0b_tight_Wtagged.GetBinContent(jet_e_0b_tight_Wtagged.GetNbinsX()+1))
    jet_n_0b_tight_Wtagged.SetBinContent(jet_n_0b_tight_Wtagged.GetNbinsX(), jet_n_0b_tight_Wtagged.GetBinContent(jet_n_0b_tight_Wtagged.GetNbinsX()) + jet_n_0b_tight_Wtagged.GetBinContent(jet_n_0b_tight_Wtagged.GetNbinsX()+1))
    sub_ljet_pt_0b_tight_Wtagged.SetBinContent(sub_ljet_pt_0b_tight_Wtagged.GetNbinsX(), sub_ljet_pt_0b_tight_Wtagged.GetBinContent(sub_ljet_pt_0b_tight_Wtagged.GetNbinsX()) + sub_ljet_pt_0b_tight_Wtagged.GetBinContent(sub_ljet_pt_0b_tight_Wtagged.GetNbinsX()+1))
    sub_ljet_m_0b_tight_Wtagged.SetBinContent(sub_ljet_m_0b_tight_Wtagged.GetNbinsX(), sub_ljet_m_0b_tight_Wtagged.GetBinContent(sub_ljet_m_0b_tight_Wtagged.GetNbinsX()) + sub_ljet_m_0b_tight_Wtagged.GetBinContent(sub_ljet_m_0b_tight_Wtagged.GetNbinsX()+1))
    sub_ljet_e_0b_tight_Wtagged.SetBinContent(sub_ljet_e_0b_tight_Wtagged.GetNbinsX(), sub_ljet_e_0b_tight_Wtagged.GetBinContent(sub_ljet_e_0b_tight_Wtagged.GetNbinsX()) + sub_ljet_e_0b_tight_Wtagged.GetBinContent(sub_ljet_e_0b_tight_Wtagged.GetNbinsX()+1))
    VLQM_0b_tight_Wtagged.SetBinContent(VLQM_0b_tight_Wtagged.GetNbinsX(), VLQM_0b_tight_Wtagged.GetBinContent(VLQM_0b_tight_Wtagged.GetNbinsX()) + VLQM_0b_tight_Wtagged.GetBinContent(VLQM_0b_tight_Wtagged.GetNbinsX()+1))
    DeltaR_0b_tight_Wtagged.SetBinContent(DeltaR_0b_tight_Wtagged.GetNbinsX(), DeltaR_0b_tight_Wtagged.GetBinContent(DeltaR_0b_tight_Wtagged.GetNbinsX()) + DeltaR_0b_tight_Wtagged.GetBinContent(DeltaR_0b_tight_Wtagged.GetNbinsX()+1))
    DeltaPhi_0b_tight_Wtagged.SetBinContent(DeltaPhi_0b_tight_Wtagged.GetNbinsX(), DeltaPhi_0b_tight_Wtagged.GetBinContent(DeltaPhi_0b_tight_Wtagged.GetNbinsX()) + DeltaPhi_0b_tight_Wtagged.GetBinContent(DeltaPhi_0b_tight_Wtagged.GetNbinsX()+1))
    
    
    ljet_pt_2b_loose_not_tight_Wtagged.SetBinContent(ljet_pt_2b_loose_not_tight_Wtagged.GetNbinsX(), ljet_pt_2b_loose_not_tight_Wtagged.GetBinContent(ljet_pt_2b_loose_not_tight_Wtagged.GetNbinsX()) + ljet_pt_2b_loose_not_tight_Wtagged.GetBinContent(ljet_pt_2b_loose_not_tight_Wtagged.GetNbinsX()+1))
    ljet_m_2b_loose_not_tight_Wtagged.SetBinContent(ljet_m_2b_loose_not_tight_Wtagged.GetNbinsX(), ljet_m_2b_loose_not_tight_Wtagged.GetBinContent(ljet_m_2b_loose_not_tight_Wtagged.GetNbinsX()) + ljet_m_2b_loose_not_tight_Wtagged.GetBinContent(ljet_m_2b_loose_not_tight_Wtagged.GetNbinsX()+1))
    ljet_e_2b_loose_not_tight_Wtagged.SetBinContent(ljet_e_2b_loose_not_tight_Wtagged.GetNbinsX(), ljet_e_2b_loose_not_tight_Wtagged.GetBinContent(ljet_e_2b_loose_not_tight_Wtagged.GetNbinsX()) + ljet_e_2b_loose_not_tight_Wtagged.GetBinContent(ljet_e_2b_loose_not_tight_Wtagged.GetNbinsX()+1))
    ljet_n_2b_loose_not_tight_Wtagged.SetBinContent(ljet_n_2b_loose_not_tight_Wtagged.GetNbinsX(), ljet_n_2b_loose_not_tight_Wtagged.GetBinContent(ljet_n_2b_loose_not_tight_Wtagged.GetNbinsX()) + ljet_n_2b_loose_not_tight_Wtagged.GetBinContent(ljet_n_2b_loose_not_tight_Wtagged.GetNbinsX()+1))
    jet_pt_2b_loose_not_tight_Wtagged.SetBinContent(jet_pt_2b_loose_not_tight_Wtagged.GetNbinsX(), jet_pt_2b_loose_not_tight_Wtagged.GetBinContent(jet_pt_2b_loose_not_tight_Wtagged.GetNbinsX()) + jet_pt_2b_loose_not_tight_Wtagged.GetBinContent(jet_pt_2b_loose_not_tight_Wtagged.GetNbinsX()+1))
    jet_m_2b_loose_not_tight_Wtagged.SetBinContent(jet_m_2b_loose_not_tight_Wtagged.GetNbinsX(), jet_m_2b_loose_not_tight_Wtagged.GetBinContent(jet_m_2b_loose_not_tight_Wtagged.GetNbinsX()) + jet_m_2b_loose_not_tight_Wtagged.GetBinContent(jet_m_2b_loose_not_tight_Wtagged.GetNbinsX()+1))
    jet_e_2b_loose_not_tight_Wtagged.SetBinContent(jet_e_2b_loose_not_tight_Wtagged.GetNbinsX(), jet_e_2b_loose_not_tight_Wtagged.GetBinContent(jet_e_2b_loose_not_tight_Wtagged.GetNbinsX()) + jet_e_2b_loose_not_tight_Wtagged.GetBinContent(jet_e_2b_loose_not_tight_Wtagged.GetNbinsX()+1))
    jet_n_2b_loose_not_tight_Wtagged.SetBinContent(jet_n_2b_loose_not_tight_Wtagged.GetNbinsX(), jet_n_2b_loose_not_tight_Wtagged.GetBinContent(jet_n_2b_loose_not_tight_Wtagged.GetNbinsX()) + jet_n_2b_loose_not_tight_Wtagged.GetBinContent(jet_n_2b_loose_not_tight_Wtagged.GetNbinsX()+1))
    sub_ljet_pt_2b_loose_not_tight_Wtagged.SetBinContent(sub_ljet_pt_2b_loose_not_tight_Wtagged.GetNbinsX(), sub_ljet_pt_2b_loose_not_tight_Wtagged.GetBinContent(sub_ljet_pt_2b_loose_not_tight_Wtagged.GetNbinsX()) + sub_ljet_pt_2b_loose_not_tight_Wtagged.GetBinContent(sub_ljet_pt_2b_loose_not_tight_Wtagged.GetNbinsX()+1))
    sub_ljet_m_2b_loose_not_tight_Wtagged.SetBinContent(sub_ljet_m_2b_loose_not_tight_Wtagged.GetNbinsX(), sub_ljet_m_2b_loose_not_tight_Wtagged.GetBinContent(sub_ljet_m_2b_loose_not_tight_Wtagged.GetNbinsX()) + sub_ljet_m_2b_loose_not_tight_Wtagged.GetBinContent(sub_ljet_m_2b_loose_not_tight_Wtagged.GetNbinsX()+1))
    sub_ljet_e_2b_loose_not_tight_Wtagged.SetBinContent(sub_ljet_e_2b_loose_not_tight_Wtagged.GetNbinsX(), sub_ljet_e_2b_loose_not_tight_Wtagged.GetBinContent(sub_ljet_e_2b_loose_not_tight_Wtagged.GetNbinsX()) + sub_ljet_e_2b_loose_not_tight_Wtagged.GetBinContent(sub_ljet_e_2b_loose_not_tight_Wtagged.GetNbinsX()+1))
    VLQM_2b_loose_not_tight_Wtagged.SetBinContent(VLQM_2b_loose_not_tight_Wtagged.GetNbinsX(), VLQM_2b_loose_not_tight_Wtagged.GetBinContent(VLQM_2b_loose_not_tight_Wtagged.GetNbinsX()) + VLQM_2b_loose_not_tight_Wtagged.GetBinContent(VLQM_2b_loose_not_tight_Wtagged.GetNbinsX()+1))
    DeltaR_2b_loose_not_tight_Wtagged.SetBinContent(DeltaR_2b_loose_not_tight_Wtagged.GetNbinsX(), DeltaR_2b_loose_not_tight_Wtagged.GetBinContent(DeltaR_2b_loose_not_tight_Wtagged.GetNbinsX()) + DeltaR_2b_loose_not_tight_Wtagged.GetBinContent(DeltaR_2b_loose_not_tight_Wtagged.GetNbinsX()+1))
    DeltaR_bjet_2b_loose_not_tight_Wtagged.SetBinContent(DeltaR_bjet_2b_loose_not_tight_Wtagged.GetNbinsX(), DeltaR_bjet_2b_loose_not_tight_Wtagged.GetBinContent(DeltaR_bjet_2b_loose_not_tight_Wtagged.GetNbinsX()) + DeltaR_bjet_2b_loose_not_tight_Wtagged.GetBinContent(DeltaR_bjet_2b_loose_not_tight_Wtagged.GetNbinsX()+1))
    DeltaPhi_2b_loose_not_tight_Wtagged.SetBinContent(DeltaPhi_2b_loose_not_tight_Wtagged.GetNbinsX(), DeltaPhi_2b_loose_not_tight_Wtagged.GetBinContent(DeltaPhi_2b_loose_not_tight_Wtagged.GetNbinsX()) + DeltaPhi_2b_loose_not_tight_Wtagged.GetBinContent(DeltaPhi_2b_loose_not_tight_Wtagged.GetNbinsX()+1))


    ljet_pt_0b_loose_not_tight_Wtagged.SetBinContent(ljet_pt_0b_loose_not_tight_Wtagged.GetNbinsX(), ljet_pt_0b_loose_not_tight_Wtagged.GetBinContent(ljet_pt_0b_loose_not_tight_Wtagged.GetNbinsX()) + ljet_pt_0b_loose_not_tight_Wtagged.GetBinContent(ljet_pt_0b_loose_not_tight_Wtagged.GetNbinsX()+1))
    ljet_m_0b_loose_not_tight_Wtagged.SetBinContent(ljet_m_0b_loose_not_tight_Wtagged.GetNbinsX(), ljet_m_0b_loose_not_tight_Wtagged.GetBinContent(ljet_m_0b_loose_not_tight_Wtagged.GetNbinsX()) + ljet_m_0b_loose_not_tight_Wtagged.GetBinContent(ljet_m_0b_loose_not_tight_Wtagged.GetNbinsX()+1))
    ljet_e_0b_loose_not_tight_Wtagged.SetBinContent(ljet_e_0b_loose_not_tight_Wtagged.GetNbinsX(), ljet_e_0b_loose_not_tight_Wtagged.GetBinContent(ljet_e_0b_loose_not_tight_Wtagged.GetNbinsX()) + ljet_e_0b_loose_not_tight_Wtagged.GetBinContent(ljet_e_0b_loose_not_tight_Wtagged.GetNbinsX()+1))
    ljet_n_0b_loose_not_tight_Wtagged.SetBinContent(ljet_n_0b_loose_not_tight_Wtagged.GetNbinsX(), ljet_n_0b_loose_not_tight_Wtagged.GetBinContent(ljet_n_0b_loose_not_tight_Wtagged.GetNbinsX()) + ljet_n_0b_loose_not_tight_Wtagged.GetBinContent(ljet_n_0b_loose_not_tight_Wtagged.GetNbinsX()+1))
    jet_pt_0b_loose_not_tight_Wtagged.SetBinContent(jet_pt_0b_loose_not_tight_Wtagged.GetNbinsX(), jet_pt_0b_loose_not_tight_Wtagged.GetBinContent(jet_pt_0b_loose_not_tight_Wtagged.GetNbinsX()) + jet_pt_0b_loose_not_tight_Wtagged.GetBinContent(jet_pt_0b_loose_not_tight_Wtagged.GetNbinsX()+1))
    jet_m_0b_loose_not_tight_Wtagged.SetBinContent(jet_m_0b_loose_not_tight_Wtagged.GetNbinsX(), jet_m_0b_loose_not_tight_Wtagged.GetBinContent(jet_m_0b_loose_not_tight_Wtagged.GetNbinsX()) + jet_m_0b_loose_not_tight_Wtagged.GetBinContent(jet_m_0b_loose_not_tight_Wtagged.GetNbinsX()+1))
    jet_e_0b_loose_not_tight_Wtagged.SetBinContent(jet_e_0b_loose_not_tight_Wtagged.GetNbinsX(), jet_e_0b_loose_not_tight_Wtagged.GetBinContent(jet_e_0b_loose_not_tight_Wtagged.GetNbinsX()) + jet_e_0b_loose_not_tight_Wtagged.GetBinContent(jet_e_0b_loose_not_tight_Wtagged.GetNbinsX()+1))
    jet_n_0b_loose_not_tight_Wtagged.SetBinContent(jet_n_0b_loose_not_tight_Wtagged.GetNbinsX(), jet_n_0b_loose_not_tight_Wtagged.GetBinContent(jet_n_0b_loose_not_tight_Wtagged.GetNbinsX()) + jet_n_0b_loose_not_tight_Wtagged.GetBinContent(jet_n_0b_loose_not_tight_Wtagged.GetNbinsX()+1))
    sub_ljet_pt_0b_loose_not_tight_Wtagged.SetBinContent(sub_ljet_pt_0b_loose_not_tight_Wtagged.GetNbinsX(), sub_ljet_pt_0b_loose_not_tight_Wtagged.GetBinContent(sub_ljet_pt_0b_loose_not_tight_Wtagged.GetNbinsX()) + sub_ljet_pt_0b_loose_not_tight_Wtagged.GetBinContent(sub_ljet_pt_0b_loose_not_tight_Wtagged.GetNbinsX()+1))
    sub_ljet_m_0b_loose_not_tight_Wtagged.SetBinContent(sub_ljet_m_0b_loose_not_tight_Wtagged.GetNbinsX(), sub_ljet_m_0b_loose_not_tight_Wtagged.GetBinContent(sub_ljet_m_0b_loose_not_tight_Wtagged.GetNbinsX()) + sub_ljet_m_0b_loose_not_tight_Wtagged.GetBinContent(sub_ljet_m_0b_loose_not_tight_Wtagged.GetNbinsX()+1))
    sub_ljet_e_0b_loose_not_tight_Wtagged.SetBinContent(sub_ljet_e_0b_loose_not_tight_Wtagged.GetNbinsX(), sub_ljet_e_0b_loose_not_tight_Wtagged.GetBinContent(sub_ljet_e_0b_loose_not_tight_Wtagged.GetNbinsX()) + sub_ljet_e_0b_loose_not_tight_Wtagged.GetBinContent(sub_ljet_e_0b_loose_not_tight_Wtagged.GetNbinsX()+1))
    VLQM_0b_loose_not_tight_Wtagged.SetBinContent(VLQM_0b_loose_not_tight_Wtagged.GetNbinsX(), VLQM_0b_loose_not_tight_Wtagged.GetBinContent(VLQM_0b_loose_not_tight_Wtagged.GetNbinsX()) + VLQM_0b_loose_not_tight_Wtagged.GetBinContent(VLQM_0b_loose_not_tight_Wtagged.GetNbinsX()+1))
    DeltaR_0b_loose_not_tight_Wtagged.SetBinContent(DeltaR_0b_loose_not_tight_Wtagged.GetNbinsX(), DeltaR_0b_loose_not_tight_Wtagged.GetBinContent(DeltaR_0b_loose_not_tight_Wtagged.GetNbinsX()) + DeltaR_0b_loose_not_tight_Wtagged.GetBinContent(DeltaR_0b_loose_not_tight_Wtagged.GetNbinsX()+1))
    DeltaPhi_0b_loose_not_tight_Wtagged.SetBinContent(DeltaPhi_0b_loose_not_tight_Wtagged.GetNbinsX(), DeltaPhi_0b_loose_not_tight_Wtagged.GetBinContent(DeltaPhi_0b_loose_not_tight_Wtagged.GetNbinsX()) + DeltaPhi_0b_loose_not_tight_Wtagged.GetBinContent(DeltaPhi_0b_loose_not_tight_Wtagged.GetNbinsX()+1))
    
    
    ljet_pt_2b_not_loose_Wtagged.SetBinContent(ljet_pt_2b_not_loose_Wtagged.GetNbinsX(), ljet_pt_2b_not_loose_Wtagged.GetBinContent(ljet_pt_2b_not_loose_Wtagged.GetNbinsX()) + ljet_pt_2b_not_loose_Wtagged.GetBinContent(ljet_pt_2b_not_loose_Wtagged.GetNbinsX()+1))
    ljet_m_2b_not_loose_Wtagged.SetBinContent(ljet_m_2b_not_loose_Wtagged.GetNbinsX(), ljet_m_2b_not_loose_Wtagged.GetBinContent(ljet_m_2b_not_loose_Wtagged.GetNbinsX()) + ljet_m_2b_not_loose_Wtagged.GetBinContent(ljet_m_2b_not_loose_Wtagged.GetNbinsX()+1))
    ljet_e_2b_not_loose_Wtagged.SetBinContent(ljet_e_2b_not_loose_Wtagged.GetNbinsX(), ljet_e_2b_not_loose_Wtagged.GetBinContent(ljet_e_2b_not_loose_Wtagged.GetNbinsX()) + ljet_e_2b_not_loose_Wtagged.GetBinContent(ljet_e_2b_not_loose_Wtagged.GetNbinsX()+1))
    ljet_n_2b_not_loose_Wtagged.SetBinContent(ljet_n_2b_not_loose_Wtagged.GetNbinsX(), ljet_n_2b_not_loose_Wtagged.GetBinContent(ljet_n_2b_not_loose_Wtagged.GetNbinsX()) + ljet_n_2b_not_loose_Wtagged.GetBinContent(ljet_n_2b_not_loose_Wtagged.GetNbinsX()+1))
    jet_pt_2b_not_loose_Wtagged.SetBinContent(jet_pt_2b_not_loose_Wtagged.GetNbinsX(), jet_pt_2b_not_loose_Wtagged.GetBinContent(jet_pt_2b_not_loose_Wtagged.GetNbinsX()) + jet_pt_2b_not_loose_Wtagged.GetBinContent(jet_pt_2b_not_loose_Wtagged.GetNbinsX()+1))
    jet_m_2b_not_loose_Wtagged.SetBinContent(jet_m_2b_not_loose_Wtagged.GetNbinsX(), jet_m_2b_not_loose_Wtagged.GetBinContent(jet_m_2b_not_loose_Wtagged.GetNbinsX()) + jet_m_2b_not_loose_Wtagged.GetBinContent(jet_m_2b_not_loose_Wtagged.GetNbinsX()+1))
    jet_e_2b_not_loose_Wtagged.SetBinContent(jet_e_2b_not_loose_Wtagged.GetNbinsX(), jet_e_2b_not_loose_Wtagged.GetBinContent(jet_e_2b_not_loose_Wtagged.GetNbinsX()) + jet_e_2b_not_loose_Wtagged.GetBinContent(jet_e_2b_not_loose_Wtagged.GetNbinsX()+1))
    jet_n_2b_not_loose_Wtagged.SetBinContent(jet_n_2b_not_loose_Wtagged.GetNbinsX(), jet_n_2b_not_loose_Wtagged.GetBinContent(jet_n_2b_not_loose_Wtagged.GetNbinsX()) + jet_n_2b_not_loose_Wtagged.GetBinContent(jet_n_2b_not_loose_Wtagged.GetNbinsX()+1))
    sub_ljet_pt_2b_not_loose_Wtagged.SetBinContent(sub_ljet_pt_2b_not_loose_Wtagged.GetNbinsX(), sub_ljet_pt_2b_not_loose_Wtagged.GetBinContent(sub_ljet_pt_2b_not_loose_Wtagged.GetNbinsX()) + sub_ljet_pt_2b_not_loose_Wtagged.GetBinContent(sub_ljet_pt_2b_not_loose_Wtagged.GetNbinsX()+1))
    sub_ljet_m_2b_not_loose_Wtagged.SetBinContent(sub_ljet_m_2b_not_loose_Wtagged.GetNbinsX(), sub_ljet_m_2b_not_loose_Wtagged.GetBinContent(sub_ljet_m_2b_not_loose_Wtagged.GetNbinsX()) + sub_ljet_m_2b_not_loose_Wtagged.GetBinContent(sub_ljet_m_2b_not_loose_Wtagged.GetNbinsX()+1))
    sub_ljet_e_2b_not_loose_Wtagged.SetBinContent(sub_ljet_e_2b_not_loose_Wtagged.GetNbinsX(), sub_ljet_e_2b_not_loose_Wtagged.GetBinContent(sub_ljet_e_2b_not_loose_Wtagged.GetNbinsX()) + sub_ljet_e_2b_not_loose_Wtagged.GetBinContent(sub_ljet_e_2b_not_loose_Wtagged.GetNbinsX()+1))
    VLQM_2b_not_loose_Wtagged.SetBinContent(VLQM_2b_not_loose_Wtagged.GetNbinsX(), VLQM_2b_not_loose_Wtagged.GetBinContent(VLQM_2b_not_loose_Wtagged.GetNbinsX()) + VLQM_2b_not_loose_Wtagged.GetBinContent(VLQM_2b_not_loose_Wtagged.GetNbinsX()+1))
    DeltaR_2b_not_loose_Wtagged.SetBinContent(DeltaR_2b_not_loose_Wtagged.GetNbinsX(), DeltaR_2b_not_loose_Wtagged.GetBinContent(DeltaR_2b_not_loose_Wtagged.GetNbinsX()) + DeltaR_2b_not_loose_Wtagged.GetBinContent(DeltaR_2b_not_loose_Wtagged.GetNbinsX()+1))
    DeltaR_bjet_2b_not_loose_Wtagged.SetBinContent(DeltaR_bjet_2b_not_loose_Wtagged.GetNbinsX(), DeltaR_bjet_2b_not_loose_Wtagged.GetBinContent(DeltaR_bjet_2b_not_loose_Wtagged.GetNbinsX()) + DeltaR_bjet_2b_not_loose_Wtagged.GetBinContent(DeltaR_bjet_2b_not_loose_Wtagged.GetNbinsX()+1))
    DeltaPhi_2b_not_loose_Wtagged.SetBinContent(DeltaPhi_2b_not_loose_Wtagged.GetNbinsX(), DeltaPhi_2b_not_loose_Wtagged.GetBinContent(DeltaPhi_2b_not_loose_Wtagged.GetNbinsX()) + DeltaPhi_2b_not_loose_Wtagged.GetBinContent(DeltaPhi_2b_not_loose_Wtagged.GetNbinsX()+1))


    ljet_pt_0b_not_loose_Wtagged.SetBinContent(ljet_pt_0b_not_loose_Wtagged.GetNbinsX(), ljet_pt_0b_not_loose_Wtagged.GetBinContent(ljet_pt_0b_not_loose_Wtagged.GetNbinsX()) + ljet_pt_0b_not_loose_Wtagged.GetBinContent(ljet_pt_0b_not_loose_Wtagged.GetNbinsX()+1))
    ljet_m_0b_not_loose_Wtagged.SetBinContent(ljet_m_0b_not_loose_Wtagged.GetNbinsX(), ljet_m_0b_not_loose_Wtagged.GetBinContent(ljet_m_0b_not_loose_Wtagged.GetNbinsX()) + ljet_m_0b_not_loose_Wtagged.GetBinContent(ljet_m_0b_not_loose_Wtagged.GetNbinsX()+1))
    ljet_e_0b_not_loose_Wtagged.SetBinContent(ljet_e_0b_not_loose_Wtagged.GetNbinsX(), ljet_e_0b_not_loose_Wtagged.GetBinContent(ljet_e_0b_not_loose_Wtagged.GetNbinsX()) + ljet_e_0b_not_loose_Wtagged.GetBinContent(ljet_e_0b_not_loose_Wtagged.GetNbinsX()+1))
    ljet_n_0b_not_loose_Wtagged.SetBinContent(ljet_n_0b_not_loose_Wtagged.GetNbinsX(), ljet_n_0b_not_loose_Wtagged.GetBinContent(ljet_n_0b_not_loose_Wtagged.GetNbinsX()) + ljet_n_0b_not_loose_Wtagged.GetBinContent(ljet_n_0b_not_loose_Wtagged.GetNbinsX()+1))
    jet_pt_0b_not_loose_Wtagged.SetBinContent(jet_pt_0b_not_loose_Wtagged.GetNbinsX(), jet_pt_0b_not_loose_Wtagged.GetBinContent(jet_pt_0b_not_loose_Wtagged.GetNbinsX()) + jet_pt_0b_not_loose_Wtagged.GetBinContent(jet_pt_0b_not_loose_Wtagged.GetNbinsX()+1))
    jet_m_0b_not_loose_Wtagged.SetBinContent(jet_m_0b_not_loose_Wtagged.GetNbinsX(), jet_m_0b_not_loose_Wtagged.GetBinContent(jet_m_0b_not_loose_Wtagged.GetNbinsX()) + jet_m_0b_not_loose_Wtagged.GetBinContent(jet_m_0b_not_loose_Wtagged.GetNbinsX()+1))
    jet_e_0b_not_loose_Wtagged.SetBinContent(jet_e_0b_not_loose_Wtagged.GetNbinsX(), jet_e_0b_not_loose_Wtagged.GetBinContent(jet_e_0b_not_loose_Wtagged.GetNbinsX()) + jet_e_0b_not_loose_Wtagged.GetBinContent(jet_e_0b_not_loose_Wtagged.GetNbinsX()+1))
    jet_n_0b_not_loose_Wtagged.SetBinContent(jet_n_0b_not_loose_Wtagged.GetNbinsX(), jet_n_0b_not_loose_Wtagged.GetBinContent(jet_n_0b_not_loose_Wtagged.GetNbinsX()) + jet_n_0b_not_loose_Wtagged.GetBinContent(jet_n_0b_not_loose_Wtagged.GetNbinsX()+1))
    sub_ljet_pt_0b_not_loose_Wtagged.SetBinContent(sub_ljet_pt_0b_not_loose_Wtagged.GetNbinsX(), sub_ljet_pt_0b_not_loose_Wtagged.GetBinContent(sub_ljet_pt_0b_not_loose_Wtagged.GetNbinsX()) + sub_ljet_pt_0b_not_loose_Wtagged.GetBinContent(sub_ljet_pt_0b_not_loose_Wtagged.GetNbinsX()+1))
    sub_ljet_m_0b_not_loose_Wtagged.SetBinContent(sub_ljet_m_0b_not_loose_Wtagged.GetNbinsX(), sub_ljet_m_0b_not_loose_Wtagged.GetBinContent(sub_ljet_m_0b_not_loose_Wtagged.GetNbinsX()) + sub_ljet_m_0b_not_loose_Wtagged.GetBinContent(sub_ljet_m_0b_not_loose_Wtagged.GetNbinsX()+1))
    sub_ljet_e_0b_not_loose_Wtagged.SetBinContent(sub_ljet_e_0b_not_loose_Wtagged.GetNbinsX(), sub_ljet_e_0b_not_loose_Wtagged.GetBinContent(sub_ljet_e_0b_not_loose_Wtagged.GetNbinsX()) + sub_ljet_e_0b_not_loose_Wtagged.GetBinContent(sub_ljet_e_0b_not_loose_Wtagged.GetNbinsX()+1))
    VLQM_0b_not_loose_Wtagged.SetBinContent(VLQM_0b_not_loose_Wtagged.GetNbinsX(), VLQM_0b_not_loose_Wtagged.GetBinContent(VLQM_0b_not_loose_Wtagged.GetNbinsX()) + VLQM_0b_not_loose_Wtagged.GetBinContent(VLQM_0b_not_loose_Wtagged.GetNbinsX()+1))
    DeltaR_0b_not_loose_Wtagged.SetBinContent(DeltaR_0b_not_loose_Wtagged.GetNbinsX(), DeltaR_0b_not_loose_Wtagged.GetBinContent(DeltaR_0b_not_loose_Wtagged.GetNbinsX()) + DeltaR_0b_not_loose_Wtagged.GetBinContent(DeltaR_0b_not_loose_Wtagged.GetNbinsX()+1))
    DeltaPhi_0b_not_loose_Wtagged.SetBinContent(DeltaPhi_0b_not_loose_Wtagged.GetNbinsX(), DeltaPhi_0b_not_loose_Wtagged.GetBinContent(DeltaPhi_0b_not_loose_Wtagged.GetNbinsX()) + DeltaPhi_0b_not_loose_Wtagged.GetBinContent(DeltaPhi_0b_not_loose_Wtagged.GetNbinsX()+1))
    
    

    '''
	#Clearing Underflow & Overflow
    ljet_pt_2b_tight_Wtagged.ClearUnderflowAndOverflow()
    ljet_eta_2b_tight_Wtagged.ClearUnderflowAndOverflow()
    ljet_phi_2b_tight_Wtagged.ClearUnderflowAndOverflow()
    ljet_m_2b_tight_Wtagged.ClearUnderflowAndOverflow()
    ljet_e_2b_tight_Wtagged.ClearUnderflowAndOverflow()	
    ljet_n_2b_tight_Wtagged.ClearUnderflowAndOverflow()	
    jet_pt_2b_tight_Wtagged.ClearUnderflowAndOverflow()
    jet_eta_2b_tight_Wtagged.ClearUnderflowAndOverflow()
    jet_phi_2b_tight_Wtagged.ClearUnderflowAndOverflow()
    jet_m_2b_tight_Wtagged.ClearUnderflowAndOverflow()
    jet_e_2b_tight_Wtagged.ClearUnderflowAndOverflow()
    jet_n_2b_tight_Wtagged.ClearUnderflowAndOverflow()		
    sub_ljet_pt_2b_tight_Wtagged.ClearUnderflowAndOverflow()
    sub_ljet_eta_2b_tight_Wtagged.ClearUnderflowAndOverflow()
    sub_ljet_phi_2b_tight_Wtagged.ClearUnderflowAndOverflow()
    sub_ljet_m_2b_tight_Wtagged.ClearUnderflowAndOverflow()
    sub_ljet_e_2b_tight_Wtagged.ClearUnderflowAndOverflow()
    VLQM_2b_tight_Wtagged.ClearUnderflowAndOverflow()
    DeltaR_2b_tight_Wtagged.ClearUnderflowAndOverflow()
    DeltaPhi_2b_tight_Wtagged.ClearUnderflowAndOverflow()
    DeltaR_bjet_2b_tight_Wtagged.ClearUnderflowAndOverflow()


    ljet_pt_1b_tight_Wtagged.ClearUnderflowAndOverflow()
    ljet_eta_1b_tight_Wtagged.ClearUnderflowAndOverflow()
    ljet_phi_1b_tight_Wtagged.ClearUnderflowAndOverflow()
    ljet_m_1b_tight_Wtagged.ClearUnderflowAndOverflow()
    ljet_e_1b_tight_Wtagged.ClearUnderflowAndOverflow()		
    ljet_n_1b_tight_Wtagged.ClearUnderflowAndOverflow()
    jet_pt_1b_tight_Wtagged.ClearUnderflowAndOverflow()
    jet_eta_1b_tight_Wtagged.ClearUnderflowAndOverflow()
    jet_phi_1b_tight_Wtagged.ClearUnderflowAndOverflow()
    jet_m_1b_tight_Wtagged.ClearUnderflowAndOverflow()
    jet_e_1b_tight_Wtagged.ClearUnderflowAndOverflow()		
    jet_n_1b_tight_Wtagged.ClearUnderflowAndOverflow()
    sub_ljet_pt_1b_tight_Wtagged.ClearUnderflowAndOverflow()
    sub_ljet_eta_1b_tight_Wtagged.ClearUnderflowAndOverflow()
    sub_ljet_phi_1b_tight_Wtagged.ClearUnderflowAndOverflow()
    sub_ljet_m_1b_tight_Wtagged.ClearUnderflowAndOverflow()
    sub_ljet_e_1b_tight_Wtagged.ClearUnderflowAndOverflow()
    VLQM_1b_tight_Wtagged.ClearUnderflowAndOverflow()
    DeltaR_1b_tight_Wtagged.ClearUnderflowAndOverflow()
    DeltaPhi_1b_tight_Wtagged.ClearUnderflowAndOverflow()
    DeltaR_bjet_lead_1b_tight_Wtagged.ClearUnderflowAndOverflow()
    DeltaR_bjet_sub_1b_tight_Wtagged.ClearUnderflowAndOverflow()


    ljet_pt_0b_tight_Wtagged.ClearUnderflowAndOverflow()
    ljet_eta_0b_tight_Wtagged.ClearUnderflowAndOverflow()
    ljet_phi_0b_tight_Wtagged.ClearUnderflowAndOverflow()
    ljet_m_0b_tight_Wtagged.ClearUnderflowAndOverflow()
    ljet_e_0b_tight_Wtagged.ClearUnderflowAndOverflow()		
    ljet_n_0b_tight_Wtagged.ClearUnderflowAndOverflow()
    jet_pt_0b_tight_Wtagged.ClearUnderflowAndOverflow()
    jet_eta_0b_tight_Wtagged.ClearUnderflowAndOverflow()
    jet_phi_0b_tight_Wtagged.ClearUnderflowAndOverflow()
    jet_m_0b_tight_Wtagged.ClearUnderflowAndOverflow()
    jet_e_0b_tight_Wtagged.ClearUnderflowAndOverflow()	
    jet_n_0b_tight_Wtagged.ClearUnderflowAndOverflow()	
    sub_ljet_pt_0b_tight_Wtagged.ClearUnderflowAndOverflow()
    sub_ljet_eta_0b_tight_Wtagged.ClearUnderflowAndOverflow()
    sub_ljet_phi_0b_tight_Wtagged.ClearUnderflowAndOverflow()
    sub_ljet_m_0b_tight_Wtagged.ClearUnderflowAndOverflow()
    sub_ljet_e_0b_tight_Wtagged.ClearUnderflowAndOverflow()
    VLQM_0b_tight_Wtagged.ClearUnderflowAndOverflow()
    DeltaR_0b_tight_Wtagged.ClearUnderflowAndOverflow()
    DeltaPhi_0b_tight_Wtagged.ClearUnderflowAndOverflow()


    ljet_pt_2b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()
    ljet_eta_2b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()
    ljet_phi_2b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()
    ljet_m_2b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()
    ljet_e_2b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()		
    ljet_n_2b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()
    jet_pt_2b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()
    jet_eta_2b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()
    jet_phi_2b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()
    jet_m_2b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()
    jet_e_2b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()
    jet_n_2b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()		
    sub_ljet_pt_2b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()
    sub_ljet_eta_2b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()
    sub_ljet_phi_2b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()
    sub_ljet_m_2b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()
    sub_ljet_e_2b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()
    VLQM_2b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()
    DeltaR_2b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()
    DeltaPhi_2b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()
    DeltaR_bjet_2b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()


    ljet_pt_1b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()
    ljet_eta_1b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()
    ljet_phi_1b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()
    ljet_m_1b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()
    ljet_e_1b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()		
    ljet_n_1b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()
    jet_pt_1b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()
    jet_eta_1b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()
    jet_phi_1b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()
    jet_m_1b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()
    jet_e_1b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()		
    jet_n_1b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()
    sub_ljet_pt_1b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()
    sub_ljet_eta_1b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()
    sub_ljet_phi_1b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()
    sub_ljet_m_1b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()
    sub_ljet_e_1b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()
    VLQM_1b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()
    DeltaR_1b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()
    DeltaPhi_1b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()
    DeltaR_bjet_lead_1b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()
    DeltaR_bjet_sub_1b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()


    ljet_pt_0b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()
    ljet_eta_0b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()
    ljet_phi_0b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()
    ljet_m_0b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()
    ljet_e_0b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()		
    ljet_n_0b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()
    jet_pt_0b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()
    jet_eta_0b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()
    jet_phi_0b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()
    jet_m_0b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()
    jet_e_0b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()		
    jet_n_0b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()
    sub_ljet_pt_0b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()
    sub_ljet_eta_0b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()
    sub_ljet_phi_0b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()
    sub_ljet_m_0b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()
    sub_ljet_e_0b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()	
    VLQM_0b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()
    DeltaR_0b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()
    DeltaPhi_0b_loose_not_tight_Wtagged.ClearUnderflowAndOverflow()


    ljet_pt_2b_not_loose_Wtagged.ClearUnderflowAndOverflow()
    ljet_eta_2b_not_loose_Wtagged.ClearUnderflowAndOverflow()
    ljet_phi_2b_not_loose_Wtagged.ClearUnderflowAndOverflow()
    ljet_m_2b_not_loose_Wtagged.ClearUnderflowAndOverflow()
    ljet_e_2b_not_loose_Wtagged.ClearUnderflowAndOverflow()		
    ljet_n_2b_not_loose_Wtagged.ClearUnderflowAndOverflow()
    jet_pt_2b_not_loose_Wtagged.ClearUnderflowAndOverflow()
    jet_eta_2b_not_loose_Wtagged.ClearUnderflowAndOverflow()
    jet_phi_2b_not_loose_Wtagged.ClearUnderflowAndOverflow()
    jet_m_2b_not_loose_Wtagged.ClearUnderflowAndOverflow()
    jet_e_2b_not_loose_Wtagged.ClearUnderflowAndOverflow()
    jet_n_2b_not_loose_Wtagged.ClearUnderflowAndOverflow()		
    sub_ljet_pt_2b_not_loose_Wtagged.ClearUnderflowAndOverflow()
    sub_ljet_eta_2b_not_loose_Wtagged.ClearUnderflowAndOverflow()
    sub_ljet_phi_2b_not_loose_Wtagged.ClearUnderflowAndOverflow()
    sub_ljet_m_2b_not_loose_Wtagged.ClearUnderflowAndOverflow()
    sub_ljet_e_2b_not_loose_Wtagged.ClearUnderflowAndOverflow()	
    VLQM_2b_not_loose_Wtagged.ClearUnderflowAndOverflow()
    DeltaR_2b_not_loose_Wtagged.ClearUnderflowAndOverflow()
    DeltaPhi_2b_not_loose_Wtagged.ClearUnderflowAndOverflow()
    DeltaR_bjet_2b_not_loose_Wtagged.ClearUnderflowAndOverflow()


    ljet_pt_1b_not_loose_Wtagged.ClearUnderflowAndOverflow()
    ljet_eta_1b_not_loose_Wtagged.ClearUnderflowAndOverflow()
    ljet_phi_1b_not_loose_Wtagged.ClearUnderflowAndOverflow()
    ljet_m_1b_not_loose_Wtagged.ClearUnderflowAndOverflow()
    ljet_e_1b_not_loose_Wtagged.ClearUnderflowAndOverflow()		
    ljet_n_1b_not_loose_Wtagged.ClearUnderflowAndOverflow()
    jet_pt_1b_not_loose_Wtagged.ClearUnderflowAndOverflow()
    jet_eta_1b_not_loose_Wtagged.ClearUnderflowAndOverflow()
    jet_phi_1b_not_loose_Wtagged.ClearUnderflowAndOverflow()
    jet_m_1b_not_loose_Wtagged.ClearUnderflowAndOverflow()
    jet_e_1b_not_loose_Wtagged.ClearUnderflowAndOverflow()		
    jet_n_1b_not_loose_Wtagged.ClearUnderflowAndOverflow()
    sub_ljet_pt_1b_not_loose_Wtagged.ClearUnderflowAndOverflow()
    sub_ljet_eta_1b_not_loose_Wtagged.ClearUnderflowAndOverflow()
    sub_ljet_phi_1b_not_loose_Wtagged.ClearUnderflowAndOverflow()
    sub_ljet_m_1b_not_loose_Wtagged.ClearUnderflowAndOverflow()
    sub_ljet_e_1b_not_loose_Wtagged.ClearUnderflowAndOverflow()
    VLQM_1b_not_loose_Wtagged.ClearUnderflowAndOverflow()
    DeltaR_1b_not_loose_Wtagged.ClearUnderflowAndOverflow()
    DeltaPhi_1b_not_loose_Wtagged.ClearUnderflowAndOverflow()
    DeltaR_bjet_lead_1b_not_loose_Wtagged.ClearUnderflowAndOverflow()
    DeltaR_bjet_sub_1b_not_loose_Wtagged.ClearUnderflowAndOverflow()


    ljet_pt_0b_not_loose_Wtagged.ClearUnderflowAndOverflow()
    ljet_eta_0b_not_loose_Wtagged.ClearUnderflowAndOverflow()
    ljet_phi_0b_not_loose_Wtagged.ClearUnderflowAndOverflow()
    ljet_m_0b_not_loose_Wtagged.ClearUnderflowAndOverflow()
    ljet_e_0b_not_loose_Wtagged.ClearUnderflowAndOverflow()		
    ljet_n_0b_not_loose_Wtagged.ClearUnderflowAndOverflow()
    jet_pt_0b_not_loose_Wtagged.ClearUnderflowAndOverflow()
    jet_eta_0b_not_loose_Wtagged.ClearUnderflowAndOverflow()
    jet_phi_0b_not_loose_Wtagged.ClearUnderflowAndOverflow()
    jet_m_0b_not_loose_Wtagged.ClearUnderflowAndOverflow()
    jet_e_0b_not_loose_Wtagged.ClearUnderflowAndOverflow()		
    jet_n_0b_not_loose_Wtagged.ClearUnderflowAndOverflow()
    sub_ljet_pt_0b_not_loose_Wtagged.ClearUnderflowAndOverflow()
    sub_ljet_eta_0b_not_loose_Wtagged.ClearUnderflowAndOverflow()
    sub_ljet_phi_0b_not_loose_Wtagged.ClearUnderflowAndOverflow()
    sub_ljet_m_0b_not_loose_Wtagged.ClearUnderflowAndOverflow()
    sub_ljet_e_0b_not_loose_Wtagged.ClearUnderflowAndOverflow()
    VLQM_0b_not_loose_Wtagged.ClearUnderflowAndOverflow()
    DeltaR_0b_not_loose_Wtagged.ClearUnderflowAndOverflow()
    DeltaPhi_0b_not_loose_Wtagged.ClearUnderflowAndOverflow()
	'''


	#Writing to the ROOT file
    ljet_pt_2b_tight_Wtagged.Write()
    ljet_eta_2b_tight_Wtagged.Write()
    ljet_phi_2b_tight_Wtagged.Write()
    ljet_m_2b_tight_Wtagged.Write()
    ljet_e_2b_tight_Wtagged.Write()	
    ljet_n_2b_tight_Wtagged.Write()	
    jet_pt_2b_tight_Wtagged.Write()
    jet_eta_2b_tight_Wtagged.Write()
    jet_phi_2b_tight_Wtagged.Write()
    jet_m_2b_tight_Wtagged.Write()
    jet_e_2b_tight_Wtagged.Write()
    jet_n_2b_tight_Wtagged.Write()		
    sub_ljet_pt_2b_tight_Wtagged.Write()
    sub_ljet_eta_2b_tight_Wtagged.Write()
    sub_ljet_phi_2b_tight_Wtagged.Write()
    sub_ljet_m_2b_tight_Wtagged.Write()
    sub_ljet_e_2b_tight_Wtagged.Write()
    VLQM_2b_tight_Wtagged.Write()
    DeltaR_2b_tight_Wtagged.Write()
    DeltaPhi_2b_tight_Wtagged.Write()
    DeltaR_bjet_2b_tight_Wtagged.Write()


    ljet_pt_0b_tight_Wtagged.Write()
    ljet_eta_0b_tight_Wtagged.Write()
    ljet_phi_0b_tight_Wtagged.Write()
    ljet_m_0b_tight_Wtagged.Write()
    ljet_e_0b_tight_Wtagged.Write()		
    ljet_n_0b_tight_Wtagged.Write()
    jet_pt_0b_tight_Wtagged.Write()
    jet_eta_0b_tight_Wtagged.Write()
    jet_phi_0b_tight_Wtagged.Write()
    jet_m_0b_tight_Wtagged.Write()
    jet_e_0b_tight_Wtagged.Write()	
    jet_n_0b_tight_Wtagged.Write()	
    sub_ljet_pt_0b_tight_Wtagged.Write()
    sub_ljet_eta_0b_tight_Wtagged.Write()
    sub_ljet_phi_0b_tight_Wtagged.Write()
    sub_ljet_m_0b_tight_Wtagged.Write()
    sub_ljet_e_0b_tight_Wtagged.Write()
    VLQM_0b_tight_Wtagged.Write()
    DeltaR_0b_tight_Wtagged.Write()
    DeltaPhi_0b_tight_Wtagged.Write()


    ljet_pt_2b_loose_not_tight_Wtagged.Write()
    ljet_eta_2b_loose_not_tight_Wtagged.Write()
    ljet_phi_2b_loose_not_tight_Wtagged.Write()
    ljet_m_2b_loose_not_tight_Wtagged.Write()
    ljet_e_2b_loose_not_tight_Wtagged.Write()		
    ljet_n_2b_loose_not_tight_Wtagged.Write()
    jet_pt_2b_loose_not_tight_Wtagged.Write()
    jet_eta_2b_loose_not_tight_Wtagged.Write()
    jet_phi_2b_loose_not_tight_Wtagged.Write()
    jet_m_2b_loose_not_tight_Wtagged.Write()
    jet_e_2b_loose_not_tight_Wtagged.Write()
    jet_n_2b_loose_not_tight_Wtagged.Write()		
    sub_ljet_pt_2b_loose_not_tight_Wtagged.Write()
    sub_ljet_eta_2b_loose_not_tight_Wtagged.Write()
    sub_ljet_phi_2b_loose_not_tight_Wtagged.Write()
    sub_ljet_m_2b_loose_not_tight_Wtagged.Write()
    sub_ljet_e_2b_loose_not_tight_Wtagged.Write()
    VLQM_2b_loose_not_tight_Wtagged.Write()
    DeltaR_2b_loose_not_tight_Wtagged.Write()
    DeltaPhi_2b_loose_not_tight_Wtagged.Write()
    DeltaR_bjet_2b_loose_not_tight_Wtagged.Write()


    ljet_pt_0b_loose_not_tight_Wtagged.Write()
    ljet_eta_0b_loose_not_tight_Wtagged.Write()
    ljet_phi_0b_loose_not_tight_Wtagged.Write()
    ljet_m_0b_loose_not_tight_Wtagged.Write()
    ljet_e_0b_loose_not_tight_Wtagged.Write()		
    ljet_n_0b_loose_not_tight_Wtagged.Write()
    jet_pt_0b_loose_not_tight_Wtagged.Write()
    jet_eta_0b_loose_not_tight_Wtagged.Write()
    jet_phi_0b_loose_not_tight_Wtagged.Write()
    jet_m_0b_loose_not_tight_Wtagged.Write()
    jet_e_0b_loose_not_tight_Wtagged.Write()		
    jet_n_0b_loose_not_tight_Wtagged.Write()
    sub_ljet_pt_0b_loose_not_tight_Wtagged.Write()
    sub_ljet_eta_0b_loose_not_tight_Wtagged.Write()
    sub_ljet_phi_0b_loose_not_tight_Wtagged.Write()
    sub_ljet_m_0b_loose_not_tight_Wtagged.Write()
    sub_ljet_e_0b_loose_not_tight_Wtagged.Write()	
    VLQM_0b_loose_not_tight_Wtagged.Write()
    DeltaR_0b_loose_not_tight_Wtagged.Write()
    DeltaPhi_0b_loose_not_tight_Wtagged.Write()


    ljet_pt_2b_not_loose_Wtagged.Write()
    ljet_eta_2b_not_loose_Wtagged.Write()
    ljet_phi_2b_not_loose_Wtagged.Write()
    ljet_m_2b_not_loose_Wtagged.Write()
    ljet_e_2b_not_loose_Wtagged.Write()		
    ljet_n_2b_not_loose_Wtagged.Write()
    jet_pt_2b_not_loose_Wtagged.Write()
    jet_eta_2b_not_loose_Wtagged.Write()
    jet_phi_2b_not_loose_Wtagged.Write()
    jet_m_2b_not_loose_Wtagged.Write()
    jet_e_2b_not_loose_Wtagged.Write()
    jet_n_2b_not_loose_Wtagged.Write()		
    sub_ljet_pt_2b_not_loose_Wtagged.Write()
    sub_ljet_eta_2b_not_loose_Wtagged.Write()
    sub_ljet_phi_2b_not_loose_Wtagged.Write()
    sub_ljet_m_2b_not_loose_Wtagged.Write()
    sub_ljet_e_2b_not_loose_Wtagged.Write()	
    VLQM_2b_not_loose_Wtagged.Write()
    DeltaR_2b_not_loose_Wtagged.Write()
    DeltaPhi_2b_not_loose_Wtagged.Write()
    DeltaR_bjet_2b_not_loose_Wtagged.Write()


    ljet_pt_0b_not_loose_Wtagged.Write()
    ljet_eta_0b_not_loose_Wtagged.Write()
    ljet_phi_0b_not_loose_Wtagged.Write()
    ljet_m_0b_not_loose_Wtagged.Write()
    ljet_e_0b_not_loose_Wtagged.Write()		
    ljet_n_0b_not_loose_Wtagged.Write()
    jet_pt_0b_not_loose_Wtagged.Write()
    jet_eta_0b_not_loose_Wtagged.Write()
    jet_phi_0b_not_loose_Wtagged.Write()
    jet_m_0b_not_loose_Wtagged.Write()
    jet_e_0b_not_loose_Wtagged.Write()		
    jet_n_0b_not_loose_Wtagged.Write()
    sub_ljet_pt_0b_not_loose_Wtagged.Write()
    sub_ljet_eta_0b_not_loose_Wtagged.Write()
    sub_ljet_phi_0b_not_loose_Wtagged.Write()
    sub_ljet_m_0b_not_loose_Wtagged.Write()
    sub_ljet_e_0b_not_loose_Wtagged.Write()
    VLQM_0b_not_loose_Wtagged.Write()
    DeltaR_0b_not_loose_Wtagged.Write()
    DeltaPhi_0b_not_loose_Wtagged.Write()
    
    print "Wrote "
    f0.Close()


#dsid = sys.argv[1]
#makeHist(dsid)

data=sys.argv[1]
dsid=sys.argv[2]
label = sys.argv[3]
weight_branch = sys.argv[4]
print type(dsid)
makeHists(data,dsid,label,weight_branch)