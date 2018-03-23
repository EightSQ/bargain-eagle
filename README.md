# Bargain Eagle

This tool is meant to be executed via a cronjob. It calls the Ebay Finding API and looks for promising auctions.
If it finds something crispy it sends the interesting stuff via the unix `mail` utility.

## Usage

### Prerequisites
Make sure you have
- python3 (>=3.6)
- along with `pip`
- and a newer version of the unix `mail` utility
This tool should be run on a server with static IP address, so that the mails won't be filtered as spam too easily.

### Install
1. Install required python packages with `pip install -r requirements.txt`.
2. Create an Ebay-Developer Account with an app and get yourself an **Production** api-key. (Don't worry, just a few cliks)
3. Create a `.env` file in the apps' root directory.
4. Create a `tasks/` directory and a `call0.xml` file inside, representing a valid Finding API call, more on that [here](https://developer.ebay.com/devzone/finding/CallRef/findItemsAdvanced.html).
5. Setup a cronjob, e.g.
```cron
# run every Sunday at 7am
0 7 * * sun	cd /path/to/app && python3 .
```

## Roadmap
- Option to send notifications via SMTP with external mail account
- Introduce containerization with docker
- Enable multiple API "search" calls

# LICENSE
Copyright 2018 EightSQ

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
