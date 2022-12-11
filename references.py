from jinja2.utils import markupsafe

REFERENCES = {
    2020:
    ['Jenjaroenpun, Piroon, et al. "Decoding the epitranscriptional landscape from native RNA sequences." Nucleic Acids Research (2020).',
     'Rotzinger, David C., et al. "CT pulmonary angiography for risk stratification of patients with nonmassive acute pulmonary embolism." Radiology: Cardiothoracic Imaging 2.4 (2020): e190188.',
     'Zhou, Yonghe, et al. "Chromatic, achromatic and bimodal negative patterning discrimination by free-flying bumble bees." Animal Behaviour 169 (2020): 93-101.',
     'Fugere, Tyler, Zhongning Jim Chen, and Issam Makhoul. "Practical Vitamin D Supplementation Using Machine Learning." Journal of bone metabolism 27.2 (2020): 111.',
     'Ulu, K. Narynbek, et al. "On the Use of Cox Regression for Statistical Analysis of Fatigue Life Results." Journal of Testing and Evaluation 48.2 (2020): 1439-1451.',
     'Ponti, Alexandre, et al. "First-Line Selective Internal Radiation Therapy in Patients with Uveal Melanoma Metastatic to the Liver." Journal of Nuclear Medicine 61.3 (2020): 350-356.',
     'Diamantopoulos, Nikos, et al. "Engineering for a science-centric experimentation platform." Proceedings of the ACM/IEEE 42nd International Conference on Software Engineering: Software Engineering in Practice. 2020.',
     'Chopin, Nicolas, and Omiros Papaspiliopoulos. "Linear-Gaussian State-Space Models." An Introduction to Sequential Monte Carlo. Springer, Cham, 2020. 73-80.',
     'Edgcomb, Juliet Beni, et al. "Predicting suicidal behavior and self-harm after general hospitalization of adults with serious mental illness." Journal of psychiatric research (2020).'     
    ],
    2019:
    ['Diamantopoulos, Nikos, et al. "Engineering for a Science-Centric Experimentation Platform." arXiv preprint arXiv:1910.03878 (2019).',
     'Ponti, Alexandre, et al. "First-Line Selective Internal Radiation Therapy in Patient with Uveal Melanoma Liver Metastases." Journal of Nuclear Medicine (2019): jnumed-119.',
     'Levy, Joshua J., et al. "PyMethylProcess—convenient high-throughput preprocessing workflow for DNA methylation data." Bioinformatics (2019).',
     'Gruber, Michaela, et al. "Growth dynamics in naturally progressing chronic lymphocytic leukaemia." Nature (2019): 1.',
     'Dunnmon, Jared, et al. "Cross-Modal Data Programming Enables Rapid Medical Machine Learning." arXiv preprint arXiv:1903.11101 (2019).'],
    2018:
    ['Christophides, Damianos, et al. "A method for automatic selection of parameters in NTCP modelling." International Journal of Radiation Oncology• Biology• Physics (2018).',
     'Fadda, Giulia, et al. "MRI and laboratory features and the performance of international criteria in the diagnosis of multiple sclerosis in children and adolescents: a prospective cohort study." The Lancet Child & Adolescent Health (2018).',
     'Muschelli, John, et al. "Neuroconductor: an R platform for medical imaging analysis." Biostatistics (2018).',
     'Domingues, Rémi, et al. "A comparative evaluation of outlier detection algorithms: Experiments and analyses." Pattern Recognition 74 (2018): 406-421.',
     'Poirion, Olivier B., and Benedicte Lafay. "Neo-formation of chromosomes in bacteria." bioRxiv (2018): 264945.',
     'de Melo, Vinícius Veloso, and Wolfgang Banzhaf. "Automatic feature engineering for regression models with machine learning: An evolutionary computation and statistics hybrid." Information Sciences 430 (2018): 287-313.',
     'Giuliano, Christopher J., et al. "MELK expression correlates with tumor mitotic activity but is not required for cancer growth." eLife 7 (2018).',
     'De Vries, Stefan PW, et al. "Phylogenetic analyses and antimicrobial resistance profiles of Campylobacter spp. from diarrhoeal patients and chickens in Botswana." PloS one 13.3 (2018): e0194481.'],
    2017:
    ['Cherifi, Nadir, et al. "Automatic Inference of Energy Models for Peripheral Components in Embedded Systems." FiCloud 2017: The 5th International Conference on Future Internet of Things and Cloud. 2017.',
     'Lowe, Andrew John. "Language-agnostic data analysis workflows and reproducible research." (2017).',
     'Alexander, William M., et al. "multiplierz v2. 0: a Python‐based ecosystem for shared access and analysis of native mass spectrometry data." Proteomics (2017).',
     'Liu, Lingjie, et al. "An approach of identifying differential nucleosome regions in multiple samples." BMC genomics 18.1 (2017): 135.',
     'Olesen, Scott W., Claire Duvallet, and Eric J. Alm. "dbOTU3: A new implementation of distribution-based OTU calling." PloS one 12.5 (2017): e0176335.',
     'Peacock, Jacob, and Harish Sethu. "Which Leaflet is More Effective: A Reanalysis." (2017).',
     'Sharker, Yushuf, and Eben Kenah. "Estimation of the Household Secondary Attack Rate: Binomial Considered Harmful." arXiv preprint arXiv:1705.01135 (2017).',
     'Domingues, Rémi, et al. "A comparative evaluation of outlier detection algorithms: experiments and analyses." Pattern Recognition (2017).',
     'Zhao, Xuefang, Alexandra M. Weber, and Ryan E. Mills. "A recurrence based approach for validating structural variation using long-read sequencing technology." bioRxiv (2017): 105817.',
     'Laycock, Silas GT. "From blackbirds to black holes: Investigating capture-recapture methods for time domain astronomy." New Astronomy 54 (2017): 91-102.',
     'Chiera, Belinda A., and Małgorzata W. Korolkiewicz. "Visualizing Big Data: Everything Old Is New Again." Big Data Management. Springer International Publishing, 2017. 1-27.',
     'Amarante, Linda M., Marcelo S. Caetano, and Mark Laubach. "Medial frontal theta is entrained to rewarded actions." Journal of Neuroscience (2017): 1965-17.'],
    2016:
    ['Freer, Rosie, et al. "A protein homeostasis signature in healthy brains recapitulates tissue vulnerability to Alzheimer’s disease." Science Advances 2.8 (2016): e1600947.',
     'Haslwanter, Thomas. An Introduction to Statistics with Python. Springer, 2016.',
     'Ekmekci, Berk, Charles E. McAnany, and Cameron Mura. "An Introduction to Programming for Bioscientists: A Python-Based Primer." PLoS Comput Biol 12.6 (2016): e1004867.',
     markupsafe.Markup('<a href="https://aws.amazon.com/blogs/compute/analyzing-genomics-data-at-scale-using-r-aws-lambda-and-amazon-api-gateway/">Analyzing genomics data at scale with R, AWS Lambda and Amazon API gateway</a> (AWS Compute Blog)'),
     'Anaya, Jordan. "OncoLnc: Linking TCGA survival data to mRNAs, miRNAs, and lncRNAs." PeerJ PrePrints 4 (2016): e1780v1.',
     'Cleland, Edward John, et al. "The bacterial microbiome in chronic rhinosinusitis: Richness, diversity, postoperative changes, and patient outcomes." American journal of rhinology & allergy 30.1 (2016): 37-43.',
     'Vandenbulcke, Hélène, et al. "Alcohol intake increases the risk of hepatocellular carcinoma in patients with hepatitis C virus-related compensated cirrhosis: a prospective study." Journal of hepatology (2016).',
     'Jeong, Seongwoon, et al. "A NoSQL Data Management Infrastructure for Bridge Monitoring." (2016).',
     'Kenah, Eben, et al. "Molecular Infectious Disease Epidemiology: Survival Analysis and Algorithms Linking Phylogenies to Transmission Trees." PLoS Comput Biol 12.4 (2016): e1004869.',
     'Kittas, Aristotelis, et al. "Organizational principles of the Reactome human BioPAX model using graph theory methods." Journal of Complex Networks (2016): cnw003.'],
    2015:
    ['Zhang, Zhi-Min, et al. "Multiscale peak detection in wavelet space." Analyst 140.23 (2015): 7955-7964.',
     'Woon, Wei Lee, et al. "Changes in Occupational Skills-A Case Study Using Non-negative Matrix Factorization." Neural Information Processing. Springer International Publishing, 2015.',
     'Antao, Tiago. Bioinformatics with Python cookbook. Packt Publishing Ltd, 2015.',
     'Terna, Pietro. "Introducing the Swarm-Like Agent Protocol in Python (SLAPP)." Agent-based Models of the Economy. Palgrave Macmillan UK, 2015. 31-54.'],
     2014:
    ['Nakamura, Kunio, et al. "Correlation between brain volume change and T2 relaxation time induced by dehydration and rehydration: implications for monitoring atrophy in clinical studies." NeuroImage: Clinical 6 (2014): 166-170.',
     'Filosi, Michele, et al. "ReNette: a web-infrastructure for reproducible network analysis." bioRxiv (2014): 008433.',
     'Angeli, Nicole F., et al. A process to support species conservation planning and climate change readiness in protected areas. No. e492v2. PeerJ PrePrints, 2014.',
     'Röst, Hannes L., et al. "pyOpenMS: A Python‐based interface to the OpenMS mass‐spectrometry algorithm library." Proteomics 14.1 (2014): 74-77.',
     'Heavey, Cathal, et al. "Development of an open-source discrete event simulation cloud enabled platform." Proceedings of the 2014 Winter Simulation Conference. IEEE Press, 2014.',
     'De Melo, Vinícius Veloso. "Kaizen programming." Proceedings of the 2014 conference on Genetic and evolutionary computation. ACM, 2014.',
     'Onggo, B. S., et al. "TOWARDS AUTOMATED SIMULATION INPUT DATA." 8TH SIMULATION WORKSHOP. 2014.',
     'Via, Allegra, Kristian Rother, and Anna Tramontano. Managing Your Biological Data with Python. CRC Press, 2014.',
     'Brown, Robert A., Sridar Narayanan, and Douglas L. Arnold. "Imaging of repeated episodes of demyelination and remyelination in multiple sclerosis." NeuroImage: Clinical 6 (2014): 20-25.'],
    2013:
    ['Krishnan, Hari, et al. "Exploring Collaborative HPC Visualization Workflows using VisIt and Python." Proceedings of the 12th Python in Science Conference (SciPy 2013). 2013.',
     'Parks, Donovan H., et al. "GenGIS 2: Geospatial analysis of traditional and genetic biodiversity, with new gradient algorithms and an extensible plugin framework." PloS one 8.7 (2013): e69885.'],
    2012:
    ['Harper, Marc, and Christopher J. Lee. "Genome-wide analysis of mutagenesis bias and context sensitivity of N-methyl-N′-nitro-N-nitrosoguanidine (NTG)." Mutation Research/Fundamental and Molecular Mechanisms of Mutagenesis 731.1 (2012): 64-67.',
     'Strickland, C. M., et al. "PyMCMC: A Python Package for Bayesian Estimation Using Markov Chain Monte Carlo." (2012).',
     'Vitolo, Claudia, W. O. U. T. E. R. Buytaert, and D. Reusser. "Hydrological Models as Web Services: An Implementation Using OGC Standards." Proceedings of the 10th International Conference on Hydroinformatics, HIC, Hamburg, Germany. 2012.',
     'Talevich, Eric, et al. "Bio. Phylo: A unified toolkit for processing, analyzing and visualizing phylogenetic trees in Biopython." BMC bioinformatics 13.1 (2012): 1.',
     'Bagger, Frederik Otzen, et al. "HemaExplorer: a database of mRNA expression profiles in normal and malignant haematopoiesis." Nucleic acids research (2012): gks1021.'],
    2011:
    ['Buske, Orion J., et al. "Exploratory analysis of genomic segmentations with Segtools." BMC bioinformatics 12.1 (2011): 1.',
     'Tolk, A., et al. "TOWARDS AUTOMATED SIMULATION INPUT DATA: AN OPEN SOURCE TOOL TO ENHANCE THE INPUT DATA PHASE IN DISCRETE EVENT SIMULATION."',
     'Patton, Evan W., et al. "SemNExT: A Framework for Semantically Integrating and Exploring Numeric Analyses."',
     'Connolly, Daniel W., et al. "Integrating R efficiently to allow secure, interactive analysis within a clinical data warehouse." The 8th International R User Conference. Vanderbilt University.',
     'Masica, David L., and Rachel Karchin. "Correlation of somatic mutation and expression identifies genes important in human glioblastoma progression and survival." Cancer research 71.13 (2011): 4550-4561.',
     'Simone, James. "PoS (Lattice 2011) 048 Data analysis using the Gnu R system for statistical computation." (2011).',
     'Liu, Sanmin, et al. "HDX-analyzer: a novel package for statistical analysis of protein structure dynamics." BMC bioinformatics 12.1 (2011): 1.'],
    2009:
    ['Roseline, Bilina, and Steve Lawford. "Python for Unified Research in Econometrics and Statistics." Available at SSRN 1429822 (2009).',
     'Wijffels, Jan. "Prediction and Fuzzy Logic at ThomasCook to automate price settings of last minute offers." (2009).',
     'McBeth, Rafe. "Computational investigation of biological dose-volume outcome predictors in 29 canine nasal tumor patients treated with stereotactic radiation therapy." (2007).']
}
  
