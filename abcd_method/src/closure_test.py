from ROOT import TFile, TTree, TH1, TH1F, TH2, TH2F, TCanvas, TPad, TPaveLabel, TLegend, TChain
from ROOT import gStyle, kBlue, kRed, gROOT
import math
import time
import os
import numpy as np
import ROOT
from array import array


#Data & background samples
f1 = TFile.Open('/cephfs/user/s6marahm/output/abcd_dijets.root',"update")
f2 = TFile.Open('/cephfs/user/s6marahm/output/abcd_312335.root',"update")
f4 = TFile.Open('/cephfs/user/s6marahm/output/abcd_312337.root',"update")
f5 = TFile.Open('/cephfs/user/s6marahm/output/abcd_background_closure_test_I.root',"update")
f3 = ROOT.TFile.Open('/cephfs/user/s6marahm/output/abcd_closure_test.root',"RECREATE")


bkg1 = f5.Get('jet_eta_2b_tight_Wtagged')
bkg2 = f5.Get('jet_eta_2b_loose_not_tight_Wtagged')
bkg3 = f5.Get('jet_eta_2b_not_loose_Wtagged')
bkg4 = f5.Get('jet_eta_0b_tight_Wtagged')
bkg5 = f5.Get('jet_eta_0b_loose_not_tight_Wtagged')
bkg6 = f5.Get('jet_eta_0b_not_loose_Wtagged')

#reg1 = f1.Get('jet_eta_2b_tight_Wtagged')
#reg2 = f1.Get('jet_eta_2b_loose_not_tight_Wtagged')
#reg3 = f1.Get('jet_eta_2b_not_loose_Wtagged')
#reg4 = f1.Get('jet_eta_0b_tight_Wtagged')
#reg5 = f1.Get('jet_eta_0b_loose_not_tight_Wtagged')
#reg6 = f1.Get('jet_eta_0b_not_loose_Wtagged')
#
#total = reg1.Integral() + reg2.Integral() + reg3.Integral() + reg4.Integral() + reg5.Integral() + reg6.Integral()
#
#temp  = TH2F( 'Dijets', 'W-tagging vs bjet multiplicity', 2, 0, 2, 3, 0, 3 )
#temp.Sumw2()
#temp.SetBinContent(1, 1, (reg1.Integral()*100)/total)
#print reg1.Integral()*100/total
#temp.SetBinContent(1, 2, (reg2.Integral()*100)/total)
#print reg2.Integral()*100/total
#temp.SetBinContent(1, 3, (reg3.Integral()*100)/total)
#print reg3.Integral()*100/total
#temp.SetBinContent(2, 1, (reg4.Integral()*100)/total)
#print reg4.Integral()*100/total
#temp.SetBinContent(2, 2, (reg5.Integral()*100)/total)
#print reg5.Integral()*100/total
#temp.SetBinContent(2, 3, (reg6.Integral()*100)/total)
#print reg6.Integral()*100/total
#
#temp.Write()

print '\n 312335'

reg1 = f2.Get('jet_eta_2b_tight_Wtagged')
reg2 = f2.Get('jet_eta_2b_loose_not_tight_Wtagged')
reg3 = f2.Get('jet_eta_2b_not_loose_Wtagged')
reg4 = f2.Get('jet_eta_0b_tight_Wtagged')
reg5 = f2.Get('jet_eta_0b_loose_not_tight_Wtagged')
reg6 = f2.Get('jet_eta_0b_not_loose_Wtagged')

total = reg1.Integral() + reg2.Integral() + reg3.Integral() + reg4.Integral() + reg5.Integral() + reg6.Integral()

temp  = TH2F( '312335', 'W-tagging vs bjet multiplicity', 2, 0, 2, 3, 0, 3 )
temp.Sumw2()
temp.SetBinContent(1, 1, (reg1.Integral())/math.sqrt(bkg1.Integral()))
print 'jet_eta_2b_tight_Wtagged', reg1.Integral()/math.sqrt(bkg1.Integral())
temp.SetBinContent(1, 2, (reg2.Integral())/math.sqrt(bkg2.Integral()))
print 'jet_eta_2b_loose_not_tight_Wtagged', reg2.Integral()/math.sqrt(bkg2.Integral())
temp.SetBinContent(1, 3, (reg3.Integral())/math.sqrt(bkg3.Integral()))
print 'jet_eta_2b_not_loose_Wtagged', reg3.Integral()/math.sqrt(bkg3.Integral())
temp.SetBinContent(2, 1, (reg4.Integral())/math.sqrt(bkg4.Integral()))
print 'jet_eta_0b_tight_Wtagged', reg4.Integral()/math.sqrt(bkg4.Integral())
temp.SetBinContent(2, 2, (reg5.Integral())/math.sqrt(bkg5.Integral()))
print 'jet_eta_0b_loose_not_tight_Wtagged', reg5.Integral()/math.sqrt(bkg5.Integral())
temp.SetBinContent(2, 3, (reg6.Integral())/math.sqrt(bkg6.Integral()))
print 'jet_eta_0b_not_loose_Wtagged', reg6.Integral()/math.sqrt(bkg6.Integral())

temp.Write()


print '\n 312337'


reg1 = f4.Get('jet_eta_2b_tight_Wtagged')
reg2 = f4.Get('jet_eta_2b_loose_not_tight_Wtagged')
reg3 = f4.Get('jet_eta_2b_not_loose_Wtagged')
reg4 = f4.Get('jet_eta_0b_tight_Wtagged')
reg5 = f4.Get('jet_eta_0b_loose_not_tight_Wtagged')
reg6 = f4.Get('jet_eta_0b_not_loose_Wtagged')

total = reg1.Integral() + reg2.Integral() + reg3.Integral() + reg4.Integral() + reg5.Integral() + reg6.Integral()

temp  = TH2F( '312337', 'W-tagging vs bjet multiplicity', 2, 0, 2, 3, 0, 3 )
temp.Sumw2()
temp.SetBinContent(1, 1, (reg1.Integral())/math.sqrt(bkg1.Integral()))
print 'jet_eta_2b_tight_Wtagged', reg1.Integral()/math.sqrt(bkg1.Integral())
temp.SetBinContent(1, 2, (reg2.Integral())/math.sqrt(bkg2.Integral()))
print 'jet_eta_2b_loose_not_tight_Wtagged', reg2.Integral()/math.sqrt(bkg2.Integral())
temp.SetBinContent(1, 3, (reg3.Integral())/math.sqrt(bkg3.Integral()))
print 'jet_eta_2b_not_loose_Wtagged', reg3.Integral()/math.sqrt(bkg3.Integral())
temp.SetBinContent(2, 1, (reg4.Integral())/math.sqrt(bkg4.Integral()))
print 'jet_eta_0b_tight_Wtagged', reg4.Integral()/math.sqrt(bkg4.Integral())
temp.SetBinContent(2, 2, (reg5.Integral())/math.sqrt(bkg5.Integral()))
print 'jet_eta_0b_loose_not_tight_Wtagged', reg5.Integral()/math.sqrt(bkg5.Integral())
temp.SetBinContent(2, 3, (reg6.Integral())/math.sqrt(bkg6.Integral()))
print 'jet_eta_0b_not_loose_Wtagged', reg6.Integral()/math.sqrt(bkg6.Integral())

temp.Write()



'''
reg1 = f4.Get('jet_eta_2b_tight_Wtagged')
reg2 = f4.Get('jet_eta_2b_loose_not_tight_Wtagged')
reg3 = f4.Get('jet_eta_2b_not_loose_Wtagged')
reg4 = f4.Get('jet_eta_1b_tight_Wtagged')
reg5 = f4.Get('jet_eta_1b_loose_not_tight_Wtagged')
reg6 = f4.Get('jet_eta_1b_not_loose_Wtagged')
reg7 = f4.Get('jet_eta_0b_tight_Wtagged')
reg8 = f4.Get('jet_eta_0b_loose_not_tight_Wtagged')
reg9 = f4.Get('jet_eta_0b_not_loose_Wtagged')

total = reg1.Integral() + reg2.Integral() + reg3.Integral() + reg4.Integral() + reg5.Integral() + reg6.Integral() + reg7.Integral() + reg8.Integral() + reg9.Integral()

temp  = TH2F( '310497', 'W-tagging vs bjet multiplicity', 3, 0, 3, 3, 0, 3 )
temp.Sumw2()
temp.SetBinContent(1, 1, (reg1.Integral()*100)/total)
temp.SetBinContent(1, 2, (reg2.Integral()*100)/total)
temp.SetBinContent(1, 3, (reg3.Integral()*100)/total)
temp.SetBinContent(2, 1, (reg4.Integral()*100)/total)
temp.SetBinContent(2, 2, (reg5.Integral()*100)/total)
temp.SetBinContent(2, 3, (reg6.Integral()*100)/total)
temp.SetBinContent(3, 1, (reg7.Integral()*100)/total)
temp.SetBinContent(3, 2, (reg8.Integral()*100)/total)
temp.SetBinContent(3, 3, (reg9.Integral()*100)/total)

temp.Write()




reg1 = f2.Get('jet_eta_2b_tight_Wtagged')
reg2 = f2.Get('jet_eta_2b_loose_not_tight_Wtagged')
reg3 = f2.Get('jet_eta_2b_not_loose_Wtagged')
reg4 = f2.Get('jet_eta_1b_tight_Wtagged')
reg5 = f2.Get('jet_eta_1b_loose_not_tight_Wtagged')
reg6 = f2.Get('jet_eta_1b_not_loose_Wtagged')
reg7 = f2.Get('jet_eta_0b_tight_Wtagged')
reg8 = f2.Get('jet_eta_0b_loose_not_tight_Wtagged')
reg9 = f2.Get('jet_eta_0b_not_loose_Wtagged')

total = reg1.Integral() + reg2.Integral() + reg3.Integral() + reg4.Integral() + reg5.Integral() + reg6.Integral() + reg7.Integral() + reg8.Integral() + reg9.Integral()

temp  = TH2F( '310562', 'W-tagging vs bjet multiplicity', 3, 0, 3, 3, 0, 3 )
temp.Sumw2()
temp.SetBinContent(1, 1, (reg1.Integral()*100)/total)
temp.SetBinContent(1, 2, (reg2.Integral()*100)/total)
temp.SetBinContent(1, 3, (reg3.Integral()*100)/total)
temp.SetBinContent(2, 1, (reg4.Integral()*100)/total)
temp.SetBinContent(2, 2, (reg5.Integral()*100)/total)
temp.SetBinContent(2, 3, (reg6.Integral()*100)/total)
temp.SetBinContent(3, 1, (reg7.Integral()*100)/total)
temp.SetBinContent(3, 2, (reg8.Integral()*100)/total)
temp.SetBinContent(3, 3, (reg9.Integral()*100)/total)

temp.Write()





reg1 = f5.Get('jet_phi_2b_tight_Wtagged')
reg2 = f5.Get('jet_phi_2b_loose_not_tight_Wtagged')
reg3 = f5.Get('jet_phi_2b_not_loose_Wtagged')
reg4 = f5.Get('jet_phi_1b_tight_Wtagged')
reg5 = f5.Get('jet_phi_1b_loose_not_tight_Wtagged')
reg6 = f5.Get('jet_phi_1b_not_loose_Wtagged')
reg7 = f5.Get('jet_phi_0b_tight_Wtagged')
reg8 = f5.Get('jet_phi_0b_loose_not_tight_Wtagged')
reg9 = f5.Get('jet_phi_0b_not_loose_Wtagged')

total = reg1.Integral() + reg2.Integral() + reg3.Integral() + reg4.Integral() + reg5.Integral() + reg6.Integral() + reg7.Integral() + reg8.Integral() + reg9.Integral()

temp  = TH2F( 'dijets', 'W-tagging vs bjet multiplicity', 3, 0, 3, 3, 0, 3 )
temp.Sumw2()
temp.SetBinContent(1, 1, (reg1.Integral()*100)/total)
temp.SetBinContent(1, 2, (reg2.Integral()*100)/total)
temp.SetBinContent(1, 3, (reg3.Integral()*100)/total)
temp.SetBinContent(2, 1, (reg4.Integral()*100)/total)
temp.SetBinContent(2, 2, (reg5.Integral()*100)/total)
temp.SetBinContent(2, 3, (reg6.Integral()*100)/total)
temp.SetBinContent(3, 1, (reg7.Integral()*100)/total)
temp.SetBinContent(3, 2, (reg8.Integral()*100)/total)
temp.SetBinContent(3, 3, (reg9.Integral()*100)/total)

temp.Write()
'''

f3.Close()
print "Done!"