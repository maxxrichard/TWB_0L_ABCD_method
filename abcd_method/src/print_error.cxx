#include <iostream>
#include <string>
#include <TFile.h>
#include <TH1D.h>
#include <TStyle.h>
#include <THStack.h>
#include <TCanvas.h>

using namespace std;


void print_error(){

    string region[] = {"ljet_eta_2b_tight_Wtagged","ljet_eta_2b_loose_not_tight_Wtagged","ljet_eta_2b_not_loose_Wtagged","ljet_eta_0b_not_loose_Wtagged","ljet_eta_0b_loose_not_tight_Wtagged","ljet_eta_0b_tight_Wtagged"};
    //string region[] = {"ljet_eta_2b_loose_not_tight_Wtagged","ljet_eta_2b_not_loose_Wtagged","ljet_eta_0b_not_loose_Wtagged","ljet_eta_0b_loose_not_tight_Wtagged"};
    //string region[] = {"ljet_pt_2b_loose_not_tight_Wtagged","ljet_m_2b_loose_not_tight_Wtagged","ljet_eta_2b_loose_not_tight_Wtagged","jet_pt_2b_loose_not_tight_Wtagged","jet_m_2b_loose_not_tight_Wtagged","VLQM_2b_loose_not_tight_Wtagged",};


    TFile *file_data = TFile::Open("/cephfs/user/s6marahm/output/abcd_data.root");
    TFile *file_Wt = TFile::Open("/cephfs/user/s6marahm/output/abcd_Wt.root");
    TFile *file_Wjets = TFile::Open("/cephfs/user/s6marahm/output/abcd_Wjets.root");
    TFile *file_Zjets = TFile::Open("/cephfs/user/s6marahm/output/abcd_Zjets.root");
    TFile *file_ttbar = TFile::Open("/cephfs/user/s6marahm/output/abcd_ttbar.root");
    TFile *file_dijets = TFile::Open("/cephfs/user/s6marahm/output/abcd_dijets.root");


    Double_t error;
    Double_t integral;

   
    for(int i=0;i<6;i++)
    {
        cout<<"==================================================================================================="<<endl;
        cout<<region[i]<<endl;

        TH1F* top = (TH1F*)file_data->Get((region[i]).c_str());
        integral = top->IntegralAndError(0,100,error);
        cout<<"Data = "<<integral<<" +- "<<error<<endl;

        TH1F* top1 = (TH1F*)file_Wt->Get((region[i]).c_str());
        integral = top1->IntegralAndError(0,100,error);
        cout<<"Wt = "<<integral<<" +- "<<error<<endl;

        TH1F* top2 = (TH1F*)file_Wjets->Get((region[i]).c_str());
        integral = top2->IntegralAndError(0,100,error);
        cout<<"W+jets = "<<integral<<" +- "<<error<<endl;

        TH1F* top3 = (TH1F*)file_Zjets->Get((region[i]).c_str());
        integral = top3->IntegralAndError(0,100,error);
        cout<<"Z+jets = "<<integral<<" +- "<<error<<endl;

        TH1F* top4 = (TH1F*)file_ttbar->Get((region[i]).c_str());
        integral = top4->IntegralAndError(0,100,error);
        cout<<"ttbar = "<<integral<<" +- "<<error<<endl;

        TH1F* top5 = (TH1F*)file_dijets->Get((region[i]).c_str());
        integral = top5->IntegralAndError(0,100,error);
        cout<<"Dijets = "<<integral<<" +- "<<error<<endl;
    }

    //file->Close();

}
    
