from ROOT import TFile, TTree, TH1, TH1F, TCanvas, TPad, TPaveLabel, TLegend, TChain
from ROOT import gStyle, kBlue, kRed, gROOT
import math
import time
import os
import numpy as np
import ROOT
import sys
from array import array

def makeHists(corr_type,corr_cal):

    tagger = ['tight_Wtagged','loose_not_tight_Wtagged','not_loose_Wtagged']
    region = ['2b','0b']
    variable = ['ljet_pt','ljet_eta','ljet_phi','ljet_e','ljet_m','ljet_n','jet_pt','jet_eta','jet_phi','jet_e','jet_m','jet_n','sub_ljet_pt','sub_ljet_eta','sub_ljet_phi','sub_ljet_m','sub_ljet_e','VLQM','DeltaR','DeltaPhi']

    region_calculated = ['2b']
    if (corr_cal == "prefit"):
        tagger_calculated = ['tight_Wtagged','loose_not_tight_Wtagged']
    else:
        tagger_calculated = ['loose_not_tight_Wtagged']
    variable_calculated = ['ljet_pt','jet_pt','VLQM','ljet_m','jet_m','ljet_eta']

    jet_pt_var_bin = np.array((350.,400.,500.,600.,700.,800.,1200.))
    #VLQM_var_bin = np.array((400.,1000.,1100.,1200.,1300.,1400.,1500.,1600.,1700.,1800.,1900.,2000.,2100.,2200.,2300.,2400.,2500.,3400.))
    VLQM_var_bin = np.array((800.,900.,1000.,1100.,1200.,1300.,1400.,1500.,1600.,1700.,1800.,1900.,2000.,2100.,2200.,2300.,2400.,2500.,3400.))
    ljet_pt_var_bin = np.array((500.,550.,600.,650.,700.,750.,800.,850.,900.,1400.))

    if (corr_cal == "prefit"):
        f11 = TFile.Open('/cephfs/user/s6marahm/output/abcd_dijets.root',"update")
    else:
        f11 = TFile.Open('/cephfs/user/s6marahm/output/abcd_dijets_postfit.root',"update")
    f12 = ROOT.TFile.Open("/cephfs/user/s6marahm/output/abcd_correlation.root","RECREATE")


    print "Bin by Bin Correlation calculating..."
    for t in tagger_calculated:
        for r in region_calculated:
            for v in variable_calculated:
                n1 = f11.Get(v+'_'+r+'_'+t)
                d1 = f11.Get(v+'_'+r+'_not_loose_Wtagged')
                n2 = f11.Get(v+'_0b_not_loose_Wtagged')
                d2 = f11.Get(v+'_0b_'+t)
                temp = n1.Clone()
                temp.Multiply(n2)
                temp.Divide(d1)
                temp.Divide(d2)
                temp.Write()
    f12.Close()
    print "abcd_correlation.root created!"



    #Data & background samples
    f1 = TFile.Open('/cephfs/user/s6marahm/output/abcd_data.root',"update")
    f2 = TFile.Open('/cephfs/user/s6marahm/output/abcd_background.root',"update")
    if (corr_cal == "prefit"):
        f3 = TFile.Open('/cephfs/user/s6marahm/output/abcd_dijets.root',"update")
        print "CALCULATING PREFIT ABCD..."
    else:
        f3 = TFile.Open('/cephfs/user/s6marahm/output/abcd_dijets_postfit.root',"update")
        print "CALCULATING POSTFIT ABCD..."
    f4 = TFile.Open('/cephfs/user/s6marahm/output/abcd_correlation.root',"update")
    f5 = ROOT.TFile.Open("/cephfs/user/s6marahm/output/abcd_output.root","RECREATE")


    #Calculation of (Data-MC Dijets) for all the regions
    for t in tagger:
        for r in region:
            for v in variable:
                if r == '0b' or t == 'not_loose_Wtagged':
                    a = f1.Get(v+'_'+r+'_'+t)
                    b = f2.Get(v+'_'+r+'_'+t)
                    c = a.Clone()
                    c.Add(b,-1)
                    c.Write()
    
    #Calculation of (Data-MC Dijets) for all the regions
#    for t in tagger:
#        for r in region:
#            for v in variable:
#                if r == '0b' or t == 'not_loose_Wtagged':
#                    a = f3.Get(v+'_'+r+'_'+t)
#                    c = a.Clone()
#                    c.Write()


    #Regions to be accounted (SR,VR) for the calculation of Correlation factor
    R = []
    p = 0
    s = 0


    #calculating the correlation factors for SR & VR
    print "Integral Correlation calculating..."
    for r in region_calculated:
        for t in tagger_calculated:
            for v in variable_calculated:
                if r == '1b':
                    R.append(1.0)
                else:
                    n1 = f3.Get(v+'_'+r+'_'+t)
                    d1 = f3.Get(v+'_'+r+'_not_loose_Wtagged')
                    n2 = f3.Get(v+'_0b_not_loose_Wtagged')
                    d2 = f3.Get(v+'_0b_'+t)
                    #print(v+'_'+r+'_'+t)
                    #print n1.Integral(),n2.Integral(),d1.Integral(),d2.Integral()
                    R.append((n1.Integral()*n2.Integral())/(d1.Integral()*d2.Integral()))
    print "Integral Correlation calculated!"



    #Multiplying according to the ABCD formula for estimating dijets
    print "Implementing ABCD in SR/VR..."
    for r in region_calculated:
        for t in tagger_calculated:
            for v in variable_calculated:
                d1 = f5.Get(v+'_0b_not_loose_Wtagged')
                n1 = f5.Get(v+'_0b_'+t)
                n2 = f5.Get(v+'_'+r+'_not_loose_Wtagged')
                corr = f4.Get(v+'_'+r+'_'+t)

                k = v+'_'+r+'_'+t
                print v
                
                if(v == 'ljet_pt'):
                    temp = ROOT.TH1F(k,k,(len(ljet_pt_var_bin)-1),ljet_pt_var_bin)
                    temp.Sumw2()
                elif(v == 'ljet_eta'):
                    temp = ROOT.TH1F(k,k,8,-2.0,2.0)
                    temp.Sumw2()
                elif(v == 'ljet_phi'):
                    temp = ROOT.TH1F(k,k,10,-3.5,3.5)
                    temp.Sumw2()
                elif(v == 'ljet_e'):
                    temp = ROOT.TH1F(k,k,20,0,3000)
                    temp.Sumw2()
                elif(v == 'ljet_m'):
                    temp = ROOT.TH1F(k,k,13,0,260)
                    temp.Sumw2()
                elif(v == 'ljet_n'):
                    temp = ROOT.TH1F(k,k,10,0,10)
                    temp.Sumw2()
                elif(v == 'jet_pt'):
                    temp = ROOT.TH1F(k,k,(len(jet_pt_var_bin)-1),jet_pt_var_bin)
                    temp.Sumw2()
                elif(v == 'var_bin_jet_pt'):
                    temp = ROOT.TH1F(k,k,(len(jet_pt_var_bin)-1),jet_pt_var_bin)
                    temp.Sumw2()
                elif(v == 'jet_eta'):
                    temp = ROOT.TH1F(k,k,20,-4.5,4.5)
                    temp.Sumw2()
                elif(v == 'jet_phi'):
                    temp = ROOT.TH1F(k,k,10,-3.5,3.5)
                    temp.Sumw2()
                elif(v == 'jet_e'):
                    temp = ROOT.TH1F(k,k,20,25,2500)
                    temp.Sumw2()
                elif(v == 'jet_m'):
                    temp = ROOT.TH1F(k,k,5,0,150)
                    temp.Sumw2()
                elif(v == 'jet_n'):
                    temp = ROOT.TH1F(k,k,10,0,10)
                    temp.Sumw2()
                elif(v == 'sub_ljet_pt'):
                    temp = ROOT.TH1F(k,k,20,0,2000)
                    temp.Sumw2()
                elif(v == 'sub_ljet_eta'):
                    temp = ROOT.TH1F(k,k,10,-2.5,2.5)
                    temp.Sumw2()
                elif(v == 'sub_ljet_phi'):
                    temp = ROOT.TH1F(k,k,10,-3.5,3.5)
                    temp.Sumw2()
                elif(v == 'sub_ljet_e'):
                    temp = ROOT.TH1F(k,k,20,0,3000)
                    temp.Sumw2()
                elif(v == 'sub_ljet_m'):
                    temp = ROOT.TH1F(k,k,10,0,200)
                    temp.Sumw2()
                elif(v == 'VLQM'):
                    temp = ROOT.TH1F(k,k,(len(VLQM_var_bin)-1),VLQM_var_bin)
                    temp.Sumw2()
                elif(v == 'var_bin_VLQM'):
                    temp = ROOT.TH1F(k,k,(len(VLQM_var_bin)-1),VLQM_var_bin)
                    temp.Sumw2()
                elif(v == 'DeltaR'):
                    temp = ROOT.TH1F(k,k,10,0,5)
                    temp.Sumw2()
                elif(v == 'DeltaPhi'):
                    temp = ROOT.TH1F(k,k,10,-5,5)
                    temp.Sumw2()

                temp.Multiply(n1,n2)
                temp.Divide(d1)
                if(corr_type == "integral"):
                    temp.Scale(R[p])                                  #Implementing the Correlation factor to the distributions (Integral)
                    print "CORRELATION CALCULATION BY INTEGRAL"
                    print R[p],k
                elif(corr_type == "nocorr"):
                    print "NO CORRELATION CALCULATION"                #Implementing the Correlation factor to the distributions (No corr)
                else:
                    temp.Multiply(corr)
                    print "CORRELATION CALCULATION BY BIN BY BIN"     #Implementing the Correlation factor to the distributions (Bin by bin)
                temp.Write()
                p+=1
    
    f5.Close()
    print "Done!"



corr_type = sys.argv[1]
corr_cal = sys.argv[2]
makeHists(corr_type,corr_cal)


                    #if(v == 'ljet_pt'):
                    #    temp.Scale(72071ting all the statistics of all the regions along with the correlation factor


#region_complete = ['ljet_eta_2b_not_loose_Wtagged','ljet_eta_0b_not_loose_Wtagged','ljet_eta_0b_loose_not_tight_Wtagged','ljet_eta_0b_tight_Wtagged','ljet_eta_2b_tight_Wtagged','ljet_eta_2b_loose_not_tight_Wtagged']

#for r in region_complete:
#    print "=================================================================="
#    print r
#    print "Data = ",(f1.Get(r)).Integral()
#    print "Background = ",(f2.Get(r)).Integral()
#    print "Dijets MC = ",(f3.Get(r)).Integral()
#    print "Dijets Subtracted = ",(f5.Get(r)).Integral()
#    if 'not_loose' not in r:
#        if '0b' not in r:
#            print "Corelation Factor = ", R[s]
#            print "Dijets Estimated = ",(f5.Get(r)).Integral()
#            s+=1

