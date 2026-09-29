# CineIR supplementary website

Static publication files. Enable GitHub Pages with **GitHub Actions** as the source.
The workflow restores a complete MP4 from byte chunks and checks its SHA-256 before publishing `site/`.
This does not re-encode, shorten, or split playback. The deployed player receives one complete MP4.
Chunks and this workflow are not included in the published website.

This repository alone does not establish an anonymous review link. Verify the limits and playback behavior of any anonymizing proxy separately.
