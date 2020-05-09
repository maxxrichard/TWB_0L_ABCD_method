import ROOT 
import math
import time
import os
import numpy as np
import heapq
import sys
from array import array


def makeHists(background,dsid,chain_name,crossection_background,label,weight_branch,signal_array):
    lumi = 58450.1
    
    location = '/cephfs/user/s6anband/ntuples/'

    tagger = ['allhad_2018_3var50_btag70','allhad_2018_3var50','allhad_2018_3var80_btag70','allhad_2018_3var80']

    file_names = []
    
    
    if "3123" in background:
        print "-------------------------------------------------------------------------------------------------------------- \n"
        print "\t \t SIGNAL \n"
        signal_array_element = int(signal_array)
        allowed_Ks = [0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6]
        crossection_background = crossection_background * allowed_Ks[signal_array_element] * allowed_Ks[signal_array_element]
    else:
        print "-------------------------------------------------------------------------------------------------------------- \n"
        print "\t \t BACKGROUND \n"
    

    print background,dsid,crossection_background,chain_name
    
    
    sumofeventsweighted = 0.
    listOfFiles = os.listdir(location + background)
    sumWeights = ROOT.TChain("sumWeights")
    nominal = ROOT.TChain(chain_name)
    nominal1 = ROOT.TChain("nominal")
    for f in listOfFiles:
        f = location + background + '/' + f 
        if 'output_root/user.abandyop' not in f:
            continue
        sumWeights.Add(f)
        nominal.Add(f)
        nominal1.Add(f)
    if "3123" in background:
            print 'Calculating signal'
            for j in xrange(sumWeights.GetEntries()):
                sumWeights.GetEntry(j)
                sumweight = getattr(sumWeights,"totalEventsWeighted_mc_generator_weights")
                sumweight_k = sumweight[signal_array_element]
                sumofeventsweighted += sumweight_k
    elif "3647" in background:
        print 'Calculating dijet'
        for j in xrange(sumWeights.GetEntries()):
            sumWeights.GetEntry(j)
            sumweight = getattr(sumWeights,"totalEventsWeighted")
            #dsid = getattr(sumWeights,"dsid")
            sumofeventsweighted += sumweight
    else:
        print 'Calculating other bkgs'
        for j in xrange(sumWeights.GetEntries()):
            sumWeights.GetEntry(j)
            sumweight = getattr(sumWeights,"totalEventsWeighted")
            sumofeventsweighted += sumweight
    if "3123" in background:
        if "weight" in weight_branch:
            os.chdir("/cephfs/user/s6marahm/output/output_sig_"+signal_array+"/output_"+weight_branch+"/")
        elif "CategoryReduction" in chain_name:
            os.chdir("/cephfs/user/s6marahm/output/output_sig_"+signal_array+"/output_"+chain_name+"/")
        else:
            os.chdir("/cephfs/user/s6marahm/output/output_sig_"+signal_array+"/output/")
    else:
        if "weight" in weight_branch:
            os.chdir("/cephfs/user/s6marahm/output/output_"+weight_branch+"/")
        elif "CategoryReduction" in chain_name:
            os.chdir("/cephfs/user/s6marahm/output/output_"+chain_name+"/")
        elif "crossection" in signal_array:
            os.chdir("/cephfs/user/s6marahm/output/output_"+signal_array+"/")
        else:
            os.chdir("/cephfs/user/s6marahm/output/")
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
    VLQM_2b_tight_Wtagged = ROOT.TH1F("VLQM_2b_tight_Wtagged","VLQM_2b_tight_Wtagged",60,0,3400)
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
    VLQM_0b_tight_Wtagged = ROOT.TH1F("VLQM_0b_tight_Wtagged","VLQM_0b_tight_Wtagged",60,0,3400)
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
    VLQM_2b_loose_not_tight_Wtagged = ROOT.TH1F("VLQM_2b_loose_not_tight_Wtagged","VLQM_2b_loose_not_tight_Wtagged",60,0,3400)
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
    VLQM_0b_loose_not_tight_Wtagged = ROOT.TH1F("VLQM_0b_loose_not_tight_Wtagged","VLQM_0b_loose_not_tight_Wtagged",60,0,3400)
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
    VLQM_2b_not_loose_Wtagged = ROOT.TH1F("VLQM_2b_not_loose_Wtagged","VLQM_2b_not_loose_Wtagged",60,0,3400)
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
    VLQM_0b_not_loose_Wtagged = ROOT.TH1F("VLQM_0b_not_loose_Wtagged","VLQM_0b_not_loose_Wtagged",60,0,3400)
    VLQM_0b_not_loose_Wtagged.Sumw2()
    DeltaR_0b_not_loose_Wtagged = ROOT.TH1F("DeltaR_0b_not_loose_Wtagged","DeltaR_0b_not_loose_Wtagged",10,0,5)
    DeltaR_0b_not_loose_Wtagged.Sumw2()
    DeltaPhi_0b_not_loose_Wtagged = ROOT.TH1F("DeltaPhi_0b_not_loose_Wtagged","DeltaPhi_0b_not_loose_Wtagged",10,-5,5)
    DeltaPhi_0b_not_loose_Wtagged.Sumw2()
    
    
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
        nominal1.GetEntry(l)
        weight = 1.0
        tag2018_tight = getattr(nominal,tagger[0])
        tag2018_tight_0b = getattr(nominal,tagger[1])
        tag2018_loose = getattr(nominal,tagger[2])
        tag2018_loose_0b = getattr(nominal,tagger[3])
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
        weight *= getattr(nominal,'weight_pileup')
        weight *= getattr(nominal,'weight_oldTriggerSF')
        weight *= getattr(nominal,'weight_jvt')
        if "3123" in background:
            weight_sig = getattr(nominal1,"mc_generator_weights")
            weight *= weight_sig[signal_array_element]
        else:
            weight *= getattr(nominal,'weight_mc')
        weight_0b = weight
        if "weight" in weight_branch:
            weight *= np.mean(getattr(nominal,weight_branch))
        else:
            weight *= getattr(nominal,'weight_bTagSF_DL1r_70')

        
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
        #print len(jetpt_btag), loose[idx_ljet], jetpt[idx_jet], leadjetpt[idx_ljet], tag2015 
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


        #print tight[idx_ljet],loose[idx_ljet],leadjetpt[idx_ljet],jetpt[idx_jet]
        if forward == True:
            if len(jetpt_btag) == 1000 and abs(jeteta[idx_jet]) < 2.5 and DeltaR > 1.0 and met_met < 120e3 and tight[idx_ljet] == 1 and jetpt[idx_jet] > 350e3 and leadjetpt[idx_ljet] > 500e3 and tag2018_tight == 1: #2b_tight_Wtagged
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

        

            elif len(jetpt_btag) == 1000 and abs(jeteta[idx_jet]) < 2.5 and DeltaR > 1.0 and met_met < 120e3 and tight[idx_ljet] == 1 and jetpt[idx_jet] > 350e3 and leadjetpt[idx_ljet] > 500e3 and tag2018_tight_0b == 1: #0b_tight_Wtagged
                jet_pt_0b_tight_Wtagged.Fill(jetpt[idx_jet]/1000,weight_0b)
                jet_eta_0b_tight_Wtagged.Fill(jeteta[idx_jet],weight_0b)
                jet_phi_0b_tight_Wtagged.Fill(jetphi[idx_jet],weight_0b)
                jet_e_0b_tight_Wtagged.Fill(jete[idx_jet]/1000,weight_0b)
                jet_p4.SetPtEtaPhiE(jetpt[idx_jet],jeteta[idx_jet],jetphi[idx_jet],jete[idx_jet])
                jet_m_0b_tight_Wtagged.Fill(jet_p4.M()/1000,weight_0b)
                jet_n_0b_tight_Wtagged.Fill(jet_pt.size(),weight_0b)
                ljet_pt_0b_tight_Wtagged.Fill(leadjetpt[idx_ljet]/1000,weight_0b)
                ljet_eta_0b_tight_Wtagged.Fill(leadjeteta[idx_ljet],weight_0b)
                ljet_phi_0b_tight_Wtagged.Fill(leadjetphi[idx_ljet],weight_0b)
                ljet_m_0b_tight_Wtagged.Fill(leadjetm[idx_ljet]/1000,weight_0b)
                ljet_e_0b_tight_Wtagged.Fill(leadjete[idx_ljet]/1000,weight_0b)
                ljet_n_0b_tight_Wtagged.Fill(leadjet_pt.size(),weight_0b)
                leadjet_p4.SetPtEtaPhiE(leadjetpt[idx_ljet],leadjeteta[idx_ljet],leadjetphi[idx_ljet],leadjete[idx_ljet])
                VLQ_p4 = ROOT.TLorentzVector()
                VLQ_p4 = leadjet_p4 + jet_p4
                VLQM = VLQ_p4.M()
                DeltaR = leadjet_p4.DeltaR(jet_p4)
                DeltaPhi = leadjet_p4.DeltaPhi(jet_p4)
                VLQM_0b_tight_Wtagged.Fill(VLQM/1000,weight_0b)
                DeltaR_0b_tight_Wtagged.Fill(DeltaR,weight_0b)
                DeltaPhi_0b_tight_Wtagged.Fill(DeltaPhi,weight_0b)
                if len(leadjetpt) > 1:
                    sub_ljet_pt_0b_tight_Wtagged.Fill(leadjetpt[idx_subjet]/1000,weight_0b)
                    sub_ljet_eta_0b_tight_Wtagged.Fill(leadjeteta[idx_subjet],weight_0b)
                    sub_ljet_phi_0b_tight_Wtagged.Fill(leadjetphi[idx_subjet],weight_0b)
                    sub_ljet_m_0b_tight_Wtagged.Fill(leadjetm[idx_subjet]/1000,weight_0b)
                    sub_ljet_e_0b_tight_Wtagged.Fill(leadjete[idx_subjet]/1000,weight_0b)


            elif len(jetpt_btag) > 0 and jetpt[idx_jet] > 350e3 and leadjetpt[idx_ljet] > 500e3 and tight[idx_ljet] == 1: #2b_loose_not_tight_Wtagged
                #print tight[idx_ljet],loose[idx_ljet],leadjetpt[idx_ljet],jetpt[idx_jet],len(jetpt_btag)                
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
            
        
            elif len(jetpt_btag) == 1000 and abs(jeteta[idx_jet]) < 2.5 and DeltaR > 1.0 and met_met < 120e3 and loose[idx_ljet] == 1 and tight[idx_ljet] != 1 and jetpt[idx_jet] > 350e3 and leadjetpt[idx_ljet] > 500e3 and (tag2018_loose_0b == 1 and tag2018_tight_0b != 1): #0b_loose_not_tight_Wtagged
                #print tight[idx_ljet],loose[idx_ljet],leadjetpt[idx_ljet],jetpt[idx_jet],len(jetpt_btag)
                jet_pt_0b_loose_not_tight_Wtagged.Fill(jetpt[idx_jet]/1000,weight_0b)
                jet_eta_0b_loose_not_tight_Wtagged.Fill(jeteta[idx_jet],weight_0b)
                jet_phi_0b_loose_not_tight_Wtagged.Fill(jetphi[idx_jet],weight_0b)
                jet_e_0b_loose_not_tight_Wtagged.Fill(jete[idx_jet]/1000,weight_0b)
                jet_p4.SetPtEtaPhiE(jetpt[idx_jet],jeteta[idx_jet],jetphi[idx_jet],jete[idx_jet])
                jet_m_0b_loose_not_tight_Wtagged.Fill(jet_p4.M()/1000,weight_0b)
                jet_n_0b_loose_not_tight_Wtagged.Fill(jet_pt.size(),weight_0b)
                ljet_pt_0b_loose_not_tight_Wtagged.Fill(leadjetpt[idx_ljet]/1000,weight_0b)
                ljet_eta_0b_loose_not_tight_Wtagged.Fill(leadjeteta[idx_ljet],weight_0b)
                ljet_phi_0b_loose_not_tight_Wtagged.Fill(leadjetphi[idx_ljet],weight_0b)
                ljet_m_0b_loose_not_tight_Wtagged.Fill(leadjetm[idx_ljet]/1000,weight_0b)
                ljet_e_0b_loose_not_tight_Wtagged.Fill(leadjete[idx_ljet]/1000,weight_0b)
                ljet_n_0b_loose_not_tight_Wtagged.Fill(leadjet_pt.size(),weight_0b)
                leadjet_p4.SetPtEtaPhiE(leadjetpt[idx_ljet],leadjeteta[idx_ljet],leadjetphi[idx_ljet],leadjete[idx_ljet])
                VLQ_p4 = ROOT.TLorentzVector()
                VLQ_p4 = leadjet_p4 + jet_p4
                VLQM = VLQ_p4.M()
                DeltaR = leadjet_p4.DeltaR(jet_p4)
                DeltaPhi = leadjet_p4.DeltaPhi(jet_p4)
                VLQM_0b_loose_not_tight_Wtagged.Fill(VLQM/1000,weight_0b)
                DeltaR_0b_loose_not_tight_Wtagged.Fill(DeltaR,weight_0b)
                DeltaPhi_0b_loose_not_tight_Wtagged.Fill(DeltaPhi,weight_0b)
                if len(leadjetpt) > 1:
                    sub_ljet_pt_0b_loose_not_tight_Wtagged.Fill(leadjetpt[idx_subjet]/1000,weight_0b)
                    sub_ljet_eta_0b_loose_not_tight_Wtagged.Fill(leadjeteta[idx_subjet],weight_0b)
                    sub_ljet_phi_0b_loose_not_tight_Wtagged.Fill(leadjetphi[idx_subjet],weight_0b)
                    sub_ljet_m_0b_loose_not_tight_Wtagged.Fill(leadjetm[idx_subjet]/1000,weight_0b)
                    sub_ljet_e_0b_loose_not_tight_Wtagged.Fill(leadjete[idx_subjet]/1000,weight_0b)
            
            
            elif len(jetpt_btag) == 1000 and abs(jeteta[idx_jet]) < 2.5 and DeltaR > 1.0 and met_met < 120e3 and loose[idx_ljet] != 1 and jetpt[idx_jet] > 350e3 and leadjetpt[idx_ljet] > 500e3: #2b_not_loose_Wtagged
                #and tag2018_loose != 1
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
            

        
            elif len(jetpt_btag) == 1000 and abs(jeteta[idx_jet]) < 2.5 and DeltaR > 1.0 and met_met < 120e3 and loose[idx_ljet] != 1 and jetpt[idx_jet] > 350e3 and leadjetpt[idx_ljet] > 500e3: #0b_not_loose_Wtagged
                # and tag2018_loose_0b != 1
                jet_pt_0b_not_loose_Wtagged.Fill(jetpt[idx_jet]/1000,weight_0b)
                jet_eta_0b_not_loose_Wtagged.Fill(jeteta[idx_jet],weight_0b)
                jet_phi_0b_not_loose_Wtagged.Fill(jetphi[idx_jet],weight_0b)
                jet_e_0b_not_loose_Wtagged.Fill(jete[idx_jet]/1000,weight_0b)
                jet_p4.SetPtEtaPhiE(jetpt[idx_jet],jeteta[idx_jet],jetphi[idx_jet],jete[idx_jet])
                jet_m_0b_not_loose_Wtagged.Fill(jet_p4.M()/1000,weight_0b)
                jet_n_0b_not_loose_Wtagged.Fill(jet_pt.size(),weight_0b)
                ljet_pt_0b_not_loose_Wtagged.Fill(leadjetpt[idx_ljet]/1000,weight_0b)
                ljet_eta_0b_not_loose_Wtagged.Fill(leadjeteta[idx_ljet],weight_0b)
                ljet_phi_0b_not_loose_Wtagged.Fill(leadjetphi[idx_ljet],weight_0b)
                ljet_m_0b_not_loose_Wtagged.Fill(leadjetm[idx_ljet]/1000,weight_0b)
                ljet_e_0b_not_loose_Wtagged.Fill(leadjete[idx_ljet]/1000,weight_0b)
                ljet_n_0b_not_loose_Wtagged.Fill(leadjet_pt.size(),weight_0b)
                leadjet_p4.SetPtEtaPhiE(leadjetpt[idx_ljet],leadjeteta[idx_ljet],leadjetphi[idx_ljet],leadjete[idx_ljet])
                VLQ_p4 = ROOT.TLorentzVector()
                VLQ_p4 = leadjet_p4 + jet_p4
                VLQM = VLQ_p4.M()
                DeltaR = leadjet_p4.DeltaR(jet_p4)
                DeltaPhi = leadjet_p4.DeltaPhi(jet_p4)
                VLQM_0b_not_loose_Wtagged.Fill(VLQM/1000,weight_0b)
                DeltaR_0b_not_loose_Wtagged.Fill(DeltaR,weight_0b)
                DeltaPhi_0b_not_loose_Wtagged.Fill(DeltaPhi,weight_0b)
                if len(leadjetpt) > 1:
                    sub_ljet_pt_0b_not_loose_Wtagged.Fill(leadjetpt[idx_subjet]/1000,weight_0b)
                    sub_ljet_eta_0b_not_loose_Wtagged.Fill(leadjeteta[idx_subjet],weight_0b)
                    sub_ljet_phi_0b_not_loose_Wtagged.Fill(leadjetphi[idx_subjet],weight_0b)
                    sub_ljet_m_0b_not_loose_Wtagged.Fill(leadjetm[idx_subjet]/1000,weight_0b)
                    sub_ljet_e_0b_not_loose_Wtagged.Fill(leadjete[idx_subjet]/1000,weight_0b)

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

	#Normalisation to the Luminosity
    ljet_pt_2b_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    ljet_eta_2b_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    ljet_phi_2b_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    ljet_m_2b_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    ljet_e_2b_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    ljet_n_2b_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    jet_pt_2b_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    jet_eta_2b_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    jet_phi_2b_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    jet_m_2b_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    jet_e_2b_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    jet_n_2b_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    sub_ljet_pt_2b_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    sub_ljet_eta_2b_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    sub_ljet_phi_2b_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    sub_ljet_m_2b_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    sub_ljet_e_2b_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    VLQM_2b_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    DeltaR_2b_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    DeltaPhi_2b_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    DeltaR_bjet_2b_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)


    ljet_pt_0b_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    ljet_eta_0b_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    ljet_phi_0b_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    ljet_m_0b_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    ljet_e_0b_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    ljet_n_0b_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    jet_pt_0b_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    jet_eta_0b_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    jet_phi_0b_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    jet_m_0b_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    jet_e_0b_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    jet_n_0b_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    sub_ljet_pt_0b_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    sub_ljet_eta_0b_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    sub_ljet_phi_0b_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    sub_ljet_m_0b_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    sub_ljet_e_0b_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    VLQM_0b_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    DeltaR_0b_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    DeltaPhi_0b_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)


    ljet_pt_2b_loose_not_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    ljet_eta_2b_loose_not_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    ljet_phi_2b_loose_not_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    ljet_m_2b_loose_not_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    ljet_e_2b_loose_not_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    ljet_n_2b_loose_not_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    jet_pt_2b_loose_not_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    jet_eta_2b_loose_not_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    jet_phi_2b_loose_not_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    jet_m_2b_loose_not_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    jet_e_2b_loose_not_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    jet_n_2b_loose_not_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    sub_ljet_pt_2b_loose_not_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    sub_ljet_eta_2b_loose_not_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    sub_ljet_phi_2b_loose_not_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    sub_ljet_m_2b_loose_not_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    sub_ljet_e_2b_loose_not_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    VLQM_2b_loose_not_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    DeltaR_2b_loose_not_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    DeltaPhi_2b_loose_not_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    DeltaR_bjet_2b_loose_not_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)


    ljet_pt_0b_loose_not_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    ljet_eta_0b_loose_not_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    ljet_phi_0b_loose_not_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    ljet_m_0b_loose_not_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    ljet_e_0b_loose_not_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    ljet_n_0b_loose_not_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    jet_pt_0b_loose_not_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    jet_eta_0b_loose_not_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    jet_phi_0b_loose_not_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    jet_m_0b_loose_not_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    jet_e_0b_loose_not_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    jet_n_0b_loose_not_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    sub_ljet_pt_0b_loose_not_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    sub_ljet_eta_0b_loose_not_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    sub_ljet_phi_0b_loose_not_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    sub_ljet_m_0b_loose_not_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    sub_ljet_e_0b_loose_not_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    VLQM_0b_loose_not_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    DeltaR_0b_loose_not_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    DeltaPhi_0b_loose_not_tight_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    
    
    ljet_pt_2b_not_loose_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    ljet_eta_2b_not_loose_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    ljet_phi_2b_not_loose_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    ljet_m_2b_not_loose_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    ljet_e_2b_not_loose_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    ljet_n_2b_not_loose_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    jet_pt_2b_not_loose_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    jet_eta_2b_not_loose_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    jet_phi_2b_not_loose_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    jet_m_2b_not_loose_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    jet_e_2b_not_loose_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    jet_n_2b_not_loose_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    sub_ljet_pt_2b_not_loose_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    sub_ljet_eta_2b_not_loose_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    sub_ljet_phi_2b_not_loose_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    sub_ljet_m_2b_not_loose_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    sub_ljet_e_2b_not_loose_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    VLQM_2b_not_loose_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    DeltaR_2b_not_loose_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    DeltaPhi_2b_not_loose_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    DeltaR_bjet_2b_not_loose_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)


    ljet_pt_0b_not_loose_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    ljet_eta_0b_not_loose_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    ljet_phi_0b_not_loose_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    ljet_m_0b_not_loose_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    ljet_e_0b_not_loose_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    ljet_n_0b_not_loose_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    jet_pt_0b_not_loose_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    jet_eta_0b_not_loose_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    jet_phi_0b_not_loose_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    jet_m_0b_not_loose_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    jet_e_0b_not_loose_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    jet_n_0b_not_loose_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    sub_ljet_pt_0b_not_loose_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    sub_ljet_eta_0b_not_loose_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    sub_ljet_phi_0b_not_loose_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    sub_ljet_m_0b_not_loose_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    sub_ljet_e_0b_not_loose_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    VLQM_0b_not_loose_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    DeltaR_0b_not_loose_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)
    DeltaPhi_0b_not_loose_Wtagged.Scale(crossection_background*lumi/sumofeventsweighted)



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

background=sys.argv[1]
dsid=sys.argv[2]
chain_name =sys.argv[3]
crossection_background=float(sys.argv[4])
label = sys.argv[5]
weight_branch = sys.argv[6]
signal_array = sys.argv[7]
print type(dsid)
makeHists(background,dsid,chain_name,crossection_background,label,weight_branch,signal_array)