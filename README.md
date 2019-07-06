# DeepArtist Web Application
## An AI bot which can identify artist from paintings
Ever came across a piece of art and not able to recollect the legend behind the creation. DeepArtist AI bot is there for your rescue. Access it through one of the following links. 
* https://find-artist.herokuapp.com
* https://supratimh.github.io/find-artist

<p align="center"><img src="https://media.giphy.com/media/PzY2K7SaqIEyA/giphy.gif" width="400" height="400"></p>

## Who is DeepArtist AI bot?
DeepArtist is a Deep Learning model, built with a carefully designed Convolution Neural Network. It has been trained to understand the underlying painting styles of the following legends.

* Vincent van Gogh: (1853 - 1890), Dutch, [Post-Impressionism]
* Edgar Degas: (1834 - 1917), French, [Impressionism]
* Pablo Picasso: (1881 - 1973), Spanish, [Cubism]
* Pierre-Auguste Renoir: (1841 - 1919), French, [Impressionism]
* Albrecht Durer: (1471 - 1528), German, [Northern Renaissance]
* Paul Gauguin: (1848 - 1903), French, [Symbolism,Post-Impressionism]
* Francisco Goya: (1746 - 1828), Spanish, [Romanticism]
* Rembrandt: (1606 - 1669), Dutch, [Baroque]
* Alfred Sisley: (1839 - 1899), French,British, [Impressionism]
* Titian: (1488 - 1576), Italian, [High Renaissance,Mannerism]
* Marc Chagall: (1887 - 1985), French,Jewish,Belarusian, [Primitivism]

The code training the model is available here. Accuracy of the current model on unseen paintings of the above artists is approx 87%.
The model is being improved and trained on sample paintings of more artists.

## What does this repo contain?
The code to deploy/serve DeepArtist (or any ML or DL model, for that matter) on cloud, as a web application. At present, it is deployed on Heroku and can be accessed through the links provided above.

## Instructions to use DeepArtist Bot application
1. Open the application through the links provided above.
2. From web, copy the url/location/address of the image jpeg or png file (usually by right click on the image --> copy image address option). The list of artists it can identify are provided above.
3. Paste the url in text box and click "Who's the artist?" button.
4. That's it. DeepArtist Bot will read the image from url, run prediction on it and show the probable artist name and accuracy probability.
5. Bonus - try an image or painting of your own to see which artist's style is the closest match :)

## Instructions to deploy this application on Heroku
* Create an account in [Heroku](https://www.heroku.com). A free tier would suffice for an application of this scale.
* Fork this repo. It is important to fork the repo, because you'll be able to connect to only your own repo.
* Create a new app from [here](https://dashboard.heroku.com/apps).
* Connect the app to "your" GitHub account, and select the repo to deploy.
* Perform "manual deploy" from the Deploy tab.
* When deployment is complete, click "Open App" to run the command associated with your Flask app's default route (i.e. @app.route('/') decorator).

## Instructions to deploy this application on local system
* Fork and Clone the repo.
* Run: pip install -r requirements.txt
* cd to home directory of this app
* Run: python app.py
* Access the API from web browser from http://127.0.0.0.1:5000. Since a HTML file is rendered in default route, the find-artist.html will open in browser.

## Which files should be modified?
* app.py - Behavior of all the endpoints, which can be associated with different functions/APIs the app will provide.
* serve.py - Implementation of backend business logic. For an ML or DL app, this is where we should read the trained weights and make predictions.
* requirements.txt - List of packages required to run this app. This is required by Heroku.
* runtime.txt - Required by Heroku, to determine exact version of Python required to run this app.
* Procfile - To tell Heroku about how to run this app.
* NOTE: If your saved model is smaller than 100 MB, it is advisable to commit it into Github and make the app read from the corresponding directory. However, if it is larger, then save it on a remote storage (like Google Drive, Dropbox etc) and make the app download and read it from there. The second approach has been taken for this application.

## Contact
:love_letter: For any feedback or questions or just to say "Hi", drop me a line anytime at supratimh[at]gmail[dot]com.

To read about other projects I am working on, please visit [my home page](https://supratimh.github.io).

Thank you for reading :heart:
