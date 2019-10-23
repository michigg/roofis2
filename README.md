<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/github_username/repo">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">RooFiS 2</h3>

  <p align="center">
    Room Finding Service Version 2.0
    <br />
    <a href="https://github.com/michigg/roofis2"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://roofis.michigg.de">View Demo</a>
    ·
    <a href="https://github.com/michigg/roofis2/issues">Report Bug</a>
    ·
    <a href="https://github.com/michigg/roofis2/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About The Project

[![RooFiS Screen Shot][product-screenshot]](https://github.com/michigg/roofis2/master/img/demo.png)

"RooFiS2" or "Room Finder Service2" is a room search for free learning rooms at the Otto-Friedrich University Bamberg. The search is limited by day and time and can be further restricted by location and minimum number of persons.

For the implementation the UnivIS PRG interface is used, which is accessed via the json univis api (see the following [repository](https://github.com/michigg/univis_api)). 

The project is a rewrite to the well-known RooFiS service, which was developed by a former student council member of the WIAI student council and is operated by the server team of the WIAI student council. 

The rewrite started at Bamberger Hackaton 2018 with the Python framework Django. After a long break, a new simple approach could be pursued due to new endpoints in the [UnivIS PRG interface](http://www.config.de/cgi-bin/prg-wizard.pl), which was implemented with Flask. At the same time an improved UnivIS API was developed, which returns json instead of xml as response type. 


### Built With
The project was realized with the following modules:
* [Flask](https://github.com/pallets/flask)
* [Flask-Caching](https://github.com/sh4nks/flask-caching)
* [requests](https://requests.kennethreitz.org/en/master/)
* [UnivIS](https://http://univis.uni-bamberg.de/)
* [univis_api](https://github.com/michigg/univis_api)
* [roofis_api](https://github.com/michigg/roofis2_api)


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites
To run this project you need to pre install [docker](https://docs.docker.com/v17.09/engine/installation/) with [docker-compose](https://docs.docker.com/compose/install/)

### Installation
#### Produktion with Docker
1. Clone the repo
```sh
git clone https:://github.com/michigg/roofis2.git
```
2. Update envs images
```
Set the correct api Endpoints
```
3. Build images
```sh
docker-compose build
```
3. Build images
```sh
docker-compose up -d
```
4. Finished
```
Roofis runs per default on `127.0.0.1:8080`
```

#### Develop with Docker
`# TODO`

<!-- USAGE EXAMPLES -->
## Usage
`TODO`

<!-- _For more examples, please refer to the [Documentation](https://example.com)_ -->



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/michigg/roofis2/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the AGPL License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Michael Götz - michael-guenther.goetz@stud.uni-bamberg.de

Project Link: [https://github.com/michigg/roofis2](https://github.com/michigg/roofis2)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
 `TODO`





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=flat-square
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=flat-square
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=flat-square
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=flat-square
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=flat-square
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
