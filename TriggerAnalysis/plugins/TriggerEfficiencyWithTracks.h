#ifndef TRIGGER_EFFICIENCY_WITH_TRACKS
#define TRIGGER_EFFICIENCY_WITH_TRACKS

#include <string>
#include <map>
#include <vector>

#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/TriggerObjectStandAlone.h"
#include "DataFormats/TrackReco/interface/Track.h"

#include "FWCore/Common/interface/TriggerNames.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"

#include "TH1D.h"

using namespace std;

class TriggerEfficiencyWithTracks : public edm::EDAnalyzer
{
  public:
    TriggerEfficiencyWithTracks (const edm::ParameterSet &);
    ~TriggerEfficiencyWithTracks ();

    void analyze (const edm::Event &, const edm::EventSetup &);

    static bool ptDescending (const reco::Track *, const reco::Track *);

  private:
    void logSpace (const unsigned, const double, const double, vector<double> &) const;
    void linSpace (const unsigned, const double, const double, vector<double> &) const;
    void fillHistograms (const vector<pat::MET> &, const vector<reco::Track> &, const string &) const;
    void fillHistograms (const vector<pat::MET> &, const reco::Track &, const string &) const;
    bool passesTriggerFilter (const edm::TriggerNames &, const vector<pat::TriggerObjectStandAlone> &, const string &) const;
    bool passesTrigger (const edm::TriggerNames &, const edm::TriggerResults &, const string &) const;
    double trackIsolation (const reco::Track &, const vector<reco::Track> &, const double, const double) const;
    bool genMatched (const reco::Track &, const vector<reco::GenParticle> &, const int, const int, const double) const;

    edm::InputTag  mets_;
    edm::InputTag  tracks_;
    edm::InputTag  triggerBits_;
    edm::InputTag  triggerObjs_;
    edm::InputTag  vertices_;
    edm::InputTag  genParticles_;

    edm::Service<TFileService> fs_;
    map<string, TH1D *> oneDHists_;
};

#endif