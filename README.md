# GAN stability - Cryptokitty edition
This repository contains an experiment based on the paper [Which Training Methods for GANs do actually Converge?](https://avg.is.tuebingen.mpg.de/publications/meschedericml2018), using a dataset of cryptokitties.

You can find further details on [the project page](https://avg.is.tuebingen.mpg.de/research_projects/convergence-and-stability-of-gan-training).

# Usage
First download your data and put it into the `./data` folder.

To train a new model, first create a config script similar to the ones provided in the `./configs` folder.  You can then train you model using
```
python train.py PATH_TO_CONFIG
```

To compute the inception score for your model and generate samples, use
```
python test.py PATH_TO_CONIFG
```

Finally, you can create nice latent space interpolations using
```
python interpolate.py PATH_TO_CONFIG
```
or
```
python interpolate_class.py PATH_TO_CONFIG
```

# Notes
* For the results presented in the paper, we did not use a moving average over the weights. However, using a moving average helps to reduce noise and we therefore recommend its usage. Indeed, we found that using a moving average leads to much better inception scores on Imagenet.
* Batch normalization is currently *not* supported when using an exponential running average, as the running average is only computed over the parameters of the models and not the other buffers of the model.

# Results
## celebA-HQ
![300000 iterations](results/00300000.png)
![400000 iterations](results/00400000.png)
![470000 iterations](results/00470000.png)
