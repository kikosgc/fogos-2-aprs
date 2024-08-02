# fogos-2-aprs 🇵🇹
<img src="https://i.postimg.cc/MHkJNQTS/fogos2aprs.png" width="50%" height="50%">

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub issues](https://img.shields.io/github/issues/kikosgc/fogos-2-aprs)](https://github.com/kikosgc/fogos-2-aprs/issues)
[![GitHub forks](https://img.shields.io/github/forks/kikosgc/fogos-2-aprs)](https://github.com/kikosgc/fogos-2-aprs/network)
[![GitHub stars](https://img.shields.io/github/stars/kikosgc/fogos-2-aprs)](https://github.com/kikosgc/fogos-2-aprs/stargazers)

## 📚 Table of Contents

- [Introduction](#introduction)
- [How It Works](#how-it-works)
- [What is APRS?](#what-is-aprs)
- [Importance of Amateur Radio in Civil Protection](#importance-of-amateur-radio-in-civil-protection)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## 🚒🔥 Introduction<a id='introduction'></a>

Welcome to **fogos-2-aprs**, a project aimed at gating/forwarding Portuguese rural fire data to the APRS service. This project collects fire data such as location and status from [ANEPC, Autoridade Nacional de Emergência e Proteção Civil](https://prociv.gov.pt/en/home/) 🇵🇹 and forwards it to the APRS network, helping enhance situational awareness and emergency response.

## ⚙️ How It Works<a id='how-it-works'></a>

The project utilizes open data from ANEPC 🇵🇹 to obtain real-time information about rural fires. This information is then formatted and transmitted via the APRS network. APRS is a digital communication protocol used by amateur radio operators to exchange information such as position data, weather reports, and messages.

## 🌐 What is APRS?<a id='what-is-aprs'></a>

APRS, or Automatic Packet Reporting System, is an amateur radio-based system for real-time communication of information. It utilizes digital packet radio to transmit data, which can include:

- 📍 Position information
- ☁️ Weather data
- 📬 Messages and alerts
- 📡 Telemetry and remote control

APRS provides a robust and reliable means of communication, particularly valuable in remote areas or during emergencies when traditional communication infrastructure may be unavailable.

## 🦺️ Importance of Amateur Radio in Civil Protection<a id='importance-of-amateur-radio-in-civil-protection'></a>

Amateur radio operators play a critical role in civil protection and emergency response. Their ability to establish communication networks during disasters and their proficiency with radio technology make them invaluable assets in times of crisis. By integrating fire data with the APRS network, this project aims to leverage the skills and infrastructure of the amateur radio community to enhance public safety and response capabilities.

## 🚀 Usage<a id='usage'></a>

Once the application is running, it will continuously fetch the latest fire data from ANEPC and transmit it to the APRS network. Ensure that your APRS equipment is set up and configured to receive the transmitted data.

## 🤝 Contributing<a id='contributing'></a>

We welcome contributions from the community! To contribute:

1. Fork the dev repository.
2. Make your changes and commit them:
    ```bash
    git commit -m "Description of your changes"
    ```
3. Push your changes to your forked repository:
    ```bash
    git push origin dev
    ```
4. Open a pull request on the original repository.

Please ensure that your code adheres to our coding standards and includes appropriate tests.
> Important: Only accepting PRs on the "dev" branch.

## 📄 License<a id='license'></a>

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

![Alt](https://repobeats.axiom.co/api/embed/fe4e35eb2e43113587ae076013fbf701910ee9b8.svg "Repobeats analytics image")

Thank you for your interest in **fogos-2-aprs**! We hope this project contributes to improving fire response and public safety through the use of amateur radio and APRS technology.
