cd /cephfs/user/s6marahm/output

hadd -f abcd_data_MC16a.root abcd_periodA.grp16_MC16a.root abcd_periodB.grp16_MC16a.root abcd_periodC.grp16_MC16a.root abcd_periodD.grp15_MC16a.root abcd_periodD.grp16_MC16a.root abcd_periodE.grp15_MC16a.root abcd_periodE.grp16_MC16a.root abcd_periodF.grp15_MC16a.root abcd_periodF.grp16_MC16a.root abcd_periodG.grp15_MC16a.root abcd_periodG.grp16_MC16a.root abcd_periodH.grp15_MC16a.root abcd_periodI.grp16_MC16a.root abcd_periodJ.grp15_MC16a.root abcd_periodK.grp16_MC16a.root abcd_periodL.grp16_MC16a.root
hadd -f abcd_data_MC16d.root abcd_periodB.grp17_MC16d.root abcd_periodC.grp17_MC16d.root abcd_periodD.grp17_MC16d.root abcd_periodE.grp17_MC16d.root abcd_periodF.grp17_MC16d.root abcd_periodH.grp17_MC16d.root abcd_periodI.grp17_MC16d.root abcd_periodK.grp17_MC16d.root
hadd -f abcd_data_MC16e.root abcd_periodB.grp18_MC16e.root abcd_periodC.grp18_MC16e.root abcd_periodD.grp18_MC16e.root abcd_periodF.grp18_MC16e.root abcd_periodI.grp18_MC16e.root abcd_periodK.grp18_MC16e.root abcd_periodL.grp18_MC16e.root abcd_periodM.grp18_MC16e.root abcd_periodO.grp18_MC16e.root abcd_periodQ.grp18_MC16e.root

#hadd -f abcd_dijets_MC16a.root abcd_3647??_MC16a.root
#hadd -f abcd_dijets_MC16d.root abcd_3647??_MC16d.root 
#hadd -f abcd_dijets_MC16e.root abcd_3647??_MC16e.root

hadd -f abcd_ttbar_MC16a.root abcd_410471_MC16a.root
hadd -f abcd_ttbar_MC16d.root abcd_410471_MC16d.root
hadd -f abcd_ttbar_MC16e.root abcd_410471_MC16e.root

hadd -f abcd_Wt_MC16a.root abcd_410646_MC16a.root abcd_410647_MC16a.root
hadd -f abcd_Wt_MC16d.root abcd_410646_MC16d.root abcd_410647_MC16d.root
hadd -f abcd_Wt_MC16e.root abcd_410646_MC16e.root abcd_410647_MC16e.root

hadd -f abcd_Zjets_MC16a.root abcd_364375_MC16a.root abcd_364376_MC16a.root abcd_364377_MC16a.root
hadd -f abcd_Zjets_MC16d.root abcd_364375_MC16d.root abcd_364376_MC16d.root abcd_364377_MC16d.root
hadd -f abcd_Zjets_MC16e.root abcd_364375_MC16e.root abcd_364376_MC16e.root abcd_364377_MC16e.root

hadd -f abcd_Wjets_MC16a.root abcd_364378_MC16a.root abcd_364379_MC16a.root abcd_364380_MC16a.root
hadd -f abcd_Wjets_MC16d.root abcd_364378_MC16d.root abcd_364379_MC16d.root abcd_364380_MC16d.root
hadd -f abcd_Wjets_MC16e.root abcd_364378_MC16e.root abcd_364379_MC16e.root abcd_364380_MC16e.root

hadd -f abcd_background_MC16a.root abcd_ttbar_MC16a.root abcd_Wt_MC16a.root abcd_Zjets_MC16a.root abcd_Wjets_MC16a.root
hadd -f abcd_background_MC16d.root abcd_ttbar_MC16d.root abcd_Wt_MC16d.root abcd_Zjets_MC16d.root abcd_Wjets_MC16d.root
hadd -f abcd_background_MC16e.root abcd_ttbar_MC16e.root abcd_Wt_MC16e.root abcd_Zjets_MC16e.root abcd_Wjets_MC16e.root

hadd -f abcd_data.root abcd_data_MC16a.root abcd_data_MC16d.root abcd_data_MC16e.root
#hadd -f abcd_dijets.root abcd_dijets_MC16a.root abcd_dijets_MC16d.root abcd_dijets_MC16e.root
hadd -f abcd_ttbar.root abcd_ttbar_MC16a.root abcd_ttbar_MC16d.root abcd_ttbar_MC16e.root
hadd -f abcd_Wt.root abcd_Wt_MC16a.root abcd_Wt_MC16d.root abcd_Wt_MC16e.root
hadd -f abcd_Zjets.root abcd_Zjets_MC16a.root abcd_Zjets_MC16d.root abcd_Zjets_MC16e.root
hadd -f abcd_Wjets.root abcd_Wjets_MC16a.root abcd_Wjets_MC16d.root abcd_Wjets_MC16e.root
hadd -f abcd_background.root abcd_background_MC16a.root abcd_background_MC16d.root abcd_background_MC16e.root 

#hadd -f abcd_312335.root abcd_312335_MC16a.root abcd_312335_MC16d.root abcd_312335_MC16e.root
#hadd -f abcd_312336.root abcd_312336_MC16a.root abcd_312336_MC16d.root abcd_312336_MC16e.root
#hadd -f abcd_312337.root abcd_312337_MC16a.root abcd_312337_MC16d.root abcd_312337_MC16e.root
#hadd -f abcd_312338.root abcd_312338_MC16a.root abcd_312338_MC16d.root abcd_312338_MC16e.root
#hadd -f abcd_312339.root abcd_312339_MC16a.root abcd_312339_MC16d.root abcd_312339_MC16e.root
#hadd -f abcd_312340.root abcd_312340_MC16a.root abcd_312340_MC16d.root abcd_312340_MC16e.root
#hadd -f abcd_312341.root abcd_312341_MC16a.root abcd_312341_MC16d.root abcd_312341_MC16e.root

mkdir orig
cp abcd_data.root orig/
cp abcd_dijets.root orig/
cp abcd_ttbar.root orig/
cp abcd_Wt.root orig/
cp abcd_Zjets.root orig/
cp abcd_Wjets.root orig/
cp abcd_background.root orig/
cp abcd_312335.root orig/
#cp abcd_312336.root orig/
#cp abcd_312337.root orig/
#cp abcd_312338.root orig/
#cp abcd_312339.root orig/
#cp abcd_312340.root orig/
#cp abcd_312341.root orig/



