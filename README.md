# RADAR: A Realistic Dataset for Advancing Ransomware Detection
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14542547.svg)](https://doi.org/10.5281/zenodo.14542547)
## Overview

### Note: Code to be dropped into this repo after publication

This repository accompanies the paper "RADAR: A Realistic Dataset for Advancing Ransomware Detection and Mitigation Strategies" and provides valuable resources for researchers and practitioners focused on ransomware detection using machine learning. The RADAR dataset is structured as a continuous stream of Sysmon logs, combining ransomware events with benign activities to reflect realistic scenarios. Captured in a lab environment using Windows 11, Sysmon, and Elasticsearch, the dataset is ideal for training and testing incremental learning algorithms on a data stream. It includes gradual and abrupt drift scenarios and imbalanced datasets, which better represent real-world conditions where ransomware attacks are rare compared to benign activities. Additionally, the repository includes scripts for preprocessing, feature extraction, and evaluation, enabling the development and benchmarking of ransomware detection models in practical and dynamic environments.

## Citation
If you use this dataset, please cite this work:

```bib
@article{radar2024,
  title={RADAR: A Realistic Dataset for Advancing Ransomware Detection and Mitigation Strategies},
  author={Jamil Ispahany, Oscar Blessed Deho, Md Rafiqul Islam, M. Arif Khan, Md Zahidul Islam},
  year={2024},
  publisher={Charles Sturt University and Cyber Security Cooperative Research Centre}
}
```

## Features

- Comprehensive Dataset: Over 400,000 Sysmon events collected from multiple ransomware families and benign programs
- Realistic Environment: Logs generated using a controlled, virtualised environment simulating real-world scenarios
- Addressing Challenges: 
    - Handles data drift and class imbalance
    - Supports reproducible research for incremental and real-time learning
- Advanced Techniques:
    - Feature engineering for dynamic analysis
    - FastText for vectorising system events
- Evaluation Framework: Scripts for evaluating models with metrics such as F2-score for imbalanced datasets

## Dataset
### Highlights

- Event Count: 413,556 events (302,260 benign, 111,296 ransomware-related)
- Ransomware Families: Includes Akira, BlackBasta, LockBit, Medusa, and more
- Feature Set: 48 extracted features and 19 engineered features to capture behavioral distinctions between ransomware and benign software
- Drift Simulation: Datasets include abrupt and gradual concept drift scenarios

### Structure

- Drift Dataset: Designed for incremental learning evaluation
- Imbalanced datasets: For testing under different ransomware-to-benign ratios.

### Tools and frameworks

- [Sysmon](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon) - Used for logging detailed system events.
- [Winlogbeat](https://www.elastic.co/beats/winlogbeat) - For real-time log forwarding to a central server.
- [Elasticsearch, Logstash, Kibana (ELK)](https://www.elastic.co/elastic-stack) - Centralised data storage, processing, and visualization.
- [FastText](https://fasttext.cc/) - For feature vectorisation.
- Machine Learning:
    - [River](https://riverml.xyz/latest/) - Online learning framework
    - [TensorFlow](https://www.tensorflow.org/) - Deep learning
    - [Python](https://www.python.org/) - Surely you know what this is!

## License

This work is licensed under a CC BY 4.0 license.