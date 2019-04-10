DNA sequencing has revolutionized microbial ecology. There are two orthogonal approaches commonly used to explore the microbial universe: amplicon where a part of a single gene (usually the 16S rRNA gene) is amplified and sequenced and untargeted (“shotgun”) sequencing of all (“meta”) microbial genomes (“genomics”) where all the DNA is extracted and sequenced. 16S rRNA sequencing provides a rapid, portable and cheap method to identify bacterial organisms in a sample. Drawbacks of this technique are its low taxonomic resolution (typically only to the genus level), its inability to identify community members from other phylogenetic kingdoms or tell us what functional genes are present in a given community. Shotgun metagenomics allows for finer taxonomic resolution (species and/or strain level), cross kingdom identification and details about what genes microbial organisms are carrying in a given community.

<p align="center">
 <img src="./figures/shotgun.jpg" width="600">
</p>

Data analysis pipelines will always follow a pretty standard workflow. Once you understand this, then you will be able to apply these same ideas to other omics technologies using a different set of tools. 


<p align="center">
 <img src="./figures/workflow.jpg" width="800">
</p>

## Mock Communities
To assess the performance of different microbiome workflows, there is an urgent need in the field for reliable reference materials, e.g. a mock microbial community with defined composition. 

When analyzing your dataset keep in mind that if your raw read is similar enough to anything in your reference database and your alignment parameters are 'loose' enough then it will align to that; however, you should always be skeptical of your output if you have not done the proper optimization of have a full understanding of your pipeline is doing. You are the bioinformatician and you need to be comfortable and confident in your pipeline. Sometimes you will just insert your raw reads to an online repository and press a button and you will get an output. How did they get that output, what were their parameters, their cutoffs, how confident are you in their results? Sometimes you will have to create your own pipeline and there will not be a solid blueprint - you are now the trailblazer and bioinformatician. So how can we be confident that we are going in the right direction? The simplest answer right now is understand what parameters you used and why (yes this means actually reading the papers pertaining to a given tool and figuring out if the default parameters are your best choice) and test your pipeline using a mock community.

There are a number of public resources for microbiome bioinformatics benchmarking using artificially constructed (i.e., mock) communities. The one that we will use in this tutorial will be a subset of the [ZymoBiomics Mock Community](https://www.zymoresearch.com/blogs/blog/zymobiomics-microbial-standards-optimize-your-microbiomics-workflow). 


# Shotgun Metagenomic Basic Workflow
```bash
git clone https://github.com/pjtorres/metagenomics_tutorial.git
```

### 1. Quality Control

As the old saying goes 'Garbage in garbage out'. This saying applies to a lot of things including shotgun metagenomic reads. Remember that your are classifying reads based on their similarity to other known reads in your reference database. If your reads are too short they will align to a lot of different genomes, if there is too much error (low sequencing quality) you will make too many erroneous alignments or non at all. These errors will can cause problems will become more apparent as you start analyzing your data and come to find elephant virus exist in your mouth! OMG!

You should check the quality of your data  with programs such as [FastQC](http://www.bioinformatics.babraham.ac.uk/projects/fastqc/). This is an easy drag and drop approach and you will get an html output. You can see and example of it in  ```mock_community/insub732_2_R1_fastqc.html```.

This is great but imagine having to do this for 100 files, oy vey!

On top of that you will also need to preprocess your reads. This means you need to remove filter out bad reads (reads that are too short -typically <=60bp, or of too low quality, too many N's). Need top cut low quality bases in the 5' and 3' region, and removal of adaptors ect. 

Programs you can use include [Trimmomatic](http://www.usadellab.org/cms/?page=trimmomatic), [TagCleaner](http://tagcleaner.sourceforge.net/), [prinseq++](https://github.com/Adrian-Cantu/PRINSEQ-plus-plus). Today we will use [fastp](https://github.com/OpenGene/fastp) which allows you to kill two birds with one stone:1. check quality of data and 2. preprocess your reads! 

