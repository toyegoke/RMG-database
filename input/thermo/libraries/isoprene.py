#!/usr/bin/env python
# encoding: utf-8

name = "isoprene"
shortDesc = ""
longDesc = """
ARC v1.1.0
ARC project isoprene

Levels of theory used:

Conformers:       b3lyp/6-31g(d,p) empiricaldispersion=gd3bj
TS guesses:       b3lyp/6-31g(d,p) empiricaldispersion=gd3bj
Composite method: cbs-qb3 (using a fine grid)
Frequencies:      b3lyp/cbsb7
Rotor scans:      b3lyp/cbsb7
Using bond additivity corrections for thermo

Using the following ESS settings: {'gaussian': ['local'], 'molpro': ['local'], 'qchem': ['local'], 'onedmin': ['local']}

Considered the following species and TSs:
Species isoprene (run time: 1:48:51)
Species DISP2 (run time: 21:16:49)
Species DISP1 (run time: 17:55:02)
Species DISP3 (run time: 20:04:23)
Species DISP4 (run time: 17:41:44)

Overall time since project initiation: 11:42:40
"""
entry(
    index = 0,
    label = "isoprene",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {4,D}
3  C u0 p0 c0 {2,S} {5,D} {9,S}
4  C u0 p0 c0 {2,D} {12,S} {13,S}
5  C u0 p0 c0 {3,D} {10,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.89894,0.00603929,0.000144039,-2.78783e-07,1.65721e-10,7351.46,9.49626], Tmin=(10,'K'), Tmax=(544.247,'K')),
            NASAPolynomial(coeffs=[1.37999,0.0468185,-2.97201e-05,9.23067e-09,-1.10776e-12,7295.88,17.0868], Tmin=(544.247,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (61.0849,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (299.321,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-H': 8, 'C=C': 2, 'C-C': 2}
1D rotors:
pivots: [1, 2], dihedral: [6, 1, 2, 3], rotor symmetry: 3, max scan energy: 9.77 kJ/mol
pivots: [2, 3], dihedral: [1, 2, 3, 5], rotor symmetry: 1, max scan energy: 26.00 kJ/mol


External symmetry: 1, optical isomers: 1

Geometry:
{'symbols': ('C', 'C', 'C', 'C', 'C', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'), 'isotopes': (12, 12, 12, 12, 12, 1, 1, 1, 1, 1, 1, 1, 1), 'coords': ((-1.029329, -0.803347, 0.613931), (-0.352769, 0.403879, 0.014561), (1.029207, 0.274508, -0.461397), (-0.984582, 1.581993, -0.09049), (1.777138, -0.832626, -0.419939), (-0.481046, -1.168504, 1.488312), (-1.07276, -1.6279, -0.104903), (-2.048157, -0.567721, 0.924378), (1.460406, 1.17998, -0.882632), (1.408708, -1.76762, -0.013504), (2.793164, -0.835835, -0.796362), (-0.49492, 2.448339, -0.522156), (-2.00506, 1.714852, 0.250203))}
""",
)

entry(
    index = 1,
    label = "DISP2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {7,S} {15,S} {16,S}
4  C u0 p0 c0 {2,S} {9,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {7,S} {20,S} {21,S} {22,S}
7  C u0 p0 c0 {3,S} {6,S} {9,D}
8  C u0 p0 c0 {1,S} {10,D} {23,S}
9  C u0 p0 c0 {4,S} {7,D} {24,S}
10 C u0 p0 c0 {8,D} {25,S} {26,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {9,S}
25 H u0 p0 c0 {10,S}
26 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.41429,0.0526092,7.65116e-05,-1.42858e-07,6.50093e-11,-3608.09,13.713], Tmin=(10,'K'), Tmax=(747.571,'K')),
            NASAPolynomial(coeffs=[-0.105564,0.0945696,-5.40859e-05,1.49878e-08,-1.61575e-12,-3728.06,25.348], Tmin=(747.571,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-30.0493,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (619.428,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 8, 'C-H': 16, 'C=C': 2}
1D rotors:
pivots: [1, 8], dihedral: [2, 1, 8, 10], rotor symmetry: 1, max scan energy: 9.13 kJ/mol
pivots: [1, 5], dihedral: [2, 1, 5, 17], rotor symmetry: 3, max scan energy: 17.25 kJ/mol
pivots: [6, 7], dihedral: [20, 6, 7, 3], rotor symmetry: 3, max scan energy: 9.06 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
{'symbols': ('C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'), 'isotopes': (12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1), 'coords': ((-0.854576, 0.096118, -0.262128), (-0.221237, 1.419245, -0.769368), (0.19618, -1.033563, -0.440835), (1.069379, 1.78542, -0.025223), (-1.243948, 0.217799, 1.219987), (2.547254, -1.823284, 0.18403), (1.600884, -0.667585, -0.008016), (-2.046771, -0.219257, -1.14182), (1.976727, 0.601255, 0.172477), (-3.313295, -0.394789, -0.775141), (0.003645, 1.304878, -1.836257), (-0.952183, 2.229667, -0.687064), (1.600198, 2.567162, -0.581262), (0.834513, 2.23585, 0.949125), (0.226746, -1.344396, -1.494677), (-0.137697, -1.921033, 0.110958), (-1.929956, 1.054168, 1.381682), (-0.362265, 0.376743, 1.843201), (-1.734338, -0.694127, 1.570866), (3.551223, -1.483626, 0.447184), (2.193994, -2.494796, 0.975478), (2.620764, -2.427622, -0.728203), (-1.803254, -0.29997, -2.201626), (2.996273, 0.810728, 0.489026), (-3.638596, -0.329384, 0.256744), (-4.08085, -0.612849, -1.509476))}
""",
)

entry(
    index = 2,
    label = "DISP1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {9,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {7,S} {15,S} {16,S}
5  C u0 p0 c0 {1,S} {17,S} {18,S} {19,S}
6  C u0 p0 c0 {7,S} {20,S} {21,S} {22,S}
7  C u0 p0 c0 {4,S} {6,S} {9,D}
8  C u0 p0 c0 {1,S} {10,D} {23,S}
9  C u0 p0 c0 {3,S} {7,D} {24,S}
10 C u0 p0 c0 {8,D} {25,S} {26,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {9,S}
25 H u0 p0 c0 {10,S}
26 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.41287,0.0531526,7.30802e-05,-1.36495e-07,6.13384e-11,-3568.85,13.7077], Tmin=(10,'K'), Tmax=(761.746,'K')),
            NASAPolynomial(coeffs=[0.108495,0.0939804,-5.35448e-05,1.47833e-08,-1.58843e-12,-3746.54,24.2794], Tmin=(761.746,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-29.7193,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (619.428,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 8, 'C-H': 16, 'C=C': 2}
1D rotors:
pivots: [1, 8], dihedral: [2, 1, 8, 10], rotor symmetry: 1, max scan energy: 9.11 kJ/mol
pivots: [1, 5], dihedral: [2, 1, 5, 17], rotor symmetry: 3, max scan energy: 17.17 kJ/mol
pivots: [6, 7], dihedral: [20, 6, 7, 4], rotor symmetry: 3, max scan energy: 8.85 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
{'symbols': ('C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'), 'isotopes': (12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1), 'coords': ((-0.996387, -0.225283, 0.401811), (0.022258, 0.402185, 1.390766), (-0.29943, -1.429136, -0.28948), (1.313855, 0.870116, 0.707942), (-1.429454, 0.80524, -0.653228), (3.26496, 0.115066, -0.772355), (1.859221, -0.125382, -0.29002), (-2.168663, -0.746308, 1.206825), (1.116756, -1.147441, -0.723721), (-3.452787, -0.418668, 1.092397), (-0.448631, 1.235751, 1.921328), (0.27317, -0.349974, 2.147807), (-0.897968, -1.741663, -1.153248), (-0.301258, -2.292159, 0.390971), (2.07505, 1.071702, 1.471856), (1.155034, 1.832668, 0.201991), (-1.851476, 1.698944, -0.184602), (-2.185487, 0.38458, -1.321444), (-0.582753, 1.112253, -1.269526), (3.361546, 1.109961, -1.22371), (3.569642, -0.624813, -1.515514), (3.979016, 0.079009, 0.058965), (-1.890648, -1.473944, 1.969857), (1.548142, -1.845535, -1.438307), (-4.201037, -0.863661, 1.738962), (-3.811775, 0.296791, 0.361546))}
""",
)

entry(
    index = 3,
    label = "DISP3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {8,S} {16,S} {17,S}
4  C u0 p0 c0 {2,S} {9,S} {14,S} {15,S}
5  C u0 p0 c0 {7,S} {18,S} {19,S} {20,S}
6  C u0 p0 c0 {8,S} {21,S} {22,S} {23,S}
7  C u0 p0 c0 {1,S} {5,S} {10,D}
8  C u0 p0 c0 {3,S} {6,S} {9,D}
9  C u0 p0 c0 {4,S} {8,D} {24,S}
10 C u0 p0 c0 {7,D} {25,S} {26,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {9,S}
25 H u0 p0 c0 {10,S}
26 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.40347,0.0509804,0.000110366,-2.48704e-07,1.55e-10,-3606.32,14.0072], Tmin=(10,'K'), Tmax=(422.76,'K')),
            NASAPolynomial(coeffs=[-1.60612,0.0983793,-5.78109e-05,1.65011e-08,-1.82985e-12,-3182.75,33.8626], Tmin=(422.76,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-30.047,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (619.428,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 8, 'C-H': 16, 'C=C': 2}
1D rotors:
pivots: [1, 7], dihedral: [2, 1, 7, 5], rotor symmetry: 1, max scan energy: 19.16 kJ/mol
pivots: [5, 7], dihedral: [18, 5, 7, 1], rotor symmetry: 3, max scan energy: 6.93 kJ/mol
pivots: [6, 8], dihedral: [21, 6, 8, 3], rotor symmetry: 3, max scan energy: 9.08 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
{'symbols': ('C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'), 'isotopes': (12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1), 'coords': ((0.473029, -0.102715, -0.555174), (0.007214, -1.579628, -0.588079), (-0.435823, 0.689399, 0.406782), (-1.451134, -1.703712, -1.042283), (1.81772, 0.032153, -2.72984), (-2.835137, 1.275109, 1.069778), (0.59778, 0.478576, -1.958744), (-1.908575, 0.342183, 0.335512), (-2.349411, -0.734493, -0.320788), (-0.281624, 1.325141, -2.496543), (1.485371, -0.092976, -0.131342), (0.102845, -1.988318, 0.424217), (0.659065, -2.178069, -1.230507), (-1.80355, -2.728214, -0.876538), (-1.523363, -1.534455, -2.125328), (-0.306101, 1.764108, 0.234593), (-0.093961, 0.518516, 1.437223), (1.840436, 0.468089, -3.730199), (1.853327, -1.057192, -2.836561), (2.735977, 0.325559, -2.207742), (-3.874014, 0.944407, 1.007375), (-2.775088, 2.292748, 0.665574), (-2.563514, 1.345104, 2.13017), (-3.418337, -0.93472, -0.350504), (-1.165392, 1.657498, -1.966183), (-0.146242, 1.708284, -3.502662))}
""",
)

entry(
    index = 4,
    label = "DISP4",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {7,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {8,S} {16,S} {17,S}
4  C u0 p0 c0 {1,S} {9,S} {14,S} {15,S}
5  C u0 p0 c0 {7,S} {18,S} {19,S} {20,S}
6  C u0 p0 c0 {8,S} {21,S} {22,S} {23,S}
7  C u0 p0 c0 {1,S} {5,S} {10,D}
8  C u0 p0 c0 {3,S} {6,S} {9,D}
9  C u0 p0 c0 {4,S} {8,D} {24,S}
10 C u0 p0 c0 {7,D} {25,S} {26,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {6,S}
24 H u0 p0 c0 {9,S}
25 H u0 p0 c0 {10,S}
26 H u0 p0 c0 {10,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(coeffs=[3.41852,0.0500161,0.000117422,-2.6537e-07,1.68093e-10,-3584.08,13.9963], Tmin=(10,'K'), Tmax=(414.819,'K')),
            NASAPolynomial(coeffs=[-1.61317,0.0985358,-5.80278e-05,1.66018e-08,-1.84502e-12,-3166.64,33.8438], Tmin=(414.819,'K'), Tmax=(3000,'K')),
        ],
        Tmin = (10,'K'),
        Tmax = (3000,'K'),
        E0 = (-29.8579,'kJ/mol'),
        Cp0 = (33.2579,'J/(mol*K)'),
        CpInf = (619.428,'J/(mol*K)'),
    ),
    shortDesc = """""",
    longDesc = 
"""
Bond corrections: {'C-C': 8, 'C-H': 16, 'C=C': 2}
1D rotors:
pivots: [1, 7], dihedral: [2, 1, 7, 5], rotor symmetry: 1, max scan energy: 19.88 kJ/mol
pivots: [5, 7], dihedral: [18, 5, 7, 1], rotor symmetry: 3, max scan energy: 6.92 kJ/mol
pivots: [6, 8], dihedral: [21, 6, 8, 3], rotor symmetry: 3, max scan energy: 9.09 kJ/mol


External symmetry: 1, optical isomers: 2

Geometry:
{'symbols': ('C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'), 'isotopes': (12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1), 'coords': ((-0.579927, 0.111076, -0.468558), (0.194733, -1.228453, -0.537891), (1.696617, -1.009965, -0.749843), (-0.014512, 0.94982, 0.695664), (-1.563445, 0.211786, -2.830627), (3.773467, 0.0324, 0.335907), (-0.613083, 0.812571, -1.821427), (2.275698, 0.025644, 0.187653), (1.487019, 0.893924, 0.826776), (0.121645, 1.883855, -2.124839), (-1.622327, -0.131448, -0.2255), (0.040147, -1.759127, 0.408316), (-0.208854, -1.871028, -1.325347), (-0.464645, 0.59643, 1.633715), (-0.339395, 1.990931, 0.593301), (1.891609, -0.700578, -1.785829), (2.229029, -1.959772, -0.617989), (-2.593578, 0.236134, -2.456344), (-1.329371, -0.838692, -3.033268), (-1.532763, 0.751034, -3.779071), (4.111113, 0.831137, 0.99986), (4.135639, -0.922008, 0.736356), (4.262594, 0.168935, -0.636232), (1.938051, 1.618231, 1.502444), (0.05939, 2.344951, -3.105159), (0.810741, 2.332385, -1.419978))}
""",
)

