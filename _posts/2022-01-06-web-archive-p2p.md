---
date: 2022-01-07
title: web-archive Peer to Peer
categories: gist
---

just tried it following the instructions here: https://trafilatura.readthedocs.io/en/latest/

simple steps to extract web page content from a url:
> python -m pip installl trafilatura
> trafilatura -u "https://github.blog/2019-03-29-leader-spotlight-erin-spiceland/"
# outputs main content and comments as plain text ...

then tried with 
> trafilatura -u https://www.20minutes.fr/societe/3213019-20220107-affaire-delphine-jubillar-indices-couette-podometre-reste-dossier-contre-mari > test.md

and the generated text file was very clean only containing the main content