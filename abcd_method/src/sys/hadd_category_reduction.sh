
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


hadd -f abcd_ttbar.root abcd_ttbar_MC16a.root abcd_ttbar_MC16d.root abcd_ttbar_MC16e.root
hadd -f abcd_Wt.root abcd_Wt_MC16a.root abcd_Wt_MC16d.root abcd_Wt_MC16e.root
hadd -f abcd_Zjets.root abcd_Zjets_MC16a.root abcd_Zjets_MC16d.root abcd_Zjets_MC16e.root
hadd -f abcd_Wjets.root abcd_Wjets_MC16a.root abcd_Wjets_MC16d.root abcd_Wjets_MC16e.root
hadd -f abcd_background.root abcd_background_MC16a.root abcd_background_MC16d.root abcd_background_MC16e.root 

mkdir orig
cp abcd_ttbar.root orig/
cp abcd_Wt.root orig/
cp abcd_Zjets.root orig/
cp abcd_Wjets.root orig/
cp abcd_background.root orig/