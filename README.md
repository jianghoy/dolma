# Jianghong's fork of Dolma toolkit

You can find the original Dolma [here](https://github.com/allenai/dolma)

## Inspiration and plan

I encountered Dolma from [RedPajama 2's data preparation package](https://github.com/togethercomputer/RedPajama-Data). Both are very great tools for building pretraining dataset. One thing I found it not so useful about RP2 is that it's in the middle of data pipeline, meaning it assumes you already have a cc-net processed common crawl dataset. I want to move the crutial functionality of RP2 data, which is tagging, into Dolma. So that all kinds of data can be used as input, instead of having to go through cc-net.

Now that also means we would lose a fasttext classifier metric. Haven't quite figure that part out yet, maybe just try to rebuild it into tagging?

## TODO:
fix `make setup`  stuck at `openssl` and
```
ERROR: Could not build wheels for patchelf, which is required to install pyproject.toml-based projects
```