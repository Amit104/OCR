# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 19:21:45 2017

@author: Axle
"""

from initialisations import * 

def denoise():
    astro = img_as_float(data.astronaut())
    astro = astro[30:180, 150:300]
    
    noisy = astro + 0.3 * np.random.random(astro.shape)
    noisy = np.clip(noisy, 0, 1)
    
    denoise = denoise_nl_means(noisy, 7, 9, 0.08)
    
    fig, ax = plt.subplots(ncols=2, figsize=(8, 4), sharex=True, sharey=True, subplot_kw={'adjustable':'box-forced'})
    
    ax[0].imshow(noisy)
    ax[0].axis('off')
    ax[0].set_title('noisy')
    ax[1].imshow(denoise)
    ax[1].axis('off')
    ax[1].set_title('non-local means')
    
    fig.subplots_adjust(wspace=0.02, hspace=0.2,
                        top=0.9, bottom=0.05, left=0, right=1)
    
    plt.show()