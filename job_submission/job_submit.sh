#tar -cvf $BUDDY/code_PFlow.tar code_PFlow
cd /gpfs/share/home/s6marahm/job_submit_systematics/
#condor_submit job_submit_btag_MC16a.jdl
#condor_submit job_submit_btag_MC16d.jdl
#condor_submit job_submit_btag_MC16e.jdl
#condor_submit job_submit_bkg_MC16a.jdl
#condor_submit job_submit_bkg_MC16d.jdl
#condor_submit job_submit_bkg_MC16e.jdl
condor_submit job_submit_sig_MC16a.jdl
condor_submit job_submit_sig_MC16d.jdl
condor_submit job_submit_sig_MC16e.jdl
cd ..
#condor_submit job_submit_bkg_MC16a.jdl
#condor_submit job_submit_bkg_MC16d.jdl
#condor_submit job_submit_bkg_MC16e.jdl
#condor_submit job_submit_data_MC16a.jdl
#condor_submit job_submit_data_MC16d.jdl
#condor_submit job_submit_data_MC16e.jdl