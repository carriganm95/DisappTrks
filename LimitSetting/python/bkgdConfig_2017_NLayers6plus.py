#!/usr/bin/env python

# Bkgd configuration file for limit-setting produced with makeANTables.py

backgrounds = {
    'Fake' : {
        'yield' : '0.02',
        'error' : str (1.0 - 0.02/0.2) + '/' + str(1.0 + 0.21/0.02),
    },
    'Elec' : {
        'N' : '33',
        'alpha' : '0.142867612755',
    },
    'Muon' : {
        'N' : '10',
        'alpha' : '0.0479208828347',
    },
    'Tau' : {
        'N' : '7',
        'alpha' : '0.0534253089594',
    },
}

background_systematics = {
    'Fake_alpha_NLayers6plus' : { # error on alpha
        'value' : '1.00053097569',
        'background' : 'Fake',
    },
    'Elec_alpha_NLayers6plus' : { # error on alpha
        'value' : '1.01047519123',
        'background' : 'Elec',
    },
    'Muon_alpha_NLayers6plus' : { # error on alpha
        'value' : '1.0034194308',
        'background' : 'Muon',
    },
    'Tau_alpha_NLayers6plus' : { # error on alpha
        'value' : '1.17312628559',
        'background' : 'Tau',
    },

    'Fake_syst_fit' : { # error from fit
        # correlated! between nlayers since it's the same value
        'value' : '1.38923987949',
        'background' : 'Fake',
    },
    'Fake_syst_sampleDiff_NLayers6plus' : { # difference between ZtoMuMu and ZtoEE methods
    'value' : str (1.0 + (0.07 - 0.02) / 0.02),
        'background' : 'Fake',
    },
    'Fake_syst_d0Extrapolation' : { # difference between (transfer factor) * (baseline sideband) and observed tracks |d0|<0.02cm
        # correlated! between nlayers since it's the same value
        'value' : str (1.0 + (32.6 - 32.0) / 32.0),
        'background' : 'Fake',
    },

    'Elec_energy_NLayers6plus' : { # error on energy assumption
        'value' : str (1.0 + 12.4474529027 / 100.0),
        'background' : 'Elec',
    },
    'Tau_energy_NLayers6plus' : { # error on energy assumption
        'value' : str (1.0 + 16.8609344527 / 100.0),
        'background' : 'Tau',
    },
}