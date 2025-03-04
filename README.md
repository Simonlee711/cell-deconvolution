# Bulk Deconvolution Benchmarking

![alt text](https://github.com/Simonleectx/cell-deconvolution/blob/main/figures/rmse_method.png)

This package's primary intentions are to provide the user with the following:

1. Easy to Use
2. Easy to Deploy any current models from the literature
3. Contains a Gene Expression Signature Builder (gene-average, gene-sum, gene-average-of-non-zero-entries)
4. Contains all the modules and routines to reproduce benchmarking results
5. ⚠️ Has Good Documentation ⚠️

### Package Motivation

Cellular deconvolution (also referred to as cell type composition or cell proportion estimation) refers to computational techniques aiming at estimating the proportions of different cell types in samples collected from a tissue. Over the past few years many methods have been implemented using a wide spread of machine learning methods which have been considered the "State of the Art". However based on the paper, [Clustering-independent estimation of cell abundances in bulk tissues using single-cell RNA-seq data](https://www.biorxiv.org/content/10.1101/2023.02.06.527318v1.full.pdf), we were able to learn that a lot of deconvolutions methods accuracy is highly driven on the gene expression signature which are typically required as input to estimate the cell proportions. Since then there have been more methods developed that don't require a gene signature set but require some form of single cell reference to infer the cellular proportions. Therefore this notebook takes a look at widely different methods found across the literature and provides an easy to use interface for the user. Part of the challenge when working with open source codebases is that reproducability becomes a lot of work because there may be missing files, classified datasets involving real patients, etc. Therefore this notebook's emphasis is really just to provide the user with everything they will need to be able to perform a proper benchmark of different deconvolution methods for themselves. In this repository you will find two datasets in the `\data` folder, with the required paired bulk samples along with an othogonal flow cytometry matrix ("ground truth) to benchmark on PBMC related datasets (`GSE107572, GSE1479433`). If you wou;d like to retrain these models from scratch, you will need to provide a training set with a gene signature set coming from the same tissue. For validation purposes some form of orthogonal qunaitifcation is required. If you are interested in including your own models, you are also free to do so by following the pipeline demonstarted of the three different methods seen in this notebook: **cellanneal (annealing/rank coefficients minimization function), Kassandra (Ligh Gradient Boosting Decision Tree Model), & SVR (support vector regression)**. 

### Package Organization

```/data``` - this folder contains some starter benchmarking files. Currently contains Bulk & Flow Cytometry PBMC files to get the notebook running. 

```/figures``` - this folder contains some figures generated by the package. 

```/src``` - this folder contains all the `.py` and jupyter notebooks to showcase the cell deconvolution pipeline. `src/master_deconvolution.ipynb` contains the primary notebook that showcases the analysis pipeline. `src/gene_signature.ipynb` contains a notebook that constructs gene expression signatures in case of retraining for scratch. Utilizes `ctxbio` to run some differential expression to have clusters/cell types for our gene signatures. 

```/test``` - this folder contains some test scripts to show off some methods not present in the notebook. 

### Installing Environments & Requirements

```environment.yml ``` - file is included in the repository. Takes dependencies from Simon's conda environment

```requirements.txt``` - file includes dependencies as well and can be easily installed using `pip freeze > requirements.txt`

To build an environment run the following command:

```conda env create -f environment.yml --name [environment_name] ```

```conda activate [environment_name]```

### What the Package does for You

Cell deconvolution has long been a challenge due to the variability of results seen across current existing methods. Every method is proven to be shown as the "state of the art" and yet we still do not have a method that is seen as the standard for such research problems. This is due to the variability seen across performance at a cell type level as seen in the figure below from the paper [Community assessment of methods to deconvolve cellular composition from bulk gene expression](https://www.biorxiv.org/content/10.1101/2022.06.03.494221v2):

![alt text](https://github.com/Simonleectx/cell-deconvolution/blob/main/figures/benchmark.png)

Another issue seen across methods is the lack of publicly available gene expression signatures so in this package we supply a gene expression signature builder that is typically required in training any cell deconvolution model. In order to do this you will need access to the Celsius Therapeutics Ctxbio repository specifically the `ctxbio/scdata.py` where we will use the built in differential expression methods as well as some built-in methods from scanpy to derive our gene signatures. We experimented with generating different type of signatures which should change the models capabilities to predict. Please note that different methods may require different type of signatures (e.g. Kassandra - hiearchal, proportion, starter gene information in .yaml file. See `src/Kassandra/config/custom.yaml` to see signature organization for the Kassandra model).  

### User requirements

The user is asked to provide bulk samples with corresponding "ground truth" data (e.g. flow cytometry) to perform the benchmarking. The three methods supplied were chosen due to there drastically different properties of inferring the cell proportions (Kassandra - decision tree, Cellanneal - annealing, SVR - regression). However as mentioned in the package motivation, many methods claim that they are the state of the art so this package is really meant to help assess these discrepancies. If you do decide to try new methods, simply load the methods `train()` & `fit()` functions inside the file `src/deconv.py` under the `train()` and `deconvolution()` routines. Other methods in the package should not need to be changed but routines like `benchmark()` should have slight changes in parameter arguments. If there is any confusion, please try to follow the logic of the notebook which tries to show off the functionality of the whole package with notebook annotations along the way. If there are any more questions feel free to email the authors. 

### Gene Expression Signature Builder

### How to Run Package

Remember. Easy to use. Run `src/master_deconvolution.ipynb` to look at the functionality of the package. The benchmarking pipeline is visualized below:

![alt text](https://github.com/Simonleectx/cell-deconvolution/blob/main/figures/pipeline.png)

In terms of retraining models from scratch, please be aware of the basic deconvolution assumptions. The training bulk datasets and the gene expression signatures should come from the same tissue. And if you need a gene signature to be generated from our package, please take note that life will be easier if your single-cell reference dataset contains a `cell_type` or `cell_subtype` annotation. Currently none of the model binaries are saved but possibly in a future version, I will add a feature to save pickle files so our results are reproducible and you can forgo the lenghty duration of training. 

### Authors

Simon Lee - Data Science, slee@celsiustx.com


