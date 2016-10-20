import FWCore.ParameterSet.Config as cms
import copy
from DisappTrks.StandardAnalysis.Cuts import * # Put all the individual cuts in this file
from DisappTrks.StandardAnalysis.EventSelections import *  # Get the composite cut definitions

################################################################################
## Muon tag skim
################################################################################
MuonTagSkim = cms.PSet(
    name = cms.string("MuonTagSkim"),
    triggers = triggersSingleMu2016,
    cuts = cms.VPSet (),
)
# See SMP-12-023 for example of W->mu nu selection
tagMuonCuts = [
    cutMuonPt25,
    cutMuonEta21,
    cutMuonTightID,
    cutMuonTightPFIso,
]
addCuts(MuonTagSkim.cuts, tagMuonCuts)

##################################################
## Higher pt to be closer to candidate track selection
##################################################
MuonTagPt35 = copy.deepcopy(MuonTagSkim)
MuonTagPt35.name = cms.string("MuonTagPt35")
addSingleCut(MuonTagPt35.cuts, cutMuonPt35, cutMuonPt25)
cutsToAdd = [
    cutMuonArbitration,
    cutJetPt,
    cutJetEta,
    cutJetTightLepVeto,
    cutDijetDeltaPhiMax,
    cutTrkPt35,
    cutTrkMuDR0p1,
    cutTrkMatchRecoMu,
    cutTrkEta,
    cutTrkEcalGapVeto,
    cutTrkEtaMuonIneff1,
    cutTrkEtaMuonIneff2,
    cutTrkTOBCrack,
    cutTrkFiducialElectron,
    cutTrkFiducialMuon,
    cutTrkFiducialECAL,
    cutTrkNValidHits,
    cutTrkNMissIn,
    cutTrkNMissMid,
    cutTrkIso,
    cutTrkD0,
    cutTrkDZ,
    cutTrkJetDeltaPhi,
]
addCuts(MuonTagPt35.cuts, cutsToAdd)
cutsToRemove = [
    cutMuonPt25,
    ]
removeCuts(MuonTagPt35.cuts, cutsToRemove)

MuonTagPt35NoTrig = copy.deepcopy(MuonTagPt35)
MuonTagPt35NoTrig.name = cms.string("MuonTagPt35NoTrig")
MuonTagPt35NoTrig.triggers = cms.vstring()

MuonTagPt35MetTrig = copy.deepcopy(MuonTagPt35)
MuonTagPt35MetTrig.name = cms.string("MuonTagPt35MetTrig")
MuonTagPt35MetTrig.triggers = triggersMet

MuonTagPt35MetCut = copy.deepcopy(MuonTagPt35)
MuonTagPt35MetCut.name = cms.string("MuonTagPt35MetCut")
cutsToAdd = [
    cutMuonMetMinusOne,
]
addCuts(MuonTagPt35MetCut.cuts, cutsToAdd)

##################################################
## Channels for real life background estimate. Increase pt threshold to that
## used in search region and add missing outer hits cut.
##################################################
MuonTagPt55 = copy.deepcopy(MuonTagPt35)
MuonTagPt55.name = cms.string("MuonTagPt55")
addSingleCut(MuonTagPt55.cuts, cutTrkPt55, cutTrkPt35)
cutsToAdd = [
    cutTrkEcalo,
    cutTrkNMissOut,
    #cutTrkNMissOutInv
]
addCuts(MuonTagPt55.cuts, cutsToAdd)
cutsToRemove = [
    cutTrkPt35,
]
removeCuts(MuonTagPt55.cuts, cutsToRemove)

MuonTagPt55NoTrig = copy.deepcopy(MuonTagPt55)
MuonTagPt55NoTrig.name = cms.string("MuonTagPt55NoTrig")
MuonTagPt55NoTrig.triggers = cms.vstring()

MuonTagPt55MetTrig = copy.deepcopy(MuonTagPt55)
MuonTagPt55MetTrig.name = cms.string("MuonTagPt55MetTrig")
MuonTagPt55MetTrig.triggers = triggersMet

MuonTagPt55MetCut = copy.deepcopy(MuonTagPt55)
MuonTagPt55MetCut.name = cms.string("MuonTagPt55MetCut")
cutsToAdd = [
    cutMuonMetMinusOne,
]
addCuts(MuonTagPt55MetCut.cuts, cutsToAdd)

MuonTagPt55NoNMissOut = copy.deepcopy(MuonTagPt55)
MuonTagPt55NoNMissOut.name = cms.string("MuonTagPt55NoNMissOut")
removeCuts(MuonTagPt55NoNMissOut.cuts, [cutTrkNMissOut])

MuonTagPt55NoNMissOutMetTrig = copy.deepcopy(MuonTagPt55NoNMissOut)
MuonTagPt55NoNMissOutMetTrig.name = cms.string("MuonTagPt55NoNMissOutMetTrig")
MuonTagPt55NoNMissOutMetTrig.triggers = triggersMet


################################################################################
## Muon tag and probe sample
################################################################################
ZtoMuIsoTrk = copy.deepcopy(MuonTagSkim)
ZtoMuIsoTrk.name = cms.string("ZtoMuIsoTrk")

muTrkCuts = [
    cutMuTrkInvMass10,
]
addCuts(ZtoMuIsoTrk.cuts, [cutMuonArbitration])
addCuts(ZtoMuIsoTrk.cuts, [cutTrkPt30])
addCuts(ZtoMuIsoTrk.cuts, isoTrkCuts)
addCuts(ZtoMuIsoTrk.cuts, muTrkCuts)
cutsToRemove = [
    cutTrkPt55,
]
removeCuts(ZtoMuIsoTrk.cuts, cutsToRemove)

ZtoMuProbeTrk = copy.deepcopy(ZtoMuIsoTrk)
ZtoMuProbeTrk.name = cms.string("ZtoMuProbeTrk")

cutsToAdd = [
    cutTrkElecVeto,
    cutTrkTauHadVeto,
    cutTrkEcalo,
]
addCuts(ZtoMuProbeTrk.cuts, cutsToAdd)
addCuts(ZtoMuProbeTrk.cuts, [cutTrkArbitration])

ZtoMuProbeTrkWithZCuts = copy.deepcopy(ZtoMuProbeTrk)
ZtoMuProbeTrkWithZCuts.name = cms.string("ZtoMuProbeTrkWithZCuts")
cutsToAdd = [
    cutMuTrkInvMass80To100,
    cutMuTrkOS,
]
addCuts(ZtoMuProbeTrkWithZCuts.cuts, cutsToAdd)

MuonFiducialCalcBefore = copy.deepcopy(ZtoMuProbeTrkWithZCuts)
MuonFiducialCalcBefore.name = cms.string("MuonFiducialCalcBefore")
removeCuts(MuonFiducialCalcBefore.cuts, [cutTrkFiducialElectron, cutTrkFiducialMuon])

ZtoMuProbeTrkTightVeto = copy.deepcopy(ZtoMuProbeTrkWithZCuts)
ZtoMuProbeTrkTightVeto.name = cms.string("ZtoMuProbeTrkTightVeto")
addCuts(ZtoMuProbeTrkTightVeto.cuts, [cutTrkTightMuonVeto])

ZtoMuDisTrk = copy.deepcopy(ZtoMuProbeTrkWithZCuts)
ZtoMuDisTrk.name = cms.string("ZtoMuDisTrk")
cutsToAdd = [
    cutTrkMuonVeto,
]
addCuts(ZtoMuDisTrk.cuts, cutsToAdd)

ZtoMuDisTrkLooseVeto = copy.deepcopy(ZtoMuProbeTrkWithZCuts)
ZtoMuDisTrkLooseVeto.name = cms.string("ZtoMuDisTrkLooseVeto")
addCuts(ZtoMuDisTrkLooseVeto.cuts, [cutTrkLooseMuonVeto])

MuonFiducialCalcAfter = copy.deepcopy(ZtoMuDisTrkLooseVeto)
MuonFiducialCalcAfter.name = cms.string("MuonFiducialCalcAfter")
removeCuts(MuonFiducialCalcAfter.cuts, [cutTrkFiducialElectron, cutTrkFiducialMuon])

##################################################
## Fake track control sample:  start with Z->mu mu events
##################################################
ZtoMuMu = cms.PSet(
    name = cms.string("ZtoMuMu"),
    triggers = triggersSingleMu2016,
    cuts = cms.VPSet (
        cutMuonPairPt25,
        cutMuonPairEta21,
        cutMuonPairTightID,
        cutMuonPairTightPFIso,
        cutMuMuChargeProduct,
        cutMuMuInvMassZLo,
        cutMuMuInvMassZHi,
    )
)


##################################################
## Fake track control sample:  Z->mu mu + candidate track
##################################################
ZtoMuMuCandTrk = copy.deepcopy(ZtoMuMu)
ZtoMuMuCandTrk.name = cms.string("ZtoMuMuCandTrk")
addCuts(ZtoMuMuCandTrk.cuts, candTrkCuts)


##################################################
## Fake track control sample:  Z->mu mu + disappearing track
##################################################
ZtoMuMuDisTrk = copy.deepcopy(ZtoMuMu)
ZtoMuMuDisTrk.name = cms.string("ZtoMuMuDisTrk")
addCuts(ZtoMuMuDisTrk.cuts, disTrkCuts)

##################################################
## Fake track control sample:  Z->mu mu + candidate track in Ecalo sideband
##################################################
ZtoMuMuCandTrkEcaloSdband = copy.deepcopy(ZtoMuMu)
ZtoMuMuCandTrkEcaloSdband.name = cms.string("ZtoMuMuCandTrkEcaloSdband")
addCuts(ZtoMuMuCandTrkEcaloSdband.cuts, candTrkEcaloSdbandCuts)

##################################################
## Fake track control sample:  Z->mu mu + candidate track in NMissOut sideband
##################################################
ZtoMuMuCandTrkNMissOutSdband = copy.deepcopy(ZtoMuMu)
ZtoMuMuCandTrkNMissOutSdband.name = cms.string("ZtoMuMuCandTrkNMissOutSdband")
addCuts(ZtoMuMuCandTrkNMissOutSdband.cuts, candTrkNMissOutSdbandCuts)

##################################################
## Fake track control sample:  Z->mu mu + disappearing track with 3 hits
##################################################
ZtoMuMuDisTrkNHits3 = copy.deepcopy(ZtoMuMuDisTrk)
ZtoMuMuDisTrkNHits3.name = cms.string("ZtoMuMuDisTrkNHits3")
cutsToRemove = [
    cutTrkNValidHits,
]
cutsToAdd = [
    cutTrkNValidHits3,
]
removeCuts(ZtoMuMuDisTrkNHits3.cuts, cutsToRemove)
addCuts   (ZtoMuMuDisTrkNHits3.cuts, cutsToAdd)

##################################################
## Fake track control sample:  Z->mu mu + disappearing track with 4 hits
##################################################
ZtoMuMuDisTrkNHits4 = copy.deepcopy(ZtoMuMuDisTrk)
ZtoMuMuDisTrkNHits4.name = cms.string("ZtoMuMuDisTrkNHits4")
cutsToRemove = [
    cutTrkNValidHits,
]
cutsToAdd = [
    cutTrkNValidHits4,
]
removeCuts(ZtoMuMuDisTrkNHits4.cuts, cutsToRemove)
addCuts   (ZtoMuMuDisTrkNHits4.cuts, cutsToAdd)

##################################################
## Fake track control sample:  Z->mu mu + disappearing track with 5 hits
##################################################
ZtoMuMuDisTrkNHits5 = copy.deepcopy(ZtoMuMuDisTrk)
ZtoMuMuDisTrkNHits5.name = cms.string("ZtoMuMuDisTrkNHits5")
cutsToRemove = [
    cutTrkNValidHits,
]
cutsToAdd = [
    cutTrkNValidHits5,
]
removeCuts(ZtoMuMuDisTrkNHits5.cuts, cutsToRemove)
addCuts   (ZtoMuMuDisTrkNHits5.cuts, cutsToAdd)

##################################################
## Fake track control sample:  Z->mu mu + disappearing track with 6 hits
##################################################
ZtoMuMuDisTrkNHits6 = copy.deepcopy(ZtoMuMuDisTrk)
ZtoMuMuDisTrkNHits6.name = cms.string("ZtoMuMuDisTrkNHits6")
cutsToRemove = [
    cutTrkNValidHits,
]
cutsToAdd = [
    cutTrkNValidHits6,
]
removeCuts(ZtoMuMuDisTrkNHits6.cuts, cutsToRemove)
addCuts   (ZtoMuMuDisTrkNHits6.cuts, cutsToAdd)