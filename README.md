<a name="readme-top"></a>

# 📗 Table of Contents

- [📖 About the Project](#about-project)
  - [🛠 Built With](#built-with)
    - [Tech Stack](#tech-stack)
    - [Key Features](#key-features)
- [💻 Getting Started](#getting-started)
  - [Setup](#setup)
  - [Prerequisites](#prerequisites)
  - [Install](#install)
  - [Usage](#usage)
  - [Run tests](#run-tests)
  - [Deployment](#triangular_flag_on_post-deployment)
- [👥 Authors](#authors)
- [🔭 Future Features](#future-features)
- [🤝 Contributing](#contributing)
- [⭐️ Show your support](#support)
- [🙏 Acknowledgements](#acknowledgements)
- [📝 License](#license)

# 📖 [Spotipy Consol App] <a name="about-project"></a>

**[Spotipy Consol App]**
The Spotipy Consol App is a desktop command line app that lets the user sign in to Spotify System, and browse through songs by artist name, albums, and songs, using the Spotipy API. The app can get the users' preferred songs and also plays a fragment of some tracks on the default local environment web browser.

## 🛠 Built With <a name="built-with"></a>

### Tech Stack <a name="tech-stack"></a>

<details>
  <summary>Client</summary>
  <ul>
    <li><a href="https://learn.microsoft.com/es-es/windows-server/administration/windows-commands/cmd">CMD</a></li>
  </ul>
</details>

<details>
  <summary>Server</summary>
  <ul>
    <li><a href="">N/A</a></li>
  </ul>
</details>

<details>
<summary>Database</summary>
  <ul>
    <li><a href="">N/A</a></li>
  </ul>
</details>

### Key Features <a name="key-features"></a>

- **[Spotify Python API - Spotipy]**
- **[Comand Line Application]**
- **[Local Desktop App]**
- **[User Authentication]**
- **[Spotify Songs Collection Browsing]**

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 💻 Getting Started <a name="getting-started"></a>

To get a local copy up and running, follow these steps.

### Prerequisites

First, install Visual Studio Code.

<a href="https://code.visualstudio.com/">Visual Studio Code</a>

To run this project you need to have <a href="https://www.python.org/">Python</a> installed.

### Setup

Clone this repository to your desired folder:

```sh
  cd my-folder-project
  git https://github.com/alexansaa/SpotipySongApp.git
```

### Install

To make this App work you must have a <a href="https://developer.spotify.com/documentation/web-api">Spotify Developer Profile</a> where you have created a Web API app and provided a working Redirect URI. Do not use Google URLs for this purpose, use some URI of your own.

You need to set some environment variables to make this app work. These environment variables must match the ones you have been given when creating the app instance on your Spotify Developer Profile.

On Windows OS you may set client ID, client Secret, and redirect URI variables like this:

```sh
  cd my-project-frontend
  $env:SPOTIPY_CLIENT_ID = "my_client_id"
  $env:SPOTIPY_CLIENT_SECRET = "my_client_secret"
  $env:SPOTIPY_REDIRECT_URI = "www.google.com"
```

### Usage

To run the project, execute the following command:

```sh
  py.exe .\menu.py
```

This will show you the command line options of the application menu, and you can start checking the application features.

At some point, for the first time using the app, you will be prompted to give the URL where you were redirected. This means some web browser have open a window and redirected to the URI you have provided on your Spotify Developer Profile. Copy the URL from this window and paste it into the command line window.

Now you can search artists by name. The application will show you the most similar names of the string you have typed in.
To look for artist's albums, you can type in the exact name of the artist. The application will show you the names of the artist's albums following by it's Id.
To look for the album's songs you can type in the album ID. The application will show you the names of the album's songs following by it's Id.
To play a fragment of any song, you can type in the song ID. The application will open a web browser window and play the track fragment.


### Deployment

It is needed a Front-End project for this application to be deployed. The Spotify Song App may be deployed as a back-end app in this case.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- AUTHORS -->

## 👥 Authors <a name="authors"></a>

👤 **Alexander**

- [GitHub](https://github.com/alexansaa)
- [LinkedIn](https://www.linkedin.com/in/alexander-saavedra-garcia/)

👤 **Veronica**

- [GitHub](https://github.com/Verolu)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- FUTURE FEATURES -->

## 🔭 Future Features <a name="future-features"></a>

- [ ] **[Front-End UI for the App]**
- [ ] **[Better UI Experience]**

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## 🤝 Contributing <a name="contributing"></a>

Contributions, issues, and feature requests are welcome!

Feel free to check the [issues page](https://github.com/alexansaa/SpotipySongApp/issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## ⭐️ Show your support <a name="support"></a>

If you like this project, please give it a star on GitHub

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 🙏 Acknowledgments <a name="acknowledgements"></a>

I want to thank <a href="https://github.com/Verolu">Verolu</a> for making me part of this interesting project!

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## 📝 License <a name="license"></a>

This project is [MIT](./LICENSE.md) licensed.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
