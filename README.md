# Telegram Client-reposter

Repost messages from channels which the client is subscribed to two receiver channels, hereinafter referred to as Receiver 1 and Receiver 2.

_Read this in other languages: [English](README.md), [Russian](README.ru.md)_

## About The Project

Receiver 1 reposts all messages from the channels which the client is subscribed in the form of full text + abbreviated links to the source.

Receiver 2 publishes only the headlines ( the first 2 lines ) messages published in the Receiver 1 + two links in the form of buttons - DETAILS and SOURCE.

The "DETAILS" link leads to the full text of the message in source 1.

The "SOURCE" link leads to the source channel 1.

## Getting Started

This is instructions how to start using it.

### Installation

1. Clone the repo

```sh
git clone https://github.com/hatedestiny6/tgchannels_parsing/
```

2. Launch the "set_api.py" script and follow the instructions

```sh
python set_api.py
```

3. Launch the "set_client.py" script and follow the instructions

```sh
python set_client.py
```

4. Launch the "set_receivers.py" script and follow the instructions

```sh
python set_receivers.py
```

## How to get api_id and api_hash

1. Go to my.telegram.org
2. In the Your Phone Number field, enter your phone number and click Next. A Telegram message will be sent to this number, which we will need in the next paragraph.
3. After that, you will have the Confirmation code field. In this field, you need to insert the code that you will receive in the Telegram application On your phone or computer and click the Sign In button.
4. Next, click on the link "API development tools"
5. You will be prompted to create a new application. Fill in the fields for example:
   - App title: Any name in English
   - Shortname: Any line in English without spaces! Length from 5 to 32 characters
   - Url: A link to any site that is not popular
   - Platform: Desktop
   - Description: Come up with any description
6. Click "Create application"
7. Copy the "api_id" and "api_hash" fields

   > Source: https://pythonbot.tilda.ws/about_api

## Usage

Launch the "main.py" script

```sh
python main.py
```
