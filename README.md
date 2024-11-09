# Chemical space 2D projections against DrugBank

This tool performs PCA, UMAP and tSNE projections taking the DrugBank chemical space as a reference. The Ersilia Compound Embeddings as used as descriptors. Four PCA components and two UMAP and tSNE components are returned.

## Identifiers

* EOS model ID: `eos9gg2`
* Slug: `chemical-space-projections-drugbank`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Representation`
* Output: `Descriptor`
* Output Type: `Float`
* Output Shape: `List`
* Interpretation: Coordinates of 2D projections, namely PCA, UMAP and tSNE.

## References

* [Publication](https://academic.oup.com/nar/article/52/D1/D1265/7416367)
* [Source Code](https://github.com/ersilia-os/compound-embedding)
* Ersilia contributor: [miquelduranfrigola](https://github.com/miquelduranfrigola)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos9gg2)
* [AWS S3](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos9gg2.zip)
* [DockerHub](https://hub.docker.com/r/ersiliaos/eos9gg2) (AMD64, ARM64)

## Citation

If you use this model, please cite the [original authors](https://academic.oup.com/nar/article/52/D1/D1265/7416367) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a GPL-3.0-or-later license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!