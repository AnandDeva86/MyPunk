# PUNK

A simple command line interface application(CLI).

## Description

A command line interface application(CLI) application to fetch the data from the API: [PunkAPI](https://punkapi.com/documentation/v2)  and save the data between a specific date as text file locally.

## Getting Started

### Dependencies

* click
* requests


### Executing program

* Build the docker image with a name

```
docker build -t <image_name> .
```

* Run the docker image with

```
docker run -v ${pwd}/data:/data/ --rm <image_name> punk beers brewed-from <mm-yyyy> brewed-until <mm-yyyy> --output-format csv --output-path /data/selected_beers.csv
```

## Authors
[Anand Devarajan](https://www.linkedin.com/in/ananddevarajan)

## Version History
* 0.1
    * Initial Release

## License

see the LICENSE.md file for details