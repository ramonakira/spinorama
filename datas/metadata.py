# -*- coding: utf-8 -*-

from . import SpeakerDatabase

# database
from .metadata_a import speakers_info_a
from .metadata_b import speakers_info_b
from .metadata_c import speakers_info_c
from .metadata_d import speakers_info_d
from .metadata_e import speakers_info_e
from .metadata_f import speakers_info_f
from .metadata_g import speakers_info_g
from .metadata_h import speakers_info_h
from .metadata_i import speakers_info_i
from .metadata_j import speakers_info_j
from .metadata_k import speakers_info_k
from .metadata_l import speakers_info_l
from .metadata_m import speakers_info_m
from .metadata_n import speakers_info_n
from .metadata_o import speakers_info_o
from .metadata_p import speakers_info_p
from .metadata_q import speakers_info_q
from .metadata_r import speakers_info_r
from .metadata_s import speakers_info_s
from .metadata_t import speakers_info_t
from .metadata_u import speakers_info_u
from .metadata_v import speakers_info_v
from .metadata_w import speakers_info_w
from .metadata_x import speakers_info_x
from .metadata_y import speakers_info_y
from .metadata_z import speakers_info_z

speakers_info_misc: SpeakerDatabase = {
    "理性派HiFi X5": {
        "brand": "理性派HiFi",
        "model": "X5",
        "type": "passive",
        "price": "284",
        "shape": "bookshelves",
        "amount": "pair",
        "default_measurement": "asr",
        "measurements": {
            "asr": {
                "origin": "ASR",
                "format": "klippel",
                "review": "https://www.audiosciencereview.com/forum/index.php?threads/%E7%90%86%E6%80%A7%E6%B4%BEhifi-x5-speaker-review.42528/",
                "review_published": "20230302",
            },
        },
    },
}

speakers_info = (
    speakers_info_misc
    | speakers_info_a
    | speakers_info_b
    | speakers_info_c
    | speakers_info_d
    | speakers_info_e
    | speakers_info_f
    | speakers_info_g
    | speakers_info_h
    | speakers_info_i
    | speakers_info_j
    | speakers_info_k
    | speakers_info_l
    | speakers_info_m
    | speakers_info_n
    | speakers_info_o
    | speakers_info_p
    | speakers_info_q
    | speakers_info_r
    | speakers_info_s
    | speakers_info_t
    | speakers_info_u
    | speakers_info_v
    | speakers_info_w
    | speakers_info_x
    | speakers_info_y
    | speakers_info_z
)

# add some information about precisions of graphs
origins_info = {
    # for example the Princeton 3d3a measurements are valid >500hz
    "ASR": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "logo": "dist/metadata/asr.png",
        "logo-small": "dist/metadata/asr-small.png",
        "url": "http://www.audiosciencereview.com",
    },
    "Princeton": {
        "min hz": 500,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "logo": "dist/metadata/3d3a.jpg",
        "logo-small": "dist/metadata/3d3a.jpg",
        "url": "https://www.princeton.edu/3D3A/Directivity.html",
    },
    "ErinsAudioCorner": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "logo": "dist/metadata/eac.png",
        "logo-small": "dist/metadata/eac.png",
        "url": "https://www.erinsaudiocorner.com",
    },
    "Misc": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "logo": "",
        "logo-small": "",
        "url": "",
    },
    "Vendors-Aalto Speakers": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "url": "https://aaltospeakers.fi",
    },
    "Vendors-AIA Cinema": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "logo": "dist/metadata/apple.png",
        "logo-small": "dist/metadata/apple.png",
        "url": "https://www.aia-cinema.com",
    },
    "Vendors-Alcons Audio": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "url": "https://www.alconsaudio.com/",
    },
    "Vendors-Amate Audio": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "url": "https://www.amateaudio.com/",
    },
    "Vendors-Apple": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "logo": "dist/metadata/apple.png",
        "logo-small": "dist/metadata/apple.png",
        "url": "https://www.apple.com",
    },
    "Vendors-Ascend Acoustics": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "url": "https://www.ascendacoustics.com/",
    },
    "Vendors-AsciLab": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "url": "https://www.audiolabinsight.com/",  # ?
    },
    "Vendors-Attack Audio": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "url": "https://www.attack.com.br",
    },
    "Vendors-Audiofocus": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "url": "https://www.audiofocus.eu/",
    },
    "Vendors-Audio First Design": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "url": "https://www.audiofirstdesign.uk.co/",
    },
    "Vendors-Axiom": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "logo": "dist/metadata/axiom.png",
        "logo-small": "dist/metadata/axiom.png",
        "url": "https://www.axiompro.com/",
    },
    "Vendors-BiAmp": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "url": "https://biamp.com/",
    },
    "Vendors-BIC America": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "logo": "dist/metadata/BIC America.jpg",
        "logo-small": "dist/metadata/BIC America.jpg",
        "url": "https://bicamerica.com/",
    },
    "Vendors-Buchardt Audio": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "logo": "dist/metadata/buchardt-audio.png",
        "logo-small": "dist/metadata/buchardt-audio-small.png",
        "url": "https://www.buchardtaudio.com",
    },
    "Vendors-Bose": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "logo": "dist/metadata/bose.png",
        "logo-small": "dist/metadata/bose.png",
        "url": "https://www.bose.com",
    },
    "Vendors-Bowers & Wilkins": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "logo": "dist/metadata/bose.png",
        "logo-small": "dist/metadata/bose.png",
        "url": "https://www.bowerswilkins.com/",
    },
    "Vendors-Coda Audio": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "logo": "dist/metadata/.png",
        "logo-small": "dist/metadata/.png",
        "url": "https://codaaudio.com/",
    },
    "Vendors-Cambridge Soundworks": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "logo": "dist/metadata/.png",
        "logo-small": "dist/metadata/.png",
        "url": "https://en.wikipedia.org/wiki/Cambridge_SoundWorks",
    },
    "Vendors-DAS Audio": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "logo": "dist/metadata/dasaudio.png",
        "logo-small": "dist/metadata/dasaudio.png",
        "url": "https://www.dasaudio.com",
    },
    "Vendors-Danley": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "logo": "dist/metadata/danley.png",
        "logo-small": "dist/metadata/danley.png",
        "url": "https://www.danleysoundlabs.com",
    },
    "Vendors-DB Audiotechnik": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "logo": "dist/metadata/dbaudio.png",
        "logo-small": "dist/metadata/dbaudio.png",
        "url": "https://www.dbaudio.com",
    },
    "Vendors-Devialet": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "url": "https://www.davialet.com",
    },
    "Vendors-Dolby": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "url": "https://professional.dolby.com/product/dolby-audio-solutions-for-movie-theaters/",
    },
    "Vendors-EAW": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "url": "https://eaw.com",
    },
    "Vendors-EV": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "url": "https://www.electrovoice.com",
    },
    "Vendors-Infinity": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "logo": "dist/metadata/infinity.png",
        "logo-small": "dist/metadata/infinity-small.png",
        "url": "https://www.infinityspeakers.com",
    },
    "Vendors-Genelec": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "logo": "dist/metadata/genelec.png",
        "logo-small": "dist/metadata/genelec.png",
        "url": "https://www.genelec.com",
    },
    "Vendors-GGNTKT": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "logo": "dist/metadata/ggntkt.png",
        "logo-small": "dist/metadata/ggntkt-small.png",
        "url": "https://www.ggntkt.de",
    },
    "Vendors-FBT": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "logo": "dist/metadata/fbt.png",
        "logo-small": "dist/metadata/fbt.png",
        "url": "https://www.fbt.it",
    },
    "Vendors-Fulcrum Acoustic": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "logo": "dist/metadata/fulcrum-acoustic.png",
        "logo-small": "dist/metadata/fulcrum-acoustic.png",
        "url": "https://www.fulcrum-acoustic.com",
    },
    "Vendors-HK Audio": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "url": "https://hkaudio.com/",
    },
    "Vendors-JBL": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "logo": "dist/metadata/jbl.png",
        "logo-small": "dist/metadata/jbl-small.png",
        "url": "https://www.jbl.com",
    },
    "Vendors-JTR": {
        "min hz": 50,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "logo": "dist/metadata/jtr.png",
        "logo-small": "dist/metadata/jtr-small.png",
        "url": "https://www.jtrspeakers.com",
    },
    "Vendors-Kali": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "logo": "dist/metadata/kali.png",
        "logo-small": "dist/metadata/kali-small.png",
        "url": "https://www.kaliaudio.com",
    },
    "Vendors-KLH": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "logo": "dist/metadata/klh.png",
        "logo-small": "dist/metadata/klh-small.png",
        "url": "https://www.klh.com",
    },
    "Vendors-KEF": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "logo": "dist/metadata/kef.png",
        "logo-small": "dist/metadata/kef.png",
        "url": "https://www.kef.com",
    },
    "Vendors-K ARRAY": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "logo": "dist/metadata/k-array.png",
        "logo-small": "dist/metadata/k-array.png",
        "url": "https://www.k-array.com",
    },
    "Vendors-KV2 Audio": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "logo": "dist/metadata/k-array.png",
        "logo-small": "dist/metadata/k-array.png",
        "url": "https://www.kv2audio.com",
    },
    "Vendors-KME Sound": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "logo": "dist/metadata/k-array.png",
        "logo-small": "dist/metadata/k-array.png",
        "url": "https://www.kmesound.com",
    },
    "Vendors-Kling Freitag": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "logo": "dist/metadata/kling-freitag.png",
        "logo-small": "dist/metadata/kling-freitag.png",
        "url": "https://www.kling-freitag.de",
    },
    "Vendors-Klipsch": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "logo": "dist/metadata/klipsch.png",
        "logo-small": "dist/metadata/klipsch.png",
        "url": "https://www.klipsch.com",
    },
    "Vendors-L-Acoustics": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "url": "https://www.l-acoustics.com/",
    },
    "Vendors-LD Systems": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "url": "https://www.ld-systems.com/",
    },
    "Vendors-Magico": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "logo": "dist/metadata/magico.png",
        "logo-small": "dist/metadata/magico.png",
        "url": "https://www.magicoaudio.com",
    },
    "Vendors-March Audio": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "url": "https://marchaudio.com/",
    },
    "Vendors-Martin Audio": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "logo": "dist/metadata/martinaudio.png",
        "logo-small": "dist/metadata/martinaudio.png",
        "url": "https://www.martinaudio.com",
    },
    "Vendors-Mesanovic": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "logo": "dist/metadata/mesanovic.png",
        "logo-small": "dist/metadata/mesanovic.png",
        "url": "https://www.mesanovicmicrophones.com",
    },
    "Vendors-Meyer Sound": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "logo": "dist/metadata/meyersound.png",
        "logo-small": "dist/metadata/meyersound.png",
        "url": "https://www.meyersound.com",
    },
    "Vendors-MoFi": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "url": "https://mofi.com/",
    },
    "Vendors-Nexo": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "logo": "dist/metadata/nexo.png",
        "logo-small": "dist/metadata/nexo.png",
        "url": "https://www.nexo-sa.com",
    },
    "Vendors-Neumann": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "logo": "dist/metadata/neumann.png",
        "logo-small": "dist/metadata/neumann.png",
        "url": "https://www.neumann.com",
    },
    "Vendors-Novacoustic": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "url": "https://www.novacoustic.de",
    },
    "Vendors-Onesystems": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "url": "https://www.onesystems.com",
    },
    "Vendors-Optimal Audio": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "url": "https://www.optimal-audio.co.uk",
    },
    "Vendors-RCF": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "logo": "dist/metadata/rcf.png",
        "logo-small": "dist/metadata/rcf.png",
        "url": "https://www.rcf.it",
    },
    "Vendors-Paradigm": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "logo": "dist/metadata/paradigm.png",
        "logo-small": "dist/metadata/paradigm.png",
        "url": "https://www.paradigm.com",
    },
    "Vendors-Pioneer": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "logo": "dist/metadata/pioneer.png",
        "logo-small": "dist/metadata/pioneer.png",
        "url": "https://www.pioneer.com",
    },
    "Vendors-Perlisten": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "logo": "dist/metadata/perlisten.png",
        "logo-small": "dist/metadata/perlisten.png",
        "url": "https://www.perlistenaudio.com",
    },
    "Vendors-PMC": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "logo": "dist/metadata/pmc.png",
        "logo-small": "dist/metadata/pmc.png",
        "url": "https://www.pmc-speakers.com/",
    },
    "Vendors-Polk Audio": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "logo": "dist/metadata/polkaudio.png",
        "logo-small": "dist/metadata/polkaudio.png",
        "url": "https://www.polkaudio.com",
    },
    "Vendors-Presonus": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "logo": "dist/metadata/presonus.png",
        "logo-small": "dist/metadata/presonus.png",
        "url": "https://www.presonus.com",
    },
    "Vendors-PSI Audio": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "url": "https://www.psiaudio.swis",
    },
    "Vendors-QSC": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "logo": "dist/metadata/qsc.png",
        "logo-small": "dist/metadata/qsc.png",
        "url": "https://www.qsc.com",
    },
    "Vendors-Taipuu Speakers": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "url": "https://aaltospeakers.fi",
    },
    "Vendors-Turbosound": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "logo": "dist/metadata/turbosound.png",
        "logo-small": "dist/metadata/turbosound.png",
        "url": "https://www.turbosound.com",
    },
    "Vendors-Sigberg Audio": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "url": "https://www.sigbergaudio.no",
    },
    "Vendors-Reflector Audio": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "logo": "",
        "logo-small": "",
        "url": "https://http://www.reflector.audio/",
    },
    "Vendors-Revel": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "logo": "dist/metadata/revel.png",
        "logo-small": "dist/metadata/jbl-small.png",
        "url": "https://www.revelspeakers.com",
    },
    "Vendors-Seeburg": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "logo": "dist/metadata/seeburg.png",
        "logo-small": "dist/metadata/seeburg.png",
        "url": "https://www.seeburg.net",
    },
    "Vendors-SONBS": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "url": "https://www.sonbs.net",
    },
    "Vendors-SunAudio": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "url": "https://sunaudio.com/",
    },
    "Vendors-Theory Audio": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "url": "https://www.theoryprofessional.com",
    },
    "Vendors-Tannoy": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "url": "https://www.tannoy.com",
    },
    "Vendors-Vue Audiotechnik": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "url": "https://vue-audiotechnik.com",
    },
    "Vendors-Wharfedale Pro": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "logo": "dist/metadata/.png",
        "logo-small": "dist/metadata/.png",
        "url": "https://www.wharfedalepro.com/",
    },
    "Vendors-Yamaha": {
        "min hz": 20,
        "max hz": 20000,
        "min dB": -40,
        "max dB": 10,
        "logo": "dist/metadata/yamaha.png",
        "logo-small": "dist/metadata/yamaha-small.png",
        "url": "https://www.yamaha.com",
    },
}
