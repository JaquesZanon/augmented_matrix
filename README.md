# Augmented_matrix

<img src="https://img.shields.io/badge/made%20with-python-blue.svg" alt="made with python">

## Info
This function coputes the augmented matrix as described by the work of Brunton et al 2016[^1] Agumented matrices are computed as a previus step for Dynamic Mode Decomposition (DMD). Typically, in DMD analysis the number of snapshots in time (m) are much less, than the number of sites (n) measured in the dynamic system (n>>m). In other cases, such as biology, we have the opposite (n<<m).To mitigate this we use the augmented matrix procedure.


The original matriz:

![Alt Original Matrix](https://github.com/JaquesZanon/augmented_matrix/blob/main/tipycal.jpg?raw=true)

And The augmented matrix:

![Alt Augmentedl Matrix](https://github.com/JaquesZanon/augmented_matrix/blob/main/augmented.jpg?raw=true)

## Setup

Use the function 'augmented_matrix' to do the computation.
```
df = data_frame
augmented_matrix(df)
```


[^1]: Bingni W. Brunton, Lise A. Johnson, Jeffrey G. Ojemann, J. Nathan Kutz.*Extracting spatial–temporal coherent patterns in large-scale neural recordings using dynamic mode decomposition*.Journal of Neuroscience Methods,Volume 258, 2016, Pages 1-15.
