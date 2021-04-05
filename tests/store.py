# tests/store.py

# Molecular structure store for unit tests

from kallisto.atom import Atom
from kallisto.molecule import Molecule
from kallisto.units import Bohr


def acetylene():
    """Create an acetylene molecule and return as Molecule."""
    coords = [
        [0.0, 0.0, -1.06176434496059],
        [0.0, 0.0, 1.06176434496059],
    ]

    symbols = [
        "C",
        "H",
    ]

    atoms = []
    for i, _ in enumerate(coords):
        atoms.append(Atom(symbols[i], position=coords[i]))
    return Molecule(symbols=atoms)


def pyridine():
    """Create a pyridine molecule and return as Molecule."""
    coords = [
        [1.3603, 0.0256, 0.0],
        [0.6971, -1.202, 0.0],
        [-0.6944, -1.2184, 0.0],
        [-1.3895, -0.0129, 0.0],
        [-0.6712, 1.1834, 0.0],
        [0.6816, 1.196, 0.0],
        [2.453, 0.1083, 0.0],
        [1.2665, -2.1365, 0.0],
        [-1.2365, -2.1696, 0.0],
        [-2.4837, 0.0011, 0.0],
        [-1.1569, 2.1657, 0.0],
    ]
    coords = [[float(j) / Bohr for j in i] for i in coords]

    symbols = [
        "C",
        "C",
        "C",
        "C",
        "C",
        "N",
        "H",
        "H",
        "H",
        "H",
        "H",
    ]

    atoms = []
    for i, _ in enumerate(coords):
        atoms.append(Atom(symbols[i], position=coords[i]))
    return Molecule(symbols=atoms)


def pyridine_mH():
    """Create a pyridine molecule minus Hydrogen on carbon #0 and return as Molecule."""
    coords = [
        [1.3603, 0.0256, 0.0],
        [0.6971, -1.202, 0.0],
        [-0.6944, -1.2184, 0.0],
        [-1.3895, -0.0129, 0.0],
        [-0.6712, 1.1834, 0.0],
        [0.6816, 1.196, 0.0],
        [1.2665, -2.1365, 0.0],
        [-1.2365, -2.1696, 0.0],
        [-2.4837, 0.0011, 0.0],
        [-1.1569, 2.1657, 0.0],
    ]
    coords = [[float(j) / Bohr for j in i] for i in coords]

    symbols = [
        "C",
        "C",
        "C",
        "C",
        "C",
        "N",
        "H",
        "H",
        "H",
        "H",
    ]

    atoms = []
    for i, _ in enumerate(coords):
        atoms.append(Atom(symbols[i], position=coords[i]))
    return Molecule(symbols=atoms)


def neopentane():
    """Create a neopentane molecule and return as Molecule."""
    coords = [
        [0.000000, 0.0, 0.0],
        [0.881905, 0.881905, 0.881905],
        [-0.881905, -0.881905, 0.881905],
        [0.881905, -0.881905, -0.881905],
        [-0.881905, 0.881905, -0.881905],
        [-1.524077, 0.276170, -1.524077],
        [1.524077, 1.524077, 0.276170],
        [1.524077, -0.276170, -1.524077],
        [1.524077, 0.276170, 1.524077],
        [-1.524077, -0.276170, 1.524077],
        [1.524077, -1.524077, -0.276170],
        [-0.276170, 1.524077, -1.524077],
        [0.276170, 1.524077, 1.524077],
        [0.276170, -1.524077, -1.524077],
        [-0.276170, -1.524077, 1.524077],
        [-1.524077, 1.524077, -0.276170],
        [-1.524077, -1.524077, 0.276170],
    ]
    coords = [[float(j) / Bohr for j in i] for i in coords]

    symbols = [
        "C",
        "C",
        "C",
        "C",
        "C",
        "H",
        "H",
        "H",
        "H",
        "H",
        "H",
        "H",
        "H",
        "H",
        "H",
        "H",
        "H",
    ]

    atoms = []
    for i, _ in enumerate(coords):
        atoms.append(Atom(symbols[i], position=coords[i]))
    return Molecule(symbols=atoms)


def toluene():
    """Create a toluene molecule and return as Molecule."""
    coords = [
        [1.2264, 0.0427, 0.0670],
        [1.0031, -1.3293, 0.0600],
        [-0.2945, -1.8256, -0.0060],
        [-1.3704, -0.9461, -0.0646],
        [-1.1511, 0.4266, -0.0578],
        [0.1497, 0.9292, 0.0066],
        [0.3871, 2.3956, -0.0022],
        [2.2495, 0.4310, 0.1211],
        [1.8510, -2.0202, 0.1071],
        [-0.4688, -2.9062, -0.0109],
        [-2.3926, -1.3347, -0.1157],
        [-2.0006, 1.1172, -0.1021],
        [0.5024, 2.7582, -1.0330],
        [1.2994, 2.6647, 0.5466],
        [-0.4475, 2.9470, 0.4506],
    ]
    coords = [[float(j) / Bohr for j in i] for i in coords]

    symbols = [
        "C",
        "C",
        "C",
        "C",
        "C",
        "C",
        "C",
        "H",
        "H",
        "H",
        "H",
        "H",
        "H",
        "H",
        "H",
    ]

    atoms = []
    for i, _ in enumerate(coords):
        atoms.append(Atom(symbols[i], position=coords[i]))
    return Molecule(symbols=atoms)


def iridiumCatalyst():
    """Create an Iridium catalyst and return as Molecule."""

    coords = [
        [-1.3672999, -1.4398999, 0.1359000],
        [-2.4911998, -0.6808999, 0.1396000],
        [-3.6534996, -1.1211999, -0.5090000],
        [-3.6468996, -2.3434998, -1.1725999],
        [-2.4848998, -3.1187997, -1.1555999],
        [-1.3670999, -2.6316997, -0.4883000],
        [-0.4373000, -3.1872997, -0.4306000],
        [-2.4432998, -4.0866996, -1.6463998],
        [-4.5575996, -0.5223999, -0.4887000],
        [-2.4206998, 0.5908999, 0.8954999],
        [-1.2879999, 0.7903999, 1.6181998],
        [-1.1378999, 1.9348998, 2.3084998],
        [-2.1077998, 2.9319997, 2.3219998],
        [-3.2770997, 2.7402997, 1.5819998],
        [-3.4330997, 1.5600998, 0.8608999],
        [-4.3267996, 1.4057999, 0.2659000],
        [-1.9411998, 3.8419996, 2.8913997],
        [-0.1872000, 2.0459998, 2.8181997],
        [0.4009000, -0.6061999, 1.1172999],
        [-1.2690999, -3.8143996, 3.7856996],
        [-0.1664000, -4.5494996, 4.2269996],
        [1.1218999, -4.0950996, 3.9273996],
        [1.2993999, -2.9384997, 3.1675997],
        [0.2001000, -2.2075998, 2.6786997],
        [-1.0849999, -2.6466997, 3.0382997],
        [-1.9573998, -2.0870998, 2.7090997],
        [0.8509999, -0.7173999, 2.6636997],
        [2.3007998, -2.5989997, 2.9226997],
        [-0.3087000, -5.4547995, 4.8119995],
        [0.6392999, 0.6220999, -0.5923999],
        [-0.0586000, 0.3754000, -1.7751998],
        [0.0637000, 1.5387999, -2.6275997],
        [0.0955000, 1.0794999, -4.0821996],
        [0.8716999, 0.3276000, -4.2397996],
        [0.2802000, 1.9248998, -4.7547995],
        [-0.8681999, 0.6330999, -4.3491996],
        [-1.1760999, 2.4077998, -2.3666998],
        [-1.2042999, 3.2867997, -3.0193997],
        [-2.0717998, 1.8058998, -2.5499998],
        [-1.2019999, 2.7410997, -1.3247999],
        [1.3891999, 2.1923998, -2.1029998],
        [1.3915999, 1.7859998, -0.7128999],
        [2.6481997, 1.5975998, -2.7492997],
        [2.6573997, 0.5124000, -2.6283997],
        [2.7186997, 1.8556998, -3.8108996],
        [3.5309997, 1.9918998, -2.2375998],
        [1.4299999, 3.7172996, -2.1670998],
        [0.6241999, 4.1645996, -1.5814998],
        [2.3812998, 4.0763996, -1.7610998],
        [1.3476999, 4.0651996, -3.2032997],
        [2.0756998, 0.4378000, 1.7666998],
        [3.3654997, -0.0810000, 1.8671998],
        [4.2709996, 1.0315999, 2.0579998],
        [5.4819995, 0.5533999, 2.8527997],
        [5.1838995, 0.0640000, 3.7825996],
        [6.0490994, -0.1689000, 2.2567998],
        [6.1442994, 1.3928999, 3.0939997],
        [4.6909995, 1.5017999, 0.6583999],
        [5.4398995, 2.2997998, 0.7063999],
        [5.1090995, 0.6483999, 0.1171000],
        [3.8181996, 1.8505998, 0.1015000],
        [3.3502997, 2.0656998, 2.7942997],
        [2.0458998, 1.7442998, 2.2507998],
        [3.6590996, 3.5300997, 2.4959998],
        [3.5358997, 3.7464996, 1.4332999],
        [2.9753997, 4.1760996, 3.0565997],
        [4.6847995, 3.7776996, 2.7930997],
        [3.2796997, 1.8273998, 4.3083996],
        [3.0708997, 0.7747999, 4.5225996],
        [4.2123996, 2.1093998, 4.8080995],
        [2.4671998, 2.4302998, 4.7258995],
        [1.7917998, -1.7489998, 0.1412000],
        [1.8500998, -3.1467997, 0.2110000],
        [3.0569997, -3.5802997, -0.4612000],
        [4.1632996, -3.6178996, 0.6029999],
        [4.3272996, -2.6173997, 1.0149999],
        [3.8420996, -4.2739996, 1.4174999],
        [5.1055995, -3.9992996, 0.1957000],
        [2.8261997, -4.9693995, -1.0466999],
        [2.6792997, -5.6906994, -0.2364000],
        [3.6907996, -5.2904995, -1.6389998],
        [1.9392998, -4.9911995, -1.6839998],
        [3.2640997, -2.4330998, -1.5048999],
        [2.7238997, -1.2952999, -0.7998999],
        [4.7166995, -2.1413998, -1.8718998],
        [5.1881995, -3.0188997, -2.3293998],
        [4.7565995, -1.3170999, -2.5912997],
        [5.2941995, -1.8488998, -0.9925999],
        [2.4197998, -2.6279997, -2.7728997],
        [1.3752999, -2.8206997, -2.5121998],
        [2.4501998, -1.7101998, -3.3667997],
        [2.7924997, -3.4536997, -3.3878997],
        [-2.2764998, -4.1481996, 4.0262996],
        [1.9905998, -4.6454995, 4.2840996],
        [-4.5414996, -2.6926997, -1.6821998],
        [-4.0522996, 3.5020997, 1.5576998],
    ]
    coords = [[float(j) / Bohr for j in i] for i in coords]

    symbols = [
        "N",
        "C",
        "C",
        "C",
        "C",
        "C",
        "H",
        "H",
        "H",
        "C",
        "N",
        "C",
        "C",
        "C",
        "C",
        "H",
        "H",
        "H",
        "Ir",
        "C",
        "C",
        "C",
        "C",
        "C",
        "C",
        "H",
        "H",
        "H",
        "H",
        "B",
        "O",
        "C",
        "C",
        "H",
        "H",
        "H",
        "C",
        "H",
        "H",
        "H",
        "C",
        "O",
        "C",
        "H",
        "H",
        "H",
        "C",
        "H",
        "H",
        "H",
        "B",
        "O",
        "C",
        "C",
        "H",
        "H",
        "H",
        "C",
        "H",
        "H",
        "H",
        "C",
        "O",
        "C",
        "H",
        "H",
        "H",
        "C",
        "H",
        "H",
        "H",
        "B",
        "O",
        "C",
        "C",
        "H",
        "H",
        "H",
        "C",
        "H",
        "H",
        "H",
        "C",
        "O",
        "C",
        "H",
        "H",
        "H",
        "C",
        "H",
        "H",
        "H",
        "H",
        "H",
        "H",
        "H",
    ]

    atoms = []
    for i, _ in enumerate(coords):
        atoms.append(Atom(symbols[i], position=coords[i]))
    return Molecule(symbols=atoms)


def propanolLowest():
    """Create lowest conformer of 1-propanol and return as Molecule."""
    coords = [
        [-1.9554949371, 0.1467391618, 0.0031595607],
        [-0.5906278346, -0.5279387138, -0.0201649611],
        [0.5440986558, 0.4958779663, 0.0283462055],
        [0.4812068385, 1.1678478833, -0.8308000219],
        [0.4590669813, 1.0993020658, 0.9450529713],
        [1.8195161785, -0.0957487212, -0.0534239359],
        [1.9103706588, -0.7338049177, 0.6631507673],
        [-0.5004127933, -1.2028008461, 0.8364936998],
        [-0.4854009629, -1.1250023438, -0.9282499098],
        [-2.7476736372, -0.5972665554, -0.0242488945],
        [-2.0700756998, 0.8040326560, -0.8554507953],
        [-2.0722381370, 0.7410005769, 0.9069567477],
    ]

    symbols = [
        "C",
        "C",
        "C",
        "H",
        "H",
        "O",
        "H",
        "H",
        "H",
        "H",
        "H",
        "H",
    ]

    atoms = []
    for i, _ in enumerate(coords):
        atoms.append(Atom(symbols[i], position=coords[i]))
    return Molecule(symbols=atoms)


def propanolIntermediate():
    """Create higher conformer of 1-propanol and return as Molecule."""
    coords = [
        [-1.60306996, 0.10333519, 0.50792736],
        [-0.66904416, -0.46962566, -0.55371646],
        [0.67345677, 0.26436258, -0.61179298],
        [1.26292797, -0.10585085, -1.45392921],
        [0.49744830, 1.34089332, -0.75955140],
        [1.47742183, 0.05176805, 0.52349829],
        [0.98773122, 0.34094585, 1.30125393],
        [-0.48213061, -1.52528483, -0.34815476],
        [-1.14165995, -0.39229359, -1.53423716],
        [-2.56608070, -0.40007121, 0.47312929],
        [-1.76619136, 1.16652831, 0.34003517],
        [-1.19366144, -0.03197289, 1.50775619],
    ]

    symbols = [
        "C",
        "C",
        "C",
        "H",
        "H",
        "O",
        "H",
        "H",
        "H",
        "H",
        "H",
        "H",
    ]

    atoms = []
    for i, _ in enumerate(coords):
        atoms.append(Atom(symbols[i], position=coords[i]))
    return Molecule(symbols=atoms)
