
# This code is inspired by the work of Brunton et al 2016,
# 10.1016/j.jneumeth.2015.10.010

import pandas as pd

def augmented_matrix(df_abio_aux):

  start = 0
  m = df_abio_aux.shape[1]
  n = df_abio_aux.shape[0]
  h = 2*m/n
  h = int(h+1)
  df_aug = pd.DataFrame([])

  for i in range(0, m-h):
    df_aug =pd.concat([df_aug,pd.DataFrame(df_abio_aux[:,0+i:43+i]).melt()['value']],axis=1)

  df_aug.columns=range(0,df_aug.shape[1])
  print('Snapshots =',m)
  print('Vector size (n site samples) =',n)
  print('Number of rows =',n*h)
  print('Number of columns',m-h)
  return(df_aug)