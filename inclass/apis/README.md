# APIs

In today's in-class, we're going to use two APIs to give us data to work with. The first API is a simple dictionary definitions API. We will use this to get definitions, synonyms, and antonyms of any English word we like. The second API is a weather API that will give us information about any city. The second API will require more setup as we will require an API Key.

## define.py

### Instructions

1. Start by running the program with `python3 define.py hello`. This will give us the definition for "hello". We have some arguments we can pass in to test different aspects. For example, if we want to see the raw data given from the API, we can write `python3 define.py hello raw`. This will give us the raw JSON data.
2. Next, let's implement the `get_synonyms` function first. Start by running `python3 define.py hide raw` to get the raw data from the API. Next, we want to iterate through eacn definition and pull out any synonyms that exist. This should be found under the "meanings/synonyms", however, we will have to keep iterating through to find these. Add each synonym into a list. At the end, make sure you remove any duplicated synonyms.
3. Next, do the same with `get_antonyms`. Find the antonyms using the same method you did for the synonyms. Add each antonym into a list. At the end, make sure you remnove any duplicated antonyms.
4. Lastly, do the same with `get_meanings`, which should add all of the definitions into a list of meanings. These can be found in the "meanings/definitions". Iterate through each definition and add them into your list. You don't have to remove duplicates here as the definitions shouldn't have duplicates.

### Output

```bash

$ python3 define.py show

Word: show
Part of Speech: noun
Definitions:
        Definition: A play, dance, or other entertainment.
        Definition: An exhibition of items.
        Definition: A broadcast program/programme.
        Definition: A movie.
        Definition: An agricultural show.
        Definition: A project or presentation.
        Definition: A demonstration.
        Definition: Mere display or pomp with no substance. (Usu
ally seen in the phrases "all show" and "for show".)
        Definition: Outward appearance; wileful or deceptive app
earance.
        Definition: (with "the") The major leagues.
        Definition: A pale blue flame at the top of a candle fla
me, indicating the presence of firedamp.
        Definition: Pretence.
        Definition: Sign, token, or indication.
        Definition: Semblance; likeness; appearance.
        Definition: Plausibility.
        Definition: A discharge, from the vagina, of mucus strea
ked with blood, occurring a short time before labor.
        Synonyms:
                - big leagues
                - program(me)
                - demonstration
                - illustration
                - proof
                - exhibition
                - exposition
                - façade
                - front
                - superficiality

Part of Speech: verb
Definitions:
        Definition: To display, to have somebody see (something)
.
        Definition: To bestow; to confer.
        Definition: To indicate (a fact) to be true; to demonstr
ate.
        Definition: To guide or escort.
        Definition: To be visible; to be seen; to appear.
        Definition: To put in an appearance; show up.
        Definition: To have an enlarged belly and thus be recogn
izable as pregnant.
        Definition: (racing) To finish third, especially of hors
es or dogs.
        Definition: To have a certain appearance, such as well o
r ill, fit or unfit; to become or suit; to appear.
        Synonyms:
                - display
                - exhibit
                - indicate
                - point out
                - reveal
                - demonstrate
                - prove
                - arrive
                - show up
        Antonyms:
                - conceal
                - cover up
                - hide
                - disprove
                - refute


$ python3 define.py show raw

Word: show
{
 "word": "show",
 "phonetic": "/\u0283\u0259\u028a/",
 "phonetics": [
  {
   "text": "/\u0283\u0259\u028a/",
   "audio": "https://api.dictionaryapi.dev/media/pronunciations/
en/show-uk.mp3",
   "sourceUrl": "https://commons.wikimedia.org/w/index.php?curid
=9028730",
   "license": {
    "name": "BY 3.0 US",
    "url": "https://creativecommons.org/licenses/by/3.0/us"
   }
  },
  {
   "text": "/\u0283o\u028a/",
   "audio": "https://api.dictionaryapi.dev/media/pronunciations/
en/show-us.mp3",
   "sourceUrl": "https://commons.wikimedia.org/w/index.php?curid
=711287",
   "license": {
    "name": "BY-SA 3.0",
    "url": "https://creativecommons.org/licenses/by-sa/3.0"
   }
  }
 ],
 "meanings": [
  {
   "partOfSpeech": "noun",
   "definitions": [
    {
     "definition": "A play, dance, or other entertainment.",
     "synonyms": [],
     "antonyms": []
    },
    {
     "definition": "An exhibition of items.",
     "synonyms": [],
     "antonyms": [],
     "example": "art show;\u00a0 dog show"
    },
    {
     "definition": "A broadcast program/programme.",
     "synonyms": [],
     "antonyms": [],
     "example": "radio show;\u00a0 television show"
    },
    {
     "definition": "A movie.",
     "synonyms": [],
     "antonyms": [],
     "example": "Let's catch a show."
    },
    {
     "definition": "An agricultural show.",
     "synonyms": [],
     "antonyms": [],
     "example": "I'm taking the kids to the show on Tuesday."
    },
    {
     "definition": "A project or presentation.",
     "synonyms": [],
     "antonyms": [],
     "example": "Let's get on with the show.\u00a0\u00a0 Let's g
et this show on the road.\u00a0\u00a0 They went on an internatio
nal road show to sell the shares to investors.\u00a0\u00a0 It wa
s Apple's usual dog and pony show."
    },
    {
     "definition": "A demonstration.",
     "synonyms": [],
     "antonyms": [],
     "example": "show of force"
    },
    {
     "definition": "Mere display or pomp with no substance. (Usu
ally seen in the phrases \"all show\" and \"for show\".)",
     "synonyms": [],
     "antonyms": [],
     "example": "The dog sounds ferocious but it's all show."
    },
    {
     "definition": "Outward appearance; wileful or deceptive app
earance.",
     "synonyms": [],
     "antonyms": []
    },
    {
     "definition": "(with \"the\") The major leagues.",
     "synonyms": [],
     "antonyms": [],
     "example": "He played AA ball for years, but never made it 
to the show."
    },
    {
     "definition": "A pale blue flame at the top of a candle fla
me, indicating the presence of firedamp.",
     "synonyms": [],
     "antonyms": []
    },
    {
     "definition": "Pretence.",
     "synonyms": [],
     "antonyms": []
    },
    {
     "definition": "Sign, token, or indication.",
     "synonyms": [],
     "antonyms": []
    },
    {
     "definition": "Semblance; likeness; appearance.",
     "synonyms": [],
     "antonyms": []
    },
    {
     "definition": "Plausibility.",
     "synonyms": [],
     "antonyms": []
    },
    {
     "definition": "A discharge, from the vagina, of mucus strea
ked with blood, occurring a short time before labor.",
     "synonyms": [],
     "antonyms": []
    }
   ],
   "synonyms": [
    "big leagues",
    "program(me)",
    "demonstration",
    "illustration",
    "proof",
    "exhibition",
    "exposition",
    "fa\u00e7ade",
    "front",
    "superficiality"
   ],
   "antonyms": []
  },
  {
   "partOfSpeech": "verb",
   "definitions": [
    {
     "definition": "To display, to have somebody see (something)
.",
     "synonyms": [],
     "antonyms": [],
     "example": "All he had to show for four years of attendance
 at college was a framed piece of paper."
    },
    {
     "definition": "To bestow; to confer.",
     "synonyms": [],
     "antonyms": []
    },
    {
     "definition": "To indicate (a fact) to be true; to demonstr
ate.",
     "synonyms": [],
     "antonyms": []
    },
    {
     "definition": "To guide or escort.",
     "synonyms": [],
     "antonyms": [],
     "example": "Could you please show him on his way. He has ov
erstayed his welcome."
    },
    {
     "definition": "To be visible; to be seen; to appear.",
     "synonyms": [],
     "antonyms": [],
     "example": "At length, his gloom showed."
    },
    {
     "definition": "To put in an appearance; show up.",
     "synonyms": [],
     "antonyms": [],
     "example": "We waited for an hour, but they never showed."
    },
    {
     "definition": "To have an enlarged belly and thus be recogn
izable as pregnant.",
     "synonyms": [],
     "antonyms": []
    },
    {
     "definition": "(racing) To finish third, especially of hors
es or dogs.",
     "synonyms": [],
     "antonyms": [],
     "example": "In the third race: Aces Up won, paying eight do
llars; Blarney Stone placed, paying three dollars; and Cinnamon 
showed, paying five dollars."
    },
    {
     "definition": "To have a certain appearance, such as well o
r ill, fit or unfit; to become or suit; to appear.",
     "synonyms": [],
     "antonyms": []
    }
   ],
   "synonyms": [
    "display",
    "exhibit",
    "indicate",
    "point out",
    "reveal",
    "demonstrate",
    "prove",
    "arrive",
    "show up"
   ],
   "antonyms": [
    "conceal",
    "cover up",
    "hide",
    "disprove",
    "refute"
   ]
  }
 ],
 "license": {
  "name": "CC BY-SA 3.0",
  "url": "https://creativecommons.org/licenses/by-sa/3.0"
 },
 "sourceUrls": [
  "https://en.wiktionary.org/wiki/show"
 ]
}

$ python3 define.py show antonyms

Word: show
Antonyms:
        - refute
        - cover up
        - conceal
        - disprove
        - hide

$ python3 define.py show synonyms

Word: show
Synonyms:
        - façade
        - point out
        - front
        - big leagues
        - illustration
        - indicate
        - show up
        - prove
        - arrive
        - reveal
        - proof
        - program(me)
        - superficiality
        - demonstration
        - exposition
        - exhibition
        - exhibit
        - display
        - demonstrate

$ python3 define.py show meaning

Word: show
Meanings:
        - A play, dance, or other entertainment.
        - An exhibition of items.
        - A broadcast program/programme.
        - A movie.
        - An agricultural show.
        - A project or presentation.
        - A demonstration.
        - Mere display or pomp with no substance. (Usually seen 
in the phrases "all show" and "for show".)
        - Outward appearance; wileful or deceptive appearance.
        - (with "the") The major leagues.
        - A pale blue flame at the top of a candle flame, indica
ting the presence of firedamp.
        - Pretence.
        - Sign, token, or indication.
        - Semblance; likeness; appearance.
        - Plausibility.
        - A discharge, from the vagina, of mucus streaked with b
lood, occurring a short time before labor.
        - To display, to have somebody see (something).
        - To bestow; to confer.
        - To indicate (a fact) to be true; to demonstrate.
        - To guide or escort.
        - To be visible; to be seen; to appear.
        - To put in an appearance; show up.
        - To have an enlarged belly and thus be recognizable as 
pregnant.
        - (racing) To finish third, especially of horses or dogs
.
        - To have a certain appearance, such as well or ill, fit
 or unfit; to become or suit; to appear.

```

## weather.py

### Instructions

1. Start by changing the `API_TOKEN` to use your API token/key from your account in OpenWeatherMap.
2. Next, start by running `python3 weather.py "San Francisco" forecast` to get the weather forecast for the next 5 days with 3 hour time intervals. This will give us the raw data from the API. We need to format this.
3. Start by implementing the `format_forecast` function. This should take in the data from the forecast and pass each date dictionary value into the `format_date` and concatenate the resulting string. At the end of `format_forecast`, the format string should contain all of the concatenated formatted forecasts. The function should then return this formatted forecast. 
4. Now, let's go back to `format_date` and implement this function. It should get the `date` itself from `forecast_date.get("dt_txt")`. It sould get the temperature data from `forecast_date.get("main")`. Lastly, it should get the weather data from `forecast_date.get("weather")[0]`. We only want the first value since the data only contains one value. This makes parsing the data easier. 
5. Next, for the function contents, following the example output below for an individual date, we will pull out the necessary information and show that date to the user. Keep concatenating each string to the `format` variable. At the end, return this formatted string out.

### Output

```bash

$ python3 weather.py "San Francisco" forecast clean

Date: 2024-04-06 21:00:00
Temperature
        Average Temperature: 57.21800000000009
        Temperature Feels Like: 55.22000000000006
        Min Temperature: 54.33800000000005
        Max Temperature: 57.21800000000009
Weather
        Clouds: scattered clouds

Date: 2024-04-07 00:00:00
Temperature
        Average Temperature: 55.99400000000007
        Temperature Feels Like: 53.924000000000014
        Min Temperature: 53.54600000000005
        Max Temperature: 55.99400000000007
Weather
        Clouds: scattered clouds

Date: 2024-04-07 03:00:00
Temperature
        Average Temperature: 53.20400000000005
        Temperature Feels Like: 51.27800000000006
        Min Temperature: 51.20600000000003
        Max Temperature: 53.20400000000005
Weather
        Clouds: broken clouds

Date: 2024-04-07 06:00:00
Temperature
        Average Temperature: 50.360000000000085
        Temperature Feels Like: 48.524000000000015
        Min Temperature: 50.360000000000085
        Max Temperature: 50.360000000000085
Weather
        Clouds: overcast clouds

Date: 2024-04-07 09:00:00
Temperature
        Average Temperature: 49.064000000000036
        Temperature Feels Like: 45.518000000000086
        Min Temperature: 49.064000000000036
        Max Temperature: 49.064000000000036
Weather
        Clouds: scattered clouds

Date: 2024-04-07 12:00:00
Temperature
        Average Temperature: 48.182000000000016
        Temperature Feels Like: 44.81600000000001
        Min Temperature: 48.182000000000016
        Max Temperature: 48.182000000000016
Weather
        Clouds: few clouds

Date: 2024-04-07 15:00:00
Temperature
        Average Temperature: 47.87600000000009
        Temperature Feels Like: 45.82400000000001
        Min Temperature: 47.87600000000009
        Max Temperature: 47.87600000000009
Weather
        Clear: clear sky

Date: 2024-04-07 18:00:00
Temperature
        Average Temperature: 51.69199999999999
        Temperature Feels Like: 48.280000000000044
        Min Temperature: 51.69199999999999
        Max Temperature: 51.69199999999999
Weather
        Clouds: few clouds

Date: 2024-04-07 21:00:00
Temperature
        Average Temperature: 54.788000000000046
        Temperature Feels Like: 52.50200000000008
        Min Temperature: 54.788000000000046
        Max Temperature: 54.788000000000046
Weather
        Clouds: few clouds

Date: 2024-04-08 00:00:00
Temperature
        Average Temperature: 55.274000000000015
        Temperature Feels Like: 53.276000000000096
        Min Temperature: 55.274000000000015
        Max Temperature: 55.274000000000015
Weather
        Clouds: scattered clouds

$ python3 weather.py "San Francisco" current clean

Temperature
        Average Temperature: 57.110000000000085
        Temperature Feels Like: 55.11200000000006
        Min Temperature: 53.366000000000014
        Max Temperature: 62.06000000000009
Weather
        Clouds: scattered clouds

```

