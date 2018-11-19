import FWCore.ParameterSet.Config as cms

dturosunpacker = cms.EDProducer("DTuROSRawToDigi",
                                  DTuROS_FED_Source = cms.InputTag("source"),
                                  feds     = cms.untracked.vint32( 0,),
                                  debug = cms.untracked.bool(True),
                               )