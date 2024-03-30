# websurfer-apitgateway

A proof of concept for a script that does Google searches.

## Setup

First, clone this repository.

```
git clone https://github.com/MatheusOPP/websurfer_gatewayapi.git

cd websurfer_gatewayapi
```

Then create a virtual environment, activate it and install the project requirements. You will need ``pip`` and ``venv`` for this.

```
python -m venv env

pip install -r requirements.txt
```

### Configuration

In order to use APIGateway, you will need an AWS Access Key. You can obtain one yourself by going to the [AWS website](https://aws.amazon.com/) and signing up for an account. Mind that you will need a credit/debit card and will be temporarily debited ~$1 on it for verification - it is reimbursed later.

Then you can follow the [documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user_manage_add-key.html) to create access keys for yourself. 

With your access keys in hand, create a ``.env`` file at the root of the project the following this template:

```
AWS_ACCESS_KEY_ID="your-api-key-id-here"
AWS_ACCESS_KEY_SECRET="your-api-key-secret-here"
```

## Usage

Simply edit the ``keywords`` variable in the ``websurfer_apigateway.py`` with your search terms and then run it in your terminal of choice:

``
python websurfer_apigateway.py
``

The script will output all the URLs for each of the search terms as lists. In my case, for example, using 'joe biden' as the only search term, I got this output:

``
['https://www.whitehouse.gov/administration/president-biden/', 'https://joebiden.com/', 'https://en.wikipedia.org/wiki/Joe_Biden', 'https://www.instagram.com/joebiden/?hl=en', 'https://www.facebook.com/joebiden/', 'https://apnews.com/hub/joe-biden', 'https://twitter.com/POTUS', 'https://www.cnn.com/politics/joe-biden', 'https://thehill.com/people/joe-biden/', 'https://www.instagram.com/potus/?hl=en']
``


P.S.: For the people in the SPAR project led by Aidan O'Gara, contact me directly and I may be able to share my own key with you.
