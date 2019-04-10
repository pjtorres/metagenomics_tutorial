DNA sequencing has revolutionized microbial ecology. There are two orthogonal approaches commonly used to explore the microbial universe: amplicon where a part of a single gene (usually the 16S rRNA gene) is amplified and sequenced and untargeted (“shotgun”) sequencing of all (“meta”) microbial genomes (“genomics”) where all the DNA is extracted and sequenced. 16S rRNA sequencing provides a rapid, portable and cheap method to identify bacterial organisms in a sample. Drawbacks of this technique are its low taxonomic resolution (typically only to the genus level), its inability to identify community members from other phylogenetic kingdoms or tell us what functional genes are present in a given community. Shotgun metagenomics allows for finer taxonomic resolution (species and/or strain level), cross kingdom identification and details about what genes microbial organisms are carrying in a given community.

<p align="center">
 <img src="./figures/shotgun.jpg" width="500">
</p>

Data analysis pipelines will always follow a pretty standard workflow. Once you understand this, then you will be able to apply these same ideas to other omics technologies using a different set of tools. 


<p align="center">
 <img src="./figures/workflow.jpg" width="800">
</p>

## Mock Communities
When analyzing your dataset keep in mind that if your raw reads is similar enough to anything in your reference reads then it will align to that; however, you should always be skeptical of your output if you have not done the proper optimization of your pipeline. You are the bioinformatician and you need to be comfortable and confident in your pipeline. Sometimes you will just inset your raw reads to an online repository and press a button and you will get an output. How did they get that output, what were their parameters, their cutoffs, how confident are you in their results? Sometimes you will have to create your own pipeline and there will not be a solid blueprint - you are now the trailblazer. So how can we be confident that we are going in the right direction? The simplest answer righ now is understand what parameters you used and why (do not leave everything in the default setting) and use a mock community.

To assess the performance of different microbiome workflows, there is an urgent need in the field for reliable reference materials, e.g. a mock microbial community with defined composition. There are a number of public resources for microbiome bioinformatics benchmarking using artificially constructed (i.e., mock) communities. The one that we will use in this tutorial will be a subset of the [ZymoBiomics Mock Community](https://www.zymoresearch.com/blogs/blog/zymobiomics-microbial-standards-optimize-your-microbiomics-workflow).


For this tutorial we will be using a small subset of the ZymoBiomics community standard.
