# augmented_matrix

This function coputes the augmented matrix as described by the work of [Brunton et al 2016](https://www.sciencedirect.com/science/article/pii/S0165027015003829?casa_token=zdJlfAAerywAAAAA:zHCEP_x0fal_TqZqMeXj1EYkiq75bMw_8fCSoSkRh5uEAT29bkCdty3N0guQRSWXHtHETJfB3Uc).
Agumented matrices are computed as a previus step for Dynamic Mode Decomposition (DMD). Typically, in DMD analysis the number of snapshots in time (m) are much less, than the number of sites (n) measured in the dynamic system (n>>m). In other cases, such as biology, we have the opposite (n<<m).To mitigate this we use the augmented matrix procedure.

