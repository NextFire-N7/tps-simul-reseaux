# mm1

```
Lancement de la simulation
Traitement du temps de reponse (tr)
    nb_pkt   tr_instant      tr_mean     int_conf    borne_inf    borne_sup
       165     0.004320     0.048980     0.006392     0.042588     0.055372
Traitement de la taille des files d'attente (fa)
             fa_instant      fa_mean     int_conf    borne_inf    borne_sup
                      2     0.819445     0.705672     0.113773     1.525117
Affichage des graphes tr & fa
```

0.7/0.8 => 90% erreur = pas ouf

intervale de confiance en 1/sqrt(t)

1000s :

```
Lancement de la simulation
Traitement du temps de reponse (tr)
    nb_pkt   tr_instant      tr_mean     int_conf    borne_inf    borne_sup
     21368     0.160640     0.079006     0.001063     0.077942     0.080069
Traitement de la taille des files d'attente (fa)
             fa_instant      fa_mean     int_conf    borne_inf    borne_sup
                      6     1.688604     0.139219     1.549385     1.827824
Affichage des graphes tr & fa
```

On prend $\mu = 10$

| $\rho$                 | 0.3 | 0.6 | 0.9 |
| ---------------------- | --- | --- | --- |
| $\lambda = \rho / \mu$ | 3    |     |     |
| $E[L]$                 |     |     |     |
| $E[R]$                 |     |     |     |
