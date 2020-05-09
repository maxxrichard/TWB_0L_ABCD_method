
cd /cephfs/user/s6marahm/output
rm -rf abcd_data.root abcd_dijets.root abcd_Wt.root abcd_ttbar.root abcd_Wjets.root abcd_Zjets.root abcd_background.root abcd_correlation.root
cp orig/abcd_data.root .
cp orig/abcd_dijets.root .
cp orig/abcd_Wt.root .
cp orig/abcd_ttbar.root .
cp orig/abcd_Wjets.root .
cp orig/abcd_Zjets.root .
cp orig/abcd_background.root .
cp orig/abcd_312335.root .
#cp orig/abcd_312337.root .

cd /cephfs/user/s6marahm/src
python variable_binning.py

#python abcd_sr_propagating_sf.py

python abcd.py binbybin prefit
cd /cephfs/user/s6marahm/TRExFitter
trex-fitter -hd VR_abcd_prefit_binbybin.config

cd /cephfs/user/s6marahm/output
mv abcd_output.root abcd_output_prefit_binbybin.root
rm -rf abcd_correlation.root

cd /cephfs/user/s6marahm/src
python abcd.py integral prefit 
cd /cephfs/user/s6marahm/TRExFitter
trex-fitter -hd VR_abcd_prefit_integral.config

cd /cephfs/user/s6marahm/output
mv abcd_output.root abcd_output_prefit_integral.root
rm -rf abcd_correlation.root

cd /cephfs/user/s6marahm/src
python abcd.py nocorr prefit 
cd /cephfs/user/s6marahm/TRExFitter
trex-fitter -hd VR_abcd_no_corr.config

cd /cephfs/user/s6marahm/output
mv abcd_output.root abcd_output_no_corr.root
rm -rf abcd_correlation.root abcd_dijets_postfit.root

cd /cephfs/user/s6marahm/src
source fitting.sh

cd /cephfs/user/s6marahm/src
python abcd.py binbybin postfit
cd /cephfs/user/s6marahm/TRExFitter
trex-fitter -hd VR_abcd_postfit_binbybin.config

cd /cephfs/user/s6marahm/output
mv abcd_output.root abcd_output_postfit_binbybin.root
rm -rf abcd_correlation.root

cd /cephfs/user/s6marahm/src
python abcd.py integral postfit 
cd /cephfs/user/s6marahm/TRExFitter
trex-fitter -hd VR_abcd_postfit_integral.config

cd /cephfs/user/s6marahm/output
mv abcd_output.root abcd_output_postfit_integral.root

cd /cephfs/user/s6marahm/src




