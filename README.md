# Bitly Automation
A simple Python script to automate the process of shortening URLs using the Bitly API.

![automate_bitly](https://user-images.githubusercontent.com/37108394/236059422-02bb1409-72ae-4566-ac63-a3c89e2a7791.png)

## Blog Post
For a more detailed explanation of the Bitly automation process and a step-by-step guide, please refer to our [blog post](https://pycad.co/bitly-automations/).

## How Bitly Automations Work

```mermaid
sequenceDiagram
    actor User
    participant BitlyAutomations
    participant BitlyAPI
    autonumber

    Note over User, BitlyAutomations: Initialization phase
    User ->> BitlyAutomations: Provide API key and long URL
    BitlyAutomations ->> BitlyAPI: Authenticate using API key

    Note over User, BitlyAutomations: Shortening phase
    BitlyAutomations ->> BitlyAPI: Send long URL for shortening
    BitlyAPI -->> BitlyAutomations: Return shortened URL
    BitlyAutomations -->> User: Display shortened URL

```

## Prerequisites
List any prerequisites or requirements for running the script, such as:

- Python 3.9 or higher
- A Bitly account
- Conda (recommended for managing the environment)

## Environment Setup
Explain how to set up the environment using Conda, as described in the blog post:

- Update Conda
- Create a new Conda environment
- Activate the new environment
- Install the required Python packages
- Install OpenSSL

## Obtaining a Bitly API Key
Outline the steps for obtaining a Bitly API key:

- Sign up for a Bitly account
- Log in and navigate to account settings
- Generate an access token
