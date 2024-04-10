Current Population Survey (CPS) Info-Viz
========================================

Prerequisites
-------------

* Poetry

```
python -m pip insall poetry --user
```

Install
-------

```
poetry install
```

Setup CPS Token
---------------

1. Request a U.S. Census Data API Key at:
   https://api.census.gov/data/key_signup.html

2. Receive an email title with `Census Data API Key Request`, which
   includes the following content:

   ```
   Hello!

    Thank you for your interest in the Census Data API.
    Your API key is <your-api-key>. Please <a>click here to activate your key</a>.

    Save this email for future reference.

    Have Fun,

    The Census Bureau API Team

    Follow @uscensusbureau on twitter for API updates.
   ```

   Please click the link in the email to activate your key.

3. After copying the API key from the email, setup your API key
   properly, please refer to this article for how to setup the API
   key:
   https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety

   The enviroment variable name should be `CENSUS_API_KEY`.

4. Do not commit your API key in the git.

5. Check your setup by:

    ```
    $ poetry run python examples/example.py
    df = df.apply(pd.to_numeric, errors="ignore")
            a_age  marsupwt
    0          56    687.71
    1          57    687.71
    2          78    646.86
    3          65   1516.95
    4          66   1516.95
    ...       ...       ...
    163538     69    514.11
    163539     70    516.25
    163540     66    516.25
    163541     55    386.37
    163542     52    386.37

    [163543 rows x 2 columns]
    326195439.67
    ```

Run
---

```
poetry run python
```
